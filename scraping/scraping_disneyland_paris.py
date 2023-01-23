#!/usr/bin/env python
# coding: utf-8

# In[48]:


# Import packages (Beaucoup non utilisé)

import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time
import csv
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
now = datetime.today()



# In[49]:


dict_url = {"Disneyland Paris" : "https://www.google.com/search?q=disneyland+paris&rlz=1C5CHFA_enFR968FR968&oq=disneyland+paris&aqs=chrome..69i57j69i60l3.5617j0j7&sourceid=chrome&ie=UTF-8#lrd=0x47e61d19ca7ae2bd:0x57faf8cb6310e660,1,,,",
            "Parc Walt Disney Studios":"https://www.google.com/search?q=Parc+Walt+Disney+Studios&rlz=1C5CHFA_enFR968FR968&hotel_occupancy=2&sxsrf=ALiCzsbW7vWOXi6oHKahg8IPVZiWVec4Ew%3A1672929842682&ei=MuK2Y_SlKY6okdUP0POw-AE&ved=0ahUKEwj0hoeo1bD8AhUOVKQEHdA5DB8Q4dUDCA8&uact=5&oq=Parc+Walt+Disney+Studios&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzILCC4QrwEQxwEQgAQyCggAEIAEEIcCEBQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoKCAAQRxDWBBCwA0oECEEYAEoECEYYAFDjBljjBmCQCGgDcAF4AIABjwGIAY8BkgEDMC4xmAEAoAECoAEByAEIwAEB&sclient=gws-wiz-serp#lrd=0x47e61d18cbe8514f:0xa483783469fa426,1,,,",
            "Disney's Hotel New York - The Art of Marvel":"https://www.google.com/travel/hotels/Disney's%20Hotel%20New%20York%20-%20The%20Art%20of%20Marvel/entity/CgoIg7zQoKXOpJkFEAE/reviews?q=Disney%27s%20Hotel%20New%20York%20-%20The%20Art%20of%20Marvel&g2lb=2502548%2C2503771%2C2503781%2C4258168%2C4270442%2C4284970%2C4291517%2C4306835%2C4597339%2C4718358%2C4723331%2C4731329%2C4754388%2C4757164%2C4814050%2C4861688%2C4864715%2C4865467%2C4874190%2C4886082%2C4886480%2C4893075%2C4902277%2C4903082%2C4904257%2C4906050%2C4910829%2C4920622%2C4926165&hl=fr-FR&gl=fr&cs=1&ssta=1&rp=EIO80KClzqSZBRCDvNCgpc6kmQU4AkAASAHAAQI&ictx=1&ved=0CAAQ5JsGahcKEwiopvyr1bD8AhUAAAAAHQAAAAAQBA&utm_campaign=sharing&utm_medium=link&utm_source=htls&ts=CAESCgoCCAMKAggDEAEaSAoqEiYyJDB4MTJhNTYyMWM5MzYyOGY0OToweDUzMjkyNzI1NDE0MWUwMxoAEhoSFAoHCOcPEAEYHhIHCOcPEAEYHxgBMgIQACoJCgU6A0VVUhoA",
            "Disney's Newport Bay Club":"https://www.google.com/travel/hotels/Disney's%20Newport%20Bay%20Club/entity/CgoIxbmXyrKxm_8YEAE/reviews?q=Disney%27s%20Newport%20Bay%20Club&g2lb=2502548%2C2503771%2C2503781%2C4258168%2C4270442%2C4284970%2C4291517%2C4306835%2C4597339%2C4718358%2C4723331%2C4731329%2C4754388%2C4757164%2C4814050%2C4861688%2C4864715%2C4865467%2C4874190%2C4886082%2C4886480%2C4893075%2C4902277%2C4903082%2C4904257%2C4906050%2C4910829%2C4920622%2C4926165&hl=fr-FR&gl=fr&cs=1&ssta=1&rp=EMW5l8qysZv_GBDFuZfKsrGb_xg4AkAASAHAAQI&ictx=1&ved=0CAAQ5JsGahcKEwi4yK-S1bD8AhUAAAAAHQAAAAAQBA&utm_campaign=sharing&utm_medium=link&utm_source=htls&ts=CAESCgoCCAMKAggDEAEaSQorEicyJTB4MTJhNTYyMWM5MzYyOGY0OToweDE4ZmU2ZDhiMjk0NWRjYzUaABIaEhQKBwjnDxABGBkSBwjnDxABGBoYATICEAAqCQoFOgNFVVIaAA",
            "Disney's Sequoia Lodge":"https://www.google.com/travel/hotels/Disney's%20Sequoia%20Lodge/entity/CgsIu82O963YitCbARAB/reviews?q=Disney%27s%20Sequoia%20Lodge&g2lb=2502548%2C2503771%2C2503781%2C4258168%2C4270442%2C4284970%2C4291517%2C4306835%2C4597339%2C4718358%2C4723331%2C4731329%2C4754388%2C4757164%2C4814050%2C4861688%2C4864715%2C4865467%2C4874190%2C4886082%2C4886480%2C4893075%2C4902277%2C4903082%2C4904257%2C4906050%2C4910829%2C4920622%2C4926165&hl=fr-FR&gl=fr&cs=1&ssta=1&rp=ELvNjvet2IrQmwEQu82O963YitCbATgCQABIAcABAg&ictx=1&ved=0CAAQ5JsGahcKEwjgt5f61LD8AhUAAAAAHQAAAAAQBA&utm_campaign=sharing&utm_medium=link&utm_source=htls&ts=CAESCgoCCAMKAggDEAEaSQorEicyJTB4MTJhNTYyMWM5MzYyOGY0OToweDliYTAyYWMyZGVlM2E2YmIaABIaEhQKBwjnDxABGB8SBwjnDxACGAEYATICEAAqCQoFOgNFVVIaAA",
            "Disney's Hotel Cheyenne":"https://www.google.com/travel/hotels/Disney's%20Hotel%20Cheyenne/entity/CgsIzcnwtvGguNnLARAB/reviews?q=Disney%27s%20Hotel%20Cheyenne&g2lb=2502548%2C2503771%2C2503781%2C4258168%2C4270442%2C4284970%2C4291517%2C4306835%2C4597339%2C4718358%2C4723331%2C4731329%2C4754388%2C4757164%2C4814050%2C4861688%2C4864715%2C4865467%2C4874190%2C4886082%2C4886480%2C4893075%2C4902277%2C4903082%2C4904257%2C4906050%2C4910829%2C4920622%2C4926165&hl=fr-FR&gl=fr&cs=1&ssta=1&rp=EM3J8LbxoLjZywEQzcnwtvGguNnLATgCQABIAcABAg&ictx=1&ved=0CAAQ5JsGahcKEwjgm5vg1LD8AhUAAAAAHQAAAAAQBA&utm_campaign=sharing&utm_medium=link&utm_source=htls&ts=CAESCgoCCAMKAggDEAEaSQorEicyJTB4NDdlNjBlMjk5ODcxNGE0ZjoweGNiYjJlMTA3MTZkYzI0Y2QaABIaEhQKBwjnDxABGAoSBwjnDxABGAsYATICEAAqCQoFOgNFVVIaAA",
            "Disney's Hotel Santa Fe": "https://www.google.com/travel/hotels/Disney's%20Hotel%20Santa%20Fe/entity/CgoI5L6wr_jJzolsEAE/reviews?q=Disney%27s%20Hotel%20Santa%20Fe&g2lb=2502548%2C2503771%2C2503781%2C4258168%2C4270442%2C4284970%2C4291517%2C4306835%2C4597339%2C4718358%2C4723331%2C4731329%2C4754388%2C4757164%2C4810792%2C4810794%2C4814050%2C4861688%2C4864715%2C4865467%2C4874190%2C4886082%2C4886480%2C4893075%2C4902277%2C4903082%2C4906050%2C4910829%2C4911170%2C4920622%2C4926165&hl=fr-FR&gl=fr&ssta=1&rp=EOS-sK_4yc6JbBDkvrCv-MnOiWw4AkAASAHAAQI&ictx=1&sa=X&ved=0CAAQ5JsGahcKEwiwhon707D8AhUAAAAAHQAAAAAQBA&utm_campaign=sharing&utm_medium=link&utm_source=htls&ts=CAESABpJCisSJzIlMHgxMmE1NjIxYzkzNjI4ZjQ5OjB4NmMxMzNhNGY4NWVjMWY2NBoAEhoSFAoHCOcPEAEYCxIHCOcPEAEYDBgBMgIQACoJCgU6A0VVUhoA",
            "Disney's Davy Crockett Ranch":"https://www.google.com/travel/hotels/disney's%20davy%20crockett%20ranch/entity/CgsIwO3Pwtz82r7hARAB/reviews?q=disney%27s%20davy%20crockett%20ranch&g2lb=2502548%2C2503771%2C2503781%2C4258168%2C4270442%2C4284970%2C4291517%2C4306835%2C4597339%2C4718358%2C4723331%2C4731329%2C4754388%2C4757164%2C4814050%2C4861688%2C4864715%2C4865467%2C4874190%2C4886082%2C4886480%2C4893075%2C4902277%2C4903082%2C4904257%2C4906050%2C4910829%2C4920622%2C4926165&hl=fr-FR&gl=fr&cs=1&ssta=1&rp=EMDtz8Lc_Nq-4QEQwO3Pwtz82r7hATgCQABIAcABAg&ictx=1&sa=X&ved=0CAAQ5JsGahcKEwjI3vzH1LD8AhUAAAAAHQAAAAAQBA&utm_campaign=sharing&utm_medium=link&utm_source=htls&ts=CAESABpJCisSJzIlMHg0N2U2MDJiYjUwMWQ5MGI1OjB4ZTE3ZDZiZTVjODUzZjZjMBoAEhoSFAoHCOcPEAEYCxIHCOcPEAEYDBgBMgIQACoJCgU6A0VVUhoA"}


