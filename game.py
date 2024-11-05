p1=input("your turn (rock, paper, scissors)")
p2=input("your turn (rock, paper, scissors)")
if p1==p2:
    print("TIE")
elif(p1 == 'rock' and p2 == 'scissors' ) or (p1 == 'scissors' and p2 =='paper') or (p1 =='paper' and p2 =='rock'):
    print("p1 winns")
else:
    print("p2 winns")
