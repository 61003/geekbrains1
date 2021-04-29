from task_6_6 import read_data
from sys import argv

if len(argv) == 1:
    read_data()
elif len(argv) == 2:
    read_data(argv[1])
elif len(argv) == 3:
    read_data(argv[1], argv[2])
else:
    print('Invalid number of parameters')
