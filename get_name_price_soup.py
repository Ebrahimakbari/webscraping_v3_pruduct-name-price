# Importing the necessary libraries
from bs4 import BeautifulSoup
import requests
import pandas

# Initializing empty lists to store device names and prices
device_name = []
prices = []

# Looping through the first 9 pages of the website
for index in range(1, 10):
    # Sending a GET request to the specified URL
    r = requests.get(f"https://mobileshop.eu/android-os/page-{str(index)}/")

    # Parsing the HTML content using BeautifulSoup
    soup = BeautifulSoup(r.text, 'html.parser')

    # Selecting the device names and prices using CSS selectors
    mobile_info = soup.select('div.product-name h5 a')
    price = soup.select('div.price div')

    # Appending the device names and prices to the corresponding lists
    for name in mobile_info:
        device_name.append(name.contents[0])
    for p in price:
        prices.append(p.contents[0].replace('\xa0', ' '))

# Creating a dictionary with the device names and prices
data = {
    "Device Name": device_name,
    "Price": prices
}

# Creating a data frame from the dictionary
main_data = pandas.DataFrame.from_dict(data, orient='index')

# Transposing the data frame
main_data = main_data.transpose()

# Creating an Excel writer object
writer = pandas.ExcelWriter('main_data.xlsx')

# Writing the data frame to an Excel file
main_data.to_excel(writer)

# Saving the Excel file
writer._save()
