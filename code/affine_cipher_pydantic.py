import pydantic
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
        
        return "".join([self.index_to_letter(index) for index in coded_message])

    def decrypt(self):
        decrypted_message_numbered = [(pow(self.a, -1, len(self.alphabet)) * (self.letter_to_index(letter) - self.b)) % len(self.alphabet) for letter in self.message]

        return "".join([self.index_to_letter(index) for index in decrypted_message_numbered])

affine_cipher = AffineCipher(a=5, b=8, message="GeetS dQtbo l")
print(affine_cipher.decrypt())