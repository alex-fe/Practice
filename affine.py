import collections


def decode(case):
    pass
    import pdb; pdb.set_trace()


if __name__ == '__main__':
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
        decode(test_case)
        break
