num_cases = int(input())

for _ in range(num_cases):
    case = int(input())

    max_multiple_3 = (case - 1) // 3 * 3
    max_multiple_5 = (case - 1) // 5 * 5

    sum_3 = (max_multiple_3 * (max_multiple_3 // 3 + 1)) // 2
    sum_5 = (max_multiple_5 * (max_multiple_5 // 5 + 1)) // 2

    max_multiple_15 = (case - 1) // 15 * 15
    sum_15 = (max_multiple_15 * (max_multiple_15 // 15 + 1)) // 2

    total_sum = sum_3 + sum_5 - sum_15
    print(total_sum)
