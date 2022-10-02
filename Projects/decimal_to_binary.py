def d_b():
    num = "2323232455"
    checker = 0
    x = 0
    num_var = int(num)
    while checker < num_var:
        checker = 2 ** x
        x += 1       
    if checker > num_var:
        x -= 1
    tester = x
    result = ""
    while x >= 0:
        binary = 2 ** x
        if num_var >= binary:
            num_var -= binary
            x -= 1
            result += "1"
        else:
            x -= 1
            result += "0"
    if len(result) != tester:
        result = result[1:]
    print(result)
def b_d():
    binary = "10001010011110011011011011000111"
    length_of_string = len(binary)
    result = 0
    for i in range(length_of_string):
        x = 2 ** (length_of_string-1)
        print(binary[i])
        if binary[i] == "1":
            result += x
            length_of_string -= 1
        else:
            result += 0
            length_of_string -= 1
    print(result) 
b_d()
d_b()   
            
            
    
