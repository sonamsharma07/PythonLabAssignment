Matchsticks = 21 
print("Total Matchsticks Initially: ", Matchsticks)

while(Matchsticks>1):
    user_pick = int(input("Choose a number between 1 to 4: "))
    print("You picked", user_pick)

    if user_pick < 1 or user_pick > 4 or user_pick >= Matchsticks:
        print("Invalid pick!")
    else:  
        Matchsticks = Matchsticks - user_pick
        print("Matchsticks left", Matchsticks)   
        system_pick = 5 - user_pick   
        print("The system picked", system_pick)
        Matchsticks = Matchsticks - system_pick
        print("Matchsticks left", Matchsticks)


print("You lost!")


