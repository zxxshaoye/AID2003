list_merge = [2, 0, 2, 0]
map = [
            [2, 0, 0, 2],
            [4, 2, 0, 2],
            [2, 4, 2, 4],
            [0, 4, 0, 4],
        ]




line=[]

for line in map:
    # line=list01[::-1]
    for i in range(len(line) - 1, -1, -1):
        if line[i] == 0:
            line.append(0)
            del line[i]

    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            line[i] *= 2
            # 删除后一个的元素
            del line[i + 1]
            # 在后面补0
            line.append(0)
    # list01[::-1]= line
print(map)



