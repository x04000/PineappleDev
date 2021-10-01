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
           \x1b[0;36mVersion: 0.3
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
    """)
def p_clear():
    try:
        import os
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    except:
        print("Error with clear command!")
def p_exit():
    try:
        exit()
    except:
        print("Program can't exit!")
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
            print("Error during creating the file!")
def p_DELFILE(file):
    import os
    delfilewin = "del /f /a "+file
    delfilelinux = "rm "+file
    try:
        os.system(delfilewin if os.name in ('nt', 'dos') else delfilelinux)
    except:
        print("Error during deletion of file!")
def p_WFILE(file, write):
    try:
        f=open(file, "w")
        f.write(write)
        f.close()
    except:
        print("Error during writting of file")
def p_RFILE(file):
    try:
        with open(file,"r") as archivo:
            for linea in archivo:
                print(linea)
    except:
        print("File can't load!")
def p_gitclone(gitcloneurl):
    import os
    gitcloneurl = str(input("URL of Git > "))
    gitclonecommand = "git clone "+gitcloneurl
    try:
        os.system(gitclonecommand)
    except:
        print("Git error!")
def p_ls():
    import os
    try:
        os.system("dir" if os.name in ('nt', 'dos') else "ls")
        print("")
    except:
        print("Ls error")
def p_pipinstall(pipinstallpackage):
    import os
    pipinstallpackage = str(input("Name of package > "))
    pipinstallcommand = "pip install "+pipinstallpackage
    try:
        os.system(pipinstallcommand)
    except:
        print("Python: Pip error!")
def p_pipuninstall(pipuninstallpackage):
    import os
    pipuninstallpackage = str(input("Name of package > "))
    pipuninstallcommand = "pip uninstall "+pipuninstallpackage
    try:
        os.system(pipuninstallcommand)
    except:
        print("Python: Pip error!")
def p_piplist():
    import os
    try:
        os.system("pip list")
    except:
        print("Python: Pip error!")
def p_systemterminal():
    import os
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
                os.system(systemterminalcommand)
            except:
                print("PineappleDev System Terminal error!")
def p_python():
    import os
    try:
        os.system("python")
    except:
        print("PineappleDev can't load python. Revise your python installation")
def p_python3():
    import os
    try:
        os.system("python3")
    except:
        print("PineappleDev can't load python3. Revise your python3 installation")
def p_sys(command):
    try:
        import os
        os.system(command)
    except:
        print("Command error")