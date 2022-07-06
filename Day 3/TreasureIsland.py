print('''

                           #####
                       #######
            ######    ########       #####
        ###########/#####\#####  #############
    ############/##########--#####################
  ####         ######################          #####
 ##          ####      ##########/@@              ###
#          ####        ,-.##/`.#\#####               ##
          ###         /  |$/  |,-. ####                 #
         ##           \_,'$\_,'|  \  ###
         #              \_$$$$$`._/   ##
                          $$$$$_/     ##
                          $$$$$        #
                          $$$$$
                         $$$$$
                         $$$$$
                         $$$$$        ___
                         $$$$$    _.-'   `-._
                        $$$$$   ,'           `.
                        $$$$$  /               \
~~~~~~~~~~~~~~~~~~~~~~~$$$$$~~~'~~~~~~~~~~~~~~~~`~~~~~~~~~~~~
   ~      ~  ~    ~  ~ $$$$$  ~   ~       ~          ~
       ~ ~      .o,    $$$$$     ~    ~  ~        ~
  ~            ~ ^   ~ $$$$$~        ______    ~        ~
_______________________$$$$$________|\\\\\\\_________________
                       $$$$$        |>\\\\\\\
    ______             $$$$$        |>>\\\\\\\
   \Q%=/\,\            $$$$$       /\>>|#####|
    `------`           $$$$$      /=|\>|#####|
                       $$$$$        ||\|#####|
                      $$$$$$$          ||"""||
                      $$$$$$$          ||   ||
                     $$$$$$$$$
"""""""""""""""""""""$$$$$$$$$""""""""""""""""""""""""""""""

''')
print("Welcome to Teasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at the crossroad, where do you want to go? Type "left" or "right".').lower()

if choice1 == 'left':
    # Continue the game
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swin" to swim across. ').lower()

    if choice2 == 'wait':
        # Game will continue

        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color "
              "do you choose?\n").lower()
        if choice3 == 'red':
            print("It's a room full of fire. Game Over.")
        elif choice3 == 'yellow':
            print("You found the treasure1 You Win!")
        elif choice3 == 'blue':
            print("You entered a room of beast. Game Over!")
        else:
            print("You chose a door that doesn't exit. Game Over!")


    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game over")



