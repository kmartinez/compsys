#!/bin/bash
# COMP1203 Setup Script
# ONLY to configure things/hardware on a fresh Raspbian and check git files are OK
# enables SPI, serial and download git files
# Kirk Martinez 2022

read -p "Are you sure you want to configure Pi for comp1203? (y/n) " answer
if [[ $answer != y ]]
then
  echo "exiting without changing anything"
  exit
fi
echo "enabling SPI, hardware serial"
sudo raspi-config nonint do_spi 0 # enable SPI
sudo raspi-config nonint do_serial 1 # disable linux serial, enable hardware serial
sudo sed -i -e "s/enable_uart=0/enable_uart=1/" /boot/config.txt
echo "checking comp1203 files are up to date"
cd /home/pi
if [ -d comp1203 ]; then
	echo "comp1203 files exist - updating"
	cd comp1203
	git pull
	cd ..
else
	echo "getting comp1203 files"
	git clone https://github.com/kmartinez/comp1203.git
fi

pcmanfm --set-wallpaper /usr/share/rpd-wallpaper/RPiSystem.png
echo "you should Reboot with sudo reboot"
