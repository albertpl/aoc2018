import sys

assert len(sys.argv) == 2, 'did you forget input?'
with open(sys.argv[1]) as in_fd:
    fs = [int(line) for line in in_fd]
print(sum(fs))
found = False
x = 0
seen = {0}
while not found:
    for f in fs:
        x += f
        if x in seen:
            found = True
            print(x)
            break
        seen.add(x)

