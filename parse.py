import requests
from bs4 import BeautifulSoup


# The URL of the AWS EC2 service authorization page
url = "https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html"

# Actions are all at:
# https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Operations.html


# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code != 200:
    print("Failed to retrieve the page. Status code:", response.status_code)


# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find the table containing the data (you may need to inspect the page source to find the exact table)
table = soup.find("table")

# Initialize an empty list to store the data
data = []

# Loop through the rows of the table
for row in table.find_all("tr"):
    # Extract the text from each cell in the row
    cells = row.find_all("td")
    row_data = [cell.text.strip() for cell in cells]
    
    # Append the row data to the data list
    data.append(row_data)

# Remove the header row if it exists (assuming it's the first row)
# if data and data[0]:
    # header = data.pop(0)

# Now 'data' contains the table data in a list of lists
# You can process, manipulate, or store it as needed
for row in data:
    if len(row) == 6:
        print('OH YEAH BAYBEE')
    print(row)
