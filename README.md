Just tryna learn :)

Link: https://alpaca.markets/learn/building-an-end-to-end-trading-bot-using-alpacas-api-circleci-and-slack

## Main Files

- **config.yml**  
  For CircleCI to automate the building, testing, and deployment of software projects.

- **creds.cfg**  
  Configuration file containing Alpaca and Slack API keys.

- **trading_classes.py**  
  Contains the `TradingOpportunities` and `Alpaca` classes, which handle the logic for identifying trading opportunities and executing trades using the Alpaca API, respectively.

- **slack_app_notification.py**  
  Contains the `slack_app_notification` function, which generates a formatted string with a summary of the trades made by the bot and sends it as a Slack notification to your desired channel.

- **main.py**  
  The entry point of the application, which brings together the functionality of the `TradingOpportunities`, `Alpaca`, and `slack_app_notification` classes and functions.
