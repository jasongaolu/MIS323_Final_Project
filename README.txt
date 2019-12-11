Team members: Jason Lu
B#00576194

How to run the program:
No special way, just run the code

What it is? What does it do?:
This program is a Guess the Number. However, it will ask a lot from the user. The first thing it'll ask from the user would be the option to have infinite amount of guesses with no score, or to play one guess per game with a score. Then user will decide the amount of times, and the number in range to play with. Then the user will guess the number, and the program will tell the user if they guessed to high or too low. You can quit the program whenever you want by replying 'q'. Also if you reply any special characters the program will let you know and end the program.

How does it work?:
The choice() method will generate a random number, with the help of the user. And then by using the if function to check if any inputs are either 'q' to quit the game. And using the try function to check for any special characters, the program will prompt the user to re-run the program and try again. The whole program will be in a while loop until it reaches the goal that the user asked for. The hardest part of the program for me, was to incorporate the user input, the 'q' function and to eliminate the special characters all into one. If I made the input a float() then it will give an error message with special characters. If I just used the try method, strings can't be compared to each other with '>' or '<'. The program became easier the moment, I created a separate variable, 'sample(s)' for the code. 

The code also has the ability to choose between 2 options, choosing between infinite guesses or one guess per game. I set the input as 'version' and later on in the code I had an if statement, similar to how a switch works, if 'version' was == 1 then one option would start, If it was == 2, the other option would start.

References
