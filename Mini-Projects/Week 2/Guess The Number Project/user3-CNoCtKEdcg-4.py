# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import math
import random
import simplegui

# initialize global variables used in your code
guesses_left = math.ceil(math.log(101,2))
number_to_guess = random.randrange(0,100) 
num_range = 100

# define event handlers for control panel
#This event handler/function starts the game
def start_game():
    global guesses_left, number_to_guess, num_rage
    guesses_left = math.ceil(math.log(num_range+1,2))
   # number_to_guess= random.randrange(0,num_range)
    frame.start()
    print "New game. Range is from 0 to ",num_range
    print "Number of guesses left: ",guesses_left
    print ""
    
def range100():
    # button that changes range to range [0,100) and restarts
    global number_to_guess, guesses_left, num_range
    num_range = 100
    number_to_guess = random.randrange(0,num_range)
    guesses_left = math.ceil(math.log(num_range+1,2))
    print number_to_guess
    start_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global number_to_guess, guesses_left, num_range
    num_range = 1000
    number_to_guess = random.randrange(0,num_range)
    guesses_left = math.ceil(math.log(num_range+1,2))
    print number_to_guess
    start_game()
    
def get_input(guess):
    # main game logic goes here	
    global guesses_left
    guesses_left = guesses_left-1
    
    if int(guess) == number_to_guess:
         print "The number you guessed is",guess
         print "You're correct!"
         print ""
         start_game()
    
    elif guesses_left<1:
        print "Sorry, you lose. The correct number is",number_to_guess
        print ""
        start_game()
        
    else:
        if int(guess) > number_to_guess:
            print "The number you guessed is",guess
            print """Lower!
Number of guesses left:""",guesses_left
            print ""
            
        elif int(guess) < number_to_guess:
            print "The number you guessed is",guess
            print """Higher!
Number of guesses left:""",guesses_left
            print ""
            
        else:
            print "The number you guessed is",guess
            print "You're correct!"
            print ""
            start_game()

# create frame
frame = simplegui.create_frame("Guess The Number!", 200, 200)

# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", get_input, 200)

# start frame
start_game()
print number_to_guess
# always remember to check your completed program against the grading rubric

   