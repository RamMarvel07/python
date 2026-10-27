# Experiment 12: User Login and Regular Expression Validation in Django

## Aim
To develop a web application using the Django framework demonstrating user registration, login authentication, and input validation using Python's Regular Expressions (`re` module).

---

## Regular Expression Rules Used

1. **Username Validation**:
   - `^[a-zA-Z][a-zA-Z0-9_]{3,14}$`
   - Must start with a letter.
   - Length between 4 to 15 characters.
   - Allowed characters: Letters, digits, and underscores.

2. **Email Validation**:
   - `^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$`
   - Validates proper domain format with `@` and valid extension.

3. **Password Validation**:
   - `^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$`
   - Minimum 8 characters.
   - At least 1 lowercase letter.
   - At least 1 uppercase letter.
   - At least 1 numeric digit.
   - At least 1 special character from `@$!%*?&`.

---

## Project Structure

```text
Django_Exp12_SimpleLogin/
│
├── manage.py
├── db.sqlite3
│
├── exp12_project/
│   ├── __init__.py
│   ├── settings.py
│   └── urls.py
│
└── auth_app/
    ├── __init__.py
    ├── apps.py
    ├── models.py
    ├── views.py              <-- Contains regex logic & auth
    └── templates/
        ├── login.html
        ├── register.html
        └── welcome.html
```

---

## How to Run

1. Open PowerShell / Command Prompt and navigate to the directory:
   ```powershell
   cd c:\Users\shiva\Desktop\APC\python\Django_Exp12_SimpleLogin
   ```

2. Start the server:
   ```powershell
   python manage.py runserver
   ```

3. Open **`http://127.0.0.1:8000/`** in your browser.

---

## Pre-Created Demo Credentials

- **Username**: `student1`
- **Password**: `Student@123`
