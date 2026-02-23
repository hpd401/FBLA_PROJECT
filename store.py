class Item:
    def __init__(self, name, item_type, cost, multiplier_value, stat_affected, description=""):
        self.name = name
        self.item_type = item_type  # 'food', 'toy', 'bed'
        self.cost = cost
        self.multiplier_value = multiplier_value
        self.stat_affected = stat_affected  # which stat this boosts
        self.owned = 0
        self.description = description

    def purchase(self, player_currency):
        if player_currency >= self.cost:
            self.owned += 1
            return True, self.cost
        return False, 0

    def get_total_multiplier(self):
        return 1 + (self.multiplier_value * self.owned)


class PetShop:
    def __init__(self, items_per_page=3):
        self.items_per_page = items_per_page
        self.current_page = 0
        self.pet_name = "Max"
        
        self.items = {
            # FOOD for all the food needs
            'kibble': Item('Premium Kibble', 'food', 30, 0.10, 'health', 'Nutritious pet food - boosts health'),
            'fruit_treats': Item('Fruit Treats', 'food', 50, 0.15, 'happiness', 'Sweet fruity snacks - increases happiness'),
            'protein_mix': Item('Protein Mix', 'food', 60, 0.20, 'strength', 'High protein meal - strengthens your pet'),
            'gourmet_meal': Item('Gourmet Meal', 'food', 100, 0.25, 'health', 'Finest ingredients - major health boost'),
            
            # TOYS
            'rubber_ball': Item('Rubber Ball', 'toy', 40, 0.12, 'happiness', 'Classic bouncy toy - pets love it'),
            'squeaky_toy': Item('Squeaky Toy', 'toy', 55, 0.18, 'Energy', 'Fun squeaky toy - boosts playtime energy'),
            'laser_toy': Item('Laser Toy', 'toy', 90, 0.25, 'Energy', 'Interactive laser - maximum energy boost'),
            
            # BEDS 
            'basic_bed': Item('Cozy Bed', 'bed', 75, 0.15, 'rest', 'Comfortable sleeping spot - better rest'),
            'memory_foam_bed': Item('Memory Foam Bed', 'bed', 150, 0.30, 'rest', 'Premium comfort - excellent recovery'),
            'luxury_bed': Item('Luxury Bed', 'bed', 250, 0.40, 'Energy', 'The finest bed - ultimate comfort boost'),
        }
        self.item_keys = list(self.items.keys())

    def get_total_pages(self):
        return (len(self.items) + self.items_per_page - 1) // self.items_per_page

    def get_page_items(self):
        start_idx = self.current_page * self.items_per_page
        end_idx = start_idx + self.items_per_page
        return self.item_keys[start_idx:end_idx]

    def next_page(self):     #to the right, to the right, to the right to the right to the rightttt
        """Move to next page"""
        if self.current_page < self.get_total_pages() - 1:
            self.current_page += 1
            return True
        return False

    def prev_page(self):       # to the left, to the left, to the left to the left to the left
        if self.current_page > 0:
            self.current_page -= 1
            return True
        return False

    def display_menu(self, player_currency):    # now kick now kick now cmon baby kick
        total_pages = self.get_total_pages()
        page_items = self.get_page_items()

        print("\n" + "="*70)
        print(f"🐾 {self.pet_name}'s SHOP 🐾")
        print("="*70)
        print(f"💰 Currency: {player_currency} coins")
        print(f"📄 Page {self.current_page + 1}/{total_pages}")
        print("="*70 + "\n")

        for idx, key in enumerate(page_items, 1):
            item = self.items[key]
            total_mult = item.get_total_multiplier()
            
            # Icons based on item type
            icon = "🍖" if item.item_type == "food" else "🎾" if item.item_type == "toy" else "🛏️"
            
            print(f"{idx}. {icon} {item.name} ({item.item_type.upper()})")
            print(f"   📝 {item.description}")
            print(f"   💵 Cost: {item.cost} | 📊 Owned: {item.owned}")
            print(f"   ⭐ Multiplier: {total_mult:.2f}x | Boosts: {item.stat_affected}")
            print()

        print("="*70)
        if total_pages > 1:
            print("[1-3] Buy Item | [<] Prev | [>] Next | [q] Quit")
        else:
            print("[1-3] Buy Item | [q] Quit")
        print("="*70)

    def buy_item(self, item_number, player_currency):
        """Purchase an item by page item number"""
        page_items = self.get_page_items()
        
        if item_number < 1 or item_number > len(page_items):
            return False, "Invalid selection", 0

        key = page_items[item_number - 1]
        item = self.items[key]
        success, cost = item.purchase(player_currency)

        if success:
            emoji = "🍖" if item.item_type == "food" else "🎾" if item.item_type == "toy" else "🛏️"
            return True, f"✨ {self.pet_name} received {emoji} {item.name}!", cost
        else:
            return False, f"❌ Not enough coins! Need {item.cost}, have {player_currency}", 0

    def get_stat_multiplier(self, stat_name):
        """Calculate total multiplier for a specific stat"""
        total = 1.0
        for item in self.items.values():
            if item.stat_affected == stat_name:
                total *= item.get_total_multiplier()
        return total

    def save_progress(self):
        """Save item ownership progress"""
        progress = {}
        for key, item in self.items.items():
            progress[key] = item.owned
        return progress

    def load_progress(self, progress):
        """Load item ownership progress"""
        for key, owned in progress.items():
            if key in self.items:
                self.items[key].owned = owned


# Example usage
if __name__ == "__main__":
    shop = PetShop(items_per_page=3)
    player_currency = 500

    print("🐾 Welcome to Pet Sim Shop! 🐾")

    while True:
        shop.display_menu(player_currency)
        choice = input("Select action: ").strip().lower()

        if choice == 'q':
            print("\n👋 Goodbye! Your pet will miss you!")
            break
        elif choice == '<':
            if shop.prev_page():
                print("⬅️ Previous page\n")
            else:
                print("⚠️ Already on first page\n")
        elif choice == '>':
            if shop.next_page():
                print("➡️ Next page\n")
            else:
                print("⚠️ Already on last page\n")
        elif choice in ['1', '2', '3']:
            success, msg, cost = shop.buy_item(int(choice), player_currency)
            if success:
                player_currency -= cost
            print(f"{msg}\n")
        else:
            print("⚠️ Invalid input\n")
        