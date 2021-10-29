logs = input()   # [[0,5],[1,2],[0,2],[0,5],[1,3]]

logs = logs.replace('[',' ')
logs = logs.replace(']',' ')
logs = logs.replace(',',' ')

logs = logs.split()

logs_matrix = []

for i in range(0, len(logs), 2):
    l = []
    l.append(int(logs[i]))
    l.append(int(logs[i + 1]))
    logs_matrix.append(l)

# logs_matrix = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]

k = int(input())

d = dict()

for id, time in logs_matrix:
    if id not in d:
        d[id] = [time]
    else:
        d[id].append(time)

for i in d:
    d[i] = len(set(d[i]))


result = k * [0]

for i in d:
    result[d[i] - 1] += 1


print(result)










