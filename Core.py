import os
import warnings

if 'DISPLAY' not in os.environ and os.name != 'nt':
    os.environ['SDL_VIDEODRIVER'] = 'dummy'

warnings.filterwarnings('ignore', message='.*pkg_resources.*')

import time
import threading
import sys

import questionary
import economy
import UI
import animatons
import pygame
import minigames
import store
from personality_ai import pet_stats, pet_response, record_action


class GameState:
    def __init__(self, pet_type, pet_name):
        self.pet_type = pet_type
        self.pet_name = pet_name
        self.stats = pet_stats(pet_type)
        self.hunger = self.stats.get('Hunger', 50)
        self.health = self.stats.get('Health', 50)
        self.happiness = self.stats.get('Happiness', 50)
        self.energy = self.stats.get('Energy', 50)

        self.max_value = 100
        self.min_value = 0

    def cap_stats(self):
        self.hunger = min(max(self.hunger, self.min_value), self.max_value)
        self.health = min(max(self.health, self.min_value), self.max_value)
        self.happiness = min(max(self.happiness, self.min_value), self.max_value)
        self.energy = min(max(self.energy, self.min_value), self.max_value)

    def show_stats(self):
        print(f"\n--- {self.pet_name}'s Current Stats ---")
        print(f"Balance: ${economy.get_balance()} (Interest: {economy.interest_rate * 100:.1f}%)")
        print(f"Hunger: {self.hunger}")
        print(f"Health: {self.health}")
        print(f"Happiness: {self.happiness}")
        print(f"Energy: {self.energy}")


def stat_decay(state):
    state.hunger -= 5
    state.health -= 3
    state.happiness -= 4
    state.energy -= 2
    state.cap_stats()
    print(f"\n⏰ Time passes... {state.pet_name}'s stats have decayed slightly.")


def run_decay(state):
    while True:
        time.sleep(300)
        stat_decay(state)


def feed_pet(state):
    state.hunger += 10
    state.happiness += 10
    state.energy += 5
    record_action('feed')
    state.cap_stats()
    return f"You fed {state.pet_name}! {pet_response('feed', state.pet_name)}"


def play_with_pet(state):
    state.happiness += 10
    state.energy -= 10
    state.health += 10
    record_action('play')
    state.cap_stats()
    return f"You played with {state.pet_name}! {pet_response('play', state.pet_name)}"


def rest(state):
    state.energy += 25
    state.health += 10
    record_action('rest')
    state.cap_stats()
    return f"{state.pet_name} rested and feels better! {pet_response('rest', state.pet_name)}"


def clean_pet(state):
    state.health += 15
    state.happiness -= 5
    record_action('clean')
    state.cap_stats()
    return f"You cleaned {state.pet_name}. {pet_response('clean', state.pet_name)}"


def play_minigame(state, screen=None):
    minigame_selection = UI.MinigameSelectionScreen(screen=screen)
    chosen_game = minigame_selection.run()

    if chosen_game == 'minigame_health':
        result = minigames.minigame_health()
        state.health += result.get('health', 0)
        earned = result.get('dollars', 0)
        if earned:
            economy.add_dollars(earned, description='Medicine Rush reward')
        state.cap_stats()
        return f"Medicine Rush completed! Health +{result.get('health', 0)}, earned ${earned}."
    elif chosen_game == 'minigame_happiness':
        result = minigames.minigame_happiness()
        state.happiness += result.get('happiness', 0)
        state.cap_stats()
        return f"Trick Performance completed! Happiness +{result.get('happiness', 0)}."
    elif chosen_game == 'minigame_hunger':
        result = minigames.minigame_hunger()
        state.hunger = max(0, state.hunger - result.get('hunger', 0))
        state.happiness += result.get('happiness', 0)
        earned = result.get('dollars', 0)
        if earned:
            economy.add_dollars(earned, description='Treat Catch reward')
        state.cap_stats()
        return f"Treat Catch completed! Hunger -{result.get('hunger', 0)}, earned ${earned}."
    return 'Back to the hub.'


def collect_income():
    amount = economy.give_income(50, description='fixed paycheck')
    return f'You received a paycheck of ${amount}!'


