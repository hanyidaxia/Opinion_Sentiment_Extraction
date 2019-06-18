#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class product_link_get:
    import selenium
    import time
    from selenium import webdriver
    from bs4 import BeautifulSoup as BS
    from selenium.webdriver.chrome.options import Options
    import sys
    import pickle
    import pandas as pd
    # accidently delete a section use esc+z to recover
    def page_ranges():
        casual_page_range = ["",
                  "#/store/men/shoes/casual/_/N-1q3xsyk?mnid=men_shoes_casual&No=40", 
                  "#/store/men/shoes/casual/_/N-1q3xsyk?mnid=men_shoes_casual&No=80", 
                  "#/store/men/shoes/casual/_/N-1q3xsyk?mnid=men_shoes_casual&No=120", 
                  "#/store/men/shoes/casual/_/N-1q3xsyk?mnid=men_shoes_casual&No=160", 
                  "#/store/men/shoes/casual/_/N-1q3xsyk?mnid=men_shoes_casual&No=200", 
                  "#/store/men/shoes/casual/_/N-1q3xsyk?mnid=men_shoes_casual&No=240", 
                  "#/store/men/shoes/casual/_/N-1q3xsyk?mnid=men_shoes_casual&No=280", 
                  "#/store/men/shoes/casual/_/N-1q3xsyk?mnid=men_shoes_casual&No=320", 
                  "#/store/men/shoes/casual/_/N-1q3xsyk?mnid=men_shoes_casual&No=360", 
                  "#/store/men/shoes/casual/_/N-1q3xsyk?mnid=men_shoes_casual&No=400", 
                  "#/store/men/shoes/casual/_/N-1q3xsyk?mnid=men_shoes_casual&No=440", 
                  "#/store/men/shoes/casual/_/N-1q3xsyk?mnid=men_shoes_casual&No=480", 
                  "#/store/men/shoes/casual/_/N-1q3xsyk?mnid=men_shoes_casual&No=520", 
                  "#/store/men/shoes/casual/_/N-1q3xsyk?mnid=men_shoes_casual&No=560", 
                  "#/store/men/shoes/casual/_/N-1q3xsyk?mnid=men_shoes_casual&No=600", 
                  "#/store/men/shoes/casual/_/N-1q3xsyk?mnid=men_shoes_casual&No=640", 
                  "#/store/men/shoes/casual/_/N-1q3xsyk?mnid=men_shoes_casual&No=680", 
                  "#/store/men/shoes/casual/_/N-1q3xsyk?mnid=men_shoes_casual&No=720"]
        running_page_range = ["",
                  "#/store/men/shoes/running/_/N-57cgax?mnid=men_shoes_running&No=40", 
                  "#/store/men/shoes/running/_/N-57cgax?mnid=men_shoes_running&No=80", 
                  "#/store/men/shoes/running/_/N-57cgax?mnid=men_shoes_running&No=120", 
                  "#/store/men/shoes/running/_/N-57cgax?mnid=men_shoes_running&No=160", 
                  "#/store/men/shoes/running/_/N-57cgax?mnid=men_shoes_running&No=200", 
                  "#/store/men/shoes/running/_/N-57cgax?mnid=men_shoes_running&No=240", 
                  "#/store/men/shoes/running/_/N-57cgax?mnid=men_shoes_running&No=280", 
                  "#/store/men/shoes/running/_/N-57cgax?mnid=men_shoes_running&No=320", 
                  "#/store/men/shoes/running/_/N-57cgax?mnid=men_shoes_running&No=360", 
                  "#/store/men/shoes/running/_/N-57cgax?mnid=men_shoes_running&No=400", 
                  "#/store/men/shoes/running/_/N-57cgax?mnid=men_shoes_running&No=440"]
        basketball_page_range = ["",
                  "#/store/men/shoes/basketball/_/N-3z3fil?mnid=men_shoes_basketball&No=40", 
                  "#/store/men/shoes/basketball/_/N-3z3fil?mnid=men_shoes_basketball&No=80", 
                  "#/store/men/shoes/basketball/_/N-3z3fil?mnid=men_shoes_basketball&No=120", 
                  "#/store/men/shoes/basketball/_/N-3z3fil?mnid=men_shoes_basketball&No=160", 
                  "#/store/men/shoes/basketball/_/N-3z3fil?mnid=men_shoes_basketball&No=200", 
                  "#/store/men/shoes/basketball/_/N-3z3fil?mnid=men_shoes_basketball&No=240"]
        training_page_range = ["",
                  "#/store/men/shoes/training-gym/_/N-kadepn?mnid=men_shoes_traininggym&No=40", 
                  "#/store/men/shoes/training-gym/_/N-kadepn?mnid=men_shoes_traininggym&No=80", 
                  "#/store/men/shoes/training-gym/_/N-kadepn?mnid=men_shoes_traininggym&No=120", 
                  "#/store/men/shoes/training-gym/_/N-kadepn?mnid=men_shoes_traininggym&No=160"]
        return casual_page_range, running_page_range, basketball_page_range, training_page_range
    
    def get_links (i):
        browser = webdriver.Firefox()
        browser_name = "https://www.finishline.com/store/men/shoes/casual/_/N-1q3xsyk?mnid=men_shoes_casual" + i
        print(browser_name)
        browser.get(browser_name)
        time.sleep(30)
        bs_obj = BS(browser.page_source, "html.parser")
        namelist = bs_obj.findAll("div", {"product-card"})
        links = []
        for g in namelist:
            links.append(g.find("a").attrs["href"])
        browser.quit()
        

    
    def get_running (i):
        browser = webdriver.Firefox()
        browser_name = "https://www.finishline.com/store/men/shoes/running/_/N-57cgax?mnid=men_shoes_running" + i
        print(browser_name)
        browser.get(str(browser_name))
        time.sleep(45)
        bs_obj = BS(browser.page_source, "html.parser")
        namelist = bs_obj.findAll("div", {"product-card"})
        links = []
        for g in namelist:
            links.append(g.find("a").attrs["href"])
        browser.quit()
        
    
    def get_basketball (i):
        browser = webdriver.Firefox()
        browser_name = "https://www.finishline.com/store/men/shoes/basketball/_/N-3z3fil?mnid=men_shoes_basketball" + i
        print(browser_name)
        browser.get(str(browser_name))
        time.sleep(45)
        bs_obj = BS(browser.page_source, "html.parser")
        namelist = bs_obj.findAll("div", {"product-card"})
        links = []
        for g in namelist:
            links.append(g.find("a").attrs["href"])
        browser.quit()
        
    
    def get_training (i):
        browser = webdriver.Firefox()
        browser_name = "https://www.finishline.com/store/men/shoes/training-gym/_/N-kadepn?mnid=men_shoes_traininggym" + i
        print(browser_name)
        browser.get(str(browser_name))
        time.sleep(30)
        bs_obj = BS(browser.page_source, "html.parser")
        namelist = bs_obj.findAll("div", {"product-card"})
        links = []
        for g in namelist:
            links.append(g.find("a").attrs["href"])
        browser.quit
        
       
    
    def get_boots ():
        browser = webdriver.Firefox()
        browser_name = "https://www.finishline.com/store/men/shoes/boots/_/N-1psj4ir?mnid=men_shoes_boots"
        print(browser_name)
        browser.get(str(browser_name))
        time.sleep(45)
        bs_obj = BS(browser.page_source, "html.parser")
        namelist = bs_obj.findAll("div", {"product-card"})
        links = []
        for g in namelist:
            links.append(g.find("a").attrs["href"])
        browser.quit()
       
        
    def get_all_links():
        all_links = []
        Running_links = []
        Basketball_links = []
        Training_links = []
        boots_links = []
        for i in casual_page_range:
            link = get_links(i)
            all_links.append(link)
        casual_links = all_links
        
        for i in running_page_range:
            link = get_running(i)
            Running_links.append(link)
        
        for i in basketball_page_range:
            link = get_running(i)
            Basketball_links.append(link)
            
        for i in training_page_range:
            link = get_training(i)
            Training_links.append(link)
            
        link = get_boots()
        boots_links.append(link)
        
        return casual_links, Running_links, Basketball_links, Training_links
    
    
    def writing_links(file_name):
        all_product = casual_links+ Running_links+ Basketball_links+ Training_links+ boots_links
        with open ('H:/Data/product_names.txt', 'w') as f:
            for i in all_product:
                for j in i:
                    f.write(j)
                    f.write('\n')

