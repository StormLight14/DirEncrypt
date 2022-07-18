from encrypt import Encrypt

encryptor = Encrypt()

while True:
    user_input = input("")
    if user_input == "e":
        encryptor.encrypt_files()
    elif user_input == "d":
        encryptor.decrypt_files()