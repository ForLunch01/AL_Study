def dif_str(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count


def find_dif_str(a,b):
    len_dif = len(b) - len(a)
    dif_count = 50

    for i in range(len_dif+1):
        match_str = b[i: len(a)+i]
        if dif_str(a, match_str) < dif_count:
            dif_count = dif_str(a, match_str)

    return dif_count
        

A, B = input().split()

print(find_dif_str(A,B))



