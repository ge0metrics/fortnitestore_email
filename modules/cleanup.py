import os

def clean(d):
    files=os.listdir("./{}".format(d))
    for f in files:
        file="./{}/{}".format(d,f)
        os.remove(file)