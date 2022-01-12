#!/bin/zsh

./convertBookToPy.sh
cd .. 

increment=5000
start=1
stop=100000
for i in {$start..$stop..$increment}
do
    start=$i
    if [[ $i -gt 1 ]]
    then
        start=$((i-1))
    fi
    ipython ./nifty_matrix_scrapper.py $start $((i+increment)) $increment &
done

# ipython ./nifty_matrix_scrapper.py 15000 20001 &