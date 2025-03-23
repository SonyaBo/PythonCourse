class ChessFigure:
    color = True
    place = ('',0)

    def change_color(self) -> None:
        self.color = not self.color


    def change_place(self,letter: str,numb: int)-> None:
        if numb <= 8 and numb >=1:
            if letter in "acdefgh" and len(letter)==1:
                self.place = (letter,numb)

    def check(self):
        raise NotImplementedError

class Pawn(ChessFigure):

    def check(self):
        pass

class Rook(ChessFigure):
    pass


ch = ChessFigure()
print(ch.place)
ch.change_place("g",1)
print(ch.place)