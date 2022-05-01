from os import system, getcwd
from colorama import Fore
def clear():
    system("clear")

clear()
print(Fore.YELLOW+"Invento Terminal")
while True:
 try:
    print(Fore.GREEN+"InTe",end="")
    print(f"@{getcwd()}~",end="")
    cmd = input(Fore.WHITE)
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
        system(f"touch ./{commandArray[1]}")
    elif commandArray[0] == "ld":
        system("ls")
    elif commandArray[0] == "la":
        system('ls -a')
    elif commandArray[0] == "lal":
        system('ls -al')
    elif commandArray[0] == "cd":
        system(f"cd {commandArray[1]}")
    elif commandArray[0] == "folder":
        system(f"mkdir {commandArray[1]}")
    elif commandArray[0] == "show":
        system(f"less {commandArray[1]}")
    elif commandArray[0] == "log":
        clear()
        system("cat ~/.log_Invento_Terminal.log")
    elif commandArray[0] == 'se':
        system('cat ~/.error.txt')
    elif commandArray[0] == 'ls':
        print("That is a Bash command and you are using InVe Shell. So you should use ld to list directory, la to list directory with hidden files and use lal to list directories with all information avaliable to the Shell.")
    elif commandArray[0] == 'edit':
        system(f'nano {commandArray[1]}')
    elif commandArray[0] == 'get':
        system(f'echo "Downloading && Installing..." && sudo apt install --assume-yes {commandArray[1]} > .error.txt')
    elif commandArray[0] == 'geth':
        system(f'echo "Downloading && Installing..." && sudo apt install --assume-yes {commandArray[1]}')
    elif commandArray[0] == 'getha':
        system(f'echo "Downloading && Installing..." && sudo apt install {commandArray[1]}')
    elif commandArray[0] == 'qmake':
        system('make')
    elif commandArray[0] == 'qmakei':
        system('sudo make install')
    elif commandArray[0] == 'read':
        system(f'cat {commandArray[1]}')
    elif commandArray[0] == 'sys':
        system(f'systemctl {commandArray[1]}')
    else:
        print(f"Error. '{commandArray[0]}' is an unknown command")
 except Exception as e:
     system(f'echo "{e}" > ~/.error.txt')
     print("An Unknown exception occured. try 'se' to check the error.")