# DolarBot

- This simple telegram bot retrieves the "blue" values for buy and sell in argentina via the dolarsi API.
- It also gets the price of 1 USDT in ARS in Binance's P2P platform, using the criptoya.com API.
- When running main.py, it sends the user a short message with the latest values.
- More functionality can be added by adding more values aside from the "blue", such as official value, "Dólar Bolsa", but I deemed it unnecesary for my use case.
---
There can be many ways to implement this bot. Running the script as a cron job is an option, but I recently opted to run it periodically as an AWS Lambda function.