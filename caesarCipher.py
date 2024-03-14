from logo import logo

def caesar(texts, shiftAmount, direction):
    endText = ""

    if direction == "decode":
        shiftAmount *= -1 #This will make shift amount negetive

    for char in texts:
        if char not in alphabet:
            endText += char
            continue
        
        position = alphabet.index(char)
        newPosition = position + shiftAmount
        if newPosition > len(alphabet) - 1:
            newPosition -= 26
        newLetter = alphabet[newPosition]
        endText += newLetter
    print(f"The {direction}d text is {endText}")
    start = input("Do you want to restart cipher program: ").lower()
    return start

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def init(again):
    if again == "yes":
        print(logo)
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        if shift > len(alphabet):
            shift %= 26

        init(caesar(text,shift,direction))
    else:
        print("Goodby")

init("yes")