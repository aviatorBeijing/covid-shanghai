#!/bin/sh
RAW_FILE=cases-location-only.txt
OUTPUT_FILE=cases-location-clear.txt
sed 's/。/./g' $1/$RAW_FILE | tr ',' '\n' | sed 's/、$//g' | sed 's/，$//g' | tr '，' '\n' | tr '、' '\n' | tr '。' '\n' | sed 's/（住宅）//g'| sed '/滑动查看更/d' | sed '/已对相关居住地落/d' | sed '/例本土新冠/d' | sed '/例本土无症状感染/d' | sed '/已对相关居住地落实终末消毒措施等/d' | sed '/确诊病例/d' | sed '/分别居住于/d' | sed 's/　//g' | sed 's/ //g' | sed 's/，/,/g' | sed 's/[,.、]$//g' | sed '/^$/d' | sed '/[居住|症状|(月.+日)]/d' > x
python merg.py x | sort | uniq > $1/$OUTPUT_FILE
rm x

cp $1/$OUTPUT_FILE $1/$OUTPUT_FILE.v0

cat \
	./20220423/cases-location-clear.txt.v0 \
	./20220424/cases-location-clear.txt.v0 \
	./20220425/cases-location-clear.txt.v0 \
	./20220426/cases-location-clear.txt.v0 \
	./20220427/cases-location-clear.txt.v0 \
	./20220428/cases-location-clear.txt.v0 \
	./20220429/cases-location-clear.txt.v0 \
	| sort | uniq > $1/$OUTPUT_FILE.v1

cp $1/$OUTPUT_FILE.v1 $1/$OUTPUT_FILE
