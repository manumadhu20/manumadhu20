import qrcode
ls=[]
img=[]
for i in range(2):

    u=input("Enter name")
    v=input("Address")
    w=input("contact no:")

    ls=[u,v,w]
    print (ls)
    img.append(ls)
    
j=0 
for i in img:
    j+=1
    a=str(j)
    im = qrcode.make(i)
    type(im)  # qrcode.image.pil.PilImage
    im.save(a+".png")