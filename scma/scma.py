import os
import json
import hashlib
import time
import getpass
from cryptography.fernet import Fernet

# Constants for file paths
DATA_FILE = "scma_data.json"
LOG_FILE = "scma_log.txt"
KEY_FILE = "encryption.key"

# Singleton Encryption Manager
class EncryptionManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EncryptionManager, cls).__new__(cls)
            cls._instance.key = cls.load_key()
            cls._instance.cipher = Fernet(cls._instance.key)
        return cls._instance

    @staticmethod
    def load_key():
        """
        Load or generate encryption key.
        :return: Encryption key
        """
        if os.path.exists(KEY_FILE):
            with open(KEY_FILE, "rb") as key_file:
                return key_file.read()
        else:
            key = Fernet.generate_key()
            with open(KEY_FILE, "wb") as key_file:
                key_file.write(key)
            return key

    def encrypt(self, data):
        if isinstance(data, bytes):
            return self.cipher.encrypt(data).decode()
        return self.cipher.encrypt(data.encode()).decode()

    def decrypt(self, data):
        decrypted = self.cipher.decrypt(data.encode())
        try:
            return decrypted.decode()
        except UnicodeDecodeError:
            return decrypted

# Pre-defined users with RBAC
USERS = {
    "admin": "admin123",
    "user": "user123"
}

# Roles and their permissions
ROLES = {
    "admin": ["create", "read", "update", "delete"],
    "user": ["create", "read", "update"]
}

def hash_content(content):
    if isinstance(content, str):
        content = content.encode()
    return hashlib.sha256(content).hexdigest()

def log_action(username, action, artefact_name):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {username} performed {action} on {artefact_name}\n")

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def authenticate():
    print("Available users: admin, user")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    if username in USERS and USERS[username] == password:
        print("Authentication successful!")
        return username
    else:
        print("Authentication failed.")
        return None

def create_artefact(username):
    if "create" not in ROLES[username]:
        print("Unauthorized action.")
        return

    name = input("Enter artefact name: ")
    artefact_type = input("Is this a text or file artefact? (text/file): ")
    enc_manager = EncryptionManager()
    data = load_data()

    if artefact_type == "text":
        content = input("Enter artefact content: ")
        encrypted_content = enc_manager.encrypt(content)
        checksum = hash_content(content)
    elif artefact_type == "file":
        file_path = input("Enter file path: ")
        if os.path.exists(file_path):
            try:
                with open(file_path, "rb") as file:
                    file_content = file.read()
                    encrypted_content = enc_manager.encrypt(file_content)
                    checksum = hash_content(file_content)
            except Exception as e:
                print(f"Error reading file: {e}")
                return
        else:
            print("File not found. Please provide a valid file path.")
            return
    else:
        print("Invalid artefact type.")
        return

    artefact = {
        "owner": username,
        "content": encrypted_content,
        "hash": checksum,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    data[name] = artefact
    save_data(data)
    log_action(username, "created", name)
    print("Artefact created successfully.")

def read_artefact(username):
    name = input("Enter artefact name to read: ")
    data = load_data()
    if name in data:
        artefact = data[name]
        if artefact["owner"] == username or username == "admin":
            enc_manager = EncryptionManager()
            decrypted_content = enc_manager.decrypt(artefact["content"])
            print(f"Content: {decrypted_content}")
            print(f"Hash: {artefact['hash']}")
            print(f"Timestamp: {artefact['timestamp']}")
            log_action(username, "read", name)
        else:
            print("Unauthorized action.")
    else:
        print("Artefact not found.")

def update_artefact(username):
    name = input("Enter artefact name to update: ")
    data = load_data()
    if name in data:
        artefact = data[name]
        if artefact["owner"] == username or username == "admin":
            new_content = input("Enter new content: ")
            enc_manager = EncryptionManager()
            encrypted_content = enc_manager.encrypt(new_content)
            artefact["content"] = encrypted_content
            artefact["hash"] = hash_content(new_content)
            artefact["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")
            save_data(data)
            log_action(username, "updated", name)
            print("Artefact updated successfully.")
        else:
            print("Unauthorized action.")
    else:
        print("Artefact not found.")

def delete_artefact(username):
    if username != "admin":
        print("Unauthorized action.")
        return

    name = input("Enter artefact name to delete: ")
    data = load_data()
    if name in data:
        del data[name]
        save_data(data)
        log_action(username, "deleted", name)
        print("Artefact deleted successfully.")
    else:
        print("Artefact not found.")

def main():
    print("Welcome to Secure Copyright Management Application (SCMA)")
    user = authenticate()
    if not user:
        return

    while True:
        print("\nOptions:")
        print("1. Create Artefact")
        print("2. Read Artefact")
        print("3. Update Artefact")
        if user == "admin":
            print("4. Delete Artefact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_artefact(user)
        elif choice == "2":
            read_artefact(user)
        elif choice == "3":
            update_artefact(user)
        elif choice == "4" and user == "admin":
            delete_artefact(user)
        elif choice == "5":
            print("Exiting application.")
            exit()  # Corrected to terminate the program
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
