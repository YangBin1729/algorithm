"""简单密码技术"""


class CaesarCipher:
    def __init__(self, shift):
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)
    
    def encrypt(self, message):
        return self._transform(message, self._forward)
    
    def decrpt(self, secret):
        return self._transform(secret, self._backward)
    
    def _transform(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)


def test_caesar_cipher():
    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY;MEET AT JOE'S"
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrpt(coded)
    print('Message: ', answer)


if __name__ == '__main__':
    test_caesar_cipher()