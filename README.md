# Simple-Python-Encryptor

A lightweight, Python script built with the tkinter libary that allows the user to Encrypt and Decrypt messages with a fixed shift-key of 3 Caesar Cipher mechanism

* 🔒 **Instant Encryption:** Converts plain text into encrypted text using an ASCII shift cipher.
* 🔓 **Instant Decryption:** Restores scrambled text back to its original readable format.
* 📋 **Clipboard Integration:** A dedicated button to copy the output text with a single click.
* 🚫 **Secure Interface:** The output results box is strictly read-only to prevent accidental edits.

## ⚙️ How it Works

The application implements a classical **Caesar Cipher** variation operating on ASCII character code bounds:
1. **Spaces (` `)** are completely ignored and preserved to maintain natural sentence structures.
2. Every other character is shifted ahead by **3 positions** in the ASCII table during encryption.
3. Decryption shifts characters backward by **3 positions** to reveal the original message.

## 🔒 Security & Privacy

* **100% Offline:** This application runs entirely on your local machine. It does not connect to the internet, track data, or send your messages anywhere.
* It uses only standard Python libraries (`tkinter`), meaning you do not need to install any third-party packages
