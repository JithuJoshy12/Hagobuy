from django.shortcuts import render


def main(request):
    return render(request, 'core/index.html')

def short_sleeves(request):
    product_data = [
        {"name": "Polo Shirts", "image": "short_sleeves_images/image1.png", "url": "https://weidian.info/kku86"},  # Assuming the image is stored in static/images directory
        {"name": "Bape Shirts","image": "short_sleeves_images/image2.jpg", "url": "https://weidian.info/knqfu"},
        {"name": "Hellstar Shirts", "image": "short_sleeves_images/image3.webp", "url": "https://weidian.info/9wq23"},
        {"name": "ESSENTIALS Shirts", "image": "short_sleeves_images/image4.avif", "url": "https://weidian.info/v9g7s"},
        {"name": "ASSC Shirts", "image": "short_sleeves_images/image5.avif", "url": "https://weidian.info/ubjx4"},
        

        {"name": "Vlone Shirts", "image": "short_sleeves_images/image6.jpg", "url": "https://weidian.info/qajc6"},  # Assuming the image is stored in static/images directory
        {"name": "Sicko X Joy Shirts","image": "short_sleeves_images/image7.avif", "url": "https://weidian.info/5kuvw"},
        {"name": "Blank Shirts", "image": "short_sleeves_images/image8.avif", "url": "https://weidian.info/qvu8j"},
        {"name": "Yeezus Tour Merch Shirts", "image": "short_sleeves_images/image9.jpg", "url": "https://weidian.info/da82d"},
        {"name": "Jacquemes Artichoke Shirts", "image": "short_sleeves_images/image10.jpg", "url": "https://weidian.info/2j6gr"},

        {"name": "Narcissict Merch", "image": "short_sleeves_images/image11.jpg", "url": "https://weidian.info/gxpmx"},  # Assuming the image is stored in static/images directory
        {"name": "Fat Tub Of Lard Shirts ","image": "short_sleeves_images/image12.avif", "url": "https://weidian.info/5hzgr"},
        {"name": "Balenciaga Misplaced Shirt ", "image": "short_sleeves_images/image13.jpg", "url": "https://weidian.info/ujwy5"},
        {"name": "Vetements I did Nothing Shirt", "image": "short_sleeves_images/image14.avif", "url": "https://weidian.info/sam5n"},
        {"name": "30+ Travis Scot Merch ", "image": "short_sleeves_images/image15.avif", "url": "https://weidian.info/6zkzu"},

        {"name": "OnlyFans Shirts", "image": "short_sleeves_images/image16.avif", "url": "https://weidian.info/5kc2w"},  # Assuming the image is stored in static/images directory
        {"name": "Two piece Shirts ","image": "short_sleeves_images/image17.avif", "url": "https://weidian.info/85hpp"},
        {"name": "Balenciaga Sporty B Shrunk Tee", "image": "short_sleeves_images/image18.jpg", "url": "https://weidian.info/usqds"},
        {"name": "Balenciaga x Adidas Shirts", "image": "short_sleeves_images/image19.jpg", "url": "https://weidian.info/h6cwy"},
        {"name": "Carti WLR Vampire Shirt White", "image": "short_sleeves_images/image20.avif", "url": "https://weidian.info/c5t48"},

        {"name": "Carti WLR Hell Merch ", "image": "short_sleeves_images/image21.avif", "url": "https://weidian.info/v2aah"},  # Assuming the image is stored in static/images directory
        {"name": "Corteiz Shirts ","image": "short_sleeves_images/image22.jpg", "url": "https://weidian.info/gynx6"},
        {"name":"Carti x CPFM Merch White ", "image": "short_sleeves_images/image23.avif", "url": "https://weidian.info/4hcxy"},
        {"name": "Chrome Heart Cross Shirt", "image": "short_sleeves_images/image24.jpg", "url": "https://weidian.info/jjxh6"},
        {"name": "Dennis Rodman Tee ", "image": "short_sleeves_images/image25.avif", "url": "https://weidian.info/tb7q3"},

        {"name": "Golf Wang Shirts ", "image": "short_sleeves_images/image26.avif", "url": "https://weidian.info/mmycu"},  # Assuming the image is stored in static/images directory
        {"name": "Frank Ocean Blonded Tee ","image": "short_sleeves_images/image27.jpg", "url": "https://weidian.info/y86ty"},
        {"name":"Gallery Dept Alone in Silence Shirt ", "image": "short_sleeves_images/image28.jpg", "url": "https://weidian.info/7r53q"},
        {"name": "Fragment Clot Tee (2006)", "image": "short_sleeves_images/image29.jpg", "url": "https://weidian.info/jjxh6"},
        {"name": "Fuck Me? Fuck You! Number Nine Shirt ", "image": "short_sleeves_images/image30.avif", "url": "https://weidian.info/qcmyv"},

        {"name": "Gallery Dept Middle Finger Tee ", "image": "short_sleeves_images/image31.avif", "url": "https://weidian.info/fe2d6"},  # Assuming the image is stored in static/images directory
        {"name": "Gallery DEPT Hollywood T-shirt ","image": "short_sleeves_images/image32.jpg", "url": "https://weidian.info/4bwjp"},
        {"name":"Gothic Slogan Number Nine Shirt ", "image": "short_sleeves_images/image33.avif", "url": "https://weidian.info/x95b6"},
        {"name": "Corteiz Grass T-shirts", "image": "short_sleeves_images/image34.jpg", "url": "https://weidian.info/tedue"},
        {"name": "FG T-shirts ", "image": "short_sleeves_images/image35.jpg", "url": "https://weidian.info/qsky7"},
        
        {"name": "Hellstar Grateful Dead Tee ", "image": "short_sleeves_images/image36.jpg", "url": "https://weidian.info/5m997"},  # Assuming the image is stored in static/images directory
        {"name": "CPFM Hawaiian Shirt ","image": "short_sleeves_images/image37.avif", "url": "https://weidian.info/zsznf"},
        {"name":"Kapital Ringer Tee ", "image": "short_sleeves_images/image38.avif", "url": "https://weidian.info/jmkn5"},
        {"name": "House of Errors T-Shirt", "image": "short_sleeves_images/image39.avif", "url": "https://weidian.info/4g2er"},
        {"name": "Grateful Dead Shirt", "image": "short_sleeves_images/image40.jpg", "url": "https://weidian.info/r3gp9"},

        {"name": "Dior Oblique Print Polo Shirts", "image": "short_sleeves_images/image41.jpg", "url": "https://weidian.info/z98mb"},  # Assuming the image is stored in static/images directory
        {"name": "Joy Sicko Tee ","image": "short_sleeves_images/image42.avif", "url": "https://weidian.info/j3wbb"},
        {"name":"Playboi Carti Falling in Reverse WLR Shirt", "image": "short_sleeves_images/image43.avif", "url": "https://weidian.info/7zy7g"},
        {"name": "Led Zeppelin Number Nine Shirt ", "image": "short_sleeves_images/image44.avif", "url": "https://weidian.info/wbjjz"},
        {"name": "Playboi Carti WLR Merch", "image": "short_sleeves_images/image45.avif", "url": "https://weidian.info/ph4fd"},

        {"name": "10+ Vintage Rapper Graphic Tees", "image": "short_sleeves_images/image46.avif", "url": "https://weidian.info/5gu8f"},  # Assuming the image is stored in static/images directory
        {"name": "Trapstar Jerseys ","image": "short_sleeves_images/image47.jpg", "url": "https://weidian.info/qynsg"},
        {"name":"Number Nine 3 Mickey Shirts", "image": "short_sleeves_images/image48.avif", "url": "https://weidian.info/86u9c"},
        {"name": "Prada Dress Shirts", "image": "short_sleeves_images/image49.avif", "url": "https://weidian.info/ny8du"},
        {"name": "Rick Owens DRKR Tee", "image": "short_sleeves_images/image50.jpg", "url": "https://weidian.info/y3bdb"},

        {"name": "Kurt Cobain Number Nine ", "image": "short_sleeves_images/image51.avif", "url": "https://weidian.info/skqd6"},  # Assuming the image is stored in static/images directory
        {"name": "Nirvana Shirt","image": "short_sleeves_images/image52.avif", "url": "https://weidian.info/n9cvn"},
        {"name":"Loved Gun Number Nine T Shirt", "image": "short_sleeves_images/image53.avif", "url": "https://weidian.info/unefd"},
        {"name": "Ken Car$on Teen X Merch ", "image": "short_sleeves_images/image54.avif", "url": "https://weidian.info/wua3q"},
        {"name": "Narcissist Merch", "image": "short_sleeves_images/image55.avif", "url": "https://weidian.info/he6wt"},

        {"name": "Nirvana Vintage Shirts", "image": "short_sleeves_images/image56.jpg", "url": "https://weidian.info/j8fsu"},  # Assuming the image is stored in static/images directory
        {"name": "Undercover x CDG Shirt","image": "short_sleeves_images/image57.avif", "url": "https://weidian.info/8hfha"},
        {"name":"Undercover Scab Scorpion T-Shirt", "image": "short_sleeves_images/image58.avif", "url": "https://weidian.info/4vvb9"},
        {"name": "Mood Swings T-Shirts", "image": "short_sleeves_images/image59.avif", "url": "https://weidian.info/nneex"},
        {"name": "Rick Owens Fog Machine T Shirts", "image": "short_sleeves_images/image60.jpg", "url": "https://weidian.info/f8t77"},

        {"name": "Playboi Carti Anime Shirt White ", "image": "short_sleeves_images/image61.avif", "url": "https://weidian.info/vawch"},  # Assuming the image is stored in static/images directory
        {"name": "Eyeball Vintage Tee ","image": "short_sleeves_images/image62.jpg", "url": "https://weidian.info/fen4e"},
        {"name":"Kapital Two Tone Shirts", "image": "short_sleeves_images/image63.avif", "url": "https://weidian.info/wfbg6"},
        {"name": "Carti WLR Hell Merch White ", "image": "short_sleeves_images/image64.avif", "url": "https://weidian.info/cw6vx"},
        {"name": "Saint Michael Virgin Mary Tee", "image": "short_sleeves_images/image65.avif", "url": "https://weidian.info/cz957"},

        
        # Add or modify product data as needed
        
    ]
    return render(request, 'core/short_sleeves.html', {'product_data': product_data})

