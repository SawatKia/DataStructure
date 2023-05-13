def is_palindrome(num):
    """
    Determines whether a given number is a palindrome or not.
    """
    str_num = str(num)
    return str_num == str_num[::-1]

def add_with_reverse(num, iter_count):
    """
    Adds a given number to its reverse and returns the result.
    If the result is not a palindrome, calls itself recursively with the result.
    Keeps track of the number of iterations it takes to find a palindrome.
    """
    reverse = int(str(num)[::-1])
    sum = num + reverse
    iter_count += 1
    print(f"({iter_count}) {num} + {reverse} = {sum}")
    if not is_palindrome(sum):
        return add_with_reverse(sum, iter_count)
    else:
        return sum, iter_count

number = int(input("Enter a number: "))
iter_count = 0
print(f"Starting from {number}:")
while True:
    print(f"({iter_count}) {number}")
    sum, iter_count = add_with_reverse(number, iter_count)
    if is_palindrome(sum):
        print(f"Palindrome found: {sum}")
        print(f"First number: {number}")
        print(f"Total iterations: {iter_count}")
        break
    number += 1
