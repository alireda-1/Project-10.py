# Random PIN Verification System

A smart and interactive **Python** script that simulates a secure PIN code verification system, utilizing randomization and string formatting for data validation.

## Features
- **Dynamic PIN Generation:** Leverages Python's built-in `random` module to generate a unique computer PIN code.
- **Smart Formatting:** Employs the `.zfill(4)` method to guarantee the generated code always maintains a strict 4-digit structure (padding with leading zeros if necessary).
- **Two-Layer Validation:** First checks if the user input meets the exact 4-digit length requirement, then validates whether it matches the computer-generated security code.

## Technologies Used
- Python 3
