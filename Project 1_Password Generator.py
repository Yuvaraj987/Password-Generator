import random
import string

def pswd(length=12, use_numbers=True, use_symbols=True):
    if not (use_numbers or use_symbols):
        raise ValueError
    
    char_pool = ""
    if use_numbers:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    password = "".join(random.choice(char_pool) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter Password Length: "))
    use_numbers = input("Include Numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include Symbols? (y/n): ").strip().lower() == 'y'

    try:
        password = pswd(length, use_numbers, use_symbols)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")