import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser
import time


# In[2]:

def init_browser():
    executable_path = {'chromedriver.exe'}
    return Browser('chrome', headless=False)

def scrape_info():
    browser = init_browser()


    # In[3]:


    nasa_url = 'https://mars.nasa.gov/news/'
    browser.visit(nasa_url)


    # In[4]:


    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[5]:


    # extracting all news articles
    results = soup.find_all('div', class_='list_text')
    results[0]


    # In[6]:


    # extracting latest headline 
    latest_headline = results[0].a.text


    # extracting description from latest headline
    latest_headline_p=results[0].find("div", class_="article_teaser_body").text

    print(latest_headline)
    print(latest_headline_p)


    # In[7]:


    # Visiting Second Website for Scraping
    jpl_nasa_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_nasa_url)


    # In[8]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[9]:


    # results_2=soup.find_all("section", class_="centered_text clearfix main_feature primary_media_feature single")
    # results_2[0]


    # In[10]:


    browser.click_link_by_partial_text('FULL IMAGE')


    # In[11]:


    browser.click_link_by_partial_text('more info')


    # In[12]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[13]:


    results_feat_img = soup.find("aside", class_="image_detail_module")
    results_feat_img
    # results_feat_img


    # In[14]:


    # html = browser.html
    # soup = BeautifulSoup(html, 'html.parser')

    # isolating div that has links for full picture
    results_feat_img = soup.find("figure", class_="lede")
    results_feat_img_link = results_feat_img.img["src"]
    results_feat_img_link_full = f"https://www.jpl.nasa.gov{results_feat_img_link}"
    results_feat_img_link_full
    # = results_feat_img[1].a['href']

    # Cleaning the url extracted

    # feat_img_url = results_feat_img.replace('//', '')
    # print(feat_img_url)


    # In[15]:


    # browser.visit won't open the page. the url does work

    browser.visit(results_feat_img_link_full)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results_feat_img_link_full = soup.find("img")["src"]
    # In[16]:


    # featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA23853_hires.jpg'
    # browser.visit(featured_image_url)


    # # Scraping Twitter for latest Mars Weather Update

    # In[17]:


    mars_twitter_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_twitter_url)
    time.sleep(30)


    # In[18]:


    # run beautiful soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[19]:


    latest_weather = soup.find('div', class_="css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0")


    # In[20]:


    latest_weather


    # In[21]:


    # Finding span where latest post holds text
    mars_weather = latest_weather.find('span', class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0').text


    # In[22]:


    mars_weather


    # In[23]:


    # Latest Post Cleaned 
    mars_weather_clean = mars_weather.replace("\n","")
    mars_weather_clean


    # # Finding Mars Facts. Parsing with Pandas

    # In[24]:


    url = 'https://space-facts.com/mars/'
    browser.visit(url)


    # In[25]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[26]:


    mars_facts = pd.read_html(url)


    # In[27]:


    mars_facts_df = mars_facts[0]


    # In[28]:


    mars_facts_df


    # In[29]:


    mars_facts_df = mars_facts_df.rename(columns={1:"Values"})


    # In[30]:


    # mars_facts_df=mars_facts_df.set_index(0)


    # In[31]:


    mars_facts_df


    # In[32]:


    # mars_facts_df.loc['Mass:']


    # In[33]:


    html_table = mars_facts_df.to_html()
    html_table


    # In[34]:


    html_table=html_table.replace('\n', '')


    # In[35]:


    # # Finding Hemisphere Image URLs

    # In[36]:


    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)


    # In[37]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[38]:


    hemisphere_list = soup.find_all('div', class_="item")
    hemisphere_list


    # In[39]:


    hemisphere_urls=[]
    hemisphere_names=[]

    # In[40]:


    for item in hemisphere_list:
        hem_name=(item.h3.text)
        hem_source=(item.a["href"])
        hemisphere_urls.append(f"https://astrogeology.usgs.gov{hem_source}")
    #     print(item.h3.text)
    #     print(item.img["src"])
        hemisphere_names.append(hem_name)


    # In[41]:


    hemisphere_urls
    hemisphere_names


    # In[42]:


    hemisphere_image_urls=[]


    # In[43]:


    # activating beautiful soup
    # html = browser.html
    # soup = BeautifulSoup(html, 'html.parser')


    # In[44]:


    # find out why it doesn't work the first time

    for item in hemisphere_urls:
        browser.visit(item)
        time.sleep(2)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        test = soup.find("div", class_="downloads")
        hem_img_source=test.a["href"]
        hemisphere_image_urls.append(hem_img_source)
        time.sleep(2)


    # In[45]:


    hemisphere_image_urls


    # In[46]:


    valles_img = hemisphere_image_urls[0]
    cerberus_img = hemisphere_image_urls[1]
    schiaparelli_img = hemisphere_image_urls[2]
    syrtis_img = hemisphere_image_urls[3]


    # In[47]:


    # # activating beautiful soup
    # html = browser.html
    # soup = BeautifulSoup(html, 'html.parser')


    # In[48]:


    hemisphere_name_and_url = [
        {"title":hemisphere_names[0], "img_url": valles_img},
        {"title": hemisphere_names[1], "img_url":cerberus_img},
        {"title": hemisphere_names[2], "img_url":schiaparelli_img},
        {"title": hemisphere_names[3], "img_url":syrtis_img}]

    mars_data={"results_feat_img_link_full":results_feat_img_link_full,
    "valles_img":valles_img,
    "latest_headline":latest_headline,
    "latest_headline_p":latest_headline_p,
    "html_table":html_table,
    "mars_weather_clean":mars_weather_clean,
    "cerberus_img":cerberus_img,
    "schiaparelli_img":schiaparelli_img,
    "syrtis_img":syrtis_img}
    # In[49]:


    hemisphere_name_and_url
    browser.quit()
    return mars_data

