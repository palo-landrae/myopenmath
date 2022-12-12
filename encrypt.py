def main():
    run = True
    alphabet()
    print(
        "1. Encrypt\n"
        "2. Decrypt\n"
        "3. Encrypt Scalar\n"
        "4. Print shifted alphabet\n"
        "5. Exit/Quit\n"
    )
    while run:
        operation = int(input("\nWhat would you like to do? "))
        if operation == 1:
            get_user_input()
            print(encrypt(plaintext, n_shift), "\n")
        elif operation == 2:
            get_user_input()
            print(decrypt(plaintext, n_shift), "\n")
        elif operation == 3:
            get_user_input()
            print(encrypt_scalar(plaintext, n_shift), "\n")
        elif operation == 4:
            print(shift())
        elif operation == 5:
            print("Program terminated!")
            run = False
        else:
            print("Invalid input, please try again...")


def encrypt(cypher, n_shift):
    shifted_alphabet = alphabet_upper[n_shift:] + alphabet_upper[:n_shift]
    table = str.maketrans(alphabet_upper, shifted_alphabet)
    return cypher.translate(table)


def decrypt(cypher, n_shift):
    shifted_alphabet = alphabet_upper[n_shift:] + alphabet_upper[:n_shift]
    table = str.maketrans(shifted_alphabet, alphabet_upper)
    return cypher.translate(table)


def encrypt_scalar(plaintext, n_shift):
    result = []
    for i in range(len(plaintext)):
        shifted_alphabet = alphabet_upper[n_shift +
                                          i:] + alphabet_upper[:n_shift+i]
        table = str.maketrans(alphabet_upper, shifted_alphabet)
        result.append(plaintext[i].translate(table))
    return ''.join(result)


def shift():
    print("0. Left\n1. Right")
    direction = int(input("Enter direction: "))
    n_shift = int(input("Enter shift: "))
    shifted_alphabet = alphabet_upper[(
        n_shift if direction else -n_shift):] + alphabet_upper[:(n_shift if direction else -n_shift)]
    print('|'.join(alphabet_upper))
    return '|'.join(shifted_alphabet)


def get_user_input():
    global plaintext
    global n_shift
    plaintext = input("Enter text: ").upper()
    n_shift = int(input("Enter shift: "))


def alphabet():
    global alphabet_upper
    alphabet_upper = ''.join([chr(ascii) for ascii in range(65, 91)])


if __name__ == "__main__":
    main()
