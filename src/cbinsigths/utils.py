from bs4 import BeautifulSoup


def extract_text(soup, selector, attribute=None, default=""):
    """Extrae texto de un elemento BeautifulSoup usando un selector CSS."""
    element = soup.select_one(selector)
    if attribute:
        return element.get(attribute, default) if element else default
    else:
        return element.text.strip() if element else default


def extract_list(soup, list_selector, item_selector, attribute=None):
    """Extrae una lista de textos o atributos de elementos."""
    items = []
    for element in soup.select(list_selector):
        if attribute:
            items.append(element.select_one(item_selector).get(attribute, ""))
        else:
            item = element.select_one(item_selector)
            if item:
                items.append(item.text.strip())
    return items
