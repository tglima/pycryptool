from crypto.crypto_console import CryptoConsole


class Cryptool:
    """Classe intermediaria, reponsavel por encapsular a logica do crypto"""

    def __init__(self, user_key=None):
        self.crypto_console = CryptoConsole(user_key)

    def txt_encrypt(self, txt):
        return self.crypto_console.txt_encrypt(txt)

    def txt_decrypt(self, txt):
        return self.crypto_console.txt_decrypt(txt)
