import json
import sys
import itertools
import re
from BusLine import BusLine
from Stop import Stop


def bus_line_calculator(travel_log):
    busses = {}
    stops = set()

    for log in travel_log:
        bus = BusLine(log["bus_id"])

        if bus.get_id() not in busses:
            busses[bus.get_id()] = bus

        stop = Stop(log["stop_id"])
        stop_name = log["stop_name"]
        stop.add_name(stop_name)
        stop_type = log["stop_type"]

        busses[bus.get_id()].add_stop(stop)

        if stop_type == "S":
            busses[bus.get_id()].set_starting_stop(stop)
        elif stop_type == "F":
            busses[bus.get_id()].set_finishing_stop(stop)

    starting_stops = []
    finish_stops = []

    all_routes = []

    for bus_id, bus in busses.items():
        if bus.starting_and_finishing_exists():
            if bus.starting_stop.get_name() not in starting_stops:
                starting_stops.append(bus.starting_stop.get_name())
            if bus.finishing_stop.get_name() not in finish_stops:
                finish_stops.append(bus.finishing_stop.get_name())

            all_routes.append(bus.route)
        else:
            # print(f"There is no start or end stop for the line: {bus_id}")
            sys.exit()

    named_stops_in_routes = []

    for route in all_routes:
        temp_set = set()
        for stop in route:
            temp_set.add(stop.get_name())
        named_stops_in_routes.append(temp_set)

    combinations = itertools.combinations(named_stops_in_routes, 2)

    transfer_stops_initial = [i.intersection(k) for i, k in (combination for combination in combinations)]

    transfer_stops_set = set()
    for stop_set in transfer_stops_initial:
        for name in stop_set:
            transfer_stops_set.add(name)

    transfer_stops = [*transfer_stops_set]

    # print(f"Start stops: {len(starting_stops)} {sorted(starting_stops)}")
    # print(f'Transfer stops: {len(transfer_stops)} {sorted(transfer_stops)}')
    # print(f"Finish stops: {len(finish_stops)} {sorted(finish_stops)}")


def validator(travel_log):

    stop_types = ['S', 'O', 'F', '']
    bus_lines = {}
    bus_lines.setdefault(0)

    bus_id_errors = 0
    stop_id_errors = 0
    stop_name_errors = 0
    next_stop_errors = 0
    stop_type_errors = 0
    a_time_errors = 0

    for index, log in enumerate(travel_log):
        for field in log:
            if field == 'bus_id':
                if type(log[field]) is not int:
                    bus_id_errors += 1
                else:
                    if log[field] in bus_lines.keys():
                        bus_lines[log[field]] += 1
                    else:
                        bus_lines[log[field]] = 1
            if field == 'stop_id':
                if type(log[field]) is not int:
                    stop_id_errors += 1
            if field == 'stop_name':
                if type(log[field]) is not str:
                    stop_name_errors += 1
                elif len(log[field]) == 0:
                    stop_name_errors += 1
                elif not re.match("^[A-Z].*(Road|Avenue|Boulevard|Street)$", log[field]):
                    stop_name_errors += 1
            if field == 'next_stop':
                if type(log[field]) is not int:
                    next_stop_errors += 1
            if field == 'stop_type':
                if type(log[field]) != str or log[field] not in stop_types:
                    stop_type_errors += 1
            if field == 'a_time':
                if type(log[field]) is not str:
                    a_time_errors += 1
                elif len(log[field]) == 0:
                    a_time_errors += 1
                elif not re.match("([0-1][0-9]|2[0-3]):[0-5][0-9]$", log[field]):
                    a_time_errors += 1

    errors = bus_id_errors + stop_id_errors + stop_name_errors + next_stop_errors + stop_type_errors + a_time_errors


def time_checker(travel_log):
    busses_for_time = {}
    
    for log in travel_log:
        for field in log:
            if field == 'a_time':
                if (log['bus_id']) in busses_for_time:
                    busses_for_time[log['bus_id']]['a_time'].append(log[field])
                    busses_for_time[log['bus_id']]['station'].append(log['stop_name'])
                else:
                    busses_for_time[log['bus_id']] = {'a_time': [], 'station': []}
                    busses_for_time[log['bus_id']]['a_time'].append(log[field])
                    busses_for_time[log['bus_id']]['station'].append(log['stop_name'])

    print("Arrival time test:")
    no_bad_time = True

    for bus_id, bus in busses_for_time.items():
        valued_times = []
        for field in bus:
            if field == 'a_time':
                # print(bus[field])
                for time in bus[field]:
                    valued_times.append(convert_to_value(time))

        if valued_times != sorted(valued_times):
            # print(valued_times)
            for i in range(1, len(valued_times)):
                if valued_times[i] < valued_times[i-1]:
                    station = bus['station'][i]
                    break
            print(f"bus_id line {bus_id}: wrong time on station {station}")
            no_bad_time = False

    if no_bad_time:
        print("OK")


def convert_to_value(time):
    
    total_time = 0
    
    for i, char in enumerate(time):
        if char != ':':
            if i == 0:
                total_time += (int(char) * 10) * 60
            elif i == 1:
                total_time += (int(char)) * 60
            elif i == 3:
                total_time += (int(char) * 10)
            elif i == 4:
                total_time += (int(char))
                
    return total_time


travel_log = json.loads(input())

# validator(travel_log)
# bus_line_calculator(travel_log)
time_checker(travel_log)
