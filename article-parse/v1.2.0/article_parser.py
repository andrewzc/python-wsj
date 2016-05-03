from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

## Loading URL
extractItems = []
browser = webdriver.Firefox()
browser.get('http://markets.wsj.com/?mod=Homecle_MDW_MDC')

# ==============================================================================
## Login Credentials
# login = browser.find_element_by_link_text("Log In").click()
# loginID = browser.find_element_by_id("username").send_keys('id_')             # Input username
# loginPass = browser.find_element_by_id("password").send_keys('password_')     # Input password
# loginReady = browser.find_element_by_class_name("login_submit")
# loginReady.submit()
# ==============================================================================

search_box = browser.find_element_by_id("globalHatSearchInput")
search_box.send_keys('Tesla')                                                   # Input search keyword
search_req = browser.find_element_by_css_selector('.button-search').click()
toggleMenu = browser.find_element_by_link_text("ADVANCED SEARCH")
toggleMenu.click()
menuOptions = browser.find_element_by_class_name('datePeriod')
toggleButton = menuOptions.find_element_by_css_selector(".dropdown-toggle")
toggleButton.click()
dropdownOptions = menuOptions.find_elements_by_tag_name("li")
dropdownOptions[len(dropdownOptions)-1].click()                                 # Adjust list length for date ranges
searchArchive = browser.find_element_by_class_name('keywordSearchBar')
searchArchive.find_element_by_class_name("searchButton").click()

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
        # for texts in extractItems:                                            # Print extracted texts for reference.
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
