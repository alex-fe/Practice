import time
from urllib.request import urlopen


URL = 'https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt'
final = 1


def funnel(word, counter, words):
    global final
    if counter > final:
        final = counter
    else:
        final = 1
    for index in range(len(word)):
        newstr = word[:index] + word[index + 1:]
        if newstr in words:
            funnel(newstr, counter + 1, words)
    return final


if __name__ == '__main__':
    words = urlopen(URL).read().decode("utf8").split('\n')
    start = time.time()
    print(funnel("gnash", 1, words))  # 4
    print(funnel("princesses", 1, words))  # 9
    print(funnel("turntables", 1, words))  # 5
    print(funnel("implosive", 1, words))  # 1
    print(funnel("programmer", 1, words))  # 2
    end = time.time()
    print(end-start)
