import os

dir = ("C:\\Users\\Leonardo\\Documents\\GitHub\\parallelstick\\Conversor")
for i in os.listdir(dir):
    files = os.path.join(dir, i)
    split = os.path.splitext(files)
    if split[1] == ".py":
       os.rename(files, split[0] + ".txt")