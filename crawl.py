import os
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs
import shutil 
import psycopg2
import pyshorteners as sh
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

# Create your views here.

# conn = psycopg2.connect(
#     host="localhost",
#     database="test",
#     user="saikat1",
#     password="1234")
# cursor = conn.cursor()
# cursor.execute("""Insert Into mobiles_product_details (company_name, price, photo, ram, rom, expandable, display, camera, battery, processor, link, warranty, star, rating, review, in_the_box, product_type_id) values('ddgdgs', 9999, 'None', 4, 32, 512, 6.5, '30 mg pxl', 5000, 'mediatech', 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page=1', '1 years', 4.3, 3200, 170, 'all items', 1)""")
# conn.commit()
# cursor.close()
# conn.close()

page = requests.get("https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page=1")

# driver = webdriver.Firefox()
# driver.get("https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page=1")
# identify elements with tagname <a>
lnks=page.find_elements_by_tag_name("a")
# traverse list
for lnk in lnks:
   # get_attribute() to get all href
   print(lnk.get_attribute('href'))
# driver.quit()




# k=1
# for k in range(10):
#     print('https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page='+str(k))
#     k+=1
# link = 'https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree'
# s = sh.Shortener()
# print(s.tinyurl.short(link))

# soup = bs(page.content, "html.parser")
# i = 0
# k = 0
# Name = []
# Ram = []
# i = 0
# k = 0
# Name = []
# Ram = []
# Image = []
# Price = []
# path  = []
url = soup.find_all("div" , attrs={"class":"_4rR01T"})
# Name = soup.find_all("div" , attrs={"class":"_4rR01T"})
# Price = soup.find_all("div" , attrs={"class":"_30jeq3 _1_WHN1"})
# Ram = soup.find_all("li", attrs={"class":"rgWa7D"})
# Image = soup.find_all("img", attrs={"class":"_396cs4 _3exPp9"})
# Rating = soup.find_all("div" , attrs={"class":"_3LWZlK"})
# Review = soup.find_all("span" , attrs={"class":"_2_R_DZ"})

# for k in range(len(Name)):

#     filename = Name[k].get_text().replace(' ', '_').replace('/', '').replace(',', '') + '.jpg'
#     image_url = Image[k].get("src")
#     # Open the url image, set stream to True, this will return the stream content.
#     r = requests.get(image_url, stream = True)

#     # Check if the image was retrieved successfully
    
#     # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
#     r.raw.decode_content = True
    
    # Open a local file with wb ( write binary ) permission.

    # dest = os.path.join(BASE_DIR, 'crawler/img/') + filename
    
    # print(Rating[k].get_text())
    # print(Review[k].get_text())
    # print(filename)
    # print(Price[k].get_text().replace("₹",'').replace(",",'').strip())
    # print(Ram[i].get_text())
    # print(Ram[i+1].get_text())
    # print(Ram[i+2].get_text())
    # print(Ram[i+3].get_text())
    # print(Ram[i+4].get_text())


    # with open(dest,'wb') as f:
    #     shutil.copyfileobj(r.raw,  f)
        
    # p = Product_details(product_type = pt.objects.get(id=1),
    #                     company_name = Name[k].get_text(), 
    #                     photo = filename, 
    #                     description = Name[k].get_text(), 
    #                     price = Price[k].get_text().replace("₹",'').replace(",",'').strip(),
    #                     memory = Ram[i].get_text(), 
    #                     display = Ram[i+1].get_text(),
    #                     camera = Ram[i+2].get_text(), 
    #                     battery = Ram[i+3].get_text(), 
    #                     processor = Ram[i+4].get_text())

    # i = i+6
    # p.save()


    

    



