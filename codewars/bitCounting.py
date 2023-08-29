def count_bits(n: int):
    return str(bin(n)).count("1")


print(count_bits(1234))
