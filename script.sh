# Script to load Setup the environment for WebCrawler and executing on Ubuntu

sudo apt update
sudo apt install software-properties-common 
 
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.8

#CReate Folder for assignment Checkout on local 
cd /home/$(whoami)/
mkdir assignment
cd /home/$(whoami)/assignment

#Install Git
sudo apt install git

#CLONE the git bracnh
git clone https://github.com/SSaxena/WebCrawler.git

#instll the required python modules bs4 and requests
cd WebCrawler-master/src
sudo apt install python3
sudo apt-get install python3 python3-pip
pip3 install bs4
pip3 install requests

#Start the Exceution 
python3 Start.py
















































