from setuptools import setup, find_packages

setup(
    name="cbinsights-scraper",
    version="0.1.0",
    author="Diego Arrechea",
    author_email="diego.arrechea.job@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url="https://github.com/Diego-Arrechea/CBInsights-scraper",
    license="MIT",
    description="This project is a scraper for CB Insights, designed to gather information on companies using the public API and web scraping. It provides functionalities to search for companies by name and obtain detailed information about a specific company, including logo, website, description, specifications, news, FAQs, competitors, and address.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "requests",
        "beautifulsoup4",
    ],
    python_requires=">=3.6",
)
