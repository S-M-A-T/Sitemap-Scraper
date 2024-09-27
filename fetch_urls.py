import requests
from bs4 import BeautifulSoup

# URL of the sitemap
sitemap_url = "https://www.abc.com/sitemap.xml?page=1"

# Fetch the sitemap
response = requests.get(sitemap_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the XML
    soup = BeautifulSoup(response.content, 'xml')

    # Find all <loc> tags and extract URLs
    urls = [loc.text for loc in soup.find_all('loc')]

    # Write URLs to a text file in the desired format
    with open('urls.txt', 'w') as file:
        file.write('urls = [\n')
        for url in urls:
            file.write(f'    "{url}",\n')
        file.write('    # Add other URLs as needed\n')
        file.write(']\n')

    print(f"Fetched {len(urls)} URLs and saved to urls.txt in the desired format.")
else:
    print(f"Failed to retrieve sitemap: {response.status_code}")
