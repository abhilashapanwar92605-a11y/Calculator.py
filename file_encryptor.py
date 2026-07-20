# File Encryption and Decryption using Caesar Cipher

SHIFT = 3

def encrypt(text):
    result = ""
    for char in text:
        result += chr(ord(char) + SHIFT)
    return result

def decrypt(text):
    result = ""
    for char in text:
        result += chr(ord(char) - SHIFT)
    return result

try:
    choice = input("Enter E to Encrypt or D to Decrypt: ").upper()

    file_name = input("Enter file name: ")

    with open(file_name, "r") as file:
        content = file.read()

    if choice == "E":
        encrypted_text = encrypt(content)

        with open("encrypted.txt", "w") as file:
            file.write(encrypted_text)

        print("File encrypted successfully.")
        print("Saved as encrypted.txt")

    elif choice == "D":
        decrypted_text = decrypt(content)

        with open("decrypted.txt", "w") as file:
            file.write(decrypted_text)

        print("File decrypted successfully.")
        print("Saved as decrypted.txt")

    else:
        print("Invalid choice!")

except FileNotFoundError:
    print("Error: File not found.")

except Exception as e:
    print("An error occurred:", e)