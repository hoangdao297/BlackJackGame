import unittest
import json
from blackjack_input import Game

class TestGame(unittest.TestCase):
  
    def test_winner(self,filename):
        try:
            f = open(filename)
            test=json.load(f)
            f.close()
            game=Game()
            winner=game.playBlackJack(test)
            #Value of winner denotes (0:Dealer, 1: Player, 2:Tie)
            self.assertEqual(winner, test["result"][0], 
            f'Winner in program = {game} and test winner= '+str(test["result"][0]))
            print('\n********Test passed********\n')
        except Exception: print('\n++++++++Test failed++++++++\n')
  
if __name__ == '__main__':
    for i in range(1,12):
        test=TestGame()
        file='test'+str(i)+'.json'
        print("\n--------Test case "+str(i)+"--------\n")
        test.test_winner(file)
