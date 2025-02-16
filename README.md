# Steganography Project

This project demonstrates a simple steganography technique to hide and retrieve secret messages within an image using Python. The project includes two main scripts: `stego_encrypt.py` for encryption and `stego_decrypt.py` for decryption.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- hashlib

You can install the required packages using pip:

```sh
pip install opencv-python
```

## Usage

### Encryption

The `stego_encrypt.py` script is used to hide a secret message within an image.

1. Place the image you want to use for steganography in the same directory as the script and name it `img1.png` (or modify the script to use a different image path).
2. Run the script:

```sh
python stego_encrypt.py
```

3. Enter the secret message and a passcode when prompted.
4. The script will generate an `encryptedImage.png` file with the hidden message and open it.

### Decryption

The `stego_decrypt.py` script is used to retrieve the hidden message from the encrypted image.

1. Ensure the `encryptedImage.png` file and `password.txt` file are in the same directory as the script.
2. Run the script:

```sh
python stego_decrypt.py
```

3. Enter the passcode when prompted.
4. If the passcode is correct, the script will display the hidden message.

## Files

- `stego_encrypt.py`: Script to hide a secret message within an image.
- `stego_decrypt.py`: Script to retrieve the hidden message from the encrypted image.
- `password.txt`: File to store the hashed passcode.

## Example

### Encryption

```sh
python stego_encrypt.py
```

```
Enter secret message: Hello, World!
Enter a passcode: mypasscode
```

### Decryption

```sh
python stego_decrypt.py
```

```
Enter passcode for Decryption: mypasscode
Secret Message: Hello, World!
```

## Notes

- The secret message is terminated with a null character (`\0`) to indicate the end of the message.
- The passcode is stored in a hashed format using MD5 for security.
- Ensure the image used for encryption is large enough to store the entire message.
