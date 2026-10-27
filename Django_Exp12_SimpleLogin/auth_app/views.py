"""
views.py - Simple, clean views demonstrating regex validation
"""
import re
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# ----------------- REGULAR EXPRESSION PATTERNS -----------------
# 1. Username: 4 to 15 chars, alphanumeric or underscore, starts with a letter
USERNAME_PATTERN = r'^[a-zA-Z][a-zA-Z0-9_]{3,14}$'

# 2. Email: standard email format (name@domain.com)
EMAIL_PATTERN = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# 3. Password: at least 8 chars, 1 uppercase, 1 lowercase, 1 number, 1 special char
PASSWORD_PATTERN = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'


# ----------------- LOGIN VIEW -----------------
def login_view(request):
    error = None
    if request.method == 'POST':
        u_name = request.POST.get('username', '').strip()
        p_word = request.POST.get('password', '').strip()

        # Step 1: Validate inputs with Regular Expressions
        if not re.match(USERNAME_PATTERN, u_name):
            error = "Invalid Username format! Must start with a letter, 4-15 alphanumeric characters."
        elif len(p_word) < 8:
            error = "Password must be at least 8 characters long."
        else:
            # Step 2: Authenticate user in database
            user = authenticate(request, username=u_name, password=p_word)
            if user is not None:
                login(request, user)
                return redirect('welcome')
            else:
                error = "Incorrect Username or Password!"

    return render(request, 'login.html', {'error': error})


# ----------------- REGISTER VIEW -----------------
def register_view(request):
    error = None
    success = None

    if request.method == 'POST':
        u_name = request.POST.get('username', '').strip()
        email  = request.POST.get('email', '').strip()
        p_word = request.POST.get('password', '').strip()
        c_word = request.POST.get('confirm_password', '').strip()

        # Regular Expression Validation Checks
        if not re.match(USERNAME_PATTERN, u_name):
            error = "Username must start with a letter and have 4-15 letters/digits/underscores."
        elif not re.match(EMAIL_PATTERN, email):
            error = "Please enter a valid email address (e.g., student@college.edu)."
        elif not re.match(PASSWORD_PATTERN, p_word):
            error = "Password must be min 8 chars and include 1 uppercase, 1 lowercase, 1 digit, and 1 special symbol (@$!%*?&)."
        elif p_word != c_word:
            error = "Passwords do not match!"
        elif User.objects.filter(username=u_name).exists():
            error = "Username already taken! Please pick another."
        else:
            # Create user
            User.objects.create_user(username=u_name, email=email, password=p_word)
            success = "Registration successful! You can now log in."

    return render(request, 'register.html', {'error': error, 'success': success})


# ----------------- WELCOME / DASHBOARD -----------------
@login_required(login_url='login')
def welcome_view(request):
    return render(request, 'welcome.html', {
        'username': request.user.username,
        'email': request.user.email
    })


# ----------------- LOGOUT -----------------
def logout_view(request):
    logout(request)
    return redirect('login')
