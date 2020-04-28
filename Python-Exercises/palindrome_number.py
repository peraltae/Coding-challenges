def is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]

    #48 ms	13.8 MB


def is_pal_no_strings(x: int) -> bool:
     #Solve  without converting the integer to a string

    rev = 0
    num = x

    while (num > 0):
        y = num % 10
        num = num // 10
        rev = (rev*10) + y


    return rev == x

    #64 ms	14.1 MB
