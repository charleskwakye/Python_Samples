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

choice = menu()
while choice != 's':
    if choice == 'a':
        print_overview(playlist)
    elif choice == 'b':
        maxim = max(playlist,key=len)
        length = len(maxim)
        print('The longest title',maxim,'has',length,'characters')
    elif choice =='c':
        no_song = int(input('Enter the number of the song max 5: '))
        while no_song < len(playlist+1) and no_song > 0: