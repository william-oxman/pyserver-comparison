#!/bin/zsh
# ./kill_pyserver.sh <PORT_NUMBER> <LOWERCASE_PYSERVER_NAME>
port=$1
pid=`ps ax | grep $2 | grep $port | awk '{split($0,a," "); print a[1]}' | head -n 1`
if [ -z "$pid" ]; then
  echo "no daemon on port $port"
else
  kill -9 $pid
  echo "killed daemon on port $port"
fi