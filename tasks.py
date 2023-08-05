from typing import List
from RPA.Browser.Selenium import Selenium
from RPA.Calendar import Calendar
from RPA.Excel.Files import Files
from RPA.HTTP import HTTP
from processes import Actions
from elements import MappingElements
from RPA.Robocorp.WorkItems import WorkItems
import json
import logging


class NyTimesAutomation:
    def __init__(self):
        self.browser = Selenium()
        self.excel_file = Files()
        self.http = HTTP()
        self.calendar = Calendar()
        self.find = MappingElements(self.browser)
        self.tasks = Actions(self.browser)
        self.wi = WorkItems()
        

    def teardown(self):
        self.browser.close_all_browsers()
    
    
    def run_automation(self):
        
        self.wi.get_input_work_item()

        # variables = self.wi.get_work_item_variables()
        # for variable, value in variables.items():
            # print(variable, value)



        # sections = self.wi.get_work_item_variable("sections", default="Arts")
        # sections = str(variables["sections"])
        sections = List[str]
        sections = self.wi.get_work_item_variable("sections", default="Arts")
       
        print(sections)


        search_phrase = self.wi.get_work_item_variable("search_phrase", default="Brazil")
        # search_phrase = str(variables["search_phrase"])
        print(search_phrase)

        months_of_search = self.wi.get_work_item_variable("months_of_search", default=2)
        # months_of_search = int(variables["months_of_search"])
        print(months_of_search)



        try:
            print("*****abrindo o navegador")
            self.tasks.open_the_website("https://www.nytimes.com/")
            print("*****maximizando o navegador")
            # self.tasks.maximize_browser()

            print("*****verificando update_terms_visible")
            if self.tasks.updated_terms_visible():
                print("*****clicando em continue para update_terms_visible")
                self.tasks.click_continue_updated_terms()

            print("*****verificando cookies_message_visible")
            if self.tasks.cookies_message_visible():
                print("*****clicando accept em cookies_message_visible")
                self.tasks.click_accept_cookies()

            self.tasks.search_for(search_phrase)
            self.tasks.click_section()
            self.tasks.select_section(sections)
            self.tasks.select_news_category('newest')

            self.tasks.create_workbook()

            self.tasks.iterate_with_news(search_phrase, months_of_search)

                
        finally:
            self.teardown()


if __name__ == "__main__":

    automation = NyTimesAutomation()
    automation.run_automation()
