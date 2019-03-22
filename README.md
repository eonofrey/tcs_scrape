# Scraping Store Addresses from The Container Store's Website

This short script scrapes and cleans the addresses for all of The Container Store's stores. It outputs a .csv file with 1 column, the address. 


The Company's main site has all of the store locations displayed on the main page. Clicking each store sends you to an individual page for that store

<img src="https://user-images.githubusercontent.com/38504767/54851673-1a96cb80-4cc1-11e9-9b23-8a3850702349.png" height="400">


The url's for these sites are stored the 'href' attribute contained in every 'stateListItem storeName' 
<img src="https://user-images.githubusercontent.com/38504767/54852259-bb39bb00-4cc2-11e9-879b-25c41d0cfbb2.png" height="300" width = "400">

