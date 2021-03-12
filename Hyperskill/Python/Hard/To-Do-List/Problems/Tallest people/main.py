def tallest_people(**people):

    sorted_people = sorted(people.items(), key=lambda k: (-k[1], k))

    # for person in sorted_people:
    #     print(person[0], ':', person[1])

    for person in sorted_people:
        if person[1] == max(people.values()):
            print(person[0], ':', person[1])
