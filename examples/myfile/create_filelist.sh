#!/usr/bin/env sh
DATA=data/re/
MY=examples/myfile

echo "Creating train.txt..."
rm -rf $MY/train.txt
for i in 3 4 5 6 7
do
l=$(($i-3))
#echo $l
find $DATA/train -name $i*.jpg | cut -d '/' -f4-5 | sed "s/$/ $l/">>$MY/train.txt
done
echo "Done."

echo "Creating test.txt..."
rm -rf $MY/test.txt
for i in 3 4 5 6 7
do
l=$(($i-3))
find $DATA/test -name $i*.jpg | cut -d '/' -f4-5 | sed "s/$/ $l/">>$MY/test.txt
done
echo "All done."
