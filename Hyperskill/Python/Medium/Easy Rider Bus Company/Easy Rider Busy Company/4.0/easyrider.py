import json
import sys
import itertools
from BusLine import BusLine
from Stop import Stop

travel_log = json.loads(input())
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
        print(f"There is no start or end stop for the line: {bus_id}")
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


print(f"Start stops: {len(starting_stops)} {sorted(starting_stops)}")
print(f'Transfer stops: {len(transfer_stops)} {sorted(transfer_stops)}')
print(f"Finish stops: {len(finish_stops)} {sorted(finish_stops)}")
