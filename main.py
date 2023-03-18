from bs4 import BeautifulSoup
import smtplib
import lxml
import requests
import os

URL = "https://www.mercadolibre.com.ar/apple-iphone-14-pro-max-128-gb-morado-oscuro/p/MLA19615329?pdp_filters=category:MLA1055#searchVariation=MLA19615329&position=1&search_layout=stack&type=product&tracking_id=572aae4a-c648-4eae-8640-a0073b0d9a50"

header = {

        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7"
}

response = requests.get(url=URL, headers=header)

feedback = response.text

soup = BeautifulSoup(feedback, "lxml")

price_tag = soup.find(name="span", class_="andes-money-amount__fraction")

price = price_tag.getText()

name_tag = soup.find(name="h1", class_="ui-pdp-title")

name = name_tag.getText()

amount = float(price)


my_email = "franco.loto1995@gmail.com"
password = os.environ.get('PASSWORD')

connection = smtplib.SMTP("Smtp.gmail.com", port=587)

if amount < 628.934:

    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"ALERTA: Mercado libre alerta Bajo Precio!\n\n{name} now ${amount}\n\nComprar ahora!\n{URL}")
    connection.close()