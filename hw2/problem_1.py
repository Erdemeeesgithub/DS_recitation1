def find_nearest_temperature(sorted_temps, target_temp):
    # TODO: Please write your code here
    if not sorted_temps:
        return None

    left = 0
    right = len(sorted_temps) - 1

    if target_temp <= sorted_temps[0]:
        return sorted_temps[0]
    if target_temp >= sorted_temps[-1]:
        return sorted_temps[-1]

    while left <= right:
        mid = (left + right) // 2

        if sorted_temps[mid] == target_temp:
            return sorted_temps[mid]
        elif sorted_temps[mid] < target_temp:
            left = mid + 1
        else:
            right = mid - 1

    if abs(sorted_temps[left] - target_temp) < abs(sorted_temps[right] - target_temp):
        return sorted_temps[left]
    elif abs(sorted_temps[left] - target_temp) > abs(sorted_temps[right] - target_temp):
        return sorted_temps[right]
    else:
        return min(sorted_temps[left], sorted_temps[right])


# Do not change or remove the code below this point
def main():
    sorted_temps = [-20, -15, -5, 3, 8, 12, 30, 45, 50, 60]
    target_temp = 7

    nearest = find_nearest_temperature(sorted_temps, target_temp)
    print(nearest)  # Should print 8


if __name__ == "__main__":
    main()
