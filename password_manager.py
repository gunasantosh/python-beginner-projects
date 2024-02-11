from cryptography.fernet import Fernet

"""
def write_key():
    key = Fernet.generate_key()
    with open("pwd_manager_key.key", "wb") as key_file:
        key_file.write(key)
"""


def load_key():
    file = open("pwd_manager_key.key", "rb")
    key = file.readline()
    file.close()
    return key


key = load_key()
f = Fernet(key)


def view():
    with open("pwd_manager_passwords.txt", "r") as file:
        for line in file.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            decrypted_passw = f.decrypt(passw.encode()).decode()
            print("User:", user, "| Password:", decrypted_passw)


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    encrypted_pwd = f.encrypt(pwd.encode()).decode()
    with open("pwd_manager_passwords.txt", "a") as file:
        file.write(name + "|" + encrypted_pwd + "\n")


while True:
    mode = input("Choose a mode (view/add/quit): ").lower()
    if mode == "quit":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode choice")
        continue
