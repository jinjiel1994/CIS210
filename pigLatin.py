"""
    Author = Jinjie(Jim) Li ID:951532421
    Passphrase = Chadwick

    pigLatin

"""

import argparse

def pigLatinWord(word):
    word = list(word)
    a = word[0]
    for i in range(1, len(word)-2):
        if i == len(word)-3:
            word[i-1] = word[i]
            word[i] = a
        else:
            word[i-1] = word[i]
    word = "".join(word)
    return word
    

def pigLatinPhrase(wordlist):
    for i in range(len(wordlist)):
        wordlist[i] = pigLatinWord(wordlist[i])
    return wordlist



def main():
    parser = argparse.ArgumentParser (description="pigLatin")
    parser.add_argument("phrase", type=str, help="Enter a word: python")
    args = parser.parse_args()
    wordlist = args.phrase.split()
    pigLatinPhrase(wordlist)
    print(' '.join(wordlist))

if __name__ == "__main__":
    main()

    
    
