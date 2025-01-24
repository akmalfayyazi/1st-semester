T1, T2, T3, T4, T5, T6= map(int, input().split())

0 == False
1 == True

prop1= (not T1 and T2) or (not T2 and T1)
prop2= T3 or T4
prop3= T5 and T6
prop4= prop1 or prop2
prop5= prop2 and prop3
prop6= prop4 and prop5


if prop6==True:
    print("Lampu nyala")
else:
    print("Lampu mati")