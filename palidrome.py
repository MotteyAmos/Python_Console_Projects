def palidrome(num):
    num = num
    original_num = num

    while True:
        num_str = str(num)
        rev_str = num_str[::-1]
        if num_str == rev_str:
            print(f"{num} is a palindrome for the value {original_num}")
            break
        num = int(num_str) + int(rev_str)
    
palidrome(25)