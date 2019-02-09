## Multithreading in ZMQ
See the example in Fig 20 at [zeromq.org](http://zguide.zeromq.org/py:all#sockets-and-patterns). This example builds a proxy that takes requests from the client, and then distributes the request to multiple 'worker nodes' for processing. These worker nodes respont to the proxy when done and the result is returned to the client.

To run, do:

    $ python multithread.py

Then, open another terminal and do:

    $ python client

Output for multithread.py
 
    ~/repos/pyzmq/examples/multithread $ python multithread.py 
    Received request: [ b'Hello' ]
    Received request: [ b'Hello' ]
    Received request: [ b'Hello' ]
    Received request: [ b'Hello' ]
    Received request: [ b'Hello' ]
    Received request: [ b'Hello' ]
    Received request: [ b'Hello' ]
    Received request: [ b'Hello' ]
    Received request: [ b'Hello' ]

Ouput for client.py

    ~/repos/pyzmq/examples/multithread $ python client.py 
    Connecting to hello world server…
    Sending request 0 …
    Received reply 0 [ b'World' ]
    Sending request 1 …
    Received reply 1 [ b'World' ]
    Sending request 2 …
    Received reply 2 [ b'World' ]
    Sending request 3 …
    
