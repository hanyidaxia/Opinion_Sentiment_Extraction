#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Reviews_crawling:
    import selenium
    import time
    from selenium import webdriver
    from bs4 import BeautifulSoup as BS
    from selenium.webdriver.chrome.options import Options
    import sys
    import pickle
    import pandas as pd
    from collections import Counter
    import string


# In[42]:


def get_unique_names(file_name):
    # this function is getting the unique product name from the existing file
    with open("J:/product_names.txt", "r") as x:
        product_name = []
        product_new_name = []
        all_product = x.read().splitlines()
        for i in all_product:
            i = i.strip('\n')
        all_set = set(all_product)
        all_product = list(all_set)
        for j in all_product:
            j = j.split('/')[3]
            product_name.append(i)
        for k in product_name:
            k = k.replace("-", " ")
            k = (string.capwords(k))
            k = k.replace(" ", "_")
            k = k.replace("Mens_", "")
            product_new_name.append(j)
            new_set = set(product_new_name)
            new_product = list(new_set)


# In[ ]:


def get_all_reviews(file_name):
    # this function is the scrawling 
    with open (file_name, 'a', encoding='utf-8') as f:
        description_list = []
        jishu = 0
        product_jishu = 0
        for name in new_product:
            for index in range(1, 1000):
                browser = webdriver.Firefox()
                browser_name = "https://finishline.ugc.bazaarvoice.com/9345/Men_char39_s_" + str(name) +                 "/reviews.djs?format=embeddedhtml&page="+ str(index) +"&scrollToTop=true"
                print(browser_name)
                browser.get(browser_name)
                time.sleep(0.99)
                bs_obj = BS(browser.page_source.encode('utf-8', 'ignore'), "html.parser")
                description = bs_obj.get_text()
                star_begin = description.split("BVRRReviewTextContainer")[0]
                description = description.split("BVRRReviewTextContainer")[1:]

                for content in description:
                    reviews_list = []
                    star_list = []
                    title_list = []
                    first_star_temp = star_begin.split("BVImgOrSprite")[4]
                    first_star = first_star_temp.split("reviewRating")[0]
                    if "BVRRValue BVRRReviewTitle" in star_begin:
                        first_title_temp = star_begin.split("BVRRReviewTitleContainer")[1]
                        first_title = first_title_temp.split("BVRRLabel BVRRReviewTitleSuffix")[0]

                    star_list.append(first_star)
                    if "BVImgOrSprite" in content:
                        star_temp = content.split("BVImgOrSprite")[1]
                        star = star_temp.split("reviewRating")[0]
                        star_list.append(star)

                    title_list.append(first_title)
                    if "BVRRValue BVRRReviewTitle" in content:
                        title_temp = content.split("BVRRValue BVRRReviewTitle")[1]
                        title = title_temp.split("BVRRLabel BVRRReviewTitleSuffix")[0]
                        title_list.append(title)

                    reviews_temp = content.split("BVRRReviewTextPrefix")[1]
                    reviews = reviews_temp.split("BVRRReviewTextSuffix")[0]
                    reviews_list.append(reviews)
    #                 print(reviews_list)

                    f.write(name + "+-++++++++++++++++++++++++++++++" +                             "".join(star_list) + "+++++++++++++++++++++++++++++++" +                             "".join(title_list) + "-+-+++++++++++++++++++++++++++++++++++++++" +                             "".join(reviews_list))
                    f.write('\n')
                    f.write("****************************************************************************************")
                    f.write('\n')
                    f.flush()
                jishu += 1
                browser.quit()
    #             print(reviews_list)
                description_list.append(reviews_list)
                print(jishu)
    #             print(description_list[jishu-1])
                if index >= 2 and description_list[jishu-2] == reviews_list:
                    break
            product_jishu += 1
            print(product_jishu)
            f.write('\n')
            f.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            f.write('\n')
            f.flush()

