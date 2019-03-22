# Imports
import requests
from bs4 import BeautifulSoup 
import pandas as pd 

# Function to grab the store address from each page
def grab_address(url = 'https://www.containerstore.com/locations/showStore.htm?store=GAL'):
    try:
        a = requests.get(url)
        b = BeautifulSoup(a.text, 'html.parser')
        address = b.find('address').text.strip().replace("                  ", ' ').replace(u'\xa0', ' ')
        address = address.replace("\n","")
        print(address)
        return address
    except HTTPError as e: 
        return None

# Set up the Soup
url = 'https://www.containerstore.com/locations/index.htm'
page_response = requests.get(url)
page_content = BeautifulSoup(page_response.text, 'html.parser')

# Grab all stores from the main page 
stores = page_content.findAll(class_="stateListItem storeName")

# Grab all store url's 
store_urls= []

for store in stores: 
    surl = (store.find('a')['href'])
    store_urls.append('https://www.containerstore.com' + surl)

# Get addresses
address_container = []    

for i in store_urls:
    address_container.append(grab_address(i))
    
# Output a .csv file 
pd.DataFrame(address_container, columns = ["Address"])