def long_sleeves(request):
    product_data = [
        {"name": "Curly Stussy Sweatshirt", "image": "long_sleeves_images/image1.jpg", "url": "https://weidian.info/2jccs"},
        {"name": "Small Logo Nike Sweatshirt", "image": "long_sleeves_images/image2.jpg", "url": "https://weidian.info/ymtuz"},
        {"name": "Chrome Heart Sweatshirt", "image": "long_sleeves_images/image3.jpg", "url": "https://weidian.info/vbbry"},
        {"name": "Moncler Sweatshirt", "image": "long_sleeves_images/image4.jpg", "url": "https://weidian.info/md57h"},
        {"name": "Carhartt Half Zip", "image": "long_sleeves_images/image5.jpg", "url": "https://weidian.info/s32q5"},

        {"name": "Orange Autumn Chrome Heart Sweatshirt", "image": "long_sleeves_images/image6.jpg", "url": "https://weidian.info/29cpn"},
        {"name": "Bape Sweatshirt", "image": "long_sleeves_images/image7.avif", "url": "https://weidian.info/pxvna"},
        {"name": "Hockey X Balenciaga Jersey Sweatshirt", "image": "long_sleeves_images/image8.jpg", "url": "https://weidian.info/dj74d"},
        {"name": "Balenciaga Campaign Sweatshirt", "image": "long_sleeves_images/image9.jpg", "url": "https://weidian.info/wn6ez"},
        {"name": "Balenciaga Pride Crewneck", "image": "long_sleeves_images/image10.jpg", "url": "https://weidian.info/v7c9e"},

        {"name": "Destroyed Chrome Heart Sweatshirt", "image": "long_sleeves_images/image11.jpg", "url": "https://weidian.info/2jyap"},
        {"name": "ERD Knit Sweatshirt", "image": "long_sleeves_images/image12.jpg", "url": "https://weidian.info/5muef"},
        {"name": "ERD Lou Reed Sweatshirt", "image": "long_sleeves_images/image13.avif", "url": "https://weidian.info/qz9st"},
        {"name": "Frank Ocean Sweatshirt", "image": "long_sleeves_images/image14.avif", "url": "https://weidian.info/e8xqq"},
        {"name": "Gallery Dept Hollywood Sweatshirt", "image": "long_sleeves_images/image15.jpg", "url": "https://weidian.info/ntsa4"},

        {"name": "Golf Crewnecks", "image": "long_sleeves_images/image16.avif", "url": "https://weidian.info/9d35m"},
        {"name": "Gallery Dept Washed Sweatshirt", "image": "long_sleeves_images/image17.avif", "url": "https://weidian.info/72cp3"},
        {"name": "Brad Pitt Sweatshirt", "image": "long_sleeves_images/image18.jpg", "url": "https://weidian.info/xtkzr"},
        {"name": "Kapital Bone Sweatshirt", "image": "long_sleeves_images/image19.avif", "url": "https://weidian.info/c49f3"},
        {"name": "LV Numbers Jacquard Sweatshirt", "image": "long_sleeves_images/image20.avif", "url": "https://weidian.info/xeyw4"},

        {"name": "Mastermind Crewneck", "image": "long_sleeves_images/image21.jpg", "url": "https://weidian.info/2bp8x"},
        {"name": "Cactus Plant X Nike Sweatshirt", "image": "long_sleeves_images/image22.jpg", "url": "https://weidian.info/mkevz"},
        {"name": "Nike Sweatshirt", "image": "long_sleeves_images/image23.jpg", "url": "https://weidian.info/8zt7r"},
        {"name": "Maison Margiela Knit Sweatshirt", "image": "long_sleeves_images/image24.jpg", "url": "https://weidian.info/zzrj7"},
        {"name": "Stussy X Nike Sweatshirt", "image": "long_sleeves_images/image25.jpg", "url": "https://weidian.info/acdtw"},

        {"name": "Knitted Female Graffiti Crewneck", "image": "long_sleeves_images/image26.avif", "url": "https://weidian.info/5a9sj"},
        {"name": "RafSimons Knitted Sweatshirt", "image": "long_sleeves_images/image27.avif", "url": "https://weidian.info/qy5rz"},
        {"name": "Pool X Stussy Knitted Sweatshirt", "image": "long_sleeves_images/image28.avif", "url": "https://weidian.info/4hz7s"},
        {"name": "SickSidSweatshirt", "image": "long_sleeves_images/image29.avif", "url": "https://weidian.info/umgu6"},
        {"name": "Undercover x Evangelion Crewneck", "image": "long_sleeves_images/image30.avif", "url": "https://weidian.info/mxtrf"},
    ]
    return render(request, 'core/long_sleeves.html', {'product_data': product_data})

