# DolarBot

DolarBot is a simple Telegram bot that provides hourly information about currency prices, specifically focusing on the "blue" exchange rate in Argentina. It also retrieves the price of 1 USDT in ARS from Binance's P2P platform using the criptoya.com API. 

## Features

- Retrieves the "blue" values for buy and sell in Argentina via the dolarsi API.
- Retrieves the price of 1 USDT in ARS from Binance's P2P platform using the criptoya.com API.
- Sends users a short message with the latest currency values.
- Compares previous prices with current ones with an emoji embedded in the message.

## APIs

DolarBot utilizes the following APIs:

- [dolarsi API](https://www.dolarsi.com/): Provides the "blue" exchange rate values for buy and sell in Argentina.
- [criptoya.com API](https://criptoya.com/): Retrieves the price of 1 USDT in ARS from Binance's P2P platform.

## Packages

DolarBot relies on the following Python packages:

- [requests](https://docs.python-requests.org/en/latest/): A Python library for making HTTP requests to external APIs.
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html): The AWS SDK for Python, used for interacting with various AWS services.
- [json](https://docs.python.org/3/library/json.html): A built-in Python package for working with JSON data.
- [datetime](https://docs.python.org/3/library/datetime.html): A built-in Python package for working with dates and times.
- [dateutil](https://dateutil.readthedocs.io/): A Python library for working with dates, times, and timezones.

## Usage

To receive the latest currency prices and updates, you can join the DolarBot channel on Telegram by following this link: [DolarBot Channel](https://t.me/PrecioDolarBlue). 

## Deployment

The bot can be deployed in multiple ways. One option is to run the `main.py` script periodically as a cron job. In order to do this, one would need to modify the code to handle database queries properly.

Alternatively, you can deploy it as an AWS Lambda function to run it periodically. This is the implementation I chose due to ease of use.

Feel free to explore and extend the functionality of the bot by adding more currency values, such as the official exchange rate, "Dólar Bolsa", "Dólar MEP", etc. based on your specific requirements.

## Contributions

Contributions to the DolarBot project are welcome. If you have any suggestions, bug reports, or would like to contribute new features, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
