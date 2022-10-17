import json

class Card:
    def __init__(self,cardSuit,cardFace,cardValue) -> None:
        #Represent for the suit of card
        self.suit=cardSuit 

        #Represent for the face of card (ex: Q for Queen, K for King, A for Ace)
        self.face=cardFace

        #Represent for the value of the card (10 for Queen, King, Jack)
        self.value=cardValue

class Game:
    #This function is used for finding card in the deck with the equivalent value of card
    def findCardinDeck(self,suit,face,value,deck):
        for card in deck:
            if card.suit==suit and card.face==face and card.value==value: return card
        return None

    def playBlackJack(self,test):
        #Suits of cards
        suits=['spades','clubs','diamonds','hearts']

        #Faces and Values of cards
        card_Face_Value = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10,"A": 11}

        #deck of cards
        deck=[]

        #Making deck
        for card_suit in suits:
            for card_face,card_value in card_Face_Value.items():

                deck.append(Card(card_suit,card_face,card_value)) #Insert card to the deck

        #Initiate dealer's cards and points
        dealer_cards, dealer_points=[],0

        #Initiate player's cards and points
        player_cards, player_points=[], 0

        #winner (This is for testing only)
        winner=None

        #Test Data
        testDealer=test["Dealer"]
        testPlayer=test["Player"]

        #Welcome statement
        print("\t\tWELCOME TO BLACK JACK GAME\n")

        #Providing starting 2 cards for dealer and player
        i=0
        while (len(player_cards)<2):

            #Random card for player
            random_playerCard=self.findCardinDeck(testPlayer['Init'][i][0],testPlayer['Init'][i][1],
            card_Face_Value[testPlayer['Init'][i][1]],deck)


            #Remove that card from deck
            deck.remove(random_playerCard)

            #Add it player cards
            player_cards.append(random_playerCard)

            #Add the points of card to player points
            player_points+=random_playerCard.value

            #Case if there are 2 Ace cards in player cards, make one Ace card value to 1
            if (len(player_cards)==2 and player_cards[0].face=="A" and player_cards[1].face=="A"):
                player_cards[0].value=1
                player_points-=10

            #Random card for dealer
            random_dealerCard=self.findCardinDeck(testDealer["Init"][i][0],testDealer["Init"][i][1],
            card_Face_Value[testDealer["Init"][i][1]],deck)

            #Remove that card from deck
            deck.remove(random_dealerCard)

            #Add it dealer cards
            dealer_cards.append(random_dealerCard)

            #Add the points of card to dealer points
            dealer_points+=random_dealerCard.value

            #Case if there are 2 Ace cards in dealer cards, make one Ace card value to 1
            if (len(dealer_cards)==2 and dealer_cards[0].face=="A" and dealer_cards[1].face=="A"):
                dealer_cards[0].value=1
                dealer_points-=10

            i+=1

        #Print initial 2 cards for player and 1 card for dealer
        print("Dealer has: {} ? = ?".format(dealer_cards[0].face))
        print("Player has: {} {} = {}".format(player_cards[0].face, player_cards[1].face, player_points))

        #If player gets 21, player wins. 
        if (player_points==21):
            print("Player wins!\nBlackJack!")
            winner=1
            return winner

        #Input player commands from test
        playerCMD=testPlayer["CMD"]
        i=0

        while (player_points<21):
            #For random
            # user_choice=input("Would you like to (H)it or (S)tand? ")
            # if (len(user_choice)!=1 or (user_choice.upper() !="H" and user_choice.upper() !="S")):
            #     print("Please choose again! (type h or H for hit and s or S for stand")

            #For specific input
            user_choice=playerCMD[i][0]

            #Hit option
            if user_choice.upper()=="H":

                #Random card for player
                random_playerCard=self.findCardinDeck(playerCMD[i][1],playerCMD[i][2],
            card_Face_Value[playerCMD[i][2]],deck)

                #Remove that card from deck
                deck.remove(random_playerCard)

                #Add it player cards
                player_cards.append(random_playerCard)

                #Add the points of card to player points
                player_points+=random_playerCard.value

                # Processing player's points in case player's cards have ace(s) in them that makes them exceed 21
                index_card=0
                while (index_card<len(player_cards) and player_points>21):
                    if player_cards[index_card].value==11:
                        player_cards[index_card].value=1
                        player_points-=10
                    index_card+=1
                
                #Print player's points after hitting
                str_player_cards=" "
                for card in player_cards: str_player_cards+=card.face+" "
                print("Player has:{}= {}".format(str_player_cards, player_points))

                #Player busts (points>21)
                if (player_points>21):
                    print("Player busts with {}\nDealer wins!".format(player_points))
                    winner=0
                    return winner
                    quit()

                #Player wins (points=21)
                if (player_points==21):
                    print("\nPlayer wins!\nBlackJack!")
                    winner=1
                    return winner
                    quit()

            #Stand option
            if user_choice.upper()=="S":
                str_player_cards=" "
                for card in player_cards: str_player_cards+=card.face+" "
                print("\nPlayer stands with:{}= {}\n".format(str_player_cards, player_points))
                break

            i+=1

        #Print dealer's current cards and points
        str_dealer_cards=" "
        for card in dealer_cards: str_dealer_cards+=card.face+" "
        print("Dealer has:{}= {}".format(str_dealer_cards, dealer_points))

        #Dealer's turn

        #Dealer input card
        dealerCMD=testDealer["CMD"]
        i=0

        while (dealer_points<17):

            print("Dealer hits")

            #Random card for dealer
            random_dealerCard=self.findCardinDeck(dealerCMD[i][0],dealerCMD[i][1],
            card_Face_Value[dealerCMD[i][1]],deck)

            #Remove that card from deck
            deck.remove(random_dealerCard)

            #Add it dealer cards
            dealer_cards.append(random_dealerCard)

            #Add the points of card to dealer points
            dealer_points+=random_dealerCard.value

            # Processing dealer's points in case dealer's cards have ace(s) in them that makes them exceed 21
            index_card=0
            while (index_card<len(dealer_cards) and dealer_points>21):
                if dealer_cards[index_card].value==11:
                    dealer_cards[index_card].value=1
                    dealer_points-=10
                index_card+=1

            #Print dealer's points after hitting
            str_dealer_cards=" "
            for card in dealer_cards: str_dealer_cards+=card.face+" "
            print("Dealer has:{}= {}".format(str_dealer_cards, dealer_points))

            #Dealer busts (points>21)
            if (dealer_points>21):
                print("Dealer busts with {}\nPlayer wins!".format(dealer_points))
                winner=1
                return winner
                quit()
            i+=1
        
        print("Dealer stands\n")

        #Dealer has Black Jack
        if (dealer_points==21):
            print("Dealer wins!\nBlackJack!")
            winner=0
            return winner
            quit()

        #Dealer loses
        if (dealer_points<player_points):
            print("Player wins!")
            str_player_cards=""
            for card in player_cards: str_player_cards+=card.face+" "
            str_dealer_cards=" "
            for card in dealer_cards: str_dealer_cards+=card.face+" "
            print("{}= {} to Dealer's{}= {}".format(str_player_cards, player_points, str_dealer_cards, dealer_points))
            winner=1
            return winner
            quit()

        #Player ties with Dealer
        elif (dealer_points==player_points):
            print("Tie!")
            str_player_cards=""
            for card in player_cards: str_player_cards+=card.face+" "
            str_dealer_cards=" "
            for card in dealer_cards: str_dealer_cards+=card.face+" "
            print("{}= {} equal to Dealer's{}= {}".format(str_player_cards, player_points, str_dealer_cards, dealer_points))
            winner=2
            return winner
            quit()

        #Dealer wins
        else:
            print("Dealer wins!")
            str_player_cards=" "
            for card in player_cards: str_player_cards+=card.face+" "
            str_dealer_cards=""
            for card in dealer_cards: str_dealer_cards+=card.face+" "
            print("{}= {} to Player's{}= {}".format(str_dealer_cards, dealer_points, str_player_cards, player_points))
            winner=0
            return winner
            quit()


def main():
    f = open('test1.json')
    test=json.load(f)
    f.close()
    game=Game()
    winner=game.playBlackJack(test)
    print(winner)


#main()