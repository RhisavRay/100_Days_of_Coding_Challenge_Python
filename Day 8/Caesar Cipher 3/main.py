decision = "yes"

while decision == "yes":
    function = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if function == "encode":
        message = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        result = ""
        for letter in message:
            result += chr(ord(letter) + 2)
        print(f"Here's the encoded result: {result}")
    else:
        message = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        result = ""
        for letter in message:
            result += chr(ord(letter) - 2)
        print(f"Here's the decoded result: {result}")

    decision = input("Type 'yes' if you want to go again. Otherwise type 'no'").lower()
print("Goodbye")