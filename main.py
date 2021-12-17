import sys
from pyfiglet import Figlet
from modules import memory_connector, pagefile_connector

def Main(parameter):
    #flag = parameter

    if parameter == 'a':
        tmp = memory_connector.WindowsMemoryConnector()
        print("End")

    elif parameter == 'pagefile':
        tmp = pagefile_connector.WindowsPagefileConnector()
        print("End")



if __name__ == '__main__':
    if not Main(sys.argv[1]):
        sys.exit(1)
    else:
        sys.exit(0)