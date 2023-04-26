from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)

def Generation_key():
    public_key = key.publickey().export_key()
    private_key = key.export_key()

    public_file = open('Server_Public_Key.pem', 'wb')
    private_file = open('Server_Private_Key.pem', 'wb')

    public_file.write(public_key)
    private_file.write(private_key)

    public_file.close()
    private_file.close()

def encrypt_text(msg):
    public_file = open('Client_Public_Key.pem', 'rb')
    rsa_encryption = PKCS1_OAEP.new(RSA.import_key(public_file.read()))
    encrypted_data = rsa_encryption.encrypt(bytes(msg, 'utf-8'))
    public_file.close()
    return encrypted_data


def decrypt_text(en_msg):
    private_file = open('Server_Private_Key.pem', 'rb')
    rsa_decryption = PKCS1_OAEP.new(RSA.import_key(private_file.read()))
    decrypted_data = rsa_decryption.decrypt(en_msg)
    private_file.close()
    return decrypted_data.decode()







