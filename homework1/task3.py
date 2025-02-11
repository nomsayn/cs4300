
def check_pos_or_neg(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

# Prime numbers - any numbers that are only divisible by 1 and themselves.
#   found by checking if a number is divisible by any number less than itself.
def first_10_primes():
    prime_arr = []
    current_num = 2
    while len(prime_arr) < 10:

        for i in prime_arr:
            if current_num % i == 0: # if num is divisible by any number in prime_arr
                break
        else: # if num is not divisible by any number in prime_arr
            prime_arr.append(current_num)
        current_num += 1
    return prime_arr


def sum_100_nums():
    total = 0
    current_num = 1
    while current_num <= 100: # loop through 1 to 100
        total += current_num
        current_num += 1
    return total



print(check_pos_or_neg(45))
print(check_pos_or_neg(-333))
print(check_pos_or_neg(0))
print(first_10_primes())
print(sum_100_nums())
