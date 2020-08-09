import colorsys, sys
hex = sys.argv[1]
r,g,b=tuple(
    int(hex[i:i+2], 16) 
    for i in (0, 2 ,4)
)
r,g,b=[x/255.0 for x in r,g,b]
# print [r,g,b]
h,l,s=colorsys.rgb_to_hls(r,g,b)
print h*360,s*50,l*50