"""A word funnel is a series of words formed by removing one letter at a time
from a starting word, keeping the remaining letters in order. For the purpose
of this challenge, a word is defined as an entry in the enable1 word list.
An example of a word funnel is:
gnash => gash => ash => ah
This word funnel has length 4, because there are 4 words in it.

Given a word, determine the length of the longest word funnel that it starts.
You may optionally also return the funnel itself (or any funnel tied for the
longest, in the case of a tie).
"""


import time
from urllib.request import urlopen


URL = 'https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt'
final = 1


def funnel(word, counter, words):
    global final
    final = counter if counter > final else 1
    for index in range(len(word)):
        newstr = word[:index] + word[index + 1:]
        if newstr in words:
            funnel(newstr, counter + 1, words)
    return final


if __name__ == '__main__':
    words = urlopen(URL).read().decode('utf8').split('\n')
    tester_words = [
        'gnash', 'princesses', 'turntables', 'implosive', 'programmer'
    ]
    start = time.time()
    for tester in tester_words:
        out = funnel(tester, 1, words)
        print('{}: {}'.format(tester, out))
    end = time.time()
    print(end-start)
