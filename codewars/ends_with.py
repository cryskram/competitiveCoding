def solution(s1: str, s2: str) -> bool:
    for i in range(1, min(len(s1), len(s2)) + 1):
        if s1[-i] != s2[-i]:
            return False

    return True if min(len(s1), len(s2)) == len(s2) else False


# def solution(s1, s2):
# return s2 in s1[-len(s2)]

print(solution("ails", "fails"))