def handle_hub_action(action_name, state, pet_shop=None, screen=None):
    if action_name == 'Feed':
        return feed_pet(state)
    if action_name == 'Play':
        return play_with_pet(state)
    if action_name == 'Rest':
        return rest(state)
    if action_name == 'Clean':
        return clean_pet(state)
    if action_name == 'Mini Game':
        return play_minigame(state, screen=screen)
    if action_name == 'Shop':
        return visit_shop(pet_shop, screen=screen)
    return None


def visit_shop(pet_shop, screen=None):
    """Open the visual shop screen"""
    if pet_shop is None:
        return "Shop is temporarily closed."
    shop_screen = UI.ShopScreen(pet_shop=pet_shop, screen=screen)
    shop_screen.player_currency = economy.get_balance()
    shop_screen.run()
    economy.set_balance(shop_screen.player_currency)
    return "Thanks for visiting the shop!"


def run_text_menu(state):
    while True:
        gained = economy.apply_interest()
        if gained:
            print(f"\nPassive interest: +${gained} (new balance ${economy.get_balance()})")

        print(f"\n[Balance: ${economy.get_balance()} | Interest rate: {economy.interest_rate * 100:.1f}%]")
        choice = questionary.select(
            'What would you like to do?',
            choices=[
                f'Feed {state.pet_name}',
                f'Play with {state.pet_name}',
                'Rest',
                'Show stats',
                'Show wallet',
                'Collect income',
                'Play a minigame',
                'Quit',
            ],
        ).ask()

        if choice == f'Feed {state.pet_name}':
            print(feed_pet(state))
        elif choice == f'Play with {state.pet_name}':
            print(play_with_pet(state))
        elif choice == 'Rest':
            print(rest(state))
        elif choice == 'Show stats':
            state.show_stats()
        elif choice == 'Show wallet':
            economy.print_economy_summary()
        elif choice == 'Collect income':
            print(collect_income())
        elif choice == 'Play a minigame':
            print(play_minigame(state))
        elif choice == 'Quit':
            print(f'Thanks for playing with {state.pet_name}! Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')


def main():
    pygame.init()
    
    title = UI.TitleScreen()
    result = title.run()
    if result == 'quit':
        pygame.quit()
        sys.exit()

    pet_choice_screen = UI.PetSelection()
    pet_type = pet_choice_screen.run()
    if pet_type == 'back':
        print('Going back to title.')
        pygame.quit()
        sys.exit()

    pet_naming_screen = UI.PetNamingScreen(pet_type=pet_type)
    pet_name = pet_naming_screen.run()
    print(f'\nAwesome! You chose a {pet_type} named {pet_name}!')

    state = GameState(pet_type, pet_name)
    state.cap_stats()

    decay_thread = threading.Thread(target=run_decay, args=(state,))
    decay_thread.daemon = True
    decay_thread.start()

    if title.display_available and pet_choice_screen.display_available:
        screen = pygame.display.set_mode((800, 600), vsync=1)
        pygame.display.set_caption('Snugbit Hub')
        animations = animatons.load_pet_animation(state.pet_type)
        pet_shop = store.PetShop()
        
        # Interactive tutorial with action requirements
        tutorial_steps_with_actions = [
            ('Use the arrow keys or WASD to move your pet around.', 'move'),
            ('Walk to the food bowl and press E to feed your pet.', 'feed'),
            ('Walk to the play area and press E to play.', 'play'),
            ('Walk to the bed or bath and press E to interact.', 'rest'),  # rest or clean
            ('Walk to the shop and press E to visit!', 'shop'),
            ('You can now explore the hub freely! Press E to perform actions.', 'minigame'),
        ]
        
        interactive_tutorial = UI.InteractiveTutorialScreen(screen, tutorial_steps_with_actions)
        
        hub = UI.HubScreen(screen, state.pet_name, state.pet_type, animations, tutorial=interactive_tutorial)
        hub.run(lambda action: handle_hub_action(action, state, pet_shop, screen=screen))
        pygame.quit()
    else:
        print('\nNo graphical display detected. Starting the text-based hub instead.')
        pygame.quit()
        run_text_menu(state)


if __name__ == '__main__':
    main()
