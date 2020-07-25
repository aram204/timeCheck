import sys
from datetime import datetime,date


if sys.argv[1] == "1":
    print(date.today())


if sys.argv[1] == "2":
    print(datetime.now().replace(microsecond=0))


if sys.argv[1] == "3":
    print(datetime.now().strftime('%A %B %d %Y %H:%M:%S %z'))

