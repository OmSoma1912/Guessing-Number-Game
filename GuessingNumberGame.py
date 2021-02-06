import random

x = random.randint(1,9)

guess1 = int(input("You have 5 tries to guess the selected number between 1 and 9 : "))

if (guess1 == x):
    print ("Good Job!")
    
else:
    print ("Sorry, you didn't get it.")

    if(guess1 > x):
        print ("Here is a hint, it is less than ")
        print (guess1)

    else:
        print ("Here is a hint, it is more than")
        print (guess1)
        
    print ("4 more tries.")
    guess2 = int(input("Guess the selected number between 1 and 9 : "))

    if (guess2 == x):
        print ("Good Job!")

    else:
        print ("Sorry, you didn't get it.")

        if(guess2 > x):
            print ("Here is a hint, it is less than ")
            print (guess2)

        else:
            print ("Here is a hint, it is more than")
            print (guess2)
        
        print ("3 more tries.")
        guess3 = int(input("Guess the selected number between 1 and 9 : "))


        if (guess3 == x):
            print ("Good Job!")

        else:
            print ("Sorry, you didn't get it.")

            if(guess3 > x):
                print ("Here is a hint, it is less than ")
                print (guess3)

            else:
                print ("Here is a hint, it is more than")
                print (guess3)
        
            print ("2 more tries.")
            guess4 = int(input("Guess the selected number between 1 and 9 : "))

            if (guess4 == x):
                print ("Good Job!")

            else:
                print ("Sorry, you didn't get it. 1 last try.")

                if(guess4 > x):
                    print ("Here is a hint, it is less than ")
                    print (guess4)

                else:
                    print ("Here is a hint, it is more than")
                    print (guess4)
        
                print ("1 last try.")
                guess5 = int(input("Guess the selected number between 1 and 9 : "))

                if (guess5 == x):
                    print ("Good Job!")

                else:
                    print ("Sorry, you didn't get it. The number was")
                    print (x)
                    
