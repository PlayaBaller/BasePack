from datetime import datetime


def sun_angle(time):
    sunrise = datetime.strptime('06:00', '%H:%M')
    sunset = datetime.strptime('18:00', '%H:%M')

    time = datetime.strptime(time, '%H:%M')
    if not sunrise <= time <= sunset:
        return "I don't see the sun!"

    angle_per_hour = 180 / (sunset - sunrise).seconds * 3600
    print(angle_per_hour)
    time_since_sunrise = (time - sunrise).seconds / 3600
    print(time_since_sunrise)
    calc_angle = time_since_sunrise * angle_per_hour
    print(calc_angle)
    return calc_angle


if __name__ == '__main__':
     print(sun_angle("12:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert sun_angle("07:00") == 15
    # assert sun_angle("01:23") == "I don't see the sun!"