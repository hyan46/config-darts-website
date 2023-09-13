import pandas as pd
import matplotlib.pyplot as plt
import pathlib


print("Hello everyone!!!")

def hello_func():
    print("Hello ther!")
    return "Hello response"

def read_file():
    print("ehllo")
    print(pathlib.Path().resolve())
    print(pathlib.Path(__file__).parent.resolve())
    # f = open("./file.txt","r")
    # lines = f.readlines()
    # print(lines)
