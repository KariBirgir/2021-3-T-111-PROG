def main():
    n = int(input("How long is the sequence(>0): "))
    fibo_tuple(n)

def fibo_tuple(n):
    a = (0, 1)
    for i in range(n):
        print(a[1], end=" ")
        a_n = sum(a)
        a = (a[1], a_n)

# Recursive solution:
# def fibo_tuple(n, a=(0, 1)):
#     if n == 0:
#         return
#     else:
#         print(a[1], end=" ")
#         a_n = sum(a)
#         a = (a[1], a_n)
#         fibo_tuple(n-1, a)

if __name__ == "__main__":
    main()
