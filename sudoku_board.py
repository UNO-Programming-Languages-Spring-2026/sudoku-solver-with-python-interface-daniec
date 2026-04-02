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
        
        # split the string into rows and filter out empty lines
        rows = [row for row in s.split("\n") if row.strip()]
        
        # loop through each row with its actual sudoku row number
        for row_idx, row in enumerate(rows, start=1):
       
            # split the row into values filtering out empty strings from double spaces
            values = [v for v in row.split(" ") if v]

            # loop through each value with its column number
            for col_idx, value in enumerate(values, start=1):

                # if the value is a number add it to the dictionary
                if value.isdigit():
                    sudoku[(row_idx, col_idx)] = int(value)
                    
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
