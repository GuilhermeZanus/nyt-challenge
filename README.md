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

You can also find the full list of dependencies in the requirements.txt and use the following command to install:

pip install -r requirements.txt

## How to Use

This project is designed to be used locally or as a robot through the Robocorp Cloud using Work Items.

## Using locally

1. Ensure you have met all the requirements mentioned above.
2. Copy the provided code and save it to a Python file (e.g., nytimes_automation.py).
3. Update the sections, search_phrase, and months_of_search variables according to your preferences in the run_automation method of the NyTimesAutomation class.
4. Run the Python script

## Using as a robot through the Robocorp Cloud

1. Create a user account at robocorp.com.

2. Access the Control Room from the Robocorp Cloud dashboard.

3. Create a robot and link it to this GitHub repository.

4. In the "Unattended" section, create a new process.

5. Click on "Run Process" and choose from the following options:

    5.1 "Run": This option performs a search on the NY Times website with the following default filters:
        Sections: Sports
        Search Phrase: Brazil
        Months of Search: 2

    5.2 - "Run with Input Data": With this option, you can define custom filters for the search. Follow these steps:

Enter "sections" in the first field and choose one of the available sections from the website.
In the next line, enter "search_phrase" and provide the desired search keyword.
On the third line, enter "months_of_search" and set the number of months to be searched.
Finally, click on "Run Process" to execute the search with your custom filters.

6. Wait for the process to complete, and the robot will scrape news articles based on your selected filters and save the relevant data to an Excel file and the downloaded news images.

