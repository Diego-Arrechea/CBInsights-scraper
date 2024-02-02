# CB Insights Scraper

This project is a scraper for CB Insights, designed to gather information on companies using the public API and web scraping. It provides functionalities to search for companies by name and obtain detailed information about a specific company, including logo, website, description, specifications, news, FAQs, competitors, and address.

## Features

- **Company Search**: Performs company searches by name.
- **Detailed Company Information**: Retrieves detailed information on specific companies, including:
  - Logo
  - Website
  - Description
  - Specifications (Founded Year, Stage, Total Raised, Last Raised)
  - Recent News
  - Frequently Asked Questions (FAQs)
  - Competitors
  - Address

## Installation

To install and run this project, follow this command:

   ```bash
   pip install cbinsights-scraper
   ```

## Usage

To use this scraper, you must first import and instantiate the \`CBInsights\` class from the \`cb_insights.py\` module. Then, you can use the \`company_search\` and \`company_info\` methods to search for companies and obtain detailed information, respectively.

### Example of Company Search

```python
from cbinsigths import CBInsights

cbi = CBInsights.Scraper()
search_results = cbi.company_search("Ferrari")
print(search_results)
```

### Example of Retrieving Detailed Company Information

```python
company_details = cbi.company_info("ferrari")
print(company_details)
```

## License

This project is licensed under the MIT License - see the \`LICENSE.md\` file for details.
