def menu():
    print('\ta - Overview\n\tb - Define longest title\n\tc - 5 letters in a row\n\td '
          '- No vowels\n\te - Cutting the playlist\n\ts - Stop')
    answer = input('\tMake a selection: ').lower()
    return answer