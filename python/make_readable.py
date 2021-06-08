# https://www.codewars.com/kata/52685f7382004e774f0001f7/
# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

#     HH = hours, padded to 2 digits, range: 00 - 99
#     MM = minutes, padded to 2 digits, range: 00 - 59
#     SS = seconds, padded to 2 digits, range: 00 - 59

# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.

def make_readable(seconds) -> str:
    hours = format(seconds // 3600, '02.0f')
    mins = format((seconds // 60 - int(hours) * 60), '02.0f')
    secs = format(seconds % 60, '02.0f')
    return f'{hours}:{mins}:{secs}'