import sys

tc = sys.stdin.readline()
print(tc)
cv = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for c in cv:
    if c in tc:
        tc= tc.replace(c, '_')

tc = tc.strip()
print(len(tc))
