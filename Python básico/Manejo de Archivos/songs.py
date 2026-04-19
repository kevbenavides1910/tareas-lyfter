# main.py


def read_songs(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        songs = file.readlines()
    return [song.strip() for song in songs if song.strip()]


def sort_songs(songs):
    return sorted(songs)


def save_songs(songs, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        for song in songs:
            file.write(song + "\n")


def main():
    file_path = input("Enter the name of the file (e.g. songs.txt): ")
    songs = read_songs(file_path)
    sorted_songs = sort_songs(songs)
    save_songs(sorted_songs, "sorted_songs.txt")
    print("Done! Sorted songs saved to sorted_songs.txt")


main()
