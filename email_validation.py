#python code to take user email ID and validate its format
import re
from colorama import Fore, Style, init

init(autoreset=True)

def validate_email(email):
    # Define a regex pattern for validating an Email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

# Take user input
print(Fore.CYAN + "=" * 50)
print(Fore.CYAN + "Email Validation Tool".center(50))
print(Fore.CYAN + "=" * 50)
user_email = input(Fore.YELLOW + "\nEnter your email ID: " + Style.RESET_ALL)

# Validate the email and print the result
print(Fore.CYAN + "-" * 50)
if validate_email(user_email):
    print(Fore.GREEN + "✓ Valid email ID")
else:
    print(Fore.RED + "✗ Invalid email ID")
print(Fore.CYAN + "-" * 50 + "\n")
