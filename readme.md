# Tect Adventure game with python

This is a text-adventure game based on an old bugs bunny mobile game (Rabbit Rescue). You are given a list of items that must be selected in the correct order into order to pass the game. The game consists of three levels with the game getting a bit harder as the player progresses.
The sys and time modules are used to slow down the print function to give the game an interactive feel.
main.py displays the story and contains three functions: firstlevel, secondlevel and thirdlevel. These handle the start of each level the player should complete to complete the game.
The second file called permutation.py is the engine/functionality of the game. It contains the first, second and third functions that handles all the possible permutations and prints out the resultant outcome.
The end function runs when a mission is failed.
Config.py contains three dictionaries that contain the options that will be chosen for each level  
Level, level1 and level2 are functions that run a for loop through these dictionaries and prints it on the screen

Have fun!
