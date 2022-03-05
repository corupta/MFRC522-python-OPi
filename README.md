# MFRC522 RFID Card Reader

I ported the original library for my use-case:
* I needed to be able to read 4/7/10 byte uids and nothing else
* I did NOT need to implement any read/write for remaining sectors
* I refer to [https://www.nxp.com/docs/en/application-note/AN10927.pdf](https://www.nxp.com/docs/en/application-note/AN10927.pdf) and ISO/IEC 14443 UIDs

- [x] Modified the library to make it work on python3
- [x] Replaced old spi with spidev
- [x] Implemented support for reading 4/7/10byte uid
- [x] Implement adding some metadata about uid
- [ ] Test reading 4 byte UID
- [ ] Test reading 7 byte UID
- [ ] Test reading 10 byte UID (Cannot test, I don't have such a card)
- [ ] Test reading 4 byte RID

#### MFRC522 Python3 Library for Orange Pi
  * Preparation
  ```
  $ sudo apt-get install python3 python3-dev python3-pip
  $ sudo pip3 install -r Requirements.txt
  ```

  * Using Example
  ```
  $ git clone https://github.com/corupta/MFRC522-python-OPi
  $ cd MFRC522-python-OPi
  $ sudo python3 read.py --debug
  ```

* [Mifare-RC522 and Orange PI](https://descubriendolaorangepi.wordpress.com/2017/04/09/gpio-en-python-conectando-un-lector-rfid-nfc-por-spi)


#### See Fork History

Original repo is from 2014, and it has MIT license, the same license file is kept afterwards.

* [@corupta/MFRC522-python-OPi](https://github.com/corupta/MFRC522-python-OPi)
* [@J-Rios/MFRC522-python-OPi](https://github.com/J-Rios/MFRC522-python-OPi)
* [@yongsukki/MFRC522-python](https://github.com/yongsukki/MFRC522-python)

