#!/usr/bin/env python3

import MFRC522
import signal
import time
import json
import sys

debug_enabled = False
if len(sys.argv) >= 2 and str(sys.argv[1]) == '--debug':
  debug_enabled = True

continue_reading = True
MIFAREReader = MFRC522.MFRC522()

def end_read(signal, frame):
  global continue_reading
  continue_reading = False
  pass # print "Ctrl+C captured, ending read."
  MIFAREReader.GPIO_CLEEN()

signal.signal(signal.SIGINT, end_read)

def debug_print(*args, **kwargs):
  global debug_enabled
  if debug_enabled:
    print(*args, **kwargs)

def get_card_info(uid, iso_compliant=False):
  manufacturer_code = None if len(uid) == 4 else uid[0]
  res = {
    'uidLength': len(uid),
    'isoCompliant': iso_compliant,
    'isRandomID': len(uid) == 4 and uid[0] == 0x08,
    'isFixedNumberNonUniqueID': len(uid) == 4 and (uid[0] & 0x0F) == 0x0F,
    'isRFU': len(uid) == 4 and uid[0] == 0xF8, # I do not know what an RFU is.
    'manufacturerCode': manufacturer_code,
  }
  debug_print('Card Info', res)
  return res

def read_uid():
  # read 4 byte (1 level), 7byte (2 levels), 10 byte (3 levels) cards
  (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
  if status != MIFAREReader.MI_OK:
    return
  debug_print("Card detected")
  uid = []
  sek = 0
  uid_complete = False
  iso_compliant = False
  for cascade_level in range(1,4):
      (status,uid_part) = MIFAREReader.MFRC522_Anticoll(cascade_level=cascade_level)
      if status != MIFAREReader.MI_OK:
        return
      debug_print("Cascade level {} read.".format(cascade_level), uid_part)
      (status, sek) = MIFAREReader.MFRC522_SelectTag(uid_part, cascade_level=cascade_level)
      if status != MIFAREReader.MI_OK:
        return
      debug_print("Cascade level {} select.".format(cascade_level), sek)
      uid_complete = ((sek) & 0x04) == 0
      if uid_complete:
        uid.extend(uid_part[0:4])
        break
      else:
        uid.extend(uid_part[1:4])
      debug_print("UID not complete")
  iso_compliant = ((sek) & 0x20) == 0x20
  if not uid_complete:
    debug_print("Failed to read UID successfully", uid)
    return
  debug_print("Successfully read UID", uid)
  card_info = get_card_info(uid, iso_compliant)
  return (uid, card_info)

while continue_reading:
  time.sleep(0.1)

  res = read_uid()

  if res is None:
    continue

  (uid, card_info) = res

  json_res = "{}\n".format(json.dumps({ 'uid': uid, 'cardInfo': card_info }))

  sys.stdout.write(json_res)
  # stay idle for 4 second after reading a card
  time.sleep(4)
  # TODO maybe instead prevent printing whilst same card present, if removed allow new scan.
