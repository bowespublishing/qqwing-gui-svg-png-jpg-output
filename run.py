import subprocess
from createsudoku import Classcreateasudoku
import PySimpleGUI as gui
import shutil
import os


if __name__ == "__main__":

    ccas = Classcreateasudoku()
    if not ccas.closed:
        ccas.sudokugen()
        filepath2 = os.path.expanduser('~/SudokuGen/')
        gui.popup_ok(
            "Sudoku Puzzles Created Successfully!",
            title="Completed!",
            background_color="#000000",
            icon=(ccas.bpicon_base64),
        )
        ccas.window.close()
    filepath2 = os.path.expanduser('~/SudokuGen/')
    if os.path.exists(filepath2) == True:
        try:
            shutil.rmtree(filepath2)
        except:
            pass
