# copy of sudoku4.py modified to read input in formatted sudoku style and 
# convert it to clingo symbols using the Context class
import sys, clingo
from sudoku_board import Sudoku

class Context:
    def __init__(self, board: Sudoku):
        # store the sudoku board for use in the initial method
        self.board = board
        
    def initial(self) -> list[clingo.symbol.Symbol]:
        symbols = []
        # loop through each cell in the board
        for (row, col), value in self.board.sudoku.items():

            # create a clingo tuple symbol for each (row, col, value) entry
            symbol = clingo.Tuple_((clingo.Number(row), clingo.Number(col), clingo.Number(value)))

            # add the symbols to the list
            symbols.append(symbol)

        # return the list of symbols
        return symbols

class ClingoApp(clingo.application.Application):

    # overwrite print_model to output the solution in formatted sudoku style
    def print_model(self, model, printer):
        # use Sudoku.from_model() to parse the model into a Sudoku object
        sudoku = Sudoku.from_model(model)
        # print the Sudoku object using __str__ (which formats it correctly)
        print(sudoku)


    def main(self, ctl, files):
        # load the sudoku encoding
        ctl.load("sudoku.lp")
        # load the sudoku instance
        ctl.load(files[0])
        # ground the program and solve
        ctl.ground([("base", [])])
        ctl.solve()

if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp())