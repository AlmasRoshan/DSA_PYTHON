# Count Vowels and Consonants

def count_vc(str):
    vowels = "aeiou"
    result = [ch for ch in str.lower() if ch]
    v_count = sum(1 for ch in result if ch in vowels)
    c_count = len(result) - v_count
    return f"vowels count: {v_count}, consonants count: {c_count}"
print(count_vc("Namaste"))