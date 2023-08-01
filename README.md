# NyTimesAutomation README

## Overview

This Python code is an automation script designed to interact with the New York Times website (nytimes.com) using Robotic Process Automation (RPA) techniques. The script leverages the RPA framework, which incorporates the Selenium library for web scraping, the HTTP library for handling HTTP requests and the Excel library for managing Excel files. The automation script carries out the following tasks:

1. Opens the New York Times website.
2. Accepts the updated terms and cookies if visible.
3. Searches for news articles related to a specific phrase (e.g., "Brazil").
4. Filters the news articles by a specific section (e.g., "Sports") and sorting them by "newest".
5. Iterates through the filtered news articles, validates their dates according to the number of months selected, extracts relevant data, and saves it to an Excel file.
6. Downloads images associated with the news articles.

## Requirements

To run this automation script, you need the following libraries installed:

1. RPA.Browser.Selenium
2. RPA.Calendar
3. RPA.Excel.Files
4. RPA.HTTP

Make sure to install these libraries using pip:

pip install rpa-framework

## How to Use

1. Ensure you have met all the requirements mentioned above.
2. Copy the provided code and save it to a Python file (e.g., nytimes_automation.py).
3. Update the sections, search_phrase, and months_of_search variables according to your requirements in the run_automation method of the NyTimesAutomation class.
4. Run the Python script