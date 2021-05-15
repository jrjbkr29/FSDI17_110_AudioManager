"""
Audio Manager:
    Console application that alow the user to register his/her audio collection
Author: 
    Johnny Jimenez
Functionality:
    1 - Register Album
    2 - Register song
    3 - Display Catalog
"""

# imports
from display import print_menu, clear_screen, print_header
from album import Album
from song import Song
import pickle

# global vars
catalog = []

# functions


def serialize_data():
    writer = open('sngManager.data', 'wb')  # wb = written binary
    pickle.dump(catalog, writer)
    writer.close()
    print("** Data Saved!")


def deserialize_data():
    try:
        reader = open('sngManager.data', 'rb')  # rb = read binary
        temp_list = pickle.load(reader)
        reader.close()

        for item in temp_list:
            catalog.append(item)

        print(f"** Loaded {len(catalog)} albums ")
    except:
        print("** Error saving data")


def register_album():
    print_header("Register new album")
    title = input("Provide the Title: ")
    genre = input("Provide the Genre: ")
    artist = input("Provide the Artist Name: ")
    price = float(input("Provide the Price: "))
    year = int(input("Provide the Release Year: "))
    songs = []
    id = 1
    if(len(catalog) > 0):
        last = catalog[-1]
        id = last.id + 1

    album = Album(id, title, genre, artist, price, year, songs)
    catalog.append(album)
    print(album)


def register_song():
    print_catalog()

    id = int(input("Please select an album id"))

    found = False
    for album in catalog:
        if(album.id == id):
            found = True
            print_header(f"Add song to album: {album.title}")
            title = input("Provide the title: ")
            length = int(input("Provide length in secs"))
            composer = input("Provide the composer")

            song_id = 1
            if(len(song_id) > 0):
                last_song = song_id[-1]
                song_id = last_song.song_id + 1

            song = Song(song_id, title, length, composer)
            album.songs.append(song)
        if not found:
            print("Error: Wrong album id, try again!")


def print_catalog():
    print_header("Your catalog")

    for album in catalog:
        print(album)


def print_songs():
    print_catalog()

    id = int(input("Please select an album id"))

    found = False
    for album in catalog:
        if(album.id == id):
            found = True
            print_header(f"Songs inside album: {album.title}")
            for song in album.songs:
                print(f"{song.id} | {song.title}")
        if not found:
            print("Error: Wrong album id, try again!")

def count_songs():
    print_header("Total songs in the system")
    song_count = 0
    for album in catalog:    
        song_count += len(album.songs)
    
    song_count_array = len([al.songs for al in catalog])
    print(song_count)
    print(f"song count array: {song_count_array}")



def total():
    print_header("Total $ of the catalog")

    total = 0

    for album in catalog:
        total += album.price

    print(f"The total is ${total}")


def delete_song():
    print("delete song")
    song_to_delete = int(input(""))

def delete_album():
    print("delete album")


# instructions
deserialize_data()

opc = ''
while(opc != 'q'):
    print_menu()
    opc = input("Please select an option: ")

    if(opc == '1'):
        register_album()
        serialize_data()
    elif(opc == '2'):
        register_song()
        serialize_data()
    elif(opc == '3'):
        print_catalog()
    elif(opc == '4'):
        print_songs()
    elif(opc == '5'):
        count_songs()
    elif(opc == '6'):
        total()
    elif(opc == '7'):
        delete_song()
    elif(opc == '8'):
        delete_album()

    input("Press Enter to continue...")
    clear_screen()

print("Good bye!")
