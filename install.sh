sudo apt update
sudo apt install python-tk -y
sudo -H pip install Pillow
mv run.sh ~/
mv app.py ~/
cd ~
echo "./run.sh" >> .bashrc
