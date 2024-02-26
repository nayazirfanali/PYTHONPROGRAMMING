def calculate_total_balance(denominations, notes):
    total_balance = 0
    for denom, note in zip(denominations, notes):
        total_balance += denom * note
    return total_balance

def main():
    denominations = []
    notes = []

    for i in range(4):
        denomination = int(input(f"Enter the {i+1} Denomination: "))
        number_of_notes = int(input(f"Enter the {i+1} Denomination number of notes: "))
        denominations.append(denomination)
        notes.append(number_of_notes)

    total_balance = calculate_total_balance(denominations, notes)
    print("Total amount available in the ATM machine:", total_balance)

if __name__ == "__main__":
    main()


