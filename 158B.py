groupcount = input()
groups = [int(x) for x in input().split()]

taxis = groups.count(4)

threes = groups.count(3)
twos = groups.count(2)
ones = groups.count(1)

taxis += threes
ones -= (threes if ones > threes else ones)

taxis += twos//2
if twos%2 == 1:
    taxis += 1
    if ones >= 2:
        ones -= 2
    else:
        ones = 0

if ones > 0:
    taxis += ones//4 + (1 if ones%4 > 0 else 0)

print(taxis)
