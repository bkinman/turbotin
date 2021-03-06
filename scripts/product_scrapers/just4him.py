from . import get_html, add_item
import re


def scrape(pbar=None):
    item, price, stock, link = ["", "", "", ""]
    data = []
    name = "just4him"
    url = "http://justforhim.com/catalog/index.php?main_page=index&cPath=72"

    soup = get_html(url)
    for category in soup.find_all('div', class_="categoryListBoxContents"):
        new_soup = get_html(category.find("a").get("href"))
        products = new_soup.find_all("tr", class_="productListing-odd")
        products += new_soup.find_all("tr", class_="productListing-even")
        for product in products:
            if "There are no products to list in this category." not in str(product):
                item = product.find(class_="itemTitle").get_text()
                price = re.findall(r"\$\d+\.\d{2}", product.find_all(class_="productListing-data")[-1].get_text())[0]
                stock = "In stock"
                link = product.find("a").get("href")
                item, price, stock, link = add_item(data, name, item, price, stock, link, pbar)

    return data
