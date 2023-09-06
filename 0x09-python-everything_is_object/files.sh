#!/bin/bash

i=6

while ((i <= 28))
do
    touch "${i}-answer.txt"
    i=$((i+1))
done