# In[50]:


today = now.strftime("%Hh%M-%d-%m")


# In[51]:


# Test avec Disneyland Paris
url1 = dict_url.get("Parc Walt Disney Studios")
name = "Parc Walt Disney Studios "+today


# In[52]:


path=Service(r'/Users/RICARD/Documents/Etudiant/M2_SISE/TextMining/Projet_Disney/chromedriver_mac_arm64/chromedriver.exe')

 # Open webpage
driver=webdriver.Chrome(service=path)
time.sleep(3)

driver.get(url1)
time.sleep(5)

# Refus Cookie
driver.find_element(By.ID, "W0wltc").click() # Works only on Disneyland Paris Webpage
time.sleep(3)

driver.get(url1)
time.sleep(7)

# Filter by most recent reviews
driver.find_element(By.XPATH, '//div[@data-sort-id=\'newestFirst\']').click() # Works only on Disneyland Paris Webpage


# In[53]:


# Get total number of reviews
nb_reviews = driver.find_element(By.CLASS_NAME, 'z5jxId').text.split(' ')[0]

# Convert str to int 
nb_reviews = nb_reviews.replace(u"\u202f","") if u"\u202f" in nb_reviews else nb_reviews
nb_reviews = int(nb_reviews.replace(',', ''))

print(type(nb_reviews))
print(nb_reviews)


