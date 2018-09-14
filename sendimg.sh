clear
sudo python gpioLedwithcamera.py
sudo cp testimage.jpg /var/www/html/testimage.jpg
echo press Ctrl C within 5 seconds to Quit.
sleep 6
sleep 1
echo OK....
sudo bash sendimg.sh
