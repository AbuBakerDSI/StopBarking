# StopBarking
A script to sense dig bark above a certain sound level and play a music .wav file to calm it
Steps:
1. In termianl, write the following code to clone this repository.
 git clone https://github.com/AbuBakerDSI/StopBarking.git
2. Now open the prereq.txt and install all the modules except pyAudio using,
sudo apt-get install module_name
3. Install pyaudio using pip3 install pyaudio
4. run the cc.py using 
sudo python3 cc.py 
or 
./cc.py
5. change the value of INITIAL_TAP_THRESHOLD to fine tune the barking dog detection.
6. place some mp3 file in the directory where cc.py is place. (can be changed later)
7. ctrl + C to stop the prcess
