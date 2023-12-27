# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 19:03:47 2023

@author: AUDREY_SURYA
"""

import cv2
import numpy as np

demo = cv2.imread("D:\Semester 3\Sistem Keamanan Data dan Praktiknya\RSA\Surya.jpg", 0)
r, c = demo.shape
key = np.random.randint(0, 256, size=(r, c), dtype=np.uint8)  # Generate random key image
cv2.imwrite("D:\Semester 3\Sistem Keamanan Data dan Praktiknya\RSA\key.jpg", key)   # Save key image

cv2.imshow("demo", demo)  # Display original image
cv2.imshow("key", key)  # Display key image

encryption = cv2.bitwise_xor(demo, key)  # encryption
cv2.imwrite("D:\Semester 3\Sistem Keamanan Data dan Praktiknya\RSA\enkripsisurya.jpg", encryption)     # Save the encrypted image
decryption = cv2.bitwise_xor(encryption, key)  # decrypt
cv2.imwrite("D:\Semester 3\Sistem Keamanan Data dan Praktiknya\RSA\dekripsisurya.jpg", decryption) # Save the decrypted image

cv2.imshow("encryption", encryption)  # Display ciphertext image
cv2.imshow("decryption", decryption)  # Displays the decrypted image

cv2.waitKey(-1)
cv2.destroyAllWindows()