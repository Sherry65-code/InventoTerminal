from ast import expr_context
from os import system, getcwd
def clear():
    system("clear")

clear()
print("Invento Terminal")
while True:
    cmd = input(f"InTe({getcwd()})>>>")
    commandArray = cmd.split(' ')
    if commandArray[0] == "print":
        g = 0
        while True:
            try:
                print(f"{commandArray[g+1]}",end=" ")
                g+=1
            except Exception as e:
                print()
                break
    elif commandArray[0] == "e":
        print("Exiting...")
        break
    elif commandArray[0] == "":
        pass
    elif commandArray[0] == "c":
        system("clear")
    elif commandArray[0] == "bash":
        g = 1
        x = ""
        while True:
            try:
                x += f"{commandArray[g]} "
                g+=1
            except Exception as e:
                break
        system(x)
    elif commandArray[0] == "update":
        system("sudo apt update")
    elif commandArray[0] == "upgrade":
        system("sudo apt upgrade")
    elif commandArray[0] == "copy":
        system(f"sudo cp {commandArray[1]} {commandArray[2]}")
    elif commandArray[0] == "move":
        system(f"sudo mv {commandArray[1]} {commandArray[2]}")
    elif commandArray[0] == "delete":
        system(f"sudo rm -r {commandArray[1]}")
    elif commandArray[0] == "file":
        system(f"sudo nano {commandArray[1]}")
    elif commandArray[0] == "ld":
        system("ls")
    elif commandArray[0] == "cd":
        system(f"cd {commandArray[1]}")
    elif commandArray[0] == "folder":
        system(f"mkdir {commandArray[1]}")
    elif commandArray[0] == "show":
        system(f"less {commandArray[1]}")
    elif commandArray[0] == "log":
        clear()
        system("less ~/.log_Invento_Terminal.log")
    else:
        print(f"Error. '{commandArray[0]}' is an unknown command")
    