# rpi-streaming
Set of scripts (python? bash?) for automating streaming with a RPi3 to youtube.  
Read settings/schedule from some config file.  
Automatically create youtube live events using the Youtube API.  
Create youtube playlist and add live events to it as they are created  

# Hardware
* RPi3 with case
* Logitech C920 for video, audio, and encoding
* ? Maybe some other external mic if it's not too difficult to mount
* ? Big battery for remote abilities
* ? LCD for status

# Pre-reqs
* Some sort of minimal linux
* Cron or some sort of scheduler
* ffmpeg
* sshd -at least until things work without it

# Future ideas
package a complete .img  
web interface for configuration and monitoring  
