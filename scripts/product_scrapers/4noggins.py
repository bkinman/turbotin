from . import get_html, add_item


def scrape(pbar=None):
    item, price, stock, link = ["", "", "", ""]
    data = []
    name = "4noggins"
    url = "https://4noggins.com/tobacco/tinned-tobacco.html"

    soup = get_html(url)
    next_page = True
    while next_page:
        for product in soup.find_all("div", class_="product details product-item-details"):
            for element in product.find_all():
                if element.get("class"):
                    if " ".join(element.get("class")) == "price":
                        price = element.get_text()
                    if " ".join(element.get("class")) == "product-item-link":
                        itemraw = element.get_text().strip()
                        item = itemraw.translate({ord(":"): None})
                        link = element.get("href")
                    if " ".join(element.get("class")) == "stock unavailable":
                        stock = "Out of stock"
                if stock != "Out of stock":
                    stock = "In Stock"
            item, price, stock, link = add_item(data, name, item, price, stock, link, pbar)
        if soup.find("a", class_="action next"):
            soup = get_html(soup.find("a", class_="action next").get("href"))
        else:
            next_page = False

    return data
