# Password Generator

This project provides a command-line application to generate strong, secure passwords. It is designed to help users create customizable passwords for personal or professional use, ensuring better security for online accounts and systems.

## Features
1. **Customizable Password Length**:
   - Define the length of the password as per your needs.

2. **Character Options**:
   - Include or exclude:
     - Uppercase letters
     - Numbers
     - Special characters

3. **Randomization**:
   - Uses Python's `random` library to generate truly randomized passwords.

4. **User-Friendly Interface**:
   - Simple and intuitive prompts to guide the user through the process.

## Requirements
- Python 3.x

## How to Run
1. Clone this repository to your local machine:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd project-directory
   ```
3. Run the program:
   ```bash
   python password_generator.py
   ```

## Usage
1. Run the program in your terminal.
2. Enter the desired password length.
3. Choose whether to include uppercase letters, numbers, and special characters.
4. View the generated password.

### Example Interaction
```bash
Welcome to the Password Generator!

Enter the desired password length (e.g., 12): 16
Include uppercase letters? (yes/no): yes
Include numbers? (yes/no): yes
Include special characters? (yes/no): yes

Your generated password is: Ab8!dF@2xPq#3zY&
```

## How It Works
1. The script uses the `string` module to define sets of characters (lowercase, uppercase, digits, and special characters).
2. Based on the user's input, the character pool is built.
3. A password of the desired length is generated by randomly sampling from the pool using `random.choices()`.

## Limitations
- No option to exclude similar-looking characters (e.g., `l`, `I`, `1`, `O`, `0`).
- Cannot save generated passwords directly to a file (can be added as an enhancement).

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests with enhancements or bug fixes.

## Contact
If you have questions or suggestions, feel free to open an issue or contact the maintainer.
