start = int(input())
stop = int(input())

for idx in range(start, stop+1):
    idx_is_chr = chr(idx)
    print(idx_is_chr, end=' ')