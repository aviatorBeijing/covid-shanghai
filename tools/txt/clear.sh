#!/bin/sh

INPUTF=$1/cases-nosyndrome.txt
OUTPUTF=$1/cases-nosyndrome-clear.txt 

sed 's/无症状感染者[0-9]*/|/g' $INPUTF | tr '|' '\n' | sed 's/，/,/g' | sed 's/^,//g' | sed 's/,$//g' | sed 's/。/./g' | sed 's/居住于//g' | awk -F"," '{print $1,$2,$3}' > $OUTPUTF

INPUTF=$1/cases-confirmed.txt
OUTPUTF=$1/cases-confirmed-clear.txt 

sed 's/病例[0-9]*/|/g' $INPUTF | tr '|' '\n' | sed 's/，/,/g' | sed 's/^,//g' | sed 's/,$//g' | sed 's/。/./g' | sed 's/居住于//g' | awk -F"," '{print $1,$2,$3}' > $OUTPUTF

