import math

def fib_mod(n, m):
    a = 1
    b = 1
    k = 1
    i = 2
    pizano = [0, 1, 1]
    while pizano[i] != 1 or pizano[i-1] != 0:
        c = (a + b) % m
        pizano.append(c)
        a = b
        b = c
        k = k + 1
        i = i + 1
    return pizano[n%k]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()