echo "gpu_mem=512" >> /boot/config.txt

git clone https://github.com/SvenVD/rpisurv

cd rpisurv

./install.sh

cd ..

python3 rpisurvprogram.py

systemctl restart rpisurv
