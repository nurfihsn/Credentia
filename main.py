import random
import string

def generate_username(name):
    base = name.lower().replace(" ", "")
    return f"{base}{random.randint(10, 9999)}"

def generate_email(username):
    domains = ["example.com", "test.com", "mail.test"]
    return f"{username}@{random.choice(domains)}"

def generate_phone():
    prefix = "+62"
    number = "".join(random.choices(string.digits, k=random.randint(9, 11)))
    return prefix + number

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(length))

def main():
    print("=== Data Generator ===")
    name = input("Masukkan nama: ").strip()

    print("\nHasil Generate:\n")

    for i in range(1, 6):
        username = generate_username(name)
        email = generate_email(username)
        phone = generate_phone()
        password = generate_password()

        print(f"Data {i}")
        print(f"Nama      : {name}")
        print(f"Username  : {username}")
        print(f"Email     : {email}")
        print(f"Telepon   : {phone}")
        print(f"Password  : {password}")
        print("-" * 30)

if __name__ == "__main__":
    main()