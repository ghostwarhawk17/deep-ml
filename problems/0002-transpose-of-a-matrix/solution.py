def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    b=[]
    for i in range(len(a[0])):
        row=[]
        for j in range(len(a)):
            row.append(a[j][i])
        b.append(row)
    return b
	