def pants(request):
    product_data = [
        {"name": "SPIDER Sweatpants", "image": "pants_images/image1.jpg", "url": "https://weidian.info/5rc2g"},
        {"name": "Nike Sweatpants", "image": "pants_images/image2.jpg", "url": "https://weidian.info/rwgav"},
        {"name": "Demin Tear Sweatpants", "image": "pants_images/image3.webp", "url": "https://weidian.info/8rdya"},
        {"name": "Demin Tear Jeans", "image": "pants_images/image4.jpg", "url": "https://weidian.info/7p5xg"},
        {"name": "Carhartt Casual Pants", "image": "pants_images/image5.avif", "url": "https://weidian.info/ggmea"},


        {"name": "Minus Two Cargos", "image": "pants_images/image6.webp", "url": "https://weidian.info/p3xff"},
        {"name": "Jacov Pants", "image": "pants_images/image7.jpg", "url": "https://weidian.info/srgak"},
        {"name": "Vintage Bape Jeans", "image": "pants_images/image8.avif", "url": "https://weidian.info/673uj"},
        {"name": "Revenge Jeans", "image": "pants_images/image9.avif", "url": "https://weidian.info/wyfj7"},
        {"name": "Supreme X Burberry Denim Pants", "image": "pants_images/image10.jpg", "url": "https://weidian.info/2r8np"},


        {"name": "Supreme X Yankee Denim Pants", "image": "pants_images/image11.jpg", "url": "https://weidian.info/dtsfe"},
        {"name": "Ripped Flared Jeans", "image": "pants_images/image12.avif", "url": "https://weidian.info/zy2nn"},
        {"name": "Endless Jeans", "image": "pants_images/image13.jpg", "url": "https://weidian.info/cb2fb"},
        {"name": "Balenciaga Flared Jeans", "image": "pants_images/image14.avif", "url": "https://weidian.info/zecnr"},
        {"name": "Palm Angel Pants", "image": "pants_images/image15.avif", "url": "https://weidian.info/2wgc4"},

        {"name": "Gallery Dept Pants", "image": "pants_images/image16.jpg", "url": "https://weidian.info/4qbv6"},
        {"name": "CPFM Pants", "image": "pants_images/image17.jpg", "url": "https://weidian.info/89dyd"},
        {"name": "Nike Tech FLeece Pants", "image": "pants_images/image18.webp", "url": "https://weidian.info/ekcxy"},
        {"name": "Camo Pants", "image": "pants_images/image19.avif", "url": "https://weidian.info/d755w"},
        {"name": "Purple Jeans", "image": "pants_images/image20.jpg", "url": "https://weidian.info/vzahv"},




    ]
    return render(request, 'core/pants.html', {'product_data': product_data})

