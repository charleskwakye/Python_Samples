# studentnumber - r0879035
# family name and first name - Kwakye  Charles Nana
# class - 1 ACS 1

with open('christmas_songs.txt', encoding='utf-8') as file:
    line = file.readline().rstrip()
    line = file.readline()
    top_rank_per_year = []

    while line != '\n':
        record = line.rstrip().split(';')
        song = record[0]
        performer = record[1]
        year = record[2]
        ranking = record[3]
        while line != '\n' and record[2] == year:
            if record[3] <= ranking:
                ranking = record[3]
            else:
                line = file.readline()
                record = line.rstrip().split(';')
        to_append = year,ranking.rstrip(), song.title(),performer.title()
        top_rank_per_year.append(to_append)
        line = file.readline()
        record = line.rstrip().split(';')

print('Most popular christmas songs')
print('-'*len('Most popular christmas songs'))

for lines in top_rank_per_year:
    top_rank_per_year.sort()
    print(lines[0], '\n'+ '\t'+ line[1]+'th place with song', lines[2], '('+lines[3]+')')


def write_to_file(do_write):
    with open('most_popular_xmas_songs.txt', 'w', encoding='utf-8') as file:
        file.write('Year' + ';' + 'Ranking' + 'Song')
        file.write(line[0]+ ';' + ranking + ';'+ line[2])
        for lines in top_rank_per_year:
            file.write(lines)
        return write_to_file