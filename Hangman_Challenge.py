#Hangman Challenge Using Dictonary 
import random
print("Hello player! ")
Fruits = {"apple": "It's an adam's fruit", "banana": "Seedless and yellow when ripe" , "orange": "It's a color and fruit", "cherry": "Rhymes with jerry", "mango": "India's most loved fruit during summer season"}
print ("You get 5 guesses to guess the fruit")


Random_Fruit = random.choice(list(Fruits.items()))
Random_Fruit_Selected = ((Random_Fruit[0]))
Hint = (Random_Fruit[1])


display_word = []
for letter in Random_Fruit_Selected:
    display_word += "_"
print(display_word)


num = 0
game_over = False
while not game_over:

    User_guess = input("Guess the letter: ").lower()
    for position in range(len(Random_Fruit_Selected)):
      letter = Random_Fruit_Selected[position]
      if letter == User_guess:
          display_word[position] = letter  

    if User_guess not in Random_Fruit_Selected:
       num += 1
       guesses_left = 5 - num
       print(f"You have {guesses_left} guesses left")
       if num == 4:
          hint_input = input("If you want a hint type yes: \n").lower()
          if hint_input == "yes":
             print(f"The Hint is {Hint}")
             print("This is your last guess be cautious! ")
          elif hint_input == "no":
                print("Good luck this is your last guess")
       if num >= 5:
           print("You lost")
           print(f"The word is \"{Random_Fruit_Selected}\", Better luck next time")
           game_over = True
           break
    print(display_word)

    if "_" not in display_word:
       print("You win !")
       print(f"You are right! The word is \"{Random_Fruit_Selected}\" ")
       game_over = True
