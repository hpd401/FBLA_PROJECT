Dollars = 100 # initial balance
Dollars_Max = 999999 # stonks

# interest configuration - automatically applied each turn
interest_rate = 0.01  # 1% per cycle 

# running totals for analytics
total_earned = 0
total_spent = 0
transactions: list[dict] = []  # simple transaction history


def update_dollars():
    global Dollars
    if Dollars > Dollars_Max:
        Dollars = Dollars_Max

def record_transaction(amount: int, kind: str, description: str = ""):
   # Log a transaction and update totals. Kind should be "income" or "expense".
    global total_earned, total_spent
    transactions.append({"amount": amount, "kind": kind, "description": description})
    if kind == "income":
        total_earned += amount
    elif kind == "expense":
        total_spent += amount


def add_dollars(amount: int, description: str = "") -> int:
    # Add money to the balance and log the income. Returns the new balance.
    global Dollars
    Dollars += amount
    if Dollars > Dollars_Max:
        Dollars = Dollars_Max
    record_transaction(amount, "income", description)
    return Dollars

def subtract_dollars(amount: int, description: str = "") -> bool:
  # Subtract money from the balance if sufficient funds exist, log the expense, and return success status.
    global Dollars
    if amount <= Dollars:
        Dollars -= amount
        record_transaction(amount, "expense", description)
        return True
    return False


def get_balance() -> int:
    # Return the current balance of dollars.
    return Dollars


def apply_interest(rate: float | None = None) -> int:
  #Applies a passsive interest gain based on the current balance and configured rate. Returns the amount gained.
    global Dollars
    if rate is None:
        rate = interest_rate
    if rate <= 0 or Dollars <= 0:
        return 0
    interest = int(Dollars * rate)
    if interest:
        add_dollars(interest, description=f"Interest @{rate*100:.1f}%")
    return interest


def give_income(amount: int, description: str = "Paycheck") -> int:
    # Grant the player a fixed income amount and log the transaction.
    return add_dollars(amount, description=description)


def print_economy_summary(limit: int = 5):
   # Print current balance and recent transactions for the player.
    print(f"\n Balance: ${Dollars} (Interest rate: {interest_rate*100:.1f}%)")
    print(f" Total earned: ${total_earned}")
    print(f"  Total spent: ${total_spent}")
    print("Recent transactions:")
    for t in transactions[-limit:]:
        prefix = "+" if t["kind"] == "income" else "-"
        print(f"  {prefix}${t['amount']} ({t['description']})")
