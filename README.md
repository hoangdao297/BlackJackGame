Hoang Dao's Submission/ _Email: minhhoanghectorjack@gmail.com_

1. Python 3 should be installed on the computer if not you can download here: https://www.python.org/downloads/
The folder contains:
-3 python (.py) files: blackjack_random.py , blackjack_input.py , test_game.py (automated testing)
-11 test files with (.json) format

the blackjack_random.py file is the file with computer randomly generate cards for player and dealer
To run, navigate to the folder location on terminal and type: python blackjack_random.py

the blackjack_input.py file is the file with the desired input to simulate player input, cards as well as dealer cards, input
this file is testable and can be tested through test_game.py file
To run, navigate to the folder location on terminal and type: python test_game.py

2. The lack of clarity that I found in the challenge is the input of program. I was confused between writing random input from computer and the designed input. So I chose to write as general as I can to write both version with the same codes and little differences in 2 versions. For the random version, I use random algorithm from python library for generating cards and manual user input for program. For input version, I design the format of test case and test it with same code.


3. I implemented random generated card version as well as with the input for testing reason. In addition, my codes print out the same output as in the challenge.

4. For the card representation, I define the Card by writing the Card class (contains suit, face, value). The reason behind this is to make the array of cards (deck) with the Card objects. From that I can take the card's face and value easily in my programming process. In my codes, I always keep track of player's cards, points as well as dealer's in order to make it easier for me to check value and print it out to the terminal. For the value of the Ace card, I set default value as 11, in the codes when player or dealer encounter the case that Ace(s) card make their points exceed 21, my codes updates the value of Aces card to 1 step by step to get the maximum points under 21.

5. I encountered the tradeoff between the simplicity in codes and the well structure of the codes. At the first time, I did not write Card class and try to implement it with the hash table and and decrement the amount of each card by 1 whenever it called. But I realized that will makes the codes unstructured and hard to read as well as make it easier to raise the error. So I wrote all of my ideas in the paper and try to design it in the structured way before I coded it out.

6. I would test more !. For 2 hours, I was only able to write the codes as well as tested it with the comparison of the winner. If I was given more time, I would test on the printing output to check each line of ouput is exact to the desired output or not.  And I would test on the final points of player and dealer. In addition, I would try to reduce the overall time complexity of this program for better performance.

7. I generalized all possible scenarios into 11 test cases
All of my test cases were written in .json format {"Dealer":{"Init":[[suit_of_card,face_of_card],[suit_of_card,face_of_card]], "CMD":[[suit_of_card,face_of_card]]},
"Player":{"Init":[[suit_of_card,face_of_card],[suit_of_card,face_of_card]], "CMD":[["H",suit_of_card,face_of_card] or ["S"]}
,"result":[winner,player_points,dealer_points],
"comments":"for comment"} 
For winner 1 denotes for player, 0 for dealer and 2 for tie. 

Case 1: When player has blackjack in the initial time.
Case 2: Player hits unitl busted.
Case 3: Player hits and stands at value > when dealer reach >=17.
Case 4: Player hits and stands at value< 21 when dealer busts in dealer's turn.
Case 5: Player hits and stands at value < dealer's turn value.
Case 6: Player hits and stands at value= dealer's turn (Tie).
Case 7: Player hits unitl busted but in this case player hits more than one Ace.
Case 8: Player hits and stands at value (contains 2 Aces) > Dealer's turn value (1 Ace).
Case 9: Player hits and stands at value (2 Aces) equals to dealer's turn value (1 Ace) (Tie!).
Case 10: Player hits and stands at value (2 Aces) < dealer's turn value (1 Ace).
Case 11: Player hits and stands at value (3 Aces) > dealer's turn value (1 Ace).

8. All test cases are in .json format.
To run all the test cases, navigate to the folder location and type: python test_game.py
