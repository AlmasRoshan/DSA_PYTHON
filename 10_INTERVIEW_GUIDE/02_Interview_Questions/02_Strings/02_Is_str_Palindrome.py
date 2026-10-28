# Check if a string is Palindrome

def palindrome(str):
    str = str.lower()
    return str == str[::-1]
print(palindrome("Madam"))  # True 
print(palindrome("almas"))  # False