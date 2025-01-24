nyawa = int(input())
knight = int(input())//2
minion = int(input())//2
nyawa -= minion*2
nyawa -= knight*25
nyawa -= 1000
if nyawa<=0:
    print("Yah! Ucup Meninggoy.")
else:
    print(f"Yey! Ucup Menang! HP tersisa: {nyawa}")