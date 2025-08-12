import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Less than 8 characters"
    if not re.search(r"[A-Z]", password):
        return "Weak: No uppercase letter"
    if not re.search(r"[a-z]", password):
        return "Weak: No lowercase letter"
    if not re.search(r"\d", password):
        return "Weak: No number"
    if not re.search(r"[@$!%*?&]", password):
        return "Weak: No special character"
    return "Strong password"

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    print(check_password_strength(pwd))
