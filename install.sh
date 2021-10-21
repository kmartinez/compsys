#!/bin/bash

# COMP1203 Setup Script
# ONLY to configure things/hardware on a fresh Raspbian
# probably harmless otherwise but it will reboot the Pi
# Laurie Kirkcaldy / Josh Curry / Kirk Martinez 2018

read -p "Are you sure you want to configure Raspbian hardware settings? (y/n) " answer
if [[ $answer != y ]]
then
  echo "exiting without changing anything"
  exit
fi
echo "enabling SPI, hardware serial"
sudo raspi-config nonint do_spi 0 # enable SPI
sudo raspi-config nonint do_serial 1 # disable linux serial, enable hardware serial
sudo sed -i -e "s/enable_uart=0/enable_uart=1/" /boot/config.txt
echo "checking compy1203 python is up to date"
cd ~/comp1203-python
git pull
git checkout master
pcmanfm --set-wallpaper /usr/share/rpd-wallpaper/fjord.jpg
echo "Rebooting in 3 seconds. CTRL-C to interrupt."
sleep 3
sudo reboot
