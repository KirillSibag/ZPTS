m = int(input())
k = int(input())
s = int(input())

can = 0   # сколько может купить

while s >= m: # пока может купить хоть одну бутылку
	s -= m    # купил бутылку
	can += 1  # записали, что купил
	s += k    # сдал бутылку, получил деньги

print(can)
