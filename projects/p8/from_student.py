FIRST_LETTER = 'A'
BOOKED_LETTER = 'X'
SEATS_BOOKED = []

def main():
    rows = input("Enter number of rows: ") 
    seats_per_row = input("Enter number of seats in each row: ")
    seating = initialize_seating(int(rows), int(seats_per_row))
    print_seating(seating)

    book_another = "y"
    while book_another == "y":
        old_seating = seating
        seating = book_seat(input("Input seat number (row seat): "), seating) 
        if seating == None:
            seating = old_seating
            continue
        print_seating(seating)

        if check_if_full(seating) == False:
            book_another = input("More seats (y/n)? ")
        elif check_if_full(seating) == True:
            return None


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


def print_seating(seating):
    """ Print the seating in neat way """
    counter = 1
    middle_row = len(seating[0]) /2
    for row in seating:
        print("{:2}".format(counter), end=" ")
        for i in range(0, len(row)):
            if i == middle_row:
                print(" ", end=" ")
            print(row[i], end=" ")
        print()
        counter += 1


def book_seat(seat_number, seating):
    """ Allow user to book a seat.
    User inputs a row number and seat letter, then that seat will then be replaces with an X.
    If input is invalid = error, if seat is already booked = error """
    global SEATS_BOOKED
    try:
        booked_seat = seat_number.split()
        booked_seat_num = int(booked_seat[0])
        if seat_number in SEATS_BOOKED:
            print("That seat is taken!")
            return None
        SEATS_BOOKED.append(seat_number)
        new_seating = []
        row_counter = 1
        for row in seating:
            if row_counter == booked_seat_num:
                new_row = []
                found_seat = 0
                for seat in row:
                    if seat == booked_seat[1]:
                        new_row.append(BOOKED_LETTER)
                        found_seat += 1
                    else:
                        new_row.append(seat)
                new_seating.append(new_row)
                if found_seat < 1:
                    print("Seat number is invalid!")
                    return None
            else:
                new_seating.append(row)
            row_counter += 1
        if booked_seat_num > row_counter-1:
            print("Seat number is invalid!")
            return None
        return new_seating
    except:
        print("Seat number is invalid!")
        return None

    
def check_if_full(seating):
    total_counter = 0
    false_counter = 0
    for row in seating:
        for seat in row:
            if seat != "X":
                return False
            else:
                continue
    return True


# Main program starts here
if __name__ == "__main__":
    main()