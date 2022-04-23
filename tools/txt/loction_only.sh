#!/bin/sh
RAW_FILE=cases-location-only.txt
OUTPUT_FILE=cases-location-clear.txt
sed 's/。/./g' $1/$RAW_FILE | tr ',' '\n' | sed 's/、$//g' | sed 's/，$//g' | tr '，' '\n' | tr '、' '\n' | tr '。' '\n' | sed 's/（住宅）//g'| sed '/滑动查看更/d' | sed '/已对相关居住地落/d' | sed '/例本土新冠/d' | sed '/例本土无症状感染/d' | sed '/已对相关居住地落实终末消毒措施等/d' | sed '/确诊病例/d' | sed '/分别居住于/d' | sed 's/　//g' | sed 's/ //g' | sed 's/，/,/g' | sed 's/[,.、]$//g' | sed '/^$/d' | sed '/[居住|症状|(月.+日)]/d' > x
python merg.py x | sort | uniq > $1/$OUTPUT_FILE
rm x

cp $1/$OUTPUT_FILE $1/$OUTPUT_FILE.v0

cat \
	./20220417/cases-location-clear.txt.v0 \
	./20220418/cases-location-clear.txt.v0 \
	./20220419/cases-location-clear.txt.v0 \
	./20220420/cases-location-clear.txt.v0 \
	./20220421/cases-location-clear.txt.v0 \
	./20220422/cases-location-clear.txt.v0 \
	./20220423/cases-location-clear.txt.v0 \
	| sort | uniq > $1/$OUTPUT_FILE.v1

cp $1/$OUTPUT_FILE.v1 $1/$OUTPUT_FILE
