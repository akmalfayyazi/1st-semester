from itertools import groupby

total_stone = input("total stone : ")
total_after = "".join(i for i, _ in groupby(total_stone))
total_same = sum(len(list(same)) -1 for _, same in groupby(total_stone))
looping = False
for char, group in groupby(total_stone):
    loop = len(list(group))
    if loop > 1:
        looping = True
        asci = ord(char)
        loss_total = (1000*asci)*total_same
if looping:
    print(f"Di gudang tersisa {len(total_after)} batu Total Kerugian: {loss_total} Dolar Imbu")
else:
    print(f"Di gudang tersisa {len(total_after)} batu. Wah, Jotaro Joemama tidak jadi dipecat")

    