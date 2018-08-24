import inflect


def conversion(time):
    p = inflect.engine()
    time = list(map(int, time.split(':')))
    hour = time[0] % 12 or 12
    period = 'am' if time[0] >= 12 else 'pm'
    if not time[1]:
        minute = ''
    elif time[1] >= 10:
        minute = p.number_to_words(time[1])
    else:
        minute = 'oh {}'.format(p.number_to_words(time[1]))
    return 'Its {} {} {}'.format(p.number_to_words(hour), minute, period)



if __name__ == '__main__':
    time = input('Input: ')
    time_txt = conversion(time)
    print(time_txt)
    # speak(time_txt)
    # main()
