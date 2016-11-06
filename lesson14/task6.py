# UML

class Game:
    def __init__(self, player1,player2):
        self.player1 = player1
        self.player2 = player2

    def startGame(self):
        while True:
            if self.player1.isEmptyCell():
                self.player1.move()
                if self.player1.isWinner():
                    print("Winner" , self.player1)
                    break
            else:
                print("Draw")
                break
            if self.player2.isEmptyCell():
                self.player2.move()
                if self.player2.isWinner():
                    print("Winner" , self.player2)
                    break
            else:
                print("Draw")
                break

class Player:
    def __init__(self, field, fieldType):
        self.field = field
        self.fieldType = fieldType

    def isEmptyCell(self):
        return self.field.isEmptyCell

    def move(self):
        pass

    def isWinner(self):
        return self.field.isLine(self.fieldType) # check O or X there

class Humen(Player):
    def __init__(self, field, fieldType):
        Player.__init__(self,field, fieldType)

    def move(self):
        x = int(input('Enter x:\n'))
        y = int(input('Enter x:\n'))
        self.field.step(x,y,self.fieldType)
        self.field.show()



