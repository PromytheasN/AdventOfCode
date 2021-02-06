
def data_extraction():
    # Extract Data into a list

    data_input = open("/home/alexander/Desktop/WORK/AdvocadeOfCode_2020/"
                      "Day_5/input.txt", "r")

    all_seats = []

    for line in data_input:
        all_seats.append(line[0:10])

    data_input.close()


    return all_seats


def binary_transform(all_seats):

    all_seats_b = []
    for seat in all_seats:

        seat = seat.replace("B", "1")
        seat = seat.replace("F", "0")
        seat = seat.replace("L", "0")
        seat = seat.replace("R", "1")
        all_seats_b.append(seat)

    return all_seats_b






all_seats = data_extraction()
all_seats_b = binary_transform(all_seats)
print(all_seats_b)