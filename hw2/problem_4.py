def findMedianSortedArrays(nums1, nums2):
    # TODO: Please write your code here
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m = len(nums1)
    n = len(nums2)
    left = 0
    right = m

    while left <= right:
        i = (left + right) // 2
        j = (m + n + 1) // 2 - i

        leftA = float('-inf') if i == 0 else nums1[i - 1]
        rightA = float('inf') if i == m else nums1[i]

        leftB = float('-inf') if j == 0 else nums2[j - 1]
        rightB = float('inf') if j == n else nums2[j]

        if leftA <= rightB and leftB <= rightA:
            if (m + n) % 2 == 0:
                return (max(leftA, leftB) + min(rightA, rightB)) / 2
            else:
                return max(leftA, leftB)

        elif leftA > rightB:
            right = i - 1
        else:
            left = i + 1


# Do not change or remove the code below this point
def main():
    # Example 1
    nums1 = [1, 3, 5, 7]
    nums2 = [2]
    result = findMedianSortedArrays(nums1, nums2)
    print(result)  # Should print 3

    # Example 2
    nums1 = [1, 2]
    nums2 = [4, 5]
    result = findMedianSortedArrays(nums1, nums2)
    print(result)  # Median is (2 + 4) / 2 = 3.0
    # Should print 3


if __name__ == '__main__':
    main()
