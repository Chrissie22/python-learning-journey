
def count_vowels(text):
    """Counts the number of vowels in a given string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
# You can add this test code at the bottom.
# The `if __name__ == "__main__":` block only runs
# when you run this file directly, not when it's imported.

if __name__ == "__main__":
    print("Testing the module...")
    print(f"Vowels in 'hello': {count_vowels('hello')}")
    
        
        