import requests
from bs4 import BeautifulSoup
from cbinsigths.utils import (
    extract_text,
    extract_list,
)
import json


class Scraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
                "Accept": "*/*",
                "Accept-Language": "es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3",
                "Content-Type": "application/json",
                "x-datadog-origin": "rum",
                "x-datadog-sampled": "1",
                "x-datadog-sampling-priority": "1",
                "Origin": "https://www.cbinsights.com",
                "Connection": "keep-alive",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
            }
        )

    def company_search(self, query):
        json_data = {
            "query": query,
            "metadata": {
                "ip-address": "181.170.40.229",
                "url": "https://www.cbinsights.com/company/augtera-networks",
                "browser": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
                "device": "Win32",
            },
        }
        response = self.session.post(
            "https://www.cbinsights.com/public-pages-api/search",
            json=json_data,
        )
        try:
            return json.loads(response.text)
        except:
            return {"suggestions": []}

    def company_info(self, slug):
        """Obtiene información detallada de una compañía específica."""
        url = f"https://www.cbinsights.com/company/{slug}"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")

            # Usando funciones auxiliares para extraer información
            logo = extract_text(soup, "header.flex img", attribute="src")
            website = extract_text(soup, "a.color--blue", attribute="href")
            description = extract_text(soup, "p[data-test='description']")

            specifications = {
                spec.find("h2").text.strip(): spec.find("span").text.strip()
                for spec in soup.find_all("div", class_="Kpi_kpiItem__F9E52")
                if "Kpi_blur__m_90A" not in spec.find("span")["class"]
            }

            news = extract_list(
                soup, "div.LatestNews_newsContainer__wiYYI > div", "a", attribute="href"
            )

            questions = {
                li.find("p", class_="text-black")
                .text.strip(): li.find("p", class_="text-cbi-content")
                .text.strip()
                for li in soup.select("ul.FAQ_faqContainer__JnzL4 li")
            }

            competitors = [
                {
                    "Logo": (
                        comp.select_one("img").get("src", None)
                        if comp.select_one("img")
                        else None
                    ),
                    "Link": "https://www.cbinsights.com"
                    + comp.select_one("a").get("href", ""),
                    "Name": extract_text(comp, "a"),
                    "Description": extract_text(comp, "p"),
                }
                for comp in soup.select("div[data-test='who-to-watch-item']")
            ]

            address = {
                "street": extract_text(soup, "address p[data-test='street']"),
                "city": extract_text(
                    soup, "address p[data-test='city-state-zip']"
                ).split(", ")[0],
                "state": (
                    extract_text(soup, "address p[data-test='city-state-zip']").split(
                        ", "
                    )[1]
                    if len(
                        extract_text(
                            soup, "address p[data-test='city-state-zip']"
                        ).split(", ")
                    )
                    == 3
                    else ""
                ),
                "zip": extract_text(
                    soup, "address p[data-test='city-state-zip']"
                ).split(", ")[-1],
                "country": extract_text(soup, "address p[data-test='country']"),
            }

            return {
                "Logo": logo,
                "Website": website,
                "Description": description,
                "Specifications": specifications,
                "News": news,
                "FAQs": questions,
                "Competitors": competitors,
                "Address": address,
            }
        except requests.RequestException as e:
            print(f"Error al obtener información de la compañía: {e}")
            return None
