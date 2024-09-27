#!/bin/bash
# COMPsys Setup Script
# ONLY to configure things/hardware on a fresh Raspbian and check git files are OK
# enables SPI, serial and download git files
# Kirk Martinez 2022
echo "If you have run this without being asked to say no as this is only needed once on a new pi"
read -p "Are you sure you want to configure Pi for compsys? (y/n) " answer
if [[ $answer != y ]]
then
  echo "exiting without changing anything"
  exit
fi
echo "enabling SPI, hardware serial"
sudo raspi-config nonint do_spi 0 # enable SPI
sudo raspi-config nonint do_serial 1 # disable linux serial, enable hardware serial
sudo sed -i -e "s/enable_uart=0/enable_uart=1/" /boot/config.txt
echo "checking compsys files are up to date"
cd /home/pi
if [ -d compsys ]; then
	echo "compsys files exist - updating"
	cd compsys
	git pull
	cd ..
else
	echo "getting compsys files"
	git clone https://github.com/kmartinez/compsys.git
fi

pcmanfm --set-wallpaper /usr/share/rpd-wallpaper/RPiSystem.png
echo "you should Reboot with sudo reboot"
