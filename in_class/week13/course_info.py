room_numbers = {
    'CS110': 3004,
    'CS112': 4501,
    'CS220': 6755,
    'CS245': 1244,
    'CS212': 1411
}
instructors = {
    'CS110': 'Haynes',
    'CS112': 'Alvarado',
    'CS220': 'Rich',
    'CS245': 'Burke',
    'CS212': 'Lee'
}
meeting_times = {
    'Haynes': '8AM',
    'Alvarado': '9AM',
    'Rich': '10AM',
    'Burke': '11AM',
    'Lee': '12PM'
}


def main():
    query = input('Which course would you like to fetch details for? ')
    if query in room_numbers:
        query_room_number = room_numbers.get(query)
        query_instructor = instructors.get(query)
        query_meeting_time = meeting_times.get(query_instructor)
        print('The details for the course ' + query + ' are:')
        print('Room: ' + str(query_room_number))
        print('Instructor: ' + query_instructor)
        print('Time: ' + query_meeting_time)
    else:
        print(query + ' is an invalid course number.')


main()
