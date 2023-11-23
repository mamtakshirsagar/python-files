import os
folders=input("enter the folder path:").split()
for folder in folders:
    print("-------------------files in folder:", folder)
    try:
        files=os.listdir(folder)
    except FileNotFoundError:
        print("please enter a valid file")
        continue
    for file in files:
        print(file)
