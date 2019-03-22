# Scraping Store Addresses from The Container Store's Website

### Description 
This short script scrapes and cleans the addresses for all of The Container Store's stores. It outputs a .csv file with 1 column, the address. Note: I checked the company's robot.txt beforehand and it does not prohibit scraping store locations. 

### Site and HTML
The Company's main site has all of the store locations displayed on the main page. Clicking each store sends you to an individual page for that store

<img src="https://user-images.githubusercontent.com/38504767/54851673-1a96cb80-4cc1-11e9-9b23-8a3850702349.png" height="200">


The url's for these sites are stored the 'href' attribute contained in every 'stateListItem storeName' 
<img src="https://user-images.githubusercontent.com/38504767/54852259-bb39bb00-4cc2-11e9-879b-25c41d0cfbb2.png" height="130" width = "500">

Each of these links takes you to a page like this that has the address of the store I want. These addresses are conveniently stored in the "<address>" attributes on the page.
<img src="https://user-images.githubusercontent.com/38504767/54852421-3f8c3e00-4cc3-11e9-8daf-aaf9ca14c02d.png" height="150" width = "370">

### Process
1. Get the links to all of the stores from the main page
2. Iterate through these links to grab the address off of each page
3. Clean the text and put into a .csv file

### Output 
The final output of this script is a small .csv file that is just a column of all of TCS's store addresses

<img src="https://user-images.githubusercontent.com/38504767/54852769-3485dd80-4cc4-11e9-92df-6de039179bbb.png">