def shorts(request):
    product_data = [
        {"name": "EE Shorts", "image": "shorts_images/image1.jpg", "url": "https://weidian.info/gn33s"},
        {"name": "ASRV Shorts", "image": "shorts_images/image2.avif", "url": "https://weidian.info/zan97"},
        {"name": "KINETIC Shorts", "image": "shorts_images/image3.jpg", "url": "https://weidian.info/5qdnu"},
        {"name": "NORTH FACE Shorts", "image": "shorts_images/image4.jpg", "url": "https://weidian.com/item.html?itemID=4397132802"},
        {"name": "RHUDE Shorts", "image": "shorts_images/image5.png", "url": "https://weidian.info/zekj2"},

        {"name": "Jordan Shorts", "image": "shorts_images/image6.jpg", "url": "https://weidian.info/jhxyf"},
        {"name": "Nike NBA Shorts", "image": "shorts_images/image7.jpg", "url": "https://weidian.info/vp9sc"},
        {"name": "Billionaire Boys Club Shorts", "image": "shorts_images/image8.png", "url": "https://weidian.info/5zcuw"},
        {"name": "Represent Shorts", "image": "shorts_images/image9.avif", "url": "https://weidian.info/2hjez"},
        {"name": "Chrome Heart Shorts", "image": "shorts_images/image10.png", "url": "https://weidian.info/68rkv"},

        {"name": "Bape Shorts", "image": "shorts_images/image11.jpg", "url": "https://weidian.info/t4sqp"},
        {"name": "Revenge Shorts", "image": "shorts_images/image12.avif", "url": "https://weidian.info/wrxuh"},
        {"name": "FOG ESSENTIALS Shorts", "image": "shorts_images/image13.avif", "url": "https://weidian.info/sbw7j"},
        {"name": "Travis Scot Cactus Jack Shorts", "image": "shorts_images/image14.jpg", "url": "https://weidian.info/7uyvq"},
        {"name": "Corteiz Shorts", "image": "shorts_images/image15.jpg", "url": "https://weidian.info/4cjfg"},


        {"name": "Fendi Shorts", "image": "shorts_images/image16.webp", "url": "https://weidian.info/k5svp"},
        {"name": "Raptors Shorts", "image": "shorts_images/image17.png", "url": "https://weidian.info/yeaeg"},
        {"name": "Stussy Shorts", "image": "shorts_images/image18.png", "url": "https://weidian.info/err3d"},
        {"name": "Minus Two Cargo Shorts", "image": "shorts_images/image19.jpg", "url": "https://weidian.info/vcpy7"},
        {"name": "Trapstar Shorts", "image": "shorts_images/image20.png", "url": "https://weidian.info/9rt3x"},

    ]
    return render(request, 'core/shorts.html', {'product_data': product_data})


    
