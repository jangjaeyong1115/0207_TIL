N = int(input())

people = []

for _ in range(N):
    w, h = map(int,input().split())
    people.append([w,h])

for i in people:
    cnt = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1

        print(cnt, end ='')