# We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
# Let's try to understand this with an example.

def mutate_string(string, position, character):
    string = ''
    l = list(s)
    l[int(i)]= c
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)