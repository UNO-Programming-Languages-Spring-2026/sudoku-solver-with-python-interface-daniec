# copy of sudoku1.py modified to print the solution in the formatted sudoku style
import sys
import clingo
from sudoku_board import Sudoku


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