def reverse_prime(n):
    fact_list = []
    for i in range(1, n + 1):
        if (n % i == 0):
            n //= i
            fact_list.append(i)
    print(fact_list)
    return fact_list

n = 25
k = reverse_prime(n)
print(k)