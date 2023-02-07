import sys

sticks = int(sys.stdin.readline())

height = []

for _ in range(sticks):
    height.append(int(sys.stdin.readline()))

highest = height[-1]

res = 1

for i in range(-1,-int(sticks)-1,-1):
    if height[i] > highest:
        res += 1

    highest = height[i]

print(res)