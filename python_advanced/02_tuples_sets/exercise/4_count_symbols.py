# n = {}
#
# for symbol in input():
#     n[symbol] = n.get(symbol, 0) + 1
#
# for symbol, times in sorted(n.items()):
#     print(f"{symbol}: {times} time/s" ,sep="\n")
#

text = input()

for symbol in sorted(set(text)):
    print(f"{symbol}: {text.count(symbol)} time/s")