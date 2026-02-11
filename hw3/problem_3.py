def expression(numbers):
    # TODO: Please write your code here
    if len(numbers) == 1:
        return [str(numbers[0])]
    prev_expressions = expression(numbers[:-1])
    last_number = str(numbers[-1])
    result = []
    for expr in prev_expressions:
        result.append(expr + "+" + last_number)
        result.append(expr + "-" + last_number)
        result.append(expr + "*" + last_number)
    return result


def main():
    print(expression([1, 2, 3]))  # Should print: ['1-2*3', '1+2+3', '1-2-3', '1*2*3', '1-2+3', '1+2*3', '1+2-3', '1*2+3', '1*2-3']
    print(expression([8, 9]))  # Should print: ['8+9', '8*9', '8-9']


if __name__ == '__main__':
    main()
