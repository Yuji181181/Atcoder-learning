N = int(input())
X = int(input())
Answer = False

A = []
for _ in range(N):
    A.append(int(input()))

for i in A:
    if i == X:
        Answer = True

if Answer == True:
    print("Yes")
else:
    print("No")