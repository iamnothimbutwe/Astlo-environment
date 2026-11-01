astlotalk allows astlo and astlohorizons to 'talk' with eact other

topocentric command in astlo requires this script for Luna, mercury, venus and Sol for accuracy.


just enter the python IDE in the same environment and:

from astlotalk import talk
talk('sun') #or moon, venus, mercury.

then use the topocentric command in astlo...

If one of the json files in this directory is needed to be written on in various other ways several times, just create a directory copy of Astlo-environment under a diffrent name and create the json files in the original Astlo-environment directory or delete the json files copies and let it the astlotalk create the new json files automatically.

astlo can also track the mentioned objects without needing the script
astlo tracks all of the Solar System objects.

only for accuracy.

adding an object is straightforwad..


DIFFRENCE BETWEEN astlos astlotalk and valleys astlotalk:

- astlos astlotalk is a while loop that updates the json files every minute. while valleys astlotalk updates only once and closes.
- astlos astlotalk is more for SDK but with the correct steps followed you can use it in the CLI. 
- use valleys astlotalk via CLI valley command topocentric. valley allows usage of only just one command to be able to use astlotalk module automatically..astlos astlotalk is manual uasage..

lets collaborate and build over or around them all..