def shoes(request):
    product_data = [
        {"name": "Travis Scot 1 Low", "image": "shoes_images/image1.jpg", "url": "https://weidian.info/9fqvj"},
        {"name": "LV Slides", "image": "shoes_images/image2.jpg", "url": "https://weidian.info/763k7"},
        {"name": "LV Trainers", "image": "shoes_images/image3.jpg", "url": "https://weidian.info/wytnn"},
        {"name": "NB 550", "image": "shoes_images/image4.jpg", "url": "https://weidian.info/8vsyu"},
        {"name": "Kobe 4 / 5 / 6 / 8", "image": "shoes_images/image5.webp", "url": "https://weidian.info/z6zek"},

        {"name": "SB Lobster Dunk Lows", "image": "shoes_images/image6.jpg", "url": "https://weidian.info/pkart"},
        {"name": "SB Dunk Lows", "image": "shoes_images/image7.jpg", "url": "https://weidian.info/2dt5h"},
        {"name": "LV X SB Dunk Lows", "image": "shoes_images/image8.png", "url": "https://weidian.info/pqxrx"},
        {"name": "EBAY X SB Dunk Lows", "image": "shoes_images/image9.jpg", "url": "https://weidian.info/8mevp"},
        {"name": "PARIS X SB DUNK Lows", "image": "shoes_images/image10.jpg", "url": "https://weidian.info/2t7gq"},

        {"name": "Rare AJ1", "image": "shoes_images/image11.jpg", "url": "https://weidian.info/a65xs"},
        {"name": "AJ1 Stage Haze", "image": "shoes_images/image12.jpg", "url": "https://weidian.info/h32v6"},
        {"name": "30+ AJ1 Colorways", "image": "shoes_images/image13.jpg", "url": "https://weidian.info/74k8s"},
        {"name": "Off White AJ1 Blue High ", "image": "shoes_images/image14.jpg", "url": "https://weidian.info/3wek9"},
        {"name": "Off White AJ1 Chicago High ", "image": "shoes_images/image15.jpg", "url": "https://weidian.info/pd3nh"},

        {"name": "20+ AJ4", "image": "shoes_images/image16.webp", "url": "https://weidian.info/vhc7n"},
        {"name": "Levi X AJ4", "image": "shoes_images/image17.jpg", "url": "https://weidian.info/semn9"},
        {"name": "More AJ4", "image": "shoes_images/image18.jpg", "url": "https://weidian.info/248hz"},
        {"name": "AJ1 Low Nothing But New  ", "image": "shoes_images/image19.jpg", "url": "https://weidian.info/jabmv"},
        {"name": "AJ1 Low Lakers Blue Yellow", "image": "shoes_images/image20.jpg", "url": "https://weidian.info/yknr9"},
    ]
    return render(request, 'core/shoes.html', {'product_data': product_data})

def accessories(request):
    product_data = [
        {"name": "Carti Phonecase", "image": "accessories_images/image1.webp", "url": "https://weidian.info/67jxr"},
        {"name": "Chrome Heart Bracelet", "image": "accessories_images/image2.avif", "url": "https://weidian.info/ggfr5"},
        {"name": "Chrome Heart Necklace", "image": "accessories_images/image3.jpg", "url": "https://weidian.info/ewzd3"},
        {"name": "Carhartt Hats", "image": "accessories_images/image4.jpg", "url": "https://weidian.info/5wfw6"},
        {"name": "Nike Socks", "image": "accessories_images/image5.jpg", "url": "https://weidian.info/ng4xe"},

        {"name": "Chrome Heart Hats", "image": "accessories_images/image6.avif", "url": "https://weidian.info/8jezc"},
        {"name": "Corteiz Hats", "image": "accessories_images/image7.avif", "url": "https://weidian.info/yurfs"},
        {"name": "Gallery Dept Hats", "image": "accessories_images/image8.jpg", "url": "https://weidian.info/48hn6"},
        {"name": "Moncler Beanies", "image": "accessories_images/image9.jpg", "url": "https://weidian.info/gv2f8"},
        {"name": "Stone Island Beanies", "image": "accessories_images/image10.jpg", "url": "https://weidian.info/ed2n4"},


        {"name": "Minus Two Beanies", "image": "accessories_images/image11.jpg", "url": "https://weidian.info/qp3d8"},
        {"name": "Curly Stussy Beanie", "image": "accessories_images/image12.png", "url": "https://weidian.info/mbckx"},
        {"name": "Star Beanie", "image": "accessories_images/image13.avif", "url": "https://weidian.info/ew8zk"},
        {"name": "Bear Beanie", "image": "accessories_images/image14.png", "url": "https://weidian.info/3eqjw"},
        {"name": "Graphic Beanies", "image": "accessories_images/image15.avif", "url": "https://weidian.info/7mcgb"},

        {"name": "Chrome Heart Beanies", "image": "accessories_images/image16.avif", "url": "https://weidian.info/9w68z"},
        {"name": "Prada Hats", "image": "accessories_images/image17.jpg", "url": "https://weidian.info/bh4tj"},
        {"name": "Bape Beanies", "image": "accessories_images/image18.jpg", "url": "https://weidian.info/cnqfq"},
        {"name": "Lv Scarf +  Beanies", "image": "accessories_images/image19.jpg", "url": "https://weidian.info/ecpzf"},
        {"name": "Durags", "image": "accessories_images/image20.jpg", "url": "https://weidian.info/qwgdu"},
    ]
    return render(request, 'core/accessories.html', {'product_data': product_data})


