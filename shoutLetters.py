import argparse

SPACE = ' '

"""
    Author = Jinjie(Jim) Li ID:951532421
    Passphrase = Eisenhower
    shoutLetters - prints all characters within words of a phrase
    separated by a character (we'll start with a space, but later allow
    the option to specify the character used as a separator from the command line.
    Whitespace and punctuation are not printed with a hypen separator.
"""

def shoutLetters(phrase,sep):

    phrase = phrase.upper() # really shout out loud

    print(phrase[0],end="")
    phrase = phrase[1:]     # finished with first character


    for ch in phrase:
        if ch.isalnum() == True:      
            print(sep, ch, sep="", end="")
            phrase = phrase[1:]
    print()


if __name__ == "__main__":

    sep = SPACE
    parser = argparse.ArgumentParser(description="Shout Letters")
    parser.add_argument("phrase", type=str, help="Enter a phrase to shout")

    """
        Add an optional command line argument to specify which character to use as
        a separator.
    """


    args = parser.parse_args()

    shoutLetters(args.phrase, sep)
