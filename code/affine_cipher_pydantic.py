import pydantic
import argparse
from typing import Optional

class CoprimeError(Exception):
    def __init__(self, x: int, y: int, message: str) -> None:
        self.x = x
        self.y = y
        self.message = message
        super().__init__(message)

class AffineCipher(pydantic.BaseModel):
    alphabet: Optional[str] = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
    a: int
    b: int
    message: str

    def letter_to_index(self, letter):
        return self.alphabet.index(letter)

    def index_to_letter(self, index):
        return self.alphabet[index]

    @pydantic.validator("a")
    @classmethod
    def a_is_coprime_m(cls, value, values) -> int:
        def gcd(a, b):
            while b != 0:
                t = b
                b = a % b
                a = t
            return a

        if (gcd(value, len(values['alphabet'])) != 1):
            raise CoprimeError(x=value, y=len(values['alphabet']), message="`a` has to be coprime to the length of the alphabet")

        return value
    
    def encrypt(self):
        coded_message_numbered = [(self.a * self.letter_to_index(letter) + self.b) % len(self.alphabet) for letter in self.message]
        
        return "".join([self.index_to_letter(index) for index in coded_message_numbered])

    def decrypt(self):
        decrypted_message_numbered = [(pow(self.a, -1, len(self.alphabet)) * (self.letter_to_index(letter) - self.b)) % len(self.alphabet) for letter in self.message]

        return "".join([self.index_to_letter(index) for index in decrypted_message_numbered])

def parse_arguments():
    parser = argparse.ArgumentParser(exit_on_error=True,
                                     description="""An affine cipher encrypts a message with the following equation `(ax+b) % m`.
                                                    Decryption is done with `(a^-1)(x-b) % m`. `m` is the length of the alphabet used.""")

    parser.add_argument('mode', help="<decrypt> | <encrypt>", type=str)
    parser.add_argument('a', type=int)
    parser.add_argument('b', type=int)
    parser.add_argument('message', type=str)
    parser.add_argument('--alphabet', help="Alphabet used. (default = 'a-Z 1-9 ` `)", type=str)

    args = parser.parse_args()

    if args.mode not in ['decrypt', 'encrypt']:
        parser.error(f"Mode can't be `{args.mode}`. Only accepted values are `decrypt` or `encrypt`")

    return args

if __name__ == "__main__":
    args = parse_arguments()
    
    if args.alphabet == None:
        affine_cipher = AffineCipher(a=args.a, b=args.b, message=args.message)
    else:
        affine_cipher = AffineCipher(a=args.a, b=args.b, message=args.message, alphabet=args.alphabet)

    if args.mode == 'encrypt':
        print(affine_cipher.encrypt())
    elif args.mode == 'decrypt':
        print(affine_cipher.decrypt())