def sweaters(request):
    product_data = [
        {"name": "SPIDER Hoodie", "image": "sweaters_images/image1.webp", "url": "https://weidian.info/5rc2g"},
        {"name": "FOG Essentials Hoodie", "image": "sweaters_images/image2.webp", "url": "https://weidian.info/7vt3n"},
        {"name": "4TUNE Full Zipup", "image": "sweaters_images/image3.jpg", "url": "https://weidian.info/xehzb"},
        {"name": "Travis Scot Cactus Jack Zipup", "image": "sweaters_images/image4.jpg", "url": "https://weidian.info/vagp4"},
        {"name": "Polo Ralph Lauren Zipup", "image": "sweaters_images/image5.jpg", "url": "https://weidian.info/pr4fg"},

        {"name": "Chrome Heart Zipper/Hoodie", "image": "sweaters_images/image6.avif", "url": "https://weidian.info/dyktk"},
        {"name": "Saint Michael Graffiti Hoodie", "image": "sweaters_images/image7.avif", "url": "https://weidian.info/4vx76"},
        {"name": "Playboi Carti Hoodie", "image": "sweaters_images/image8.avif", "url": "https://weidian.info/b4x9a"},
        {"name": "Ye Must be Born Again Hoodie", "image": "sweaters_images/image9.jpg", "url": "https://weidian.info/dwhqb"},
        {"name": "123 FOG Hoodie", "image": "sweaters_images/image10.jpg", "url": "https://weidian.info/23wdy"},

        {"name": "Cuwu Amikaki Graphic printed hoodie", "image": "sweaters_images/image11.avif", "url": "https://weidian.info/943th"},
        {"name": "Palm Angels Web Hoodie", "image": "sweaters_images/image12.avif", "url": "https://weidian.info/khszt"},
        {"name": "Yeezy Gap Hoodie", "image": "sweaters_images/image13.avif", "url": "https://weidian.info/b2d58"},
        {"name": "Travis Scot MCD Hoodie", "image": "sweaters_images/image14.jpg", "url": "https://weidian.info/bnm78"},
        {"name": "Stussy 8Ball Hoodie", "image": "sweaters_images/image15.avif", "url": "https://weidian.info/ca7um"},

        {"name": "Trapstar X Dave hoodie", "image": "sweaters_images/image16.avif", "url": "https://weidian.info/mg4qr"},
        {"name": "Vetements Hoodie", "image": "sweaters_images/image17.webp", "url": "https://weidian.info/7h49y"},
        {"name": "Off White Hoodie", "image": "sweaters_images/image18.jpg", "url": "https://weidian.info/3xpc5"},
        {"name": "Y2K Titanic Hoodie", "image": "sweaters_images/image19.png", "url": "https://weidian.info/p4uv2"},
        {"name": "Vintage Sicko Hoodie", "image": "sweaters_images/image20.avif", "url": "https://weidian.info/xdhf4"},

        {"name": "Saint hoodie", "image": "sweaters_images/image21.avif", "url": "https://weidian.info/6hq5c"},
        {"name": "Mini Nike Swoosh Hoodie", "image": "sweaters_images/image22.jpg", "url": "https://weidian.info/ncgkg"},
        {"name": "Bape Full Head Zipup", "image": "sweaters_images/image23.jpg", "url": "https://weidian.info/p7c8d"},
        {"name": "Batman Bape Full Head Zipup", "image": "sweaters_images/image24.avif", "url": "https://weidian.info/x8rwq"},
        {"name": "Star Bape Full Head Zipup", "image": "sweaters_images/image25.avif", "url": "https://weidian.info/kbrj2"},

        {"name": "Travis Scot X Kaws Zipup", "image": "sweaters_images/image26.avif", "url": "https://weidian.info/4mp6a"},
        {"name": "Rick Owns Full Zip", "image": "sweaters_images/image27.avif", "url": "https://weidian.info/guzjb"},
        {"name": "All Shadows Zipup", "image": "sweaters_images/image28.jpg", "url": "https://weidian.info/dpjf4"},
        {"name": "Mastermind Travis Scot Zipup", "image": "sweaters_images/image29.avif", "url": "https://weidian.info/vagp4"},
        {"name": "Burberry Zipup", "image": "sweaters_images/image30.jpg", "url": "https://weidian.info/c7wr9"},

        {"name": "Stussy Zipup", "image": "sweaters_images/image31.jpg", "url": "https://weidian.info/stu6q"},
        {"name": "CP Zipup", "image": "sweaters_images/image32.jpg", "url": "https://weidian.info/u2phe"},
        {"name": "High Zipup Blank", "image": "sweaters_images/image33.avif", "url": "https://weidian.info/by8hg"},
        {"name": "Wrld Krisis Full Head Zipup", "image": "sweaters_images/image34.jpg", "url": "https://weidian.info/xqa5r"},
        {"name": "Ver Blee Full Head Zipup", "image": "sweaters_images/image35.avif", "url": "https://weidian.info/bf2w3"},
    ]
    return render(request, 'core/sweaters.html', {'product_data': product_data})


