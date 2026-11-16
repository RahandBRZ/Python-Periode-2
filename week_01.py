print("Hello Periode 2!")
# Stap 1 - Speler aanmaken

player_name = input("What is your name? ")
player_gold = 100
inventory = []

print(f"\nHello {player_name}! You have {player_gold} gold.")

# Stap 2 - Winkelvoorraad

items = ["Sword", "Shield", "Potion", "Bow"]

print("\nItems available in the shop:")
for item in items:
    print(f"- {item}")

# Stap 3 - Winkelmenu

def buy_item(item_name, price):
    global player_gold

    if player_gold >= price:
        player_gold -= price
        inventory.append(item_name)

        print(f"\nYou bought a {item_name}!")
        print(f"Remaining gold: {player_gold}")
    else:
        print("\nYou don't have enough gold!")

# Stap 4 en 5 - Items kopen en inventory bekijken

while True:
    print("\n=== Fantasy Item Shop ===")
    print("1. Buy Sword (50 gold)")
    print("2. Buy Shield (40 gold)")
    print("3. Buy Potion (20 gold)")
    print("4. Buy Bow (60 gold)")
    print("5. View Inventory")
    print("6. Exit Shop")

    keuze = input("\nWhat would you like to do? ")

    match keuze:
        case "1":
            buy_item("Sword", 50)

        case "2":
            buy_item("Shield", 40)

        case "3":
            buy_item("Potion", 20)

        case "4":
            buy_item("Bow", 60)

        case "5":
            if len(inventory) == 0:
                print("\nYour inventory is empty!")
            else:
                print("\nYour inventory:")
                for item in inventory:
                    print(f"- {item}")

        # Stap 6 - Winkel verlaten

        case "6":
            print(f"\nThanks for visiting, {player_name}!")
            print(f"You have {player_gold} gold left.")
            break

        case _:
            print("\nInvalid choice. Please choose between 1 and 6.")
