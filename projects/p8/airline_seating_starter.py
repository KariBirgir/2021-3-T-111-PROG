FIRST_LETTER = 'A'
BOOKED_LETTER = 'X'

def initialize_seating(no_of_rows, no_of_seats):
    ''' Returns an empty seating allocation: list of lists
        Each seat in each row is marked with a letter, starting from "A" '''
    seating = []
    for _ in range(0, no_of_rows):
        seats = []
        # creates consecutive letters starting from first_letter
        for col in range(0, no_of_seats):
            next_letter = chr(ord(FIRST_LETTER) + col)  
            seats.append(next_letter)
        seating.append(seats)
    return seating
  
# Main program starts here
if __name__ == "__main__":
    main()