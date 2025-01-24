def time_to_seconds(h, m, s):
    """Convert time to total seconds."""
    return h * 3600 + m * 60 + s

def seconds_to_time(seconds):
    """Convert total seconds to hours, minutes, seconds."""
    h = seconds // 3600
    seconds %= 3600
    m = seconds // 60
    s = seconds % 60
    return h, m, s

# Input format
event_time_gmt2 = input().strip()
current_time_gmt7 = input().strip()

# Parse the input times
HH_event, MM_event, SS_event = map(int, event_time_gmt2.split(':'))
CH, CM, CS = map(int, current_time_gmt7.split(':'))

# Convert event time to GMT
event_time_in_gmt = time_to_seconds(HH_event - 2, MM_event, SS_event)

# Convert current time to GMT
current_time_in_gmt = time_to_seconds(CH - 7, CM, CS)

# Calculate the time difference
time_difference = event_time_in_gmt - current_time_in_gmt

if time_difference <= 0:
    print("See you on the next Pear Event!")
else:
    # Convert the difference back to hours, minutes, seconds
    H, M, S = seconds_to_time(time_difference)
    print(f"{H:02d}:{M:02d}:{S:02d}")
