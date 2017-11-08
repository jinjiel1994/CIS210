"""
    Author = Jinjie(Jim) Li ID:951532421
    Passphrase = Chadwick

    pigLatin

"""

import argparse

def pigLatinWord(word):
    a = word[0]
    i = word[1:len(word)-2] + a + word[len(word)-2:]
    return i
    

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

    
    
