def who_if_winner(arr: list) -> str:
    dum = {}
    for i in arr:
        pos, player = i.split("_")
        dum.setdefault(player, []).append(pos)
    print(dum)


print(
    who_if_winner(
        [
            "A_Red",
            "B_Yellow",
            "A_Red",
            "B_Yellow",
            "A_Red",
            "B_Yellow",
            "G_Red",
            "B_Yellow",
        ]
    )
)
