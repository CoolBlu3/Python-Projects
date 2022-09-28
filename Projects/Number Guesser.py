
def main():
    def checker():
        if int(y) < answer:
            return "Higher"
        elif int(y) > answer:
            return "Lower"
        else:
            return "You got it!"
    answer = 15
    table = '''   Guess  |   Higher or Lower''' + "\n   _________________________"
    count = 1
    while count <6:
        y = input("Guess: ")
        guess = str(count) + "    " + y + "    |   " + str(checker())
        count += 1
        table = table +"\n" + guess
        print(table)
        if y == str(answer):
            print("You won! Thanks for playing!")
            quit()
    retry = input("You lose! Want to try again? (Y/N) ")
    if retry.lower() == "y":
        main()
    else:
        print("Thanks for playing!")
        
            
    



main()
