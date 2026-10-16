# O(N^2) - Quadratic Time
# NESTED LOOPS
# Every item in the input is compared to every other item in the input.
# The time taken to execute the function grows quadratically with the size of the input.

def find_duplicate_pairs(numbers):
    duplicates = []
    # i starts from 0 to [len(numbers) - 1] = 5 
    for i in range(len(numbers)):
        # j starts from i + 1 to [len(numbers) - 1] = 5
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                duplicates.append((i, j))
    return duplicates
print(find_duplicate_pairs([1, 2, 3, 2, 3, 1]))  # Output: [(0, 5), (1, 3), (2, 4)]