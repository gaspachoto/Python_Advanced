def flights(*args):
    flights_dict = {}
    for flight in range(len(args)):
        if args[flight] == "Finish":
            break
        if flight % 2 == 0:
            if args[flight] not in flights_dict:
                flights_dict[args[flight]] = 0
        else:
            flights_dict[args[flight - 1]] += args[flight]

    return flights_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))