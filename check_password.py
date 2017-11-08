MINIMUN_LENGTH = 6
import argparse

def check_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    if len(password) < MINIMUN_LENGTH:
        return False
    for ch in password:
        if ch.isalnum():
            if ch.isupper():
                has_upper = True
            elif ch.islower():
                has_lower = True
            else:
                has_digit = True
        else:
            has_special = True
    return has_upper and has_lower and has_digit and has_special

def main():
    parser = argparse.ArgumentParser(description="Check validity of password")
    parser.add_argument ('Password', type=str, help="proposed password (a string)")
    args = parser.parse_args()
    passwd = args.Password
    if check_password(passwd):
        print(passwd, "is a legal password")
    else:
        print(passwd, "is an illegal password")


if __name__ == "__main__":
    main()