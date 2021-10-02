def p_help():
    print("""\x1b[0;35m
_____________                                   ______    ________             
___  __ \__(_)_________________ ___________________  /_______  __ \_______   __
__  /_/ /_  /__  __ \  _ \  __ `/__  __ \__  __ \_  /_  _ \_  / / /  _ \_ | / /
_  ____/_  / _  / / /  __/ /_/ /__  /_/ /_  /_/ /  / /  __/  /_/ //  __/_ |/ / 
/_/     /_/  /_/ /_/\___/\__,_/ _  .___/_  .___//_/  \___//_____/ \___/_____/  
                                /_/     /_/                                   
\x1b[0;31m
###################################
             \x1b[0;34mBy x04000
     \x1b[0;33mGithub: github.com/x04000
           \x1b[0;32mBase: Python
           \x1b[0;36mVersion: 1.0
\x1b[0;31m###################################
\x1b[0;31m    
  /\  /\___| |_ __  
 / /_/ / _ \ | '_ \ 
/ __  /  __/ | |_) |
\/ /_/ \___|_| .__/ 
             |_|    
\x1b[0;35m

p_exit()                                - Exit the program
p_clear()                               - Clear the console
p_ep(text)                              - Print a text in console
p_CFILE(file.extension)                 - Create a file
p_WFILE(file.extension, text)           - Write a file
p_DELFILE(file.extension)               - Delete a file
p_RFILE(file.extension)                 - Read a file
p_gitclone(giturl)                      - Use Git clone
p_pipinstall(package)                   - Pip install
p_pipuninstall(package)                 - Pip uninstall
p_piplist()                             - Pip packahe list
p_systemterminal()                      - To use your terminal commands
p_python()                              - Use the python terminal
p_python3()                             - Use the python3 terminal
p_sys(command)                          - Execute a command in your system terminal
p_credits                               - Show the credits
p_login("username","password")          - A simple login
p_login_nologo("username","password")   - A simple login without Login logo
p_setcolor("colorid")                   - Set a color. IDs are from number 30
p_pin(pin)                              - A simple PIN function
p_pin_noint(pin)                        - A simple PIN function without having to be in int format
    """)
def p_credits():
    print("""\x1b[0;35m
_____________                                   ______    ________             
___  __ \__(_)_________________ ___________________  /_______  __ \_______   __
__  /_/ /_  /__  __ \  _ \  __ `/__  __ \__  __ \_  /_  _ \_  / / /  _ \_ | / /
_  ____/_  / _  / / /  __/ /_/ /__  /_/ /_  /_/ /  / /  __/  /_/ //  __/_ |/ / 
/_/     /_/  /_/ /_/\___/\__,_/ _  .___/_  .___//_/  \___//_____/ \___/_____/  
                                /_/     /_/                                   
\x1b[0;31m
   ______              ___ __      
  / ____/_______  ____/ (_) /______
 / /   / ___/ _ \/ __  / / __/ ___/
/ /___/ /  /  __/ /_/ / / /_(__  ) 
\____/_/   \___/\__,_/_/\__/____/  
\x1b[0;35m
Idea, desing and developer: x04000
Ideas and help: GhostTD
    """)
def p_clear():
    try:
        import os
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    except:
        print("\nPineappleDev > Error with clear command!")
def p_exit():
    try:
        exit()
    except:
        print("")
def p_ep(ep):
    try:
        print(ep)
    except:
        print("")
def p_CFILE(file):
        try:
            f=open(file,"w")
            f.close()
        except:
            print("\nPineappleDev > Error during creating the file!")
def p_DELFILE(file):
    import os
    delfilewin = "del /f /a "+file
    delfilelinux = "rm "+file
    try:
        os.system(delfilewin if os.name in ('nt', 'dos') else delfilelinux)
    except:
        print("\nPineappleDev > Error during deletion of file!")
def p_WFILE(file, write):
    try:
        f=open(file, "w")
        f.write(write)
        f.close()
    except:
        print("\nPineappleDev > Error during writting of file")
def p_RFILE(file):
    try:
        with open(file,"r") as archivo:
            for linea in archivo:
                print(linea)
    except:
        print("\nFile can't load!")
def p_gitclone(gitcloneurl):
    gitcloneurl = str(input("URL of Git > "))
    gitclonecommand = "git clone "+gitcloneurl
    try:
        import os
        os.system(gitclonecommand)
    except:
        print("\nPineappleDev > Git error!")
def p_ls():
    try:
        import os
        os.system("dir" if os.name in ('nt', 'dos') else "ls")
        print("")
    except:
        print("\nPineappleDev > Ls error")
