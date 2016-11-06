# Этой функцией находим НОД двух чисел, используя битовые операции
# Рекурсивная функция

# if a and b are not odd then a,b divide on 2 and then *2
# if a is odd then (a, b div 2)
# if a and b are odd numbers (a,b-a div 2)

def bin_gcd(a, b):
    if a == b:
        return a
    if a == 0 or b == 0:
        return max(a, b)
    if (~a & 1) != 0:       # если чётное a, то 1
        if b & 1 != 0:
            return bin_gcd(a >> 1, b)
        else:
            return bin_gcd(a >> 1, b >> 1) << 1
    if (~b & 1) != 0:
        return bin_gcd(a, b >> 1)
    if a > b:
        return bin_gcd((a - b) >> 1, b)
    return bin_gcd((b - a) >> 1, a)

print(bin_gcd(140,130))

