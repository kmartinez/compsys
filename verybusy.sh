# run four copies in the background and wait for them all to complete
time ./busycpu &
time ./busycpu &
time ./busycpu &
time ./busycpu &
wait
