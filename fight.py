

playerCharacters = ["Jenna", "Karen", "KeyboardInterupt"]
enemyCharacters = ["A seal", "An angel"]
fighters = []

def main():
    print("Hostility detected! Who's fighting?")

    for char in playerCharacters:
        if input(char+ "? [y/n]") == 'y':
            number = int(input("What's their initiative?"))
            fighters.append((number, char))
    print(fighters)

if __name__ == "__main__":
    main()