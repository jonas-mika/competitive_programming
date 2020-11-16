# 5
# 1 2 1 3 2
# 3 2

def read_in():
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    print(s, d, m)

read_in()
