def knapsack_recursive(weights, values, capacity, n):
    # TODO: Please write your code here
    if n == 0 or capacity == 0:
        return 0
    if weights[n - 1] > capacity:
        return knapsack_recursive(weights, values, capacity, n - 1)
    include = values[n - 1] + knapsack_recursive(
        weights, values, capacity - weights[n - 1], n - 1
    )
    exclude = knapsack_recursive(weights, values, capacity, n - 1)
    return max(include, exclude)


def main():
    weights, values = [1, 3, 4, 5], [1, 4, 5, 7]
    capacity, n = 7, len(weights)
    result = knapsack_recursive(weights, values, capacity, n)
    print(result)  # Should print: 9 because of weights four and five with value 5 and 7


if __name__ == '__main__':
    main()
