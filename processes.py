from RPA.Browser.Selenium import Selenium
from RPA.Calendar import Calendar
from RPA.Excel.Files import Files
from RPA.Browser.Selenium import ElementNotFound
import time
import re
import os
from RPA.HTTP import HTTP
from elements import MappingElements
from typing import List

class Actions:


    def __init__(self, browser_instance):
        self.browser = browser_instance

        self.browser = Selenium()
        self.excel_file = Files()
        self.http = HTTP()
        self.calendar = Calendar()
        self.find = MappingElements(self.browser)
        
    
    def open_the_website(self, url) -> None:
        # self.browser.open_available_browser(url, headless=True)
        time.sleep(5)
        self.browser.open_headless_chrome_browser(url)

    def maximize_browser(self) -> None:
        self.browser.maximize_browser_window()  

    def updated_terms_visible(self) -> bool:
        time.sleep(5)
        update_terms = self.find.updated_terms()
        return self.browser.is_element_visible(update_terms)
    
    def click_continue_updated_terms(self) -> None:
        time.sleep(5)
        updated_terms_button = self.find.updated_terms_continue_button()
        self.browser.click_button(updated_terms_button)

    def cookies_message_visible(self) -> bool:
        time.sleep(5)
        cookies_message = self.find.cookies_message()
        return self.browser.is_element_visible(cookies_message)
    
    def click_accept_cookies(self) -> None:
        time.sleep(5)
        accept_button = self.find.accept_button()
        self.browser.click_button(accept_button)
    
    def search_for(self, term) -> None:
        time.sleep(5)
        search_icon = self.find.search_icon()
        print("****clicando na lupa")
        self.browser.click_button(search_icon)

        search_field = self.find.search_field()
        print("****esperando o campo para digitar o texto")
        self.browser.wait_until_element_is_visible(search_field, 2)
        print("****iserindo o texto de pesquisa" + term)
        self.browser.input_text(search_field, term)
        self.browser.press_keys(search_field, "ENTER")

        section_button = self.find.section_button()
        print("*****aguardando o section button estar visível")
        self.browser.wait_until_element_is_visible(section_button, 10)

    def click_section(self) -> None:
        section_button = self.find.section_button() 
        print("******clicando no section button")       
        self.browser.click_button(section_button)

    def select_section(self, sections) -> None:

        section_list = List[str]
        
        section_list = [section_list.strip() for section_list in sections.split(",")]
        print("section_list = " + str(section_list))

        for item in section_list:
            print("***** "+str("item in section_list = " + str(item)))
            checkbox = self.find.checkbox_section(str(item))
            self.browser.click_element(checkbox)
        
        # print("***** "+sections) 
        # checkbox = self.find.checkbox_section(str(sections))            
        # self.browser.click_element(checkbox)

    def select_news_category(self, type) -> None:
        category_dropdown = self.find.category_dropdown()
        self.browser.select_from_list_by_value(category_dropdown, type)
        time.sleep(5)

    def save_workbook(self) -> None:
        # self.excel_file.save_workbook(path="./output/news.xlsx")
        self.excel_file.save_workbook()

    def create_workbook(self) -> None:
        self.excel_file.create_workbook(path="./output/news.xlsx", fmt="xlsx")
        # self.excel_file.create_workbook(path="news.xlsx")
        self.save_workbook()

    def date_validation(self, i, x) -> bool:

        date_element = self.find.date_element(i)
        article_date_with_commas = str(self.browser.get_text(date_element))
        article_date_no_commas = article_date_with_commas.replace(',', '')
        article_date_no_dot = article_date_no_commas.replace('.', '')
        today = self.calendar.create_time(str(self.calendar.time_now(return_format="MM YYYY")), "MM YYYY")            
        
        
        if x==0:
            focus_date = today.add(months=-x)
        else:
            focus_date = today.add(months=(-x+1))
        
        print("focus_date = " + str(focus_date)) 
        

        if(re.match("^[A-Za-z]{4} \d{1,2} \d{4}$", str(article_date_no_dot))):
            adjusted_article_date = self.calendar.create_time(article_date_no_dot, "MMMM DD YYYY")
            validation = self.calendar.compare_times(str(focus_date), str(adjusted_article_date))
            
            return validation 

        if(re.match("^[A-Za-z]{4} \d{1,2}$", str(article_date_no_dot))):
            adjusted_article_date = self.calendar.create_time(article_date_no_dot, "MMMM DD")
            validation = self.calendar.compare_times(str(focus_date), str(adjusted_article_date))
        
            return validation    

        if(re.match("^[A-Za-z]{3} \d{1,2} \d{3}$", str(article_date_no_dot))):
            adjusted_article_date = self.calendar.create_time(article_date_no_dot, "MMM DD YYYY")
            validation = self.calendar.compare_times(str(focus_date), str(adjusted_article_date))
    
            return validation    

        if(re.match("^[A-Za-z]{3} \d{1,2}$", str(article_date_no_dot))):
            adjusted_article_date = self.calendar.create_time(article_date_no_dot, "MMM DD")
            
            print("adjusted_article_date = " + str(adjusted_article_date))
            # validation = self.calendar.compare_times(str(focus_date), str(adjusted_article_date))
            
            # return validation    
            first_validation = self.calendar.compare_times(str(focus_date), str(adjusted_article_date))
            if first_validation or focus_date==adjusted_article_date:
                validation = True
                return validation



        if(re.match("^\d+h ago$", str(article_date_no_dot))):
            validation = True
            return validation
        
        if(re.match("\d+m ago$", str(article_date_no_dot))):
            validation = True
            return validation
    

    def get_total_of_occurrences(self, i, search_phrase) -> int:       
        try:
            lower_search_phrase = str(search_phrase).lower()
            title_element = self.find.title_element(i)
            lower_title_text = str(self.browser.get_text(title_element)).lower()
            lower_title_text_no_commas = lower_title_text.replace(',', '')
            lower_title_text_no_dot = lower_title_text_no_commas.replace('.', '')

            words_of_the_title = lower_title_text_no_dot.split()

            count = 0
            for word in words_of_the_title:
                if word == lower_search_phrase:
                    count +=1


            description_element = self.find.description_elememt(i)
            lower_description_text = str(self.browser.get_text(description_element)).lower()
            lower_description_text_no_commas = lower_description_text.replace(',', '')
            lower_description_text_no_dot = lower_description_text_no_commas.replace('.', '')

            words_of_the_description = lower_description_text_no_dot.split()

            for word in words_of_the_description:
                if word == lower_search_phrase:
                    count +=1



        except ElementNotFound:
            description_text = ""
            lower_search_phrase = str(search_phrase).lower()
            title_element = self.find.title_element(i)
            lower_title_text = str(self.browser.get_text(title_element)).lower()
            
            words_of_the_title = str(lower_title_text).lower().split()

            count = 0
            for word in words_of_the_title:
                if word == lower_search_phrase:
                    count +=1

        
        return count


    def check_contains_money(self, i) -> bool: 

        news_elements = self.browser.get_webelements('css: ol li[class="css-1l4w6pd"]')
        number_of_news = len(news_elements)

        try:
            title_element = self.find.title_element(i)
            title_text = self.browser.get_text(title_element)                
            title_text_lower = str(title_text).lower()                

            description_element = self.find.description_elememt(i)            
            description_text = self.browser.get_text(description_element)
            description_text_lower = str(description_text).lower()                

            full_text = title_text_lower + description_text_lower

            money_pattern = r"\$\d+(\.\d{1,2})?|\d+(,\d{3})*(\.\d{1,2})?\s?(dollars?|usd)"
            true_or_false = bool(re.search(money_pattern, full_text, re.IGNORECASE))

        except ElementNotFound:
            description_text = ""
            full_text = title_text_lower

            money_pattern = r"\$\d+(\.\d{1,2})?|\d+(,\d{3})*(\.\d{1,2})?\s?(dollars?|usd)"
            true_or_false = bool(re.search(money_pattern, full_text, re.IGNORECASE))
        return true_or_false
    

    def download_images(self, i) -> None:            
        try:
            picture_element = self.find.picture_element(i)
            picture_filename = self.browser.get_element_attribute(picture_element, "src")   
            self.http.download(picture_filename, "./output/")

        except ElementNotFound:
            pass  

    """ 
    This method extracts and saves in a file the title, description, file name, count of search phrases 
    in the title and description, if the title or description contains an amount of money. In addition 
    to downloading the respective news image
    """
    # def extract_data(self, i, search_phrase) -> None:
    #     article_list = self.find.news_items()
        
    #     data = []

    #     # Title text 
    #     title_element = self.find.title_element(i)
    #     title_text = self.browser.get_text(title_element)

    #     # Date
    #     date_element = self.find.date_element(i)
    #     date = self.browser.get_text(date_element)

    #     # Description text
    #     try:
    #         description_elememt = self.find.description_elememt(i)
    #         description_text = self.browser.get_text(description_elememt)

    #     except ElementNotFound:
    #             description_text = "No description available"

    #     # Picture Filename
    #     try:
    #         filename_element = self.find.filename_element(i)       
    #         filename_src = self.browser.get_element_attribute(filename_element, "src")        
    #         full_filename_text = os.path.basename(filename_src)
    #         filename_size = len(full_filename_text) - 37
    #         filename_text = full_filename_text[:filename_size]

    #     except ElementNotFound:
    #         filename_text = "No picture available"
        
    #     # Total of occurances
    #     total_of_occurrences = self.get_total_of_occurrences(i, search_phrase)

    #     # True or false amount of money
    #     true_or_false = self.check_contains_money(i)

    #     # Download images
    #     self.download_images(i)

    #     # Append to list
    #     news = [title_text, date, description_text, filename_text, total_of_occurrences, true_or_false]
    #     data.append(news)
    #     self.excel_file.set_cell_values("A"+str(i+1),data)
    #     self.save_workbook()


    def extract_data(self, i, search_phrase) -> None:
        try:
            article_list = self.find.news_items()
            
            data = []

            # Title text 
            title_element = self.find.title_element(i)
            title_text = self.browser.get_text(title_element)

            # Date
            date_element = self.find.date_element(i)
            date = self.browser.get_text(date_element)

            # Description text
            try:
                description_elememt = self.find.description_elememt(i)
                description_text = self.browser.get_text(description_elememt)

            except ElementNotFound:
                    description_text = "No description available"

            # Picture Filename
            try:
                filename_element = self.find.filename_element(i)       
                filename_src = self.browser.get_element_attribute(filename_element, "src")        
                full_filename_text = os.path.basename(filename_src)
                filename_size = len(full_filename_text) - 37
                filename_text = full_filename_text[:filename_size]

            except ElementNotFound:
                filename_text = "No picture available"
            
            # Total of occurances
            total_of_occurrences = self.get_total_of_occurrences(i, search_phrase)

            # True or false amount of money
            true_or_false = self.check_contains_money(i)

            # Download images
            self.download_images(i)


        finally:
            # Append to list
            news = [title_text, date, description_text, filename_text, total_of_occurrences, true_or_false]
            data.append(news)
            self.excel_file.set_cell_values("A"+str(i+1),data)
            self.save_workbook()
    


    """
    This method interacts with all news resulting from the search, validating the date of the news. It 
    also checks if it is necessary to click on the show_more button and, if so, updates the size of the 
    list to continue iterating until it identifies that the iteration must be interrupted
    """
    def iterate_with_news(self, search_phrase, months_of_search) -> None:
        i = 0
        has_finished = False
        while not has_finished:
            news_items = self.find.news_items()

            if self.date_validation(i, months_of_search):                    
                    
                self.extract_data(i, search_phrase)

                #has show more button
                if (i+1) % 10 == 0:
                    try:

                        self.browser.click_button(self.find.show_more_button())                       
                        time.sleep(3)    
                        news_items = self.find.news_items()                   
                        
                    except ElementNotFound:
                        has_finished = True
                    
                if i == len(news_items)-1:
                    has_finished = True
                else:
                    i += 1
            else:
                has_finished = True