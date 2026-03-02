# 🔐 Strong Password Generator

A secure and user-friendly password generator built using Python.  
This application generates strong random passwords containing letters, numbers, and special characters using Python's built-in `secrets` module for cryptographic security.

---

## 📌 Project Overview

In today’s digital world, strong passwords are essential for protecting personal and professional data.  
This project was developed as part of an internship task to demonstrate:

- Understanding of loops
- String handling in Python
- Working with built-in modules
- Secure random password generation

The program allows users to enter a desired password length and generates a secure password accordingly.

---

## 🚀 Features

✅ User-defined password length  
✅ Includes uppercase and lowercase letters  
✅ Includes digits (0-9)  
✅ Includes special characters (!@#$%^&*)  
✅ Ensures at least:
- 1 letter  
- 1 digit  
- 1 symbol  
✅ Uses Python's `secrets` module for cryptographically secure randomness  
✅ Input validation for incorrect values  

---

## 🛠 Technologies Used

- Python 3
- Built-in Modules:
  - `string`
  - `secrets`

No external libraries are required.

---

## 🧠 How It Works

1. The user enters the desired password length.
2. The program checks if the length is valid (minimum 4 characters).
3. It ensures the password contains:
   - At least one letter
   - At least one number
   - At least one special character
4. Remaining characters are randomly selected.
5. The password is shuffled for extra security.
6. The final strong password is displayed.

---

## 📂 Project Structure

```
strong-password-generator/
│
├── password_generator.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ▶️ How to Run the Program

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/strong-password-generator.git
```

### Step 2: Navigate to project folder

```bash
cd strong-password-generator
```

### Step 3: Run the program

```bash
python password_generator.py
```

---

## 💻 Sample Output

### Example 1

```
Enter password length: 12
Generated Password: A9#fL2@xQ!p1
```

### Example 2

```
Enter password length: 8
Generated Password: t7$Gk@2Z
```

### Example 3 (Invalid Input)

```
Enter password length: 2
Password length should be at least 4.
```

### Example 4 (Non-numeric Input)

```
Enter password length: abc
Please enter a valid number.
```

---

## 🔒 Why Use `secrets` Instead of `random`?

The `random` module is suitable for general purposes but not recommended for generating secure passwords.

The `secrets` module:
- Provides cryptographically strong random numbers
- Is recommended for security-sensitive applications
- Is safer for password generation

---

## 🎯 Learning Outcomes

Through this project, the following concepts were practiced:

- Python loops
- String concatenation
- Lists and shuffling
- Input validation
- Error handling using try-except
- Secure coding practices

---

## 📈 Future Improvements

- Add a graphical user interface (GUI)
- Add option to save password to a file
- Add strength checker
- Convert into a web application
- Add command-line arguments support

---

## 📄 License

This project is created for educational and internship purposes.

---

## 👨‍💻 Author

Developed as part of an internship task.
