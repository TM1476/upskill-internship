from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_password(key, password):
    cipher = Fernet(key)
    return cipher.encrypt(password.encode())

def decrypt_password(key, encrypted_password):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_password).decode()

def main():
    try:
        key = generate_key()
        print("Key generated (keep safe):", key.decode())

        password = input("Enter password: ")

        encrypted = encrypt_password(key, password)
        print("Encrypted Password:", encrypted.decode())

        decrypted = decrypt_password(key, encrypted)
        print("Decrypted Password:", decrypted)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
