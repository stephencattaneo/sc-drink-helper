#! /bin/bash

for i in `ls processor/raw_data/*.txt`
do
    python3 ./processor/main.py $i 2>> processor-errors.txt
done

for i in `ls processor/raw_data/*.json`
do
    python3 ./merger/main.py $i ./data.json 2>> merger-errors.txt
done
