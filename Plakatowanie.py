def main(pla):

    # Open file and transform to list of heights
    with open(pla + '.in', 'r') as file_pla:
        file_pla = file_pla.read().split('\n')[1:-1]

    build_list = []
    for i in file_pla:
        build_list.append(int(i.split(' ')[1]))

    '''
        MAIN ALGORITHM...
    '''
    # set variables
    # open_post - equal to current sticking posters, when poster is finish/close -> drop it to posters variable
    # posters - number of finish/close posters
    open_post = [0]
    posters = 0

    for build_H in build_list:

        while open_post[-1] > build_H:

            open_post.pop()

        if open_post[-1] < build_H:

            open_post.append(build_H)
            posters += 1

    '''
        ...MAIN ALGORITHM 
    '''

    # Save file
    with open(pla + '.out', 'w') as curr_file:
        curr_file.write(str(posters))
        curr_file.close()

    print(f'Do oklejenia budynków w pliku {pla}.in potrzeba {posters} plakatów')
    print(f'Zapisane do pliku {pla}.out')


# Initial file variable to basic name "pla.in"
pla = 'pla.in'
pla = pla.split('.')[0]

# Run code
# If file "pla.in" can not be found in current folder, ask for other name
while True:
    try:
        main(pla)
        exit()
    except FileNotFoundError:
        print(f'Nie mogę znaleźć pliku o nazwie {pla}.in w bieżacym folderze')
        pla = input('Czy plik ma inną nazwę? Jaką?: \n').split('.')[0]
