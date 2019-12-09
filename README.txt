Team members: Jason Lu
B#00576194

How to run the program:
No speical way, just run the code

What it is? What does it do?:
This program is a Guess the Number. However, it will ask a lot from the user. The user will decide the amount of times,
and the number in range. Then the user will guess the number, and the program will tell the user if they guessed to high or too low.

How does it work?:
The choice() method will generate a random number, with the help of the user. And then by checking if any inputs are either 'q' to quit the game
or any special characters, the program will prompt the user to re-run the program and try again. The whole program will be in a while loop 
until it reaches the goal that the user asked for. The hardest part of the program for me, was to incorporate the user input, the 'q' function
and to eliminate the speical characters all into one. If I made the input an float() then it will give an error message with speical characters.
If I just used the try method, strings can't be compared to each other with '>' or '<'. The program became more simple the moment, I created a 
seperate variable, 'sample(s)' for the code.

References