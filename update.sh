#!/bin/sh
cd `dirname $0`
IMG=pcduino_ubuntu_20130531.img

# if image file not found, try to use "latest" image file
if ! [ -f $IMG ]; then
    f=`ls ww_ubuntu_*.img  | sort -n -r | head -n 1`
    if [ -f $f ]; then
        IMG=$f
    else
        echo "$IMG not found"
        exit 1
    fi
fi

IMG_SIZE=`du -s $IMG  | cut -f1`
BURN_TIME=`expr $IMG_SIZE / 1024 / 3 / 60`
echo -e "\twriting $IMG to nand flash\n"
echo -e "\tit will take about $BURN_TIME minutes to finish..."

time dd if=$IMG of=/dev/nandd bs=4M && sync
if [ $? -eq 0 ]; then
    echo "update finished"
    killall blink_led.sh
    /blink_led.sh 18 1000000 & 
    /blink_led.sh 19 1000000 &          
else                                        
    echo "write ubuntu to nand failed"
    killall blink_led.sh   
    /blink_led.sh 18 100000 &
    /blink_led.sh 19 100000 &
    exit 1
fi