# In[54]:


# Récupère seulement les éléments qui nous intéresse et transforme les résultats en dataframe
def get_review_to_df(result_set):
    rev_dict = {'Review ID' : [],
        'Review Rate': [],
        'Review Time': [],
        'Review Text' : [],
        'Review Visite' : []}
    for result in result_set:
        review_rate = int(result.find('span', class_="Fam1ne EBe2gf")["aria-label"][7])
        review_time = result.find('span',class_='dehysf lTi8oc').text
        review_id = result.find('div',class_ ='TSUbDb').text
        if (result.find('span', class_='review-full-text')):
            review_text = result.find('span', class_='review-full-text').text
        else :
            review_text = "no comment"
        if (result.find('span', class_='xdR1zd')):
            review_visite = result.find('span', class_='xdR1zd').text
        else :
            review_visite = "no visite mentionned"

        rev_dict['Review ID'].append(review_id)
        rev_dict['Review Rate'].append(review_rate)
        rev_dict['Review Time'].append(review_time)
        rev_dict['Review Text'].append(review_text)
        rev_dict['Review Visite'].append(review_visite)

    return(pd.DataFrame(rev_dict))


# In[55]:


scrollable_popup = driver.find_element(By.XPATH, '/html/body/span[2]/g-lightbox/div/div[2]/div[3]/span/div/div/div/div[2]')

result_df = pd.DataFrame(columns = ['Review ID', 'Review Rate', 'Review Time','Review Text','Review Visite'])

# Normalement on le calcul avec nb_reviews sachant que par refresh on a 10 commentaires 
#nb_refresh = nb_reviews/10
#nb_refresh = 458
nb_refresh = 120
refresh_time = 2 # A ajuster selon la rapidité de refresh, parce que s'il est trop court on saute des commentaires

for i in range(nb_refresh):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
    time.sleep(refresh_time)
    if (i%10 == 0): print('Step '+str(i)+' - Scraping at '+str(round((i/nb_refresh)*100,2))+'%')
    if i%2 == 0:
        # Récupère tous les commentaires
        response = BeautifulSoup(driver.page_source, 'html.parser')

        r = response.find_all('div', class_="WMbnJf vY6njf gws-localreviews__google-review")
        df = get_review_to_df(r)
        result_df = pd.concat([result_df, df], axis=0,
            join="outer",
            ignore_index=True,
            keys=None,
            levels=None,
            names=None,
            verify_integrity=False,
            copy=True,)
       #print(result_df.shape)


# In[56]:


result_df


# In[57]:


bool_duplicates = result_df.duplicated(subset='Review ID')

bool_duplicates.value_counts()


# In[58]:


result_df.iloc[0,3]


# In[59]:


result_df[~bool_duplicates]


# In[60]:


export_df = result_df[~bool_duplicates]
export_df.to_csv('/Users/RICARD/Downloads/%s.csv' % name,index=False)


# In[61]:


driver.close()

