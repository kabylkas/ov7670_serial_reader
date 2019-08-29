import serial
from PIL import Image
import numpy

width = 320
height = 240

start_cmd = "*RDY*"
cmd_iter = 0
start_found = 0
buff = ""

with serial.Serial('/dev/ttyACM0', baudrate=2000000) as ser:  # open serial port
  print(ser.name)
  i = 0
  while True:
    # read byte
    s = ser.read()
    buff = buff + s

    # poll start command
    if start_cmd in buff:
      start_found += 1
      buff = ""

    # after start has been found
    if start_found > 0:
      print("Start command found...")
      rgb = [[[0,0,0]] * width] * height
      rgb_buff = ""
      count = 0
      im = Image.new("RGBA", (height, width), (0,0,0, 255))
      pixels = im.load()

      for i in range(height):
        for j in range(width):
          y = ord(ser.read())
          pixels[i, j] = (y, y, y, 255)
      
      im.save("out2.png")
      print("Done!")
      break
