#!/bin/zsh
pid=`ps ax | grep $1 | awk '{split($0,a," "); print a[1]}' | head -n 1`
if [ -z "$pid" ]; then
  echo "process not found"
else
  echo $pid
  kill -9 $pid
  echo "killed process"
fi