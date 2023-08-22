def solution(number: int) -> int:
    sum = 0
    for i in range(1, number):
        if i % 3 == 0 and i % 5 == 0:
            sum += i
        else:
            if i % 3 == 0:
                sum += i
            if i % 5 == 0:
                sum += i

    return sum


print(solution(200))
