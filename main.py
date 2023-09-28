import googlemaps
from selenium import webdriver
from selenium.webdriver.common.by import By

gmaps = googlemaps.Client(key='apiKey')

print(gmaps.directions('Gastgebgasse 1-7, 1230 Wien','Hauptbahnhof Wien', mode="transit"))

numberOfRoomsFrom = 2
primaryAreaFrom = 40
primaryAreaTo = 80
primaryPriceFrom = 600
primaryPriceTo = 1200

baseUrl = f"https://www.immobilienscout24.at/regional/wien/wien/wohnung-mieten?" \
          f"numberOfRoomsFrom={numberOfRoomsFrom}" \
          f"&primaryAreaFrom={primaryAreaFrom}" \
          f"&primaryAreaTo={primaryAreaTo}" \
          f"&primaryPriceFrom={primaryPriceFrom}" \
          f"&primaryPriceTo={primaryPriceTo}"


driver = webdriver.Edge()

print(f"Search url: {baseUrl}")

driver.get(baseUrl)
items = driver.find_elements(By.XPATH, "//ol/li[contains(@class, 'Item-item') and .//section]")
