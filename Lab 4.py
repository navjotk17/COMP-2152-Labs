def count_characters(s):
    counts = {}
    for char in s:
        if char in counts:  # e = 1 ===> e=2 ====> e=3 # leetcode
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def first_unique_character(s):
    char_counts = count_characters(s)
    for i in range(len(s)):
        if char_counts[s[i]] == 1:
            return i
    return -1








# Test cases
test_strings = ["leetcode", "loveleetcode", "aabb", "python", "aabbcc"]

for s in test_strings:
    index = first_unique_character(s)

    if index != -1:
        print("First unique character in '" + s + "': index " + str(index) + " (character: '" + s[index] + "')")
    else:
        print("First unique character in '" + s + "': index -1 (no unique character)")

    # Show the character counts for understanding
    counts = count_characters(s)
    print("  Character counts: " + str(counts))
    print()