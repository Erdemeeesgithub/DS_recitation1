def product_checker(A, B, m):
    # TODO: Please write your code here
    result = []
    used_a = set()

    for a in A:
        if a in used_a:
            continue

        if m % a != 0:
            continue

        b = m // a

        left = 0
        right = len(B) - 1
        found = False

        while left <= right:
            mid = (left + right) // 2
            if B[mid] == b:
                found = True
                break
            elif B[mid] < b:
                left = mid + 1
            else:
                right = mid - 1

        if found:
            result.append((a, b))
            used_a.add(a)

    return result


# Do not change or remove the code below this point
def main():
    A = [2, 4, 5, 6, 8, 10, 12]
    B = [1, 2, 4, 9, 10, 20]
    print(product_checker(A, B, 40))  # Should print [(2, 20), (4, 10), (10, 4)]

    A = [4, 5, 6, 20]
    B = [1, 2, 4, 10]
    print(product_checker(A, B, 100))  # Should print: []

    A = [1, 2, 2, 3, 5]
    B = [1, 5, 50, 50, 100]
    print(product_checker(A, B, 100))  # Should print: [(1, 100), (2, 50)]


if __name__ == '__main__':
    main()
