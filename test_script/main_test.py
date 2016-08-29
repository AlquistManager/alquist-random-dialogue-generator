import sys

from test_script.tester import Tester

# Script for stress testing of Alquist with randomly generated dialogues

if __name__ == '__main__':
    url = sys.argv[1]
    number_of_testers = int(sys.argv[2])
    threads = [None] * number_of_testers
    i = 0
    # run each thread
    for thread in threads:
        thread = Tester(url, i)
        thread.start()
        i += 1
