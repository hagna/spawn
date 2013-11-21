import sys
import time

num = int(sys.argv[1])

logfh = open('log.log', 'wb')
def log(msg):
    logfh.write(msg + '\n')
    logfh.flush()


def inc():
    i = 0
    while True:
        yield i
        i += 1


pool = inc()

def sendSome(num):
    streams = [sys.stdout, sys.stderr]
    print dir(streams[0])
    for i in xrange(num):
        log(str(i))
        stream = streams[i%2]
        i = pool.next()
        payload = ('%s_' % (i,)) * i
        stream.write(payload)
        stream.flush()


sendSome(num)
#time.sleep(2)
#sendSome(num)
