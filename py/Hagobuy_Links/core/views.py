from django.shortcuts import render


def main(request):
    return render(request, 'core/index.html')

def short_sleeves(request):
    product_data = [
        {"name": "Polo Shirts", "image": "short_sleeves_images/image1.png", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D769255629431"},  # Assuming the image is stored in static/images directory
        {"name": "Bape Shirts","image": "short_sleeves_images/image2.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fwww.pandabuy.com%2Fproduct%3Furl%3Dhttps%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D628597198711&affcode=Skint105"},
        {"name": "Hellstar Shirts", "image": "short_sleeves_images/image3.webp", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fwww.pandabuy.com%2Fproduct%3Furl%3Dhttps%3A%2F%2Fdetail.1688.com%2Foffer%2F633663198868.html&affcode=Skint105"},
        {"name": "ESSENTIALS Shirts", "image": "short_sleeves_images/image4.avif", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D642686120623"},
        {"name": "ASSC Shirts", "image": "short_sleeves_images/image5.avif", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fwww.pandabuy.com%2Fproduct%3Furl%3Dhttps%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D612763359831&affcode=Skint105"},
        

        {"name": "Vlone Shirts", "image": "short_sleeves_images/image6.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D639013003953&affcode=vllady"},  # Assuming the image is stored in static/images directory
        {"name": "Sicko X Joy Shirts","image": "short_sleeves_images/image7.avif", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D620566609945%26spm%3D1101.1101.N.N.fa3bda3&affcode=8bp9fx"},
        {"name": "Blank Shirts", "image": "short_sleeves_images/image8.avif", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D599269056085&affcode=8bp9f"},
        {"name": "Yeezus Tour Merch Shirts", "image": "short_sleeves_images/image9.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D553778141441&affcode=8bp9fx"},
        {"name": "Jacquemes Artichoke Shirts", "image": "short_sleeves_images/image10.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fspm%3Da1z09.2.0.0.67002e8dypL4CT%26id%3D620058236834%26_u%3Dt2029tsf5t34e3&affcode=8bp9fx"},
        # Add or modify product data as needed
        
    ]
    return render(request, 'core/short_sleeves.html', {'product_data': product_data})

def long_sleeves(request):
    product_data = [
        {"name": "Curly Stussy Sweatshirt", "image": "long_sleeves_images/image1.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fwww.pandabuy.com%2Fproduct%3Furl%3Dhttps%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D658802784606&affcode=Skint105"},
        {"name": "Nike Sweatshirt", "image": "long_sleeves_images/image2.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fweidian.com%2Fitem.html%3FitemID%3D5586007089&affcode=Skint105"},
        {"name": "Chrome Heart Sweatshirt", "image": "long_sleeves_images/image3.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fdetail.1688.com%2Foffer%2F674868552053.html&affcode=Skint105"},
        {"name": "Moncler Sweatshirt", "image": "long_sleeves_images/image4.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fwww.pandabuy.com%2Fproduct%3Furl%3Dhttps%3A%2F%2Fweidian.com%2Fitem.html%3FitemID%3D6716265132%26spider_token%3D4572&affcode=Skint105"},
        {"name": "Carhartt Half Zip", "image": "long_sleeves_images/image5.jpg", "url": "https://www.hagobuy.com/item/details?url=chttps%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D681986179332&affcode=Skint105"},
    ]
    return render(request, 'core/long_sleeves.html', {'product_data': product_data})

def pants(request):
    product_data = [
        {"name": "SPIDER Sweatpants", "image": "pants_images/image1.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fdetail.1688.com%2Foffer%2F633626441433.html&affcode=Skint105"},
        {"name": "Nike Sweatpants", "image": "pants_images/image2.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fwww.pandabuy.com%2Fproduct%3Furl%3Dhttps%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D693488975051&affcode=Skint105"},
        {"name": "Demin Tear Sweatpants", "image": "pants_images/image3.webp", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fwww.pandabuy.com%2Fproduct%3Furl%3Dhttps%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D714488532350&affcode=Skint105"},
        {"name": "Demin Tear Jeans", "image": "pants_images/image4.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fwww.pandabuy.com%2Fproduct%3Furl%3Dhttps%3A%2F%2Fweidian.com%2Fitem.html%3FitemID%3D4396758883%26spider_token%3D4572&affcode=Skint105"},
        {"name": "Carhartt Casual Pants", "image": "pants_images/image5.avif", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fwww.pandabuy.com%2Fproduct%3Furl%3Dhttps%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D614260353450&affcode=Skint105"},
        # Add more product data as needed
        # Add more product data as needed
    ]
    return render(request, 'core/pants.html', {'product_data': product_data})

def shorts(request):
    product_data = [
        {"name": "EE Shorts", "image": "shorts_images/image1.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D669035497036"},
        {"name": "ASRV Shorts", "image": "shorts_images/image2.avif", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D618551946198"},
        {"name": "KINETIC Shorts", "image": "shorts_images/image3.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fdetail.1688.com%2Foffer%2F678304980969.html"},
        {"name": "NORTH FACE Shorts", "image": "shorts_images/image4.jpg", "url": "https://weidian.com/item.html?itemID=4397132802"},
        {"name": "RHUDE Shorts", "image": "shorts_images/image5.png", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fdetail.1688.com%2Foffer%2F672114067770.html"},
        # Add more product data as needed
        # Add more product data as needed
    ]
    return render(request, 'core/shorts.html', {'product_data': product_data})


    
def shoes(request):
    product_data = [
        {"name": "Travis Scot 1 Low", "image": "shoes_images/image1.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fwww.pandabuy.com%2Fproduct%3Furl%3Dhttps%3A%2F%2Fdetail.tmall.com%2Fitem.htm%3Fid%3D657833520057&affcode=Skint105"},
        {"name": "LV Slides", "image": "shoes_images/image2.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fwww.pandabuy.com%2Fproduct%3Furl%3Dhttps%3A%2F%2Fweidian.com%2Fitem.html%3FitemID%3D6382333051%26utm_source%3Dsto%26utm_medium%3Dpdb%26utm_campaign%3Dnormal&affcode=Skint105"},
        {"name": "LV Trainers", "image": "shoes_images/image3.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fweidian.com%2Fitem.html%3FitemID%3D6393049889&affcode=tewgk"},
        {"name": "NB 550", "image": "shoes_images/image4.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fwww.pandabuy.com%2Fproduct%3Furl%3Dhttps%3A%2F%2Fweidian.com%2Fitem.html%3FitemID%3D6480022480%26spider_token%3D4572&affcode=Skint105"},
        {"name": "Kobe 4 / 5 / 6 / 8", "image": "shoes_images/image5.webp", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fwww.pandabuy.com%2Fproduct%3Furl%3Dhttps%3A%2F%2Fweidian.com%2Fitem.html%3FitemID%3D6141820770%26utm_source%3Dsto%26utm_medium%3Dpdb%26utm_campaign%3Dnormal&affcode=Skint105"},
    ]
    return render(request, 'core/shoes.html', {'product_data': product_data})

def accessories(request):
    product_data = [
        {"name": "Carti Phonecase", "image": "accessories_images/image1.webp", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fwww.pandabuy.com%2Fproduct%3Furl%3Dhttps%3A%2F%2Fweidian.com%2Fitem.html%3FitemID%3D6075508918%26utm_source%3Dsto%26utm_medium%3Dpdb%26utm_campaign%3Dnormal&affcode=Skint105"},
        {"name": "Chrome Heart Bracelet", "image": "accessories_images/image2.avif", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D43156377709&affcode=Skint105"},
        {"name": "Chrome Heart Necklace", "image": "accessories_images/image3.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fdetail.1688.com%2Foffer%2F708101083989.html&affcode=Skint105"},
        {"name": "Carhartt Hats", "image": "accessories_images/image6.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fdetail.1688.com%2Foffer%2F677285398760.html&affcode=Felisuko99"},
        {"name": "Nike Socks", "image": "accessories_images/image5.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fdetail.tmall.com%2Fitem.htm%3Fid%3D616770606113&affcode=Skint105"},
    ]
    return render(request, 'core/accessories.html', {'product_data': product_data})


def sweaters(request):
    product_data = [
        {"name": "SPIDER Hoodie", "image": "sweaters_images/image1.webp", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fdetail.1688.com%2Foffer%2F633626441433.html"},
        {"name": "FOG Essentials Hoodie", "image": "sweaters_images/image2.webp", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D573254630703"},
        {"name": "4TUNE Full Zipup", "image": "sweaters_images/image3.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D689300676850"},
        {"name": "Travis Scot Cactus Jack Zipup", "image": "sweaters_images/image4.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D659005357561"},
        {"name": "Polo Ralph Lauren Zipup", "image": "sweaters_images/image5.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fweidian.com%2Fitem.html%3FitemID%3D2682215440"},
    ]
    return render(request, 'core/sweaters.html', {'product_data': product_data})


def jackets(request):
    product_data = [
        {"name": " Canada Goose Men/Women Winter Gilet Vest", "image": "jackets_images/image1.webp", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fdetail.1688.com%2Foffer%2F675358399697.html"},
        {"name": "THE NORTH FACE 1996 Retro Nuptse Puffer Jacket", "image": "jackets_images/image2.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fwww.pandabuy.com%2Fproduct%3Fra%3D947%26url%3Dhttps%253A%252F%252Fweidian.com%252Fitem.html%253FitemID%253D6381347740%2526spider_token%253D4572%26utm_source%3Durl%26utm_medium%3Dpdb%26utm_campaign%3Dnormal%26inviteCode%3DZK3REWB43"},
        {"name": "Nike X Tiffany Embroidered Jacket", "image": "jackets_images/image3.jpg", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fweidian.com%2Fitem.html%3FitemID%3D6157588466"},
        {"name": "Trapster Jacket", "image": "jackets_images/image4.webp", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D692163862718&affcode=habibi"},
        {"name": "Canada Goose Wyndham Parka", "image": "jackets_images/image5.webp", "url": "https://www.hagobuy.com/item/details?url=https%3A%2F%2Fdetail.1688.com%2Foffer%2F683972358109.html"},
    ]
    return render(request, 'core/jackets.html', {'product_data': product_data})


