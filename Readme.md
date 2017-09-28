## Overview

This is a _tiny_ proof of concept of a webapp that reads gyro or other mobile sensor data, sends it the web server, which sends it to an OSC server.

It requires `flask` and `pythonosc`.

Developed during the monthly music hackathon at Spotify, July 2016.


## Running

Run `python server.py` or `python gevent_server.py`, which uses non-blocking IO.


## Problems

There's significant latency for requests. The HTTP GET requests could have too much overhead.

Should investigate using websockets or webrtc for transport.
