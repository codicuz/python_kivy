#!/bin/bash

printf "%s\n" "Исправление не корректных символов"

sed "s/\. /\./g" -i $1
sed "s/ (/(/g" -i $1
sed "s/«»»/'''/g" -i $1
sed "s/«/'/g" -i $1
sed "s/»/'/g" -i $1
sed "s/’/'/g" -i $1
sed "s/\"/'/g" -i $1
