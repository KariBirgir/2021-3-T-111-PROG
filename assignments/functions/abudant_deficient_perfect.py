
def decide(num):
    sum_of_fac = sum_of_factors(num)

    if sum_of_fac > num:
        return(f"{num} is abundant.")
    elif sum_of_fac < num:
        return(f"{num} is deficient.")
    else:
        return(f"{num} is a perfect number.")


def sum_of_factors(n):
    sum_of_fac = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            sum_of_fac += i
    return sum_of_fac
