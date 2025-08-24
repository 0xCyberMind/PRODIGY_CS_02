import matplotlib.pyplot as plt
import numpy as np

def encrypt_image(input_path, output_path, key):
    """
    Encrypt an image using a simple XOR operation.

    How it works:
      - Reads the image and converts it into pixel values (0–255).
      - Each pixel is combined with the given key using XOR (^) operation.
      - The result is saved as a new image file.

    Args:
        input_path (str): Path of the original image.
        output_path (str): Where to save the encrypted image.
        key (int): A number between 0 and 255 used as the secret key.
    """
    # Read the image as numbers (float between 0 and 1)
    img = plt.imread(input_path)

    # Convert float values (0–1) into 8-bit integers (0–255)
    img_uint8 = (img * 255).astype(np.uint8)

    # Apply XOR with the key → this scrambles the pixel values
    encrypted_uint8 = np.bitwise_xor(img_uint8, key)

    # Convert back to float (0–1) so matplotlib can save it properly
    encrypted = encrypted_uint8.astype(np.float32) / 255.0

    # Save the result
    plt.imsave(output_path, encrypted)
    print(f"✅ Encrypted image saved as: {output_path}")


def decrypt_image(input_path, output_path, key):
    """
    Decrypt an image encrypted with XOR.

    Note:
        XOR is its own reverse — applying the same operation again with the same key
        restores the original image.

    Args:
        input_path (str): Path of the encrypted image.
        output_path (str): Where to save the decrypted image.
        key (int): The same number that was used for encryption.
    """
    # Decryption = Encryption with the same key
    encrypt_image(input_path, output_path, key)
    print(f"🔓 Decrypted image saved as: {output_path}")


# Example usage:
# encrypt_image("my_photo.jpg", "secret.jpg", 123)
# decrypt_image("secret.jpg", "restored.jpg", 123)
