from RPA.Browser.Selenium import Selenium
from RPA.Calendar import Calendar
from RPA.Excel.Files import Files
from RPA.HTTP import HTTP
from processes import Actions
from elements import MappingElements
from RPA.Robocorp.WorkItems import WorkItems


class NyTimesAutomation:
    def __init__(self):
        self.browser = Selenium()
        self.excel_file = Files()
        self.http = HTTP()
        self.calendar = Calendar()
        self.find = MappingElements(self.browser)
        self.tasks = Actions(self.browser)
        self.work_items = WorkItems()

    def teardown(self):
        self.browser.close_all_browsers()
    
    
    def run_automation(self):
        # self.work_items.get_work_item_payload()

        variables =[{"sections": "Food"}, {"search_phrase": "Italy"}, {"months_of_search", "3"}]

        sections = self.work_items.get_work_item_variable("sections", variables)
        search_phrase = self.work_items.get_work_item_variable("search_phrase", variables)
        months_of_search = self.work_items.get_work_item_variable("months_of_search", variables)

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
