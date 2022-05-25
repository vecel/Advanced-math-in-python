def determinent(det):
    if len(det) == 1:
        return det[0][0]
    d = 0
    for i in range(len(det)):
        d += (-1) ** i * det[0][i] * determinent(sub_determinent(det, i))
    return d

def sub_determinent(det, elem):
    d = []
    for i in range(1, len(det)):
        d.append(det[i][:elem] + det[i][elem + 1:])
    return d

det1 = [[1, 2], [3, 4]]
det2 = [
    [5, -2, 3],
    [2, 3, -4],
    [3, 4, 5]
]

