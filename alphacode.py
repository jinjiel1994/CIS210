"""
alphacode.py: Convert PIN code to mnemonic alphabetic code
Athor: Jinjie(Jim) li ID:951532421
Credits: Information from canvas

CIS 210 assingment 1, Fall 2015.
"""

consonants = 'bcdfghjklmnpqrstvwyz'

vowels = 'aeiou'

def argpharse(pin):
    a = pin % 100 # take out the last two digits
    i = a//5
    j = a%5
    mnemonic = consonants[i] + vowels[j]
    pin = pin//100
    while pin > 0:
        a = pin % 100
        i = a//5
        j = a%5
        mnemonic = consonants[i] + vowels[j] + mnemonic
        pin = pin//100
    return mnemonic

def main():
    pin = input ('PIN code:')
    pin = int(pin)
    result = argpharse(pin)
    print("Memorable PIN:", result)


if __name__ == "__main__":
    main()