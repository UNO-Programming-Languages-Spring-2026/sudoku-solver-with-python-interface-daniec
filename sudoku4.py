# implement this solver using the clingo.ClingoApp class
import sys, clingo
from xml.parsers.expat import model

class ClingoApp(clingo.application.Application):

    # overwrite print_model to sort the output alphabetically
    def print_model(self, model, printer):
        # get the atoms in the model
        atoms = list(model.symbols(shown=True))
        # sort the atoms alphabetically by their string representation
        atoms = sorted(atoms, key=str)
        # print the sorted atoms space-separated on one line
        print(" ".join(str(atom) for atom in atoms))


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