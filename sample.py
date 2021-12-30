# 1 2 fizz 4 buzz fizz 7 ... fizbuzz 16

def verifyFizzBuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'fizzbuzz'
    elif num % 3 == 0:
        return 'fizz'
    elif num % 5 == 0:
        return 'buzz'
    else:
        return num

def main():
    for i in range(1, 17):
        print(verifyFizzBuzz(i), end=' ')
        
if __name__ == '__main__':
    main()
