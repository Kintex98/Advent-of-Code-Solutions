boarding_seats = open('Advent of Code 2020 Day 5.txt')
boarding_seats = boarding_seats.read()
boarding_seats = boarding_seats.split('\n')

def sort_row(seats):
    upper = 127
    lower = 0

    for value in seats:
        half = (upper+lower) // 2
        if value == 'F':
            upper = half
        if value == 'B':
            lower = half + 1

    if seats[6] == 'B':
        return upper

    else:
        return lower

def sort_column(seats):
    upper = 7
    lower = 0

    for value in seats:
        half = (upper+lower) // 2
        if value == 'L':
            upper = half
        elif value == 'R':
            lower = half + 1

    if seats[2] == 'R':
        return upper
    else:
        return lower


largest = 0
seat_ids = []
for seats in boarding_seats:
    row = sort_row(seats[:7])
    column = sort_column(seats[7:])

    seat_id = row * 8 + column
    seat_ids.append(seat_id)

    if seat_id > largest:
        largest = seat_id

print(largest)
seat_ids.sort()

for seat_id in seat_ids:
    if seat_id + 1 not in seat_ids and seat_id + 2 in seat_ids:
        my_id = seat_id + 1
# my_id must:
# Have seat_id + 1 and -1 in the list
# Not exist itself
# seta_id is -1 for my_id and seat_id + 2 is +1

print(my_id)