def inverse(number):
    array = list(str(number))
    inverse = ""
    for i in array : 
        inverse = i + inverse 

    return int(inverse)    

def palindrome(number):
    array = list(str(number))
    n = len(array)
    for i in range(len(array)//2):
        if array[i] != array[n-i-1]:
            return False
    return True

def Main(number):
    if palindrome(number):
        return 0
    return 1 + Main(number + inverse(number))

if __name__ == '__main__':
    print(Main(1234))
