#!/bin/bash

./convertBookToPy.sh

cd .. 

# declare -i start=1
# declare -i stop=1
# declare -i increment=1
# echo "Bash version ${BASH_VERSION}..."

# increment=50
# for ((i = 1 ; i < 1 ; i=i+$increment)); do
#   # if [$i==0] ; then
#   #   start=$i
#   # else 
#   #   start=$i+1
#   # fi
#   start=$i
#   stop=$i+$increment
#   echo "Counter: $start to $stop"
#   #ipython ./nifty_matrix_scrapper.py $start $stop
# done

ipython ./nifty_matrix_scrapper.py 1 5001 &
ipython ./nifty_matrix_scrapper.py 5000 10001 &
ipython ./nifty_matrix_scrapper.py 10000 15001 &
ipython ./nifty_matrix_scrapper.py 15000 20001 &
ipython ./nifty_matrix_scrapper.py 20000 25001 &
ipython ./nifty_matrix_scrapper.py 25000 30001 &
ipython ./nifty_matrix_scrapper.py 30000 35001 &
ipython ./nifty_matrix_scrapper.py 35000 40001 &
ipython ./nifty_matrix_scrapper.py 40000 45001 &
ipython ./nifty_matrix_scrapper.py 45000 50001 &
ipython ./nifty_matrix_scrapper.py 50000 55001 &
ipython ./nifty_matrix_scrapper.py 55000 60001 &
ipython ./nifty_matrix_scrapper.py 60000 65001 &
ipython ./nifty_matrix_scrapper.py 65000 70001 &
ipython ./nifty_matrix_scrapper.py 70000 75001 &
ipython ./nifty_matrix_scrapper.py 75000 80001 &
ipython ./nifty_matrix_scrapper.py 80000 85001 &
ipython ./nifty_matrix_scrapper.py 85000 90001 &
ipython ./nifty_matrix_scrapper.py 90000 95001 &
ipython ./nifty_matrix_scrapper.py 95000 100001 &
