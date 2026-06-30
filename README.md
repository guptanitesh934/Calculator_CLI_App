# Welcome to Calculator CLI App

A robust Command Line Interface (CLI) calculator written in Python. This upgraded version supports both integer and floating-point (decimal) calculations and includes error handling for safer execution.

## Features
*   **Multi-Type Number Support:** Accepts both whole numbers (e.g., `5`) and decimals (e.g., `5.5`) using Python's `float()` function.
*   **Core Arithmetic Operations:**
    *   Addition (`+`)
    *   Subtraction (`-`)
    *   Multiplication (`*`)
    *   Division (`/`)
*   **Error Handling:** Prevents application crashes by catching and notifying the user of **Division by zero** attempts.
*   **Input Validation:** Notifies the user if an invalid mathematical operator is entered.

## Prerequisites
*   **Python 3.x** installed on your system.
*   No external dependencies or libraries required.

## Installation & Execution
1. Download or copy the source code into a file named `calculator.py`.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the script using the command:
   ```bash
   python calculator.py
   ```

## Example Interaction
```text
=====Welcome to Calculator CLI App===== 

Enter the first number: 10.5
Enter the second number: 0

Enter the Mathematical Operator: /

Error! Division by zero is not allowed
```

---
*Developed by Nitesh*
