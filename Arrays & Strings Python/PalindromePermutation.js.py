# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# 1.5
# 1.6
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)

def generate_palindrome(string):
    # Count the number of occurrences of each character in the string
    char_counts = {}
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    # Construct the even-character string and the odd-character string (if it exists)
    even_chars = ""
    odd_char = None
    for char, count in char_counts.items():
        if count % 2 == 0:
            even_chars += char * (count // 2)
        else:
            if odd_char is not None:
                return None  # More than one character occurs an odd number of times
            odd_char = char

    # Construct the palindrome
    palindrome = even_chars + (odd_char or "") + even_chars[::-1]
    return palindrome


print(generate_palindrome("taco cat"))
