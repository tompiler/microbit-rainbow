
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
yellow = (50, 50, 0)
green = (0, 50, 0)
blue = (0, 0, 50)
indigo = (18, 15, 50)
violet = (30, 0, 50)
white = (0, 0, 0)


# Below we 'define' a function. A function is just like
# what you would make in a custom block, 'my blocks' in scratch!
# This allows us to keep running the same code whenever we like.
# The 'get_rainbow' function takes the colours we defined above
# and wraps them in something called a 'list' (with square brackets!)
# it then returns a list 12 colours long (exactly the same length as our neopixel)
def get_rainbow():
    rainbow = [red, orange, yellow, green, blue, indigo, violet]
    extra_colours = [white, white, white, white, white]
    
    rainbow = rainbow + extra_colours
    
    return rainbow
    
# The 'main' function is the function that we want to 
# run on the microbit.
# 
def main():

    # get the list of colours (12 colours long)
    rainbow = get_rainbow()
    
    # perform 100 'updates' to the neopixel
    for i in range(0, 100):
        
        # the first time we light up the neopixel,
        # we want it to light up each colour one at a time
        if i == 0:
            
            # this is a bit like a 'repeat' loop in scratch.
            # the code in the block below will run 12 times
            for pixel_id in range(0, len(neo)):
                
                # e.g. the line below will first evaluate to
                # neo[0] = rainbow[0]
                # in other words, set the first pixel to the first colour in the rainbow array
                neo[pixel_id] = rainbow[pixel_id]
                neo.show() # update the lights 
                sleep(75)
        

        else:
            
            for pixel_id in range(0, len(neo)):
                
                neo[pixel_id] = rainbow[pixel_id]
                neo.show()
                
        colour = rainbow.pop(0)
        rainbow = rainbow + [colour]
        sleep(100)
        
while True:
    if button_a.is_pressed():
        rainbow = get_rainbow()
        for pixel_id in range(0, len(neo)):
            neo[pixel_id] = (0, 0, 0)
            neo.show()
        
        main()