def p_pipinstall(pipinstallpackage):
    pipinstallpackage = str(input("Name of package > "))
    pipinstallcommand = "pip install "+pipinstallpackage
    try:
        import os
        os.system(pipinstallcommand)
    except:
        print("\nPineappleDev > Python: Pip error!")
def p_pipuninstall(pipuninstallpackage):
    pipuninstallpackage = str(input("Name of package > "))
    pipuninstallcommand = "pip uninstall "+pipuninstallpackage
    try:
        import os
        os.system(pipuninstallcommand)
    except:
        print("\nPineappleDev > Python: Pip error!")
def p_piplist():
    try:
        import os
        os.system("pip list")
    except:
        print("\nPineappleDev > Python: Pip error!")
def p_systemterminal():
    print("[PineappleDev System Terminal]")
    print("")
    print("""[INFO]

You can use your terminal commands here ;)
To close the System Terminal use: p_closeterminal

    """)
    while(True):
        systemterminalcommand = str(input("PineappleDev SysTerminal > "))
        print("")
        if systemterminalcommand == "p_closeterminal":
            break
        else:
            try:
                import os
                os.system(systemterminalcommand)
            except:
                print("\nPineappleDev > PineappleDev System Terminal error!")
def p_python():
    try:
        import os
        os.system("python")
    except:
        print("\nPineappleDev > PineappleDev can't load python. Revise your python installation")
def p_python3():
    try:
        import os
        os.system("python3")
    except:
        print("\nPineappleDev > PineappleDev can't load python3. Revise your python3 installation")
def p_sys(command):
    try:
        import os
        os.system(command)
    except:
        print("Command error")
def p_login(pineappledevusername, pineappledevpassword):
    try:
        from getpass import getpass
        print("""
    ██▓     ▒█████    ▄████  ██▓ ███▄    █ 
    ▓██▒    ▒██▒  ██▒ ██▒ ▀█▒▓██▒ ██ ▀█   █ 
    ▒██░    ▒██░  ██▒▒██░▄▄▄░▒██▒▓██  ▀█ ██▒
    ▒██░    ▒██   ██░░▓█  ██▓░██░▓██▒  ▐▌██▒
    ░██████▒░ ████▓▒░░▒▓███▀▒░██░▒██░   ▓██░
    ░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒ ░▓  ░ ▒░   ▒ ▒ 
    ░ ░ ▒  ░  ░ ▒ ▒░   ░   ░  ▒ ░░ ░░   ░ ▒░
    ░ ░   ░ ░ ░ ▒  ░ ░   ░  ▒ ░   ░   ░ ░ 
        ░  ░    ░ ░        ░  ░           ░   

        """)
        while(True):
            pineappledevusernameinput = str(input("Username: "))
            if pineappledevusernameinput == str(pineappledevusername):
                break
            else:
                print("Incorrect username!")
        while(True):
            pineappledevpasswordinput = getpass("Password: ")
            if pineappledevpasswordinput == str(pineappledevpassword):
                print("Successfully login!")
                break
            else:
                print("Incorrect password!")
    except:
        print("\nPineappleDev > A error ocurred during the login")
def p_login_nologo(pineappledevusername, pineappledevpassword):
    try:
        from getpass import getpass
        print("[Login]")
        while(True):
            pineappledevusernameinput = str(input("Username: "))
            if pineappledevusernameinput == str(pineappledevusername):
                break
            else:
                print("Incorrect username!")
        while(True):
            pineappledevpasswordinput = getpass("Password: ")
            if pineappledevpasswordinput == str(pineappledevpassword):
                print("Successfully login!")
                break
            else:
                print("Incorrect password!")
    except:
        print("\nPineappleDev > A error ocurred during the login")
def p_setcolor(pineappledevcolorid):
    try:
        pineappledevcolor = "\x1b[0;"+str(pineappledevcolorid)+"m"
        print(pineappledevcolor)
    except:
        print("PineappleDev > A error ocurred during the setcolor function")
def p_pin(pineappledevpin):
    try:
        from getpass import getpass
        while(True):
            print(str(pineappledevpin))
            pineappledevpininput = int(getpass("PIN: "))
            if pineappledevpininput == pineappledevpin:
                print("The PIN is correct!")
                break
            else:
                print("Incorrect PIN!")
    except:
        print("\nPineappleDev > A error ocurred during the PIN function")
def p_pin_noint(pineappledevpin):
    try:
        from getpass import getpass
        while(True):
            print(str(pineappledevpin))
            pineappledevpininput = getpass("PIN: ")
            if pineappledevpininput == pineappledevpin:
                print("The PIN is correct!")
                break
            else:
                print("Incorrect PIN!")
    except:
        print("\nPineappleDev > A error ocurred during the PIN function")