#!/bin/bash

input="./testText.txt"
touch rippedCode.txt
while IFS= read -r line
do
  echo "$line" | grep -o '(?<=<i>).*(?=</i>)' #>> rippedCode.txt
done < "$input"
