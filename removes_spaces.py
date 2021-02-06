import os

path = r'/Users/maximethomas/Desktop/CORSAIR'


for root, dirs, files in os.walk(path):
        for f in files:
            r = f.replace(" ", "")
            f = os.path.join(root, f)
            r = os.path.join(root, r)
            if (r != f):
                os.renames(f, r)
