# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
#
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

def longest_substring(s, k):
    max_longest = ""
    for x in range(len(s)):
        used_letters = set()
        longest = ""
        for y in range(x, len(s)):
            if (len(used_letters) < k) or s[y] in used_letters:
                used_letters.add(s[y])
                longest = longest + s[y]
            else:
                break

        if len(longest) > len(max_longest):
            max_longest = longest
    return max_longest


def longest_substring_with_k_distinct_characters(s, k):
    if k == 0:
        return 0

    # Keep a running window
    bounds = (0, 0)
    h = {}
    max_length = 0
    for i, char in enumerate(s):
        h[char] = i
        if len(h) <= k:
            new_lower_bound = bounds[0] # lower bound remains the same
        else:
            # otherwise, pop last occurring char
            key_to_pop = min(h, key=h.get)
            new_lower_bound = h.pop(key_to_pop) + 1

        bounds = (new_lower_bound, bounds[1] + 1)
        max_length = max(max_length, bounds[1] - bounds[0])

    return max_length


def main():
    string = "abcba"
    #longest = longest_substring(string, 2)
    longest = longest_substring_with_k_distinct_characters(string, 2)
    print(longest)

main()