echo "clearing the disk cache stored in the Pi's RAM"
echo "if this fails you forgot to run it with sudo ./clearcache.sh or didn't set it as executable with chmod"
echo 1 > /proc/sys/vm/drop_caches
