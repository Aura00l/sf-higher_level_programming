#!/usr/bin/python3
import os
import sys
import py_compile

if __name__ == "__main__":
    filename = os.getenv("PYFILE")
    print(f"Compiling {filename} ...")
    py_compile.compile(filename, cfile=filename + "c")
