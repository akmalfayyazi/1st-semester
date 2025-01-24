x,y = map(float, input("masukkan x dan y : ").split())

if x == 0 and y == 0:
    print(f"({x}, {y}) is the center point")
elif x == 0:
    print(f"({x}, {y}) is x axis")
elif y == 0:
    print(f"({x}, {y}) is y axis")
elif x > 0 and y > 0:
    print(f"({x}, {y}) is quadran 1")
elif x < 0 and y > 0:
    print(f"({x}, {y}) is quadran 2")
elif x < 0 and y < 0:
    print(f"({x}, {y}) is quadran 3")
else:
    print(f"({x}, {y}) is quadran 4")