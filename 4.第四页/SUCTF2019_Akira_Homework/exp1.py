from Crypto.Cipher import AES
import base64

def aes_decrypt(ciphertext, key):
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(ciphertext))
    return decrypted.decode()
strCryptoText = b"\x94\xBF\x7A\x0C\xA4\x35\x50\xD1\xC2\x15\xEC\xEF\x9D\x9A\xAA\x56"

ciphertext = base64.b64encode(strCryptoText).decode()  # 要解密的内容
key = 'Ak1i3aS3cre7K3y'.ljust(16, '\0')  # 密码，使用zeropadding填充到16字节长度

plaintext = aes_decrypt(ciphertext, key)
print('解密结果:', plaintext)