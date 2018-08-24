import inflect
import subprocess


def conversion(time):
    p = inflect.engine()
    time = list(map(int, time.split(':')))
    if not (0 <= time[0] <= 24 and 0 <= time[1] < 60):
        return 'There is no time like the present.'
    hour = time[0] % 12 or 12
    period = 'am' if time[0] <= 12 else 'pm'
    if not time[1]:
        minute = ''
    elif time[1] >= 10:
        minute = p.number_to_words(time[1])
    else:
        minute = 'oh {}'.format(p.number_to_words(time[1]))
    return 'Its {} {} {}'.format(p.number_to_words(hour), minute, period)


def say(time_txt):
    subprocess.call('say {}'.format(time_txt), shell=True)


if __name__ == '__main__':
    time = input('Input: ')
    time_txt = conversion(time)
    say(time_txt)
