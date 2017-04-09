# MFRC522 RFID Card Reader

#### MFRC522 Python Library for Orange Pi
  * Preparation
  ```
  $ sudo nano /etc/modprobe.d/raspi-blacklist.conf
  #blacklist spi-bcm2708
  ```
  ```
  $ sudo apt-get install python-dev
  $ git clone https://github.com/lthiery/SPI-Py
  $ cd SPI-Py
  $ sudo python setup.py install
  ```

  * Using Example
  ```
  $ git clone https://github.com/J-Rios/MFRC522-python-OPi
  $ cd MFRC522-python-OPi
  $ sudo python read.py
  ```

* [Mifare-RC522 and Orange PI](http://telegra.ph/GPIO-en-Python-Conectando-un-lector-RFID-NFC-por-SPI-04-09)

* [Hardware SPI as a C Extension for Python](https://github.com/lthiery/SPI-Py)
