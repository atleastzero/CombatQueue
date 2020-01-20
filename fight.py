playerCharacters = ["Jenna", "Karen", "KeyboardInterupt"]
enemyCharacters = ["A seal", "An angel"]
fighters = []

def main():
    print("Hostility detected! Who's fighting?")

    for char in playerCharacters:
        if input(char + "? [y/n]: ") == 'y':
            number = int(input("What's their initiative?: "))
            fighters.append((number, char))

    for char in enemyCharacters:
        number = int(input("What's " + char + "'s initiative?: "))
        fighters.append((number, char))

    print(fighters)

    print("Ordered fighters:")
    fighters.sort()
    print(fighters)
    
if __name__ == "__main__":
    main() 