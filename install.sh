sudo apt update
sudo apt install fbi python-tk -y
mv run.sh ~/
mv app.py ~/
cd ~
echo "./run.sh" >> .bashrc
