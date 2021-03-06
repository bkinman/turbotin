from . import get_html, add_item
import time


def scrape(pbar=None):
    item, price, stock, link = ["", "", "", ""]
    data = []
    name = "pipenook"
    url = "https://www.thepipenook.com/store/c14/pipe-tobacco"

    soup = get_html(url)
    for cat in soup.find_all("a", class_="wsite-com-category-subcategory-link"):
        error = True
        wait_time = 2.75
        while error:
            try:
                new_soup = get_html("https://www.thepipenook.com" + cat.get("href"))
                wait_time = 2.75
                error = False
            except:
                time.sleep(wait_time)
                print("An Error Occurred: sleeping " + str(wait_time) + "s")
                wait_time = wait_time + 1
            pass
            for product in new_soup.find_all('div', class_="wsite-com-category-product-wrap"):
                if product.find("div",
                                class_="wsite-com-category-product-name wsite-com-link-text"):
                    item = product.find("div",
                                        class_="wsite-com-category-product-name wsite-com-link-text").get_text().strip()
                link = "https://www.thepipenook.com" + product.find("a").get("href")
                if product.find("div", class_="wsite-com-price"):
                    price = product.find("div", class_="wsite-com-price").get_text().strip()
                stock = "In Stock"
                if product.find_all("p", class_="category__out-of-stock-badge"):
                    stock = "Out of stock"

                item, price, stock, link = add_item(data, name, item, price, stock, link, pbar)

    return data
