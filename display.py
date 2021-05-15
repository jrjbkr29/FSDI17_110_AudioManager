import os

def print_menu():
    print_header("** Audio Manager 3000**")
    print("[1]- Register Album")
    print("[2]- Register Song")
    print("[3]- Print Catalog")
    print("[4]- Print songs of album")
    print("[5]- Count all the songs in the system")
    print("[6]- Total $ in the catalog")
    print("[7]- Delete Song")
    print("[8]- Delete Album") # only let user delete empty album, do no let them delete with songs inside
    
    print("[q] Quit")


def clear_screen():
    if(os.name == 'nt'):
        return os.system('cls')
    else:
        return os.system('clear')
    # return os.system('cls' if os.name == 'nt' else 'clear')


def print_header(text):
    clear_screen()
    print("-" * 30)
    print("**" + text)
    print("-" * 30)
