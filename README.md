# Click.in Classified Ads Scraper
A Python scraper built with the Scrapy framework to extract classified ads listings from www.click.in. 
The scraper utilizes proxies to avoid bans, rotating proxy middleware for IP rotation, and output processors for data cleaning.
## Features
- Scrapes classified ads listings from www.click.in.
- Utilizes proxies to avoid bans.
- Implements rotating proxy middleware for IP rotation.
- Uses output processors for data cleaning.


### Installation

1. Clone the repository:
   git clone https://github.com/Eben001/classifieds.git
   cd classifieds
   [install a virtual environment if you wish](https://docs.python.org/3/library/venv.html)

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

### Usage
   Configuring Proxies
1. Obtain Proxies:
Acquire a list of proxies from a reliable provider.
2. Update proxies.txt with the proxies
3. Run the Scraper:
   ```bash
   scrapy crawl clickin

4. To output the result in a json file run:
   ```bash
   scrapy crawl clickin -o output.json


  Feel free to customize the content based on additional features or specific instructions for your project.
