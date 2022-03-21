#!/bin/sh
RAW_FILE=cases-location-only.txt
OUTPUT_FILE=cases-location-clear.txt
sed 's/。/./g' $1/$RAW_FILE | sed '/已对相关居住地落/d' | sed '/例本土新冠/d' | sed '/例本土无症状感染/d' | sed '/已对相关居住地落实终末消毒措施等/d' | sed 's/ //g' | sed 's/，/,/g' | sed 's/[,.、]$//g' | sed '/^$/d' | awk '{print "无 " "1 " $0}' | xargs python merg.py > $1/$OUTPUT_FILE