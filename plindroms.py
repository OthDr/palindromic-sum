try:
    arr = []
    i = 1
    palsArray = []
    j = 0
    sum = 0
    k = 0
    testSum = 0
    number = int(input('Enter an integer : '))
    print(' ')
    print(' ')
    if number > 0:
        while i < int(number):
            if (str(i) == str(i)[::-1]):
                arr.append(i)
            i += 1

        while (sum < number):

            if ((number - sum) >= arr[k]):
                sum = sum + arr[k]
                palsArray.append(arr[k])
                k = k + 1
            else:
                k = k - 1

    else:
        print('please inter a positive integer ')
    print('All palindroms ', arr)
    print(' ')
    print('**** Final Result ****')
    print(' ')
    print('Palindromic sum:')
    print(number, '= ', end='')
    for j in range(0, len(palsArray)):
        print(palsArray[j], '+ ', end='')
    print("\b\b")
except:
    print('! Only integers are valid ')