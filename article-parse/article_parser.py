from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Loading URL
extractItems = []
browser = webdriver.Firefox()
browser.get('http://markets.wsj.com/?mod=Homecle_MDW_MDC')
search_box = browser.find_element_by_id("globalHatSearchInput")
search_box.send_keys('_keyword')
req = browser.find_element_by_css_selector('.button-search').click()

def getPageUrl(elementLinks):
    extractLinks = []
    for element in elementLinks:
        links = element.get_attribute('href')
        extractLinks.append(links)
    return(extractLinks)

def extractElements(url):
    second_browser = webdriver.Firefox()
    for extracted_url in getPageUrl(elementLinks):
        second_browser.get(extracted_url)
        try:
            parent = extractItems.append(second_browser.find_element_by_xpath('//article[@id="article-contents"]').text)
        except NoSuchElementException:
            try:
                parent = extractItems.append(second_browser.find_element_by_xpath('//div[@id="article_sector"]').text)
            except NoSuchElementException:
                try:
                    parent = extractItems.append(second_browser.find_element_by_xpath('//article[@id="video-info"]').text)
                except NoSuchElementException:
                    try:
                        parent = extractItems.append(second_browser.find_element_by_xpath('//div[@class="contentwide"]').text)
                    except NoSuchElementException:
                        pass
        # for texts in extractItems:      # Print extracted texts for reference.
        #     print texts
    second_browser.close()

# Start iterating links in search results
while True:
    try:
        browser.find_element_by_class_name('next-page')
        elementLinks = browser.find_elements_by_xpath('//h3[@class="headline"]/a')
        extractElements(getPageUrl(elementLinks))
        element = browser.find_element_by_link_text('Next')
        element.click()
    except NoSuchElementException:
        break
        second_browser.close()
        browser.close()
