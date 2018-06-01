import functional


class Game:
    """
    Class to initialise game.
    """
    def __init__(self, coord1, coord2):
        self.c1 = coord1
        self.c2 = coord2
        self.move = [self.c1, self.c2]
        self.sides = [player1, player2]

    def player_move(self):
        """
        Makes a tuple of entered players move.
        :return: (tuple)
        """
        return tuple(input("Enter a move: "))

    def field_with_ships(self, choice):
        """
        Retutn string of coordinates that were shooted by player.
        :return: (list)
        """
        self.move.append(choice)


class Field(Game):
    """
    Class for representing game field.
    """
    def __init__(self, c1=[], c2=[]):
        super().__init__(c1, c2)
        self.ships = []
        self.fil = [c1, c2]

    def shoot_at(self, choice):
        """
        Return list containing shooted squares.
        :return: (list)
        """
        self.ships.append(choice)
        return self.ships



class Player(Game):
    """
    Creates the players.
    """
    def __init__(self, name, coord1, coord2):
        super().__init__(coord1, coord2)
        self.name = name

    def choice(self):
        return self.player_move()

player1 = Player("M")
player2 = Player("B")
field1 = Field()
field2 = Field()
field = [(i, str(n)) for n in range(1, 11) for i in "ABCDEFGHIK"]

