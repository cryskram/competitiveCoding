from cmath import phase


def compute(s: str):
    print(abs(complex(s)))
    print(phase(complex(s)))


if __name__ == "__main__":
    compute(input())
