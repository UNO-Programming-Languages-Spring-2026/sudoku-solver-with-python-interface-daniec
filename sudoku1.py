# implement this solver using the clingo.ClingoApp class
import sys, clingo

class ClingoApp(clingo.application.Application):

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