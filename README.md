### Domain-monitoring

This python code is written to monitor the domains and send the status report to the owner. Most of us depends upon an external monitoring tools to monitor the domains in our server. This python code can be set as a cron to check the status of the domains in a server.

# The output of the this code will looks like the following.

```

root@ip-172-31-32-118:~/python2# python3 domains.py

https://freevideolectures.com            [ 200 ] : Up
https://www.guru99.com/                  [ 200 ] : Up
https://linuxjourney.com                 [ 200 ] : Up
https://www.quora.com                    [ 200 ] : Up
https://www.tecmint.com                  [ 200 ] : Up
https://linuxsurvival.com                [ 200 ] : Up
https://www.tutorialspoint.com           [ 200 ] : Up
https://www.computerworld.com            [ 200 ] : Up
https://hackernoon.com                   [ 200 ] : Up
https://www.howtoforge.com               [ 200 ] : Up
https://asdfg.com                        [ 000 ] : Error
https://www.ubuntupit.com/               [ 200 ] : Up
https://www.techworm.net                 [ 200 ] : Up
https://www.2daygeek.com/                [ 403 ] : DOWN
https://www.linux.org                    [ 200 ] : Up
https://linuxacademy.com                 [ 200 ] : Up
https://www.cyberciti.biz                [ 200 ] : Up
https://itsfoss.com                      [ 200 ] : Up
https://blog.feedspot.com                [ 200 ] : Up
https://www.techradar.com                [ 200 ] : Up
https://phoenixts.com/                   [ 200 ] : Up
https://training.linuxfoundation.org     [ 200 ] : Up
https://www.reallinuxuser.com/           [ 200 ] : Up
https://linuxconfig.org                  [ 200 ] : Up
https://sourceforge.net                  [ 200 ] : Up
https://www.makeuseof.com                [ 200 ] : Up

Enter your  email account password : *******

The report is sending.....

```
