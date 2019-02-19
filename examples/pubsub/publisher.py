"""
publisher.py

A simple example of a Pub-Sub connection using ZeroMQ.
The Publisher prints out the current time every second

To run, open a terminal and enter:
$ python publisher.py

After that, open any amount of clients in a new terminal to subscribe to
the publisher by entering:
$ python client.py

"""

#-----------------------------------------------------------------------------
#  Original Copyright (c) 2010 Brian Granger
#  Edits Copyright (c) 2019 Gunnar Pope
#
#  Distributed under the terms of the New BSD License.  The full license is in
#  the file COPYING.BSD, distributed as part of this software.
#-----------------------------------------------------------------------------

import time
from datetime import datetime
import zmq


address ='tcp://127.0.0.1:5555'
context = zmq.Context().instance()
socket  = context.socket(zmq.PUB)
socket.bind(address)

print('Starting The Publisher....')
while True:
    try:
        
        timestr = datetime.now().__format__("%Y-%m-%dT%H-%M-%S.%f")
        socket.send_string(timestr)
        print('Sending Time: ',timestr)
        time.sleep(0.01)

    except ( KeyboardInterrupt, SystemExit ):
        socket.term()                                                  # .term  ALWAYS!
        context.close()                                                     # .close ALWAYS!
        break
