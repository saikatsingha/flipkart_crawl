import os
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs
import shutil 
import psycopg2
import pyshorteners as sh
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager



page = requests.get("https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page=1")
p=1
while(True):
   if p > 30:
      break
   
   driver = webdriver.Firefox()
   driver.get("https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page="+str(p))
   links = [my_elem.get_attribute("href") for my_elem in driver.find_elements_by_css_selector("a._1fQZEK")]
   driver.quit()
   for lnk in links :
      page = requests.get(lnk)
      soup = bs(page.content, "html.parser")
      Name = soup.find("span" , attrs={"class":"B_NuCI"})
      Price = soup.find("div" , attrs={"class":"_30jeq3 _16Jk6d"})
      Details_Data = soup.find_all("li", attrs={"class":"_21lJbe"})
      Details_Data_Type = soup.find_all("td", attrs={"class":"_1hKmbr"})
      Image = soup.find("img", attrs={"class":"_396cs4"})
      Star = soup.find("div" , attrs={"class":"_3LWZlK"})
      Rating = soup.find("span" , attrs={"class":"_2_R_DZ"})

      image_url = Image.get("src")
      # Open the url image, set stream to True, this will return the stream content.
      r = requests.get(image_url, stream = True)

      # Check if the image was retrieved successfully
      
      # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
      r.raw.decode_content = True
      
      # Open a local file with wb ( write binary ) permission.
      image_name = Name.get_text().replace(' ', '_').replace('/', '').replace(',', '').replace('  ', '_') + '.jpg'
      with open('image/'+ image_name,'wb') as f:
         shutil.copyfileobj(r.raw,  f)

      k=0

      name = Name.get_text().replace(")",'').replace("(",'').replace(",",' ')
      # print(Price.get_text().replace("₹",'').strip())
      for k in range(len(Details_Data_Type)):
         if Details_Data_Type[k].get_text() == 'In The Box':
            print(Details_Data[k].get_text())
         if Details_Data_Type[k].get_text() == 'Display Size':
            print(Details_Data[k].get_text())
         if Details_Data_Type[k].get_text() == 'Processor Type':
            print(Details_Data[k].get_text())
         if Details_Data_Type[k].get_text() == 'Processor Core':
            print(Details_Data[k].get_text())
         if Details_Data_Type[k].get_text() == 'Internal Storage':
            print(Details_Data[k].get_text().replace(' ', '').replace('GB', '').strip())
         if Details_Data_Type[k].get_text() == 'RAM':
            print(Details_Data[k].get_text().replace(' ', '').replace('GB', '').strip())
         if Details_Data_Type[k].get_text() == 'Expandable Storage':
            print(Details_Data[k].get_text().replace(' ', '').replace('GB', '').strip())
            expandable_storage = Details_Data[k].get_text()
         if Details_Data_Type[k].get_text() == 'Primary Camera':
            print(Details_Data[k].get_text())
         if Details_Data_Type[k].get_text() == 'Battery Capacity':
            print(Details_Data[k].get_text())
         
         k=k+1

      # print(Image.get_text())
      # print(Star.get_text())
      # print(Rating.get_text())
      # print(Image.get('src'))
      conn = psycopg2.connect(
      host="localhost",
      database="test",
      user="saikat1",
      password="1234")
            
      cursor = conn.cursor()
      cursor.execute("""Insert Into mobiles_product_details 
                     (company_name, price, photo, ram, rom, expandable, display, camera, battery, processor, 
                     link, warranty, star, rating, review, in_the_box, product_type_id) values
                     ("""+str(name)+""", 9999, 'None', 4, 32, 512, 6.5, '30 mg pxl', 5000, 'mediatech', 
                     'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page=1', '1 years', 
                     4.3, 3200, 170, 'all items', 1)""")
      # sql = "Insert Into mobiles_product_details (company_name, price, photo, ram, rom, expandable, display, camera, battery, processor, link, warranty, star, rating, review, in_the_box, product_type_id) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s,)"
      # val = ('hdhfhghsg', 9999, 'None', 4, 32, 512, 6.5, '30 mg pxl', 5000, 'mediatech','https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page=1', '1 years', 4.3, 3200, 170, 'all items', 1)
      # cursor.execute("""Insert Into mobiles_product_details (company_name, product_type_id) VALUES ('hhjhjh', 1)""")
      # val = (1'hdhfhghsg', )
      # cursor.execute(sql, val)
      conn.commit()
      cursor.close()
      conn.close()
   p=p+1

