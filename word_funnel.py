from urllib.request import urlopen


URL = 'https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt'



if __name__ == '__main__':
    words = urlopen(URL).read().decode("utf8").split('\n')
    