def jackets(request):
    product_data = [
        {"name": " Canada Goose Men/Women Winter Gilet Vest", "image": "jackets_images/image1.webp", "url": "https://weidian.info/2cpma"},
        {"name": "THE NORTH FACE 1996 Retro Nuptse Puffer Jacket", "image": "jackets_images/image2.jpg", "url": "https://weidian.info/jgtyn"},
        {"name": "Nike X Tiffany Embroidered Jacket", "image": "jackets_images/image3.jpg", "url": "https://weidian.info/7sx9s"},
        {"name": "Trapster Jacket", "image": "jackets_images/image4.webp", "url": "https://weidian.info/x7c6h"},
        {"name": "Canada Goose Wyndham Parka", "image": "jackets_images/image5.webp", "url": "https://weidian.info/6zq6f"},


        {"name": "Prada Puffer Jacket", "image": "jackets_images/image6.jpg", "url": "https://weidian.info/39b59"},
        {"name": "Rick Own Puffer Jacket", "image": "jackets_images/image7.jpg", "url": "https://weidian.info/6wqs6"},
        {"name": "Moncler Maya Jacket", "image": "jackets_images/image8.webp", "url": "https://weidian.info/pn9gh"},
        {"name": "THE NORTH FACE 1996 Retro Nuptse Jacket", "image": "jackets_images/image9.jpg", "url": "https://weidian.info/rk49d"},
        {"name": "Drake Nike Jacket", "image": "jackets_images/image10.jpg", "url": "https://weidian.info/5h79d"},

        {"name": "Kapital Puffer Vest", "image": "jackets_images/image11.avif", "url": "https://weidian.info/z2y6z"},
        {"name": "LV Varsity Jacket", "image": "jackets_images/image12.jpg", "url": "https://weidian.info/7kbgk"},
        {"name": "Spider X Moncler Maya Jacket", "image": "jackets_images/image13.avif", "url": "https://weidian.info/k72p5"},
        {"name": " Balenciaga X Astronaut Jacket", "image": "jackets_images/image14.avif", "url": "https://weidian.info/qe5kw"},
        {"name": "Balenciaga Cropped Fur Jacket", "image": "jackets_images/image15.jpg", "url": "https://weidian.info/5dqqa"},

        {"name": "10+ Human Made Jackets", "image": "jackets_images/image16.jpg", "url": "https://weidian.info/5qw4d"},
        {"name": "Yeezy X Gap Jacket", "image": "jackets_images/image17.avif", "url": "https://weidian.info/ftmya"},
        {"name": "Balenciaga Track Jacket", "image": "jackets_images/image18.jpg", "url": "https://weidian.info/jdqx2"},
        {"name": "Bottega Veneta Cropped Black Jacket", "image": "jackets_images/image19.jpg", "url": "https://weidian.info/2t49b"},
        {"name": "Bape Jacket", "image": "jackets_images/image20.avif", "url": "https://weidian.info/wbz6y"},

        {"name": "Canada Goose Expedition 4460 Jacket", "image": "jackets_images/image21.jpg", "url": "https://weidian.info/uysk9"},
        {"name": "Chrome Heart Jacket", "image": "jackets_images/image22.jpg", "url": "https://weidian.info/n7nas"},
        {"name": "CPFM Weed Jacket", "image": "jackets_images/image23.avif", "url": "https://weidian.info/sxr5d"},
        {"name": "Craig Green Jacket", "image": "jackets_images/image24.avif", "url": "https://weidian.info/kdnee"},
        {"name": "House of Errors Vest", "image": "jackets_images/image25.avif", "url": "https://weidian.info/czwez"},

        {"name": "Kapital Vest", "image": "jackets_images/image26.avif", "url": "https://weidian.info/nqp3m"},
        {"name": "Kapital Varsity Jacket", "image": "jackets_images/image27.avif", "url": "https://weidian.info/vxtjj"},
        {"name": "Kusikohc Jacket", "image": "jackets_images/image28.avif", "url": "https://weidian.info/bwq9j"},
        {"name": "MKSZY Multi Cargo Jacket", "image": "jackets_images/image29.avif", "url": "https://weidian.info/s64g9"},
        {"name": "Needles Jacket", "image": "jackets_images/image30.avif", "url": "https://weidian.info/2m3yt"},
        
        {"name": "Off White Laboratory of Fun Varsity Jacket", "image": "jackets_images/image31.jpg", "url": "https://weidian.info/n8849"},
        {"name": "PAF Cross-body Zip up Fleece", "image": "jackets_images/image32.avif", "url": "https://weidian.info/b6emb"},
        {"name": "Palm Angels x Moncler Maya 70 Jacket", "image": "jackets_images/image33.avif", "url": "https://weidian.info/v3j62"},
        {"name": "Rick Owens x Moncler Puffer", "image": "jackets_images/image34.jpg", "url": "https://weidian.info/2dfvb"},
        {"name": "Stussy Air Force Jacket", "image": "jackets_images/image35.avif", "url": "https://weidian.info/swqa6"},
        ]
    return render(request, 'core/jackets.html', {'product_data': product_data})


