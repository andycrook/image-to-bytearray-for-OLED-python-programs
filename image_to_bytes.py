# Simple image to bytearray for python OLED programs
#
# Input a simple black and white image (RGB bitmap though!)- image is reduced to 2 bit
#
#




from PIL import Image

image = "Nose2_large.bmp"



im = Image.open(image) # Can be many different formats.

output_ascii_image = False



pix = im.load()
print ("File:")
print (image) 
print ("")
print ("Image Dimensions:")
print (im.size) 
print ("")
if im.width % 8 == 0:
    print("Width divisible by 8")
    valid = True
else:
    valid = False
if im.height % 8 == 0:
    print("Width divisible by 8")
    valid = True
else:
    valid = False


if valid == True:
    print ("")
    print ("bytearray for Python code:")
    print ("")
    byte = [0,0,0,0,0,0,0,0]
    b_value=0
    bitstring = image[:-4].lower()
    bitstring +=" = bytearray(b"
    bitstring += "\""
    pixel_map = ""
    for y in range(im.height):
        pixel_map = ""
        for x in range(int(im.width/8)):
           
            bitvalue=128
            b_value=0
            for bit in range(8):
                if pix[(x*8)+bit,y][1]>128: # Looking at green pixel only
                    byte[bit] = 1
                    pixel_map+=("1")
                    b_value+=bitvalue
                else:
                    byte[bit] = 0
                    pixel_map+=("0")
                bitvalue=bitvalue/2


            bitstring += "\\"
         
            temp_hex = str(hex(int(b_value)))[1:]
            if len(temp_hex)==2:
                temp_hex = temp_hex.replace("x","x0")
            bitstring +=temp_hex
        # bitstring += " "
        if y<im.height-1:
            bitstring += "\\"
            bitstring += "\n"
        if  output_ascii_image == True:   
            print(pixel_map)
    bitstring += "\")"
    print(bitstring)




