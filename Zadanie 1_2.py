def ile_zamian_do_permutacji(A, n):
    k = n
    liczbaDoSprawdzenia = 1

    for i in range(n):
        for j in range(n):
            if A[j] == liczbaDoSprawdzenia:
                k -= 1
                break
        liczbaDoSprawdzenia += 1

    return k



print(ile_zamian_do_permutacji([1, 3, 1], 3))
print(ile_zamian_do_permutacji([1, 4, 2, 5], 4))
print(ile_zamian_do_permutacji([2, 2, 2, 2, 2], 5))

print(ile_zamian_do_permutacji([5, 4, 1, 5, 6, 8], 6))
