import time
import socket
from collections import defaultdict

# a print_lock is what is used to prevent "double" modification of shared variables.
# this is used so while one thread is using a variable, others cannot access
# it. Once done, the thread releases the print_lock.
# to use it, you want to specify a print_lock per thing you wish to print_lock.

# ip = socket.gethostbyname(target)


def scanPort(port, ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        out = (ip, port)
        print(out)
        s.close()
        return out
    except:
        pass


def scanPorts(ip='localhost', no_threads=1, port_range=10000):
    start = time.time()
    out = defaultdict(list)
    for ip in ip.split(','):
        for port in range(1, port_range):
            rst = scanPort(port, ip)
            if rst:
                out[rst[0]].append(str(rst[1]))

    # out['duration'] = time.time() - start
    return out


# def scanFromFile():
#     for f in open('port_list.txt'):
#         print(f)