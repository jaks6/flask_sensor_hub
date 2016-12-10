#!/bin/bash
echo "Starting sensor logging and Flask webserver..."
python ./sensor_reader/sensor_reader.py &
PID1="$!"

python start_flask.py &
PID2="$!"

trap "kill $PID1 $PID2" exit INT TERM

wait