Game N-Lug

Newton's law universal gravitation

# Buildozer requirements to compile apk on wsl ubuntu
sudo python3 setup.py install => to force buldozer with python 3 it seems not needed for may wsl

sudo apt-get update
sudo apt-get upgrade
sudo apt install python3 python3-pip ipython3
sudo apt-get install git
sudo apt-get install openjdk-8-jdk
sudo apt-get install unzip
sudo apt-get install zip

sudo apt-get install autoconf
sudo apt install build-essential libltdl-dev libffi-dev libssl-dev python-dev-is-python3

sudo pip install buildozer
sudo pip install cython
sudo pip3 install --upgrade cython

If error:
sdkmanager path "/home/u/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager" does not exist, sdkmanager is notinstalled
sudo apt-get install sdkmanager
And unzip commandlinetools-linux-6514223_latest.zip from 
sdkmanager path "/home/u/.buildozer/android/platform/android-sdk/

buildozer android debug => build apk (no need to run as sudo)