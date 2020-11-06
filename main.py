def classify(s):
    s_classified = []
    for n in s:
        totalOfFactors = 0
        for factor in range(1, n + 1):
            if n % factor == 0:
                if factor != n:
                    totalOfFactors += factor

        if totalOfFactors < n:
            s_classified.append('deficient')
        elif totalOfFactors > n:
            s_classified.append('abundant')
        elif totalOfFactors == n:
            s_classified.append('perfect')

    return s_classified


# print(classify([1,2,3,4,5,6,7,8,9,10,11,12,13,24]))