def tracksuits(request):
    product_data = [
        {"name": "Drake Nocta Tracksuit ", "image": "tracksuits_images/image1.jpg", "url": "https://weidian.info/pfr6u"},
        {"name": "Corteiz Tracksuit ", "image": "tracksuits_images/image2.webp", "url": "https://weidian.info/bvdx9"},
        {"name": "Football Tracksuit ", "image": "tracksuits_images/image3.jpg", "url": "https://weidian.info/nv4dp"},
        {"name": "SPIDER Tracksuit ", "image": "tracksuits_images/image4.jpg", "url": "https://weidian.info/fh3ez"},
        {"name": "EE Tracksuit ", "image": "tracksuits_images/image5.avif", "url": "https://weidian.info/rw6h5"},

        {"name": "Central Cee X Corteiz Tracksuit ", "image": "tracksuits_images/image6.avif", "url": "https://weidian.info/hegfm"},
        {"name": "Juicy Tracksuit ", "image": "tracksuits_images/image7.jpg", "url": "https://weidian.info/6whe6"},
        {"name": "Palm Angel Tracksuit ", "image": "tracksuits_images/image8.webp", "url": "https://weidian.info/2bnwy"},
        {"name": "30+ Trapstar Tracksuit ", "image": "tracksuits_images/image9.jpg", "url": "https://weidian.info/f6e2a"},
        {"name": "4+ Syna Tracksuit ", "image": "tracksuits_images/image10.webp", "url": "https://weidian.info/q2335"},

    ]
    return render(request, 'core/tracksuits.html', {'product_data': product_data})


def budget(request):
    product_data = [
        {"name": "NOFS Tracksuit ", "image": "budget_images/image1.jpg", "url": "https://weidian.info/58s4h"},
        {"name": "Stussy Sweater ", "image": "budget_images/image2.jpg", "url": "https://weidian.info/mh3jj"},
        {"name": "LV Belt ", "image": "budget_images/image3.jpg", "url": "https://weidian.info/mp8mt"},
        {"name": "Hermes Belt ", "image": "budget_images/image4.jpg", "url": "https://weidian.info/gvjmm"},
        {"name": "LV Trainers ", "image": "budget_images/image5.jpg", "url": "https://weidian.info/fx8j3"},

        {"name": "Iced Out Cuban Bracelet ", "image": "budget_images/image6.avif", "url": "https://weidian.info/mqgpa"},
        {"name": "Cuban Bracelet ", "image": "budget_images/image7.avif", "url": "https://weidian.info/xemsw"},
        {"name": "Rolex Watch ", "image": "budget_images/image8.jpg", "url": "https://weidian.info/m532h"},
        {"name": "Sterling Sliver Bead Bracelet ", "image": "budget_images/image9.avif", "url": "https://weidian.info/vzbh3"},
        {"name": "Prada Sunglasses ", "image": "budget_images/image10.jpg", "url": "https://weidian.info/e2k34"},

        {"name": "ASSC Shirts", "image": "budget_images/image11.jpg", "url": "https://weidian.info/qxkms"},
        {"name": "Unbranded Star Full Head Zipper ", "image": "budget_images/image12.jpg", "url": "https://weidian.info/6vu64"},
        {"name": "Jordan 4s", "image": "budget_images/image13.jpg", "url": "https://weidian.info/3hygz"},
        {"name": "Airpod Maxes", "image": "budget_images/image14.jpg", "url": "https://weidian.info/u7scw"},
        {"name": "More Stussy Hoodies", "image": "budget_images/image15.jpg", "url": "https://weidian.info/pbksh"},

        {"name": "Kayne West Heartbreak Shirt", "image": "budget_images/image21.jpg", "url": "https://weidian.info/3xaa2"},
        {"name": "Justin Bieber Colorblind Shirt", "image": "budget_images/image22.avif", "url": "https://weidian.info/qh23b"},
        {"name": "Kayne West I Feel Like Pablo Shirt", "image": "budget_images/image23.avif", "url": "https://weidian.info/tg8jv"},
        {"name": "Kayne West No More Parties In LA Shirt", "image": "budget_images/image24.jpg", "url": "https://weidian.info/fzvjd"},
        {"name": "Palm Angel Shirt", "image": "budget_images/image25.jpg", "url": "https://weidian.info/dksmr"},


    ]
    return render(request, 'core/budget.html', {'product_data': product_data})