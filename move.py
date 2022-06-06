class Move:
    def __init__(self,old_pos,new_pos,from_obj,kill_obj,kill=False,check=False):
        self.old_pos = old_pos
        self.new_pos = new_pos
        self.from_obj = from_obj.copy()
        if not kill_obj:
            self.kill_obj = None
        else:
            self.kill_obj = kill_obj.copy()
        self.kill = kill
        self.check = check

    def undo_pos(self,board):
        xo,yo = self.old_pos
        xn,yn = self.new_pos
        board[xn][yn] = self.kill_obj
        board[xo][yo] = self.from_obj

        return board
