from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""

        # loop through each row (1-9)
        for row in range(1, 10):
            # add an empty line between blocks of 3 rows
            if row % 3 == 1 and row > 1:
                s += "\n"   
            
            # loop through each column (1-9)
            for col in range(1, 10):
                # add an empty line between blocks of 3 columns
                if col % 3 == 1 and col > 1:
                    s += "  "
                else:
                    s += " "
            
                # get the value at (row, col) and add it to the string
                value = self.sudoku.get((row, col), 0)
                s += str(value)

            # add a newline at the end of each row
            s += "\n"
            
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}

        # get the symbols from the model
        for atom in model.symbols(shown=True):

            # loop through each symbol and extract the row, column, and value
            if atom.name == "sudoku" and len(atom.arguments) == 3:
                row = atom.arguments[0].number
                col = atom.arguments[1].number
                value = atom.arguments[2].number

                # add each (row, column) -> value entry to the board dictionary
                sudoku[(row, col)] = value

        return cls(sudoku)
