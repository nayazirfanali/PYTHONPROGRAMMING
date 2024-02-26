def maxGuests(T, E, L):
    events = []
    max_guests = 0
    current_guests = 0
    for i in range(len(E)):
        events.append((i, E[i]))
        events.append((i, -L[i]))

    events.sort()

    for event in events:
        current_guests += event[1]
        max_guests = max(max_guests, current_guests)

    return max_guests

T = int(input("enter the T value:"))
E = [7,0,5,1,3]
L = [1,2,1,3,4]
print("the max no.of guest on cruise at an instance is:",maxGuests(T, E, L))
