# Game N-Lug

## Presentation
Dev with Kivy.

N-Lug = Newton's law universal gravitation

Space game

## Generate APK for Android
### Requirements
YouTube tutorial to follow: [here](https://www.youtube.com/watch?v=pzsvN3fuBA0&t)
#### Linux 
Need to use Linux to create APK to use Kivy app on Android.
On windows use WSL Ubuntu.

Requirements on Linux (Ubuntu) machine:
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install autoconf
sudo apt-get install openjdk-8-jdk
sudo apt-get install unzip
sudo apt-get install zip
sudo apt-get install python3 python3-pip ipython3
sudo apt install build-essential libltdl-dev libffi-dev libssl-dev python3.10-dev
sudo apt-get install git
```
Cython install not working:
```
sudo apt-get install cython
```
Instead use: 
```
pip install cython
sudo pip install --upgrade cython
```
#### Install buildozer from git
```
git clone https://github.com/kivy/buildozer.git
cd buildozer
sudo python3 setup.py install
```
Check version with:
```
buildozer --version
```
### Clone project your project
```
git clone https://github.com/ThomasIsHere/n-lug.git
```
Then cd into project and if you use buildozer for the first time use:
```
buildozer init
```
Make sure file buildozer.spec is in the same place as the main.py file.
### Generate APK File
```
buildozer android clean
buildozer android debug
```
### Deploy APK on Android Phone
Manually deploying and installing apk on phone not working ...
Check log with: adb logcat | findstr n-lug
### Use Android Debug Bridge
Part not working find another tutorial.