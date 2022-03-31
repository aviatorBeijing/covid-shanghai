#!/bin/sh

INPUTF=$1/cases-nosyndrome.txt
OUTPUTF=$1/cases-nosyndrome-clear.txt 

#sed 's/无症状感染者[0-9]*/|/g' $INPUTF | tr '|' '\n' | sed '/间新冠病毒核/d' | sed 's/　//g' | sed 's/，/,/g' | sed 's/^,//g' | sed 's/,$//g' | sed 's/。/./g' | sed 's/居住于//g' | sed '/^$/d' | sed '/^$/d' | awk -F"," '{print $1,$2,$3}' | sort > $OUTPUTF
sed 's/无症状感染者//g' $INPUTF | sed 's/，/,/g' | sed 's/。//g' | sed '/^$/d' |sed 's/,$//g' | sed '/诊断为/d' |sed 's/居住于//g'|sed 's/—/,/g' |sed 's/、/,/g'  | xargs python e.py | sort > $OUTPUTF

INPUTF=$1/cases-confirmed.txt
OUTPUTF=$1/cases-confirmed-clear.txt 

#sed 's/病例[0-9]*/|/g' $INPUTF | tr '|' '\n' | sed '/间新冠病毒核/d' | sed 's/　//g' | sed 's/，/,/g' | sed 's/^,//g' | sed 's/,$//g' | sed 's/。/./g' | sed 's/居住于//g' | sed '/^$/d' | sed '/^$/d' | awk -F"," '{print $1,$2,$3}' | sort > $OUTPUTF
sed 's/病例//g' $INPUTF | sed 's/，/,/g' | sed 's/。//g' | sed '/^$/d' |sed 's/,$//g' | sed '/诊断为/d' |sed 's/居住于//g'|sed 's/—/,/g' |sed 's/、/,/g' | xargs python e.py | sort > $OUTPUTF
