# Python Password Generator

This project is a simple Python script that generates a **secure, random password** using a mix of letters, numbers, and symbols. It is designed to create long, hard-to-guess passwords without requiring any user input.

By default, the script generates a **60-character password**, making it suitable for high-security use cases.

## Requirements

* Python 3 or newer
* No external libraries are required

## How It Works

The script uses Python’s built-in `secrets` module to generate cryptographically secure random characters. These characters are selected from a combined pool of:

* Uppercase letters
* Lowercase letters
* Digits
* Punctuation symbols

Once the characters are generated, the password is shuffled to ensure randomness in character order before being returned and displayed.

## Usage

Run the script from the command line:

python password_generator.py

After running, the generated password will be printed directly to the terminal.

## Customization

The password length can be changed by modifying the `length` variable inside the `generate_password()` function.

Example:

* `length = 30` → generates a 30-character password
* `length = 100` → generates a 100-character password

No other changes are required.

## Notes

* The script generates a new password every time it is run
* Passwords are displayed in plain text in the terminal
* The script does not store or log generated passwords
