import random
def hangman():
        list=["india","pakistan","londan","australia","china","france"]
        word=random.choice(list)
        turns=10
        guessmade=''
        valid_entry=set("abcdefghijklmnopqrstuvwxyz")
        while len(word)>0:
            main_word=""
            for latter in word:
                if latter in guessmade:
                    main_word=main_word+latter
                else:
                    main_word=main_word+"_ "
            if main_word==word:
                print(main_word) 
                print(" congrestulation you win!!")
                break    
            print("guess the word",main_word)
            guess=input()
            if guess in valid_entry:
                guessmade=guessmade+guess
            else:
                print("enter valid character")
                guess=input()
            if guess not in word:
                turns=turns-1
                if turns==9:
                    print("9 turns left")
                    print("-------------")
                if turns==8:
                    print("8 turns left")
                    print("--------------")
                    print("     |     ")
                if turns==7:
                    print("7 turns left")
                    print("--------------")
                    print("     |      ")
                    print("     0      ")
                if turns==6:
                    print("6 turns left")
                    print("--------------")
                    print("     |      ")
                    print("     0      ")
                    print("     |      ")
                if turns==5:
                    print("5 turns left")
                    print("--------------")
                    print("     |      ")
                    print("     0      ")
                    print("     |      ")
                    print("      \     ")
                if turns==4:
                    print("4 turns left")
                    print("--------------")
                    print("     |     ")
                    print("     0      ")
                    print("     |      ")
                    print("    / \     ")
                    
                if turns==3:
                    print("3 turns left")
                    print("--------------")
                    print("     |      ")
                    print("     0      ")
                    print("    /|     ")
                    print("    / \     ")
                if turns==2:
                    print("2 turns left")
                    print("--------------")
                    print("     |      ")
                    print("     0      ")
                    print("    /|\    ")
                    print("    / \     ")
                if turns==1:
                    print("1 turns left")
                    print("--------------")
                    print("     |      ")
                    print("     0      ")
                    print("    /|\    ")
                    print("    / \     ")
                if turns==0:
                    print(" oppss you loss!")
                    print("you let a good man die")
                    break
name=input("enter the name:")
print("**************",name,"************************")
print("**************Welcome to hangman game****************")
hangman()
def playagain():
    while True:
        again=input("if you want to play again press yes or no")
        if again=="yes":
            pass
        else:
            break
playagain()

   



                    






























