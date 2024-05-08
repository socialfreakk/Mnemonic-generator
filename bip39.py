import random
import os
import colorama
from colorama import init
init()
from colorama import Back, Style, Fore
import time
from urllib.request import urlopen
import mnemonic

def generate_mnemonic():
    wordlist_url = "https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt"
    response = urlopen(wordlist_url)
    wordlist = response.read().decode().splitlines()

    mnemonic = []
    while len(mnemonic) < 12:
        word = random.choice(wordlist)
        if word not in mnemonic:
            mnemonic.append(word)

    return " ".join(mnemonic)


def generate_seed(mnemonic_phrase):
    return mnemonic.Mnemonic("english").to_seed(mnemonic_phrase)


if __name__ == "__main__":
    while True:
        mnemonic_phrase = generate_mnemonic()
        seed = generate_seed(mnemonic_phrase)

        print(Fore.GREEN + f"phrase: {mnemonic_phrase}")
        print(f"seed: {seed.hex()}")