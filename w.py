from bs4 import BeautifulSoup
import openpyxl

# Read the HTML file
with open("amazon.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all div elements with the specified class
div_elements = soup.find_all("div", class_="puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v2laelakto18k82o7cy47f2sjt0 s-latency-cf-section puis-card-border")

# Create a new Excel workbook and add a worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active

# Add headers to the worksheet
worksheet.append(["Names", "Prices", "Reviews"])

# Extract information from each div element
for div in div_elements:
    # Find the span with class="a-size-medium a-color-base a-text-normal" for Names
    names_span = div.find("span", class_="a-size-medium a-color-base a-text-normal")
    names = names_span.text.strip() if names_span else ""

    # Find the span with class="a-price-whole" for Prices
    prices_span = div.find("span", class_="a-price-whole")
    prices = prices_span.text.strip() if prices_span else ""

    # Find the span with class="a-icon-alt" for Reviews
    reviews_span = div.find("span", class_="a-icon-alt")
    reviews = reviews_span.text.strip() if reviews_span else ""

    # Add the extracted information to the worksheet
    worksheet.append([names, prices, reviews])

# Save the workbook to an Excel file
workbook.save("Amazon_Info.xlsx")

print("Data has been extracted and saved to Amazon_Info.xlsx")
