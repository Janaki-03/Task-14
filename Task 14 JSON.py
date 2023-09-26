import requests

class CountryData:
    def __init__(self, url):
        self.url = url
        self.data = self.fetch_data()

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    def display_country_info(self):
        if self.data:
            for country_info in self.data:
                name = country_info.get("name", "N/A")
                currencies = country_info.get("currencies", [])
                currency_names = [currency.get("name", "N/A") for currency in currencies]
                currency_symbols = [currency.get("symbol", "N/A") for currency in currencies]
                print(f"Country: {name}")
                print(f"Currencies: {', '.join(currency_names)}")
                print(f"Currency Symbols: {', '.join(currency_symbols)}")
                print("=" * 50)

    def display_countries_with_dollar(self):
        if self.data:
            dollar_countries = [country for country in self.data if any(
                currency.get("code") == "USD" for currency in country.get("currencies", [])
            )]
            if dollar_countries:
                print("Countries with DOLLAR currency:")
                for country in dollar_countries:
                    print(country.get("name", "N/A"))
            else:
                print("No countries use DOLLAR as currency.")

    def display_countries_with_euro(self):
        if self.data:
            euro_countries = [country for country in self.data if any(
                currency.get("code") == "EUR" for currency in country.get("currencies", [])
            )]
            if euro_countries:
                print("Countries with EURO currency:")
                for country in euro_countries:
                    print(country.get("name", "N/A"))
            else:
                print("No countries use EURO as currency.")


# Usage
url = "https://restcountries.com/v3.1/all"
country_data = CountryData(url)

# Task 4: Display country information
country_data.display_country_info()

# Task 5: Display countries with DOLLAR as currency
country_data.display_countries_with_dollar()

# Task 6: Display countries with EURO as currency
country_data.display_countries_with_euro()