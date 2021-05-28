import os
from voice import engine


def Shutdown():
    try:
        os.system("shutdown /s /t 1")
    except:
        os.system("shutdown /s /t 0")

def Restart():
    try:
        os.system("shutdown /r /t 1")
    except:
        os.system("shutdown /r /t 0")


def create_file(name):
    if(os.path.exists(f"./createdFiles/{name}.txt")):
        f = open(f"./createdFiles/{name}.txt", "a")
        f.close()
    else:
        f = open(f"./createdFiles/{name}.txt" , "w+")
        f.close()