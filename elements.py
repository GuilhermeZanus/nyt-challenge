from RPA.Browser.Selenium import Selenium

class MappingElements:

    def __init__(self, browser_instance):
        self.browser = browser_instance

    def updated_terms(self):
        return self.browser.find_element("css: #complianceOverlay")
    
    def updated_terms_continue_button(self):
        return  self.browser.find_element("css: #complianceOverlay button")
    
    def cookies_message(self):
        return self.browser.find_element("css: .gdpr")
    
    def accept_button(self):
        return self.browser.find_element("xpath: //button[text()='Accept']")
    
    def search_icon(self):
        return self.browser.find_element("css: button[data-test-id='search-button']")
    
    def search_field(self):
        return self.browser.find_element("css: #search-input input")
    
    def section_button(self):
        return self.browser.find_element("css: div[data-testid='section'] button")
    
    def checkbox_section(self, section):
        return self.browser.find_element(f"xpath: //span[contains(text(), '{section}')]/../input")
     
    def category_dropdown(self):
        return self.browser.find_element("css: select[data-testid='SearchForm-sortBy']")
    
    def news_items(self):
        return self.browser.find_elements('css: li[class="css-1l4w6pd"]')
    
    def date_element(self, i):
        news_article = self.news_items()
        return self.browser.find_element('css: li span[data-testid="todays-date"]', news_article[i])

    def title_element(self, i): 
        news_article = self.news_items()
        return self.browser.find_element('css: h4', news_article[i])
    
    def description_elememt(self, i):
        news_article = self.news_items()
        return self.browser.find_element('xpath: .//p[@class="css-16nhkrn"]', news_article[i])

    def filename_element(self, i):
        news_article = self.news_items()
        return self.browser.find_element('css: figure div img', news_article[i])
    
    def picture_element(self, i):
        news_article = self.news_items()
        return self.browser.find_element('css: figure div img', news_article[i])
    
    def show_more_button(self):
        return self.browser.find_element("css: button[data-testid='search-show-more-button']")


