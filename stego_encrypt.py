import cv2
import os
import hashlib

img = cv2.imread("img1.png")  # Replace with the correct image path

msg = input("Enter secret message:") + '\0'  # Append termination character
password = input("Enter a passcode:")

# Store password in MD5 format
password_hash = hashlib.md5(password.encode()).hexdigest()
with open("password.txt", "w") as f:
    f.write(password_hash)

d = {}
for i in range(256):  # Include 256 to cover all possible byte values
    d[chr(i)] = i

n = 0
m = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    z = (z + 1) % 3
    if z == 0:
        m = (m + 1) % img.shape[1]
        if m == 0:
            n = (n + 1) % img.shape[0]

cv2.imwrite("encryptedImage.png", img)
os.system("start encryptedImage.png")  # Use 'start' to open the image on Windows
