#!/usr/bin/python3
import os
from sys import argv
from pathlib import Path
from py_compile import compile
if __name__ == "__main__":
    filename = os.getenv("PYFILE")
    print(f"Compiling {filename} ...")
    compile(filename, cfile=filename + "c")
