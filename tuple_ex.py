# Complete the solve function below.
def swap_case(s):
    swapped =[]
        
    return ''.join(swapped.append(char.upper()) if char.upper() else swapped.append(char.lower()) for char in s)
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


