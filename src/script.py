
# module imports below!
from microbit import * # imports all the functions from the microbit library
import neopixel # imports all the neopixel classes and functions we need


# The line below is very important!
# There is a lot of code within the neopixel library 
# which helps us interact with the neopixel ring.
# We access this code via neopixel's classes and functions (or methods) 
# found by 'instantiating' (setting up) a neopixel object below:
neo = neopixel.NeoPixel(pin0, 12)


# Here we define the colours.
# In computers, colours are often set according to
# their red/green/blue (RGB) value. For example,
# 'red' below is set to Red=50, Blue=0, Green = 0.
# The numbers relate to how bright each pixel is, on
# a scale betweel 0 and 255. 255 is very bright!
red = (50, 0, 0)
orange = (70, 25, 0)
green = (0, 50, 0)

traffic_lights = [red, orange, green]

for pixel_id in range(0, len(traffic_lights)):
    neo[pixel_id] = traffic_lights[pixel_id]
    neo.show()
