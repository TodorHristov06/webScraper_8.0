# webScraper_8.0
My 8th try to build a web scraper

This Scrapy project collects hardware configuration data from [desktop.bg](https://desktop.bg/) by navigating through the `computers-all` section of the website. The goal is to scrape and store data for each computer configuration available.

## Target Data
For each configuration, the following details are collected:
- **Processor** ("Процесор")
- **GPU** ("Видеокарта")
- **Motherboard** ("Дънна платка")
- **RAM** ("Оперативна памет")

## Installation
To use this project, Python must be installed along with several dependencies via pip. Follow these steps to set up the project environment:

### Step 1: Clone the Repository
Clone the project to your local machine using the following command:
    ```bash
    git clone https://github.com/TodorHristov06/webScraper_8.0
    ```
- ## Prerequisites

- Python 3.7+
- Scrapy
- SQLite3