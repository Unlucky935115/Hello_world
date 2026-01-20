# Python code to validate anagrams
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Sort the characters of both strings and compare
    return sorted(str1) == sorted(str2)
# Example usage
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False
print(are_anagrams("Astronomer", "Moon starer"))  # True
