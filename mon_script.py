from cyriac_benousaad_miller_rabin.verification import miller_rabin_test
lst_prime = []
compteur = 0
while compteur < 50:
    for i in range(1000):
        if miller_rabin_test(i,10):
            lst_prime.append(i)
            compteur += 1
print(lst_prime)