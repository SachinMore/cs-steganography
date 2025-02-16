import cv2
import hashlib

img = cv2.imread("encryptedImage.png")  # Replace with the correct image path

# Read stored password hash
with open("password.txt", "r") as f:
    stored_password_hash = f.read().strip()

c = {}
for i in range(256):
    c[i] = chr(i)

message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption:")
# Verify password
input_password_hash = hashlib.md5(pas.encode()).hexdigest()
if stored_password_hash == input_password_hash:
    while True:
        char = c[img[n, m, z]]
        if char == '\0':  # Check for termination character
            break
        message += char
        z = (z + 1) % 3
        if z == 0:
            m = (m + 1) % img.shape[1]
            if m == 0:
                n = (n + 1) % img.shape[0]
    print("Secret Message:", message)
else:
    print("YOU ARE NOT auth")
