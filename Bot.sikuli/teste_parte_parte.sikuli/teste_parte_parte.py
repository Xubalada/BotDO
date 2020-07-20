from java.awt import Robot
cp = find(capture())
r = Robot()
c = r.getPixelColor(cp.getX(), cp.getY()) # get the color object
crgb = (c.getRed(), c.getGreen(), c.getBlue() ) # decode to RGB values
print crgb


#def get_top_line(a):
   # central_top = []
   # central_position = float(a)
   # print central_position/14
   # while central_position/14/2 != 0 and central_position > 14:
    #    if (central_position//14) % 2 == 0:
    #        central_position -=  15
    #    else:
    #        central_position -=  14
     #   central_top.append(central_position)
   # return central_top

#print(get_top_line(85))