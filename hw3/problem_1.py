def subsets(s):
    # TODO: Please write your code here
    if len(s) == 0:
        return [[]]
    first = s[0]
    rest_subsets = subsets(s[1:])
    new_subsets = []
    for subset in rest_subsets:
        new_subsets.append([first] + subset)
    return rest_subsets + new_subsets


def main():
    print(subsets(["A", "B", "C"]))  # Should print:
    # [[], ['C'], ['B'], ['B', 'C'], ['A'], ['A', 'C'], ['A', 'B'], ['A', 'B', 'C']]

    print(subsets(["K", "L", "M", "Z"]))  # Should print:
    # [[], ['Z'], ['M'], ['M', 'Z'], ['L'], ['L', 'Z'], ['L', 'M'], ['L', 'M', 'Z'], ['K'], ['K', 'Z'], ['K', 'M'],
    # ['K', 'M', 'Z'], ['K', 'L'], ['K', 'L', 'Z'], ['K', 'L', 'M'], ['K', 'L', 'M', 'Z']]


if __name__ == '__main__':
    main()
