def fill_list():
    playlist = []
    for i in range(5):
        playlist.append(input("Song" + str(i + 1) + ':'))
    return playlist

print(fill_list())
