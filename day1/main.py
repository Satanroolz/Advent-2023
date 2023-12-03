
with open ("input.txt") as f:
    s = f.read()
r = 0
for x in s.strip().split("/n"):
    fst = None
    lst = None
    for y in x:
        if y.isdigit():
            lst = y
            if fst is None:
                fst = y
r += int(fst + lst)