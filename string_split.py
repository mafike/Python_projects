def split_and_join(line):
    # write your code here
    char = '-'.join(line.split())
    return char

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)