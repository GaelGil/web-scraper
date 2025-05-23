# web-scraper
## Description
This scraper was created using selenium. We scrape links off of items on a website. 
As an example it can be used on the products page of amazon or any website where there are itmems listed.
Once we have the links to each item or product. This way we can scrape data on each individual item. 
This class also has the functionality to write to a csv file if needed.

## How to use
###  Create virtual environment
~~~
python3 -m venv env
~~~

###  Activate virtual environment
~~~
source ./env/bin/activate
~~~

### Install libraries
~~~
pip install -r requirements.txt
~~~

### Set xpaths
Typical usage example:
~~~python
 sc = Scraper()
 sc.set_url('example_url')
 sc.get_links("xpath_for_links")
 xpaths = {
 'title': "title_xpath]"
 }
 sc.set_xpaths(xpaths)
 sc.scrape_items(data_to_scrape)
 formated_data = sc.format_data()
 sc.to_csv('example.csv', formated_data)
 ~~~


### Run
~~~
python3 Scraper.py
~~~
