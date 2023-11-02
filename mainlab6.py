# Aryan Agrawal
def encode_password(user_inp):
    password_enc = ""
    for i in str(user_inp):
        i = int(i) + 3
        password_enc += str(i)
    return password_enc

def main():
    password_enc = 0
    while True:
        print("Menu\n-------------")
        print("1. Encode\n2. Decode\n3. Quit\n")
        user_opt = input(print("\nPlease enter an option: "))
        if user_opt == "1":
            user_inp = input(print("Please enter your password to encode: "))
            x = encode_password(user_inp)
            y = decode_password(x)
            print("Your password has been encoded and stored!")
        elif user_opt == "2":
            print(f'Your encoded password is {x}, and the original password is {y}.')
        elif user_opt == "3":
            break
main()
