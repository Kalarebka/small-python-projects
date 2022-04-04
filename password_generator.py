# Usage: python3 password_generator [length] [separator]
from urllib.request import urlopen
import secrets
import sys

WORD_FILE = "data/eff_large_wordlist.txt"
WORD_FILE_URL = "https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt"


def read_words_data():
    try:
        with open(WORD_FILE, "r") as f:
            words = [line.split()[1].strip() for line in f.readlines()]
    except FileNotFoundError:
        with urlopen(WORD_FILE_URL) as wordlist:
            data = wordlist.read().decode().split()
            words = [word.strip() for word in data if word.isalpha()]
    return words


def generate_passphrase(length=6, separator=" "):
    words = read_words_data()
    return separator.join(secrets.choice(words) for i in range(length))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(generate_passphrase())
    elif len(sys.argv) == 2:
        print(generate_passphrase(int(sys.argv[1])))
    elif len(sys.argv) == 3:
        print(generate_passphrase(int(sys.argv[1]), sys.argv[2]))

