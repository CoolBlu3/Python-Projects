def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]
def is_palindrome(x):
    y = len(middle(x))
    if first(x) == last(x):
        x = middle(x)
        for i in range(y//2):
            if first(x) == last(x):
                x = middle(x)
            else:
                print("False")
                break
        print("True")
    else:
        print("False")

is_palindrome("giraffarig")