import re

# prepare the input
activity_log = open("day4_input.txt")
activities = activity_log.readlines()
chronological_activities = sorted(activities)

# for event in chronological_activities:
#     print(event, end="")

# where we will store the output
guards = {}

# parsing the timestamp and event of something like this: '[1518-11-01 00:00] Guard #10 begins shift'
event_parser = re.compile('\[\d{4}-\d{2}-\d{2} \d{2}:(\d{2})\] (.+)')

# parsing out the guard's ID number
guard_getter = re.compile('Guard #(\d+)')

# parsing details
guard = None
start = -1

# process the events, one by one
for event in chronological_activities:

    parsed_event = event_parser.match(event)
    if not parsed_event:
        print(f'Unable to parse! "{event}"')

    minutes = int(parsed_event.group(1))
    message = parsed_event.group(2)

    guard_found = guard_getter.match(message)
    if guard_found:
        guard = int(guard_found.group(1))
        if start >= 0:
            print(f'ERROR! New Guard without finishing old Guard! "{event}"')
        if guard not in guards:
            empty_list = [0 for i in range(60)]
            guards[guard] = empty_list

    elif message.startswith("falls"):
        start = minutes

    elif message.startswith("wakes"):
        end = minutes
        # print(f'{guard}, {start}-{end}')
        if start < 0:
            print(f'ERROR! End without start! {event}')
        for i in range(start, end):
            guards[guard][i] += 1
        start = -1
        # print(guards[guard])

sleepiest_guard = None
sleepiest_minute = 0
sleepiest_time = 0

for guard in guards:
    for i in range(60):
        if guards[guard][i] > sleepiest_time:
            sleepiest_guard = guard
            sleepiest_minute = i
            sleepiest_time = guards[sleepiest_guard][sleepiest_minute]

print(f'Guard: {sleepiest_guard}, Minute: {sleepiest_minute}, Product={sleepiest_guard*sleepiest_minute}')
