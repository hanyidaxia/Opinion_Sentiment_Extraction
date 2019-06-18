#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class find_product_name:
    import selenium
    import time
    from selenium import webdriver
    from bs4 import BeautifulSoup as BS
    from selenium.webdriver.chrome.options import Options
    import sys
    import pickle
    import pandas as pd
    from collections import Counter
    import numpy as np
    
    
    def find_all_products(file_name):
        # this step is get the product links from the previous file  
        with open(file_name, "r") as x:
            all_product = x.read().splitlines()
            product_name = []
            for i in all_product:
                i = i.strip('\n')
                all_set = set(all_product)
                all_product = list(all_set)
            for j in all_product:
                j = j.split('/')[3]
                product_name.append(j)
            name_all_set = set(product_name)
            name_all_product = list(name_all_set)
        return name_all_product
        
    def got_product_name(file_name):
        # this function is looking for the descriptions of each unique product
        with open (file_name, 'w', encoding='utf-8') as f:
            item = 0
            for name in all_product:
                browser = webdriver.Firefox()
                item += 1
                print(name)
                print(item)
                product_name = name.split('/')[3]
                browser_name = "https://www.finishline.com" + name
                browser.get(browser_name)
                time.sleep(30)
                bs_obj = BS(browser.page_source.encode('utf-8', 'ignore'), "html.parser")
                description = bs_obj.findAll("div", {"class":"column small-12"})  
                for i in description:
                #       print(i.find_all("li"))
        #                 product_name_description[product_name] = [i.find_all("li")]
                    details = "".join(i.stripped_strings)
                    f.write(product_name + "===" + repr(details))
                    f.write('\n')
                    f.write("*****************************************************************")
                    f.flush()
                    browser.quit()
                
        return

