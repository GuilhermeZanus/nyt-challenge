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
        # variables = self.wi.get_work_item_payload()

        variables = self.wi.get_work_item_variables()
        for variable, value in variables.items():
            print(variable, value)
            # logging.info("%s = %s", variable, value)
        
        
        # with open("devdata/work-items.json", "r") as json_file:
            # work_item_data = json.load(json_file)


        # self.work_items.set_current_work_item(work_item_data)
        # sections = work_item_data[0]["sections"]
        # search_phrase = work_item_data[1]["search_phrase"]
        # months_of_search = work_item_data[2]["months_of_search"]

        # variables =[{"sections": "Food"}, {"search_phrase": "Italy"}, {"months_of_search", "3"}]

        # self.work_items.get_work_item_payload()
        # for variable, value in variables.items():
        # sections = str(self.wi.set_work_item_variable("sections",list(variables.values())[0]))
        print(variables["sections"])
        print(list(variables.values())[0])
        sections = str(self.wi.get_work_item_variable(variables["sections"]))
        
        print(sections)
        # sections = self.wi.get_work_item_variable(variables.values[0])
            # sections = self.wi.get_work_item_variable("sections" )
            # self.work_items.get_input_work_item()
        search_phrase = str(self.wi.set_work_item_variable("search_phrase",list(variables.values())[1]))
        print(list(variables.values())[1])
        print(search_phrase)
        # search_phrase = self.wi.get_work_item_variable(variables.values[1])
            # self.work_items.get_input_work_item()
        
        months_of_search = str(self.wi.set_work_item_variable("months_of_search",list(variables.values())[2]))
        print(list(variables.values())[2])
        print(months_of_search)
        # months_of_search = self.wi.get_work_item_variable(variables.values[2])

        try:
            self.tasks.open_the_website("https://www.nytimes.com/")
            self.tasks.maximize_browser()


            if self.tasks.updated_terms_visible():
                self.tasks.click_continue_updated_terms()

            if self.tasks.cookies_message_visible():
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
