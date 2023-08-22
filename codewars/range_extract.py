# not workin


def solution(arr: list) -> str:
    start = 0
    end = 0
    for i in arr:
        for j in range(len(arr)):
            if i == arr[j] - 1:
                start = i


print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]))
