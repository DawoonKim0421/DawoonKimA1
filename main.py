"""
Replace the contents of this module docstring with your own details
Name: Da Woon Kim
Date started: 17.04.2020 18:56
GitHub URL: https://github.com/DawoonKim0421/DawoonKimA1
"""

from operator import itemgetter

# Preparing the .csv for use
data_list = []
songs_file = "songs.csv"


def read_file():
    file = open(songs_file, "r")
    for data in file.readlines():
        data = data.strip()  # delete the white spaces within the csv file
        data = data.split(",")
        data_list.sort(key=itemgetter(1, 2))  # list the songs by their Artist name then by their released year
        data_list.append(data)  # adds the edited version of the csv file (data) to the data_list
    file.close()


# Welcome message and menu display
def main():
    read_file()  # read songs.csv file
    print("Songs to Learn 1.0 - by Da Woon Kim")
    number_songs = count_songs()  # counts how many songs in the csv file
    print("{} songs loaded".format(number_songs))
    while True:
        print("Menu :")
        print("L - List songs\nA - Add new song\nC - Complete a song\nQ - Quit")
        reply = input(">>>")
        reply = reply.upper()  # transform all letters to be uppercase so the menu can handle uppercase and lowercase
        reply = valid_reply(reply)  # checks the validity of the input
        if reply == "L":
            list_song()
        if reply == "C":
            complete_song()
        if reply == "A":
            add_song()
        if reply == "Q":
            quit_program()
            break
    print("Have a nice day :)")


def count_songs():
    songs = 0
    for song in range(len(data_list)):
        songs += 1
    return songs


# program will keep on asking for other input until the user give the right input
def valid_reply(choice):
    while choice != "L" and choice != "A" and choice != "C" and choice != "Q":
        print("Invalid menu choice")
        print("Menu :")
        print("L - List songs\nA - Add new song\nC - Complete a song\nQ - Quit")
        choice = input(">>>")
        choice = choice.upper()
    return choice


def list_song():
    learned = 0  # start the variable learned as 0
    unlearned = 0  # start the variable not_learned as 0
    for song_num, data in enumerate(data_list):
        if data[3] == "y":
            print("{0}. '*', {1:<30} - {2:<25} ({3})".format(song_num, data[0], data[1], data[2]))
            unlearned += 1
            song_num += 1
        else:
            print("{0}. {1:<30} - {2:<25} ({3})".format(song_num, data[0], data[1], data[2]))
            learned += 1
            song_num += 1
    print("{} songs learned, {} songs still need to learn".format(learned, unlearned))


def complete_song():
    amount_complete = 0
    for complete in data_list:
        if complete[3] == "y":
            amount_complete -= 1
    songs_amount = int(count_songs())  # counts the amount of song at the moment
    if amount_complete != 0:
        print("Enter a number of a song to mark as learned")
        while True:
            try:
                respond = int(input(">>>"))
                if respond >= songs_amount:
                    print("Invalid song number")
                elif respond < 0:
                    print("Number must be >= 0")
                else:
                    break
            except ValueError:
                print("Invalid input; enter a valid number")
        for index, data in enumerate(data_list):
            if index == respond:
                if data[3] == "y":
                    data[3] = "n"
                    print("{} by {} learned".format(data[0], data[1]))
                else:
                    print("You have already learned {}".format(data[0]))
    else:
        print("No more songs to learn!")


def add_song():
    song_add = []
    while True:
        title = str(input("Title: "))
        if title == "":  # prevent the user inserting a blank input
            print("Input can not be blank")
        else:
            break
    song_add.append(title)  # add a new info (title) to the song_add

    while True:
        artist = str(input("Artist: "))
        if artist == "":  # prevent the user inserting a blank input
            print("Input can not be blank")
        else:
            break
    song_add.append(artist)  # add a new info (title) to the song_add

    while True:
        try:
            year = int(input("Year: "))
            if year <= 0:  # to prevent the user inserting negative numbers
                print("Number must be >=0")
            else:
                break
        except ValueError:
            print("Invalid input; enter a valid number")
    song_add.append(str(year))  # add a new info (title) to the song_add
    print("{} by {} ({}) added to song list".format(title, artist, year))
    song_add.append("y")  # to add the status of the new song (in this case not learned)
    data_list.append(song_add)
    data_list.sort(key=itemgetter(1, 2))


def quit_program():
    count_songs()
    print("{} songs saved to songs.csv".format(count_songs()))
    file_overwrite = open(songs_file, "w")  # clear the the songs_file
    for song in data_list:
        new_file = "{},{},{},{}".format(song[0], song[1], song[2], song[3]) + "\n"
        file_overwrite.write(new_file)
    file_overwrite.close()


if __name__ == '__main__':
    main()