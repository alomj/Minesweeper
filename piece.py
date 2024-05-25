class Piece():
    def __init__(self, has_bomb):
        self.has_bomb = has_bomb
        self.clicked = False
        self.flagged = False

    def get_has_bomb(self):
        return self.has_bomb

    def get_clicked(self):
        return self.clicked

    def get_flagged(self):
        return self.flagged
