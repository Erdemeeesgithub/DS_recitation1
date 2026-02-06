def lengthOfLongestSubstring(s):
    # TODO: Please write your code here
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


# Do not change or remove the code below this point
def main():
    s = "abcabcbb"
    res = lengthOfLongestSubstring(s)
    print(res)  # Output: 3, Length of the substring “abc”

    # Example 2
    s = "bbbbb"
    res = lengthOfLongestSubstring(s)
    print(res)  # Output: 1, Length of the substring “b”


if __name__ == '__main__':
    main()
