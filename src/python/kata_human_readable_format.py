"""
Human readable duration format

Your task in order to complete this Kata is to write a function which formats a
duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns
"now". Otherwise, the duration is expressed as a combination of years, days,
hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"

For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.
Detailed rules

The resulting expression is made of components like 4 seconds, 1 year, etc.
In general, a positive integer and one of the valid units of time, separated by
a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last
component, which is separated by " and ", just like it would be written in
English.

A more significant units of time will occur before than a least significant one.
Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated
units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence,
1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function
should not return 61 seconds, but 1 minute and 1 second instead. Formally,
the duration specified by of a component must not be greater than any valid
more significant unit of time.

"""


def format_duration(secs: int) -> str:
    """Returns the time in a human readable format.

    Args:
        seconds (int): The time in seconds to convert from.

    Returns:
        str: The time in human readable format.
    """
    if not secs:
        return "now"

    years, time = secs // (86400 * 365), secs % (86400 * 365)
    days, time = time // 86400, time % 86400
    hours, time = time // 3600, time % 3600
    minutes, time = time // 60, time % 60
    seconds = time

    fdate = []

    if years:
        fdate.append(f"{years} years" if years > 1 else f"{years} year")
    if days:
        fdate.append(f"{days} days" if days > 1 else f"{days} day")
    if hours:
        fdate.append(f"{hours} hours" if hours > 1 else f"{hours} hour")
    if minutes:
        fdate.append(
            f"{minutes} minutes" if minutes > 1 else f"{minutes} minute"
        )
    if seconds:
        fdate.append(
            f"{seconds} seconds" if seconds > 1 else f"{seconds} second"
        )

    string_date = ""

    for index, date in enumerate(fdate):
        if len(fdate) >= 2 and index == len(fdate) - 2:
            string_date += f"{date} and "
            continue
        if index == len(fdate) - 1:
            string_date += f"{date}"
            break
        string_date += f"{date}, "

    return string_date.lstrip()


if __name__ == "__main__":
    print(format_duration(300000662))
    print(format_duration(3662))
