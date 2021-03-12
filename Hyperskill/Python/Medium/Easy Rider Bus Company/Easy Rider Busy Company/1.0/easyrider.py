# Write your awesome code here
import json

stops = ["Sesame Street", "Fifth Avenue", "Sunset Boulevard", "Elm Street", "Prospekt Avenue", "Pilotow Street", "Bourbon Street"]
stop_types = ['S', 'O', 'F', '']

usr_input = input()
travel_log = json.loads(usr_input)

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
        if field == 'stop_id':
            if type(log[field]) is not int:
                stop_id_errors += 1
        if field == 'stop_name':
            #if type(log[field]) is not str or log[field] not in stops:
            if type(log[field]) is not str:
                # print(log[field])
                stop_name_errors += 1
            elif len(log[field]) == 0:
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

errors = bus_id_errors + stop_id_errors + stop_name_errors + next_stop_errors + stop_type_errors + a_time_errors

print(f'Type and required field validation: {errors} errors')
print(f'bus_id: {bus_id_errors}')
print(f'stop_id: {stop_id_errors}')
print(f'stop_name: {stop_name_errors}')
print(f'next_stop: {next_stop_errors}')
print(f'stop_type: {stop_type_errors}')
print(f'a_time: {a_time_errors}')

