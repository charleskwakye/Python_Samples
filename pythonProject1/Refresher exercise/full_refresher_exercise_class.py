playlist=['Binding lights','Dance monkey','Sweet but psycho','Imagine dragons','Mirrors']
#number 1
def fill_list():
    playlist=[]
    for i in range(5):
       playlist.append(input('Song '+str(i+1)+':'))
    return playlist

#Number2
def menu():
    print('\ta - Overview\n\tb - Define longest title\n\tc - 5 letters in a row\n\td '
          '- No vowels\n\te - Cutting the playlist\n\ts - Stop')
    answer = input('\tMake a selection: ').lower()
    return answer

#number3
def print_overview(playlist):
    print('Playlist')
    for i in range(len(playlist)):
        print(i+1,playlist[i])
    print()

def valid_input():
    number = int(input('Enter the number of songs max' + str(len(playlist)) + ':'))
    while number not in range(1, len(playlist) + 1):
        number = int(input('Enter the number of the song max' + str(len(playlist)) + ':'))
    return number

playlist = fill_list()
choice = menu()
while choice != 's':
    if choice == 'a':
        print_overview(playlist)
    elif choice == 'b':
        longest_length = len(playlist[0])
        longest_title = playlist[0]
        for i in range(len(playlist)):
            if len(playlist[i])>longest_length:
                longest_length = len(playlist[i])
                longest_title = playlist[i]
            print("The longest title\n" + longest_title + 'has', longest_length, 'characters\n')
    elif choice == 'c':
        number = int(input('Enter the number of songs max' + str(len(playlist)) + ':'))
        while number not in range(1, len(playlist) + 1):
            number = int(input('Enter the number of the song max' + str(len(playlist)) + ':'))
        song = playlist[number-1]

        for i in range(len(song)):
            if i % 5 ==0:
                print()
            print(song[i], end='')
        print()
    elif choice =='d':
        number = valid_input(playlist)
        song = playlist[number - 1]
        vowels = 'a,e,i,o,u'
        new_song = []
        for i in range(len(song)):
            if song[i] not in vowels:
                new_song.append(song[i])
        print(*new_song)

    elif choice == 'e':
        number = valid_input(playlist)
        new_playlist = playlist[number -1:]
        print(new_playlist)
    choice = menu()