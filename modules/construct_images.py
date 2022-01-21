from PIL import Image,ImageDraw,ImageFont
import urllib.request

def get_images_and_names(all_shop_items):
    images=[]
    names=[]
    for entry in all_shop_items:
        for item in entry.items:
            item.icon=str(item.icon)
            item.name=str(item.name)

            #print(item.icon,item.name)

            if item.name in names:
                pass
            else:
                urllib.request.urlretrieve(item.icon,"./icons/{}.png".format(item.name))
                images.append(Image.open("./icons/{}.png".format(item.name)).convert("RGBA"))
                names.append(item.name)

    return images,names

def save_pages(all_shop_items):
    images,names=get_images_and_names(all_shop_items)
    background=Image.open("./bg.jpg","r")

    page=1
    count=1
    fullcount=0
    x_offset=-50
    y_offset=0
    for im in images:
        #print(count,names[fullcount],(x_offset,y_offset))

        background.paste(im,(x_offset,y_offset),im)

        font = ImageFont.truetype("./fonts/fortnite.otf",55)
        t = ImageDraw.Draw(background)
        t.text((x_offset+80,y_offset+im.size[1]), names[fullcount], fill=(255,255,255),font=font)

        x_offset+=im.size[0]

        if count%4==0:
            x_offset=0
            y_offset+=im.size[1]
        if count==8:
            background.save("./out/page{}.png".format(page))
            page+=1
            count=1
            x_offset=-50
            y_offset=0
            background=Image.open("./bg.jpg","r")
        else:
            count+=1    
        fullcount+=1