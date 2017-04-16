from redis import Redis
from rq import Queue
import sys
q = Queue(connection=Redis('10.0.0.9'))
q.enqueue('process_pe.procpe',sys.argv[1])
