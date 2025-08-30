# PRODIGY_CS_02
Task 2: Image Encryption & Decryption using Pixel Manipulation

# Image Encryption and Decryption Using XOR

This Python project demonstrates a basic form of image encryption using the XOR bitwise operation. It allows you to encrypt and decrypt an image by applying a secret key (an integer value between 0 and 255) to scramble and unscramble pixel data.

## Features

- **Encrypt**: Scrambles the image pixels with a key.
- **Decrypt**: Restores the original image using the same key (XOR is reversible).
- **Simple**: A straightforward demonstration of XOR encryption for educational purposes.
- **Tools Used**: Python, NumPy, and Matplotlib for image processing.

## How It Works

1. **Encryption**:
    - The image is read and converted into pixel values ranging from 0 to 255.
    - The pixel values are then XORed with a secret key.
    - The encrypted image is saved.

2. **Decryption**:
    - The encrypted image is XORed again with the same key.
    - The original image is restored.

**Note**: XOR encryption is symmetric, meaning that encrypting and decrypting uses the same key.

## Requirements

- Python 3.x
- Libraries: `matplotlib`, `numpy`

Install required libraries using pip:

```bash
pip install matplotlib numpy
```
## Functions

  encrypt_image(input_path, output_path, key)

  Encrypts an image using XOR with the specified key.

## Arguments:

  input_path: Path to the image you want to encrypt (e.g., image.jpg).

  output_path: Path to save the encrypted image (e.g., encrypted_image.jpg).

  key: An integer between 0 and 255 used as the secret key.
  
  decrypt_image(input_path, output_path, key)

  Decrypts an image that was encrypted using the XOR method. It uses the same key to restore the original image.

## Example Usage

  Encrypt an Image
    
   ```bash
    encrypt_image("my_photo.jpg", "encrypted_photo.jpg", 123)
 ```
## Decrypt an Image

 ```bash
    decrypt_image("encrypted_photo.jpg", "restored_photo.jpg", 123)
 ```
## Caution

  This encryption method is not secure for real-world applications. It's only meant for educational purposes to understand how basic XOR encryption works.

  The XOR operation is symmetric, so the encryption and decryption use the same key.

##  Author

  Your Name – Bhaskar uttam 


