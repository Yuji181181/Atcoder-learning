N,M = map(int,input().split())

for i in range(M):
    edges.append(list(map(int,input().split())))

G = []
for i in range(N+1):
    G.append([])

for edge in edges:
    a = edge[0]
    b = edge[1]
    G[a].append(b)
    G[b].append(a)

for i in range(1,N+1):
    output = ''
    output += str(i)
    output += ':{'
    first = True
    for neighbor in G[1]:
        if not first:
            output += ', '
        output += str(neighbor)
        first = False
    output += '}'
    print(output)