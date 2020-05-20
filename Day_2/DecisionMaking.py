
# Cách định nghĩa switch case python
def week(i):
    swicher = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
    }

    return swicher.get(i)

print(week(1))
