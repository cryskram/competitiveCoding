def create_phone_number(n: list) -> str:
    p1 = str(n[0]) + str(n[1]) + str(n[2])
    p2 = str(n[3]) + str(n[4]) + str(n[5])
    p3 = str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])
    return str("({}) {}-{}".format(p1, p2, p3))
