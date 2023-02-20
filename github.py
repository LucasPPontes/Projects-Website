import os
import time

os.system("git status")
os.system("git add .")
os.system("git commit -m done ")
os.system("git status")
os.system("git push -uf origin main")

time.sleep(10)