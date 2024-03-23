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
        # Add or modify product data as needed
        
    ]
    return render(request, 'core/short_sleeves.html', {'product_data': product_data})

def long_sleeves(request):
    product_data = [
        {"name": "Curly Stussy Sweatshirt", "image": "long_sleeves_images/image1.jpg", "url": "https://weidian.info/2jccs"},
        {"name": "Nike Sweatshirt", "image": "long_sleeves_images/image2.jpg", "url": "https://weidian.info/ymtuz"},
        {"name": "Chrome Heart Sweatshirt", "image": "long_sleeves_images/image3.jpg", "url": "https://weidian.info/vbbry"},
        {"name": "Moncler Sweatshirt", "image": "long_sleeves_images/image4.jpg", "url": "https://weidian.info/md57h"},
        {"name": "Carhartt Half Zip", "image": "long_sleeves_images/image5.jpg", "url": "https://weidian.info/s32q5"},
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
    ]
    return render(request, 'core/jackets.html', {'product_data': product_data})


def tracksuits(request):
    product_data = [
        {"name": "Drake Nocta Tracksuit ", "image": "tracksuits_images/image1.jpg", "url": "https://weidian.info/pfr6u"},
        {"name": "Corteiz Tracksuit ", "image": "tracksuits_images/image2.webp", "url": "https://weidian.info/bvdx9"},
        {"name": "Football Tracksuit ", "image": "tracksuits_images/image3.jpg", "url": "https://weidian.info/nv4dp"},
        {"name": "SPIDER Tracksuit ", "image": "tracksuits_images/image4.jpg", "url": "https://weidian.info/fh3ez"},
        {"name": "EE Tracksuit ", "image": "tracksuits_images/image5.avif", "url": "https://weidian.info/rw6h5"},
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