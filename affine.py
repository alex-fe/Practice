import collections
import itertools
import string

COPRIMES = [3, 5, 7, 11, 15, 17, 19, 21, 23, 25]


def decode(coded, a, b):
    decoded = ''
    for char in coded:
        if char in string.whitespace:
            value = ' '
        elif char in string.punctuation:
            value = char
        else:
            value = chr(((ord(char) - ord('a') - b) * a) % 26 + ord('a'))
        decoded += value
    return decoded


def solve(case, dictionary):
    for a, b in itertools.product(COPRIMES, range(26)):
        result = decode(case.coded, a, b)
        if all(word in dictionary for word in result.split()):
            return result


if __name__ == '__main__':
    with open('./Supplimentary/dict.txt') as f:
        dictionary = set(word.strip().lower() for word in f.readlines())

    TestCase = collections.namedtuple('TestCase', ['coded', 'decoded'])
    one = TestCase('NLWC WC M NECN', 'this is a test')
    two = TestCase(
        'YEQ LKCV BDK XCGK EZ BDK UEXLVM QPLQGWSKMB',
        'you lead the race of the worlds unluckiest'
    )
    two_bonus = TestCase(
        "Yeq lkcv bdk xcgk ez bdk uexlv'm qplqgwskmb.",
        "You lead the race of the world's unluckiest."
    )
    three = TestCase(
        '''NH WRTEQ TFWRX TGY T YEZVXH GJNMGRXX STPGX NH XRGXR TX QWZJDW ZK
        WRNUZFB P WTY YEJGB ZE RNSQPRY XZNR YJUU ZSPTQR QZ QWR YETPGX ZGR
        NPGJQR STXQ TGY URQWR VTEYX WTY XJGB
        ''',
        '''my heart aches and a drowsy numbness pains my sense as though of
        hemlock i had drunk or emptied some dull opiate to the drains one
        minute past and lethe wards had sunk
        '''
    )
    test_cases = [one, two, two_bonus, three]
    for test_case in test_cases:
        print(solve(test_case, dictionary))
