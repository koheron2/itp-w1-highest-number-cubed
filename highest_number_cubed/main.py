"""This is the entry point of the program."""

def highest_number_cubed(limit):
    cube = 0
    while cube ** 3 < limit:
        cube += 1
    return cube - 1
    
