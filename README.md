# Crypto Monitoring Application

## Overview

This application is designed to help users track and manage their cryptocurrency futures trades. It allows for the input and monitoring of various trade details, including token pairings, leverage, position sizes, and strategies. The app also provides tools to fetch historical price data and calculate key metrics like total value and profit and loss (PnL).

### Key Features:
- **Trade Management:** Input, edit, and track cryptocurrency trades with detailed information such as token pairing, leverage, position size, and more.
- **Historical Data Fetching:** Retrieve historical price data for specific tokens at given dates and times.
- **Calculations:** Automatically calculate total amount required for a trade based on leverage and starting balance, as well as the percentage of balance used.

## Current Issues

### 1. Updating `token_pairings.py`
- **Issue:** The `Update_token_pairings.py` script is not updating `token_pairings.py` as expected.
- **Solution:** Investigate and correct the path used in the script to ensure it accurately points to `token_pairings.py`. Verify the existence and accessibility of `token_pairings.py` in the specified directory.

### 2. Calculating Total Amount Required & Percentage
- **Issue:** The app is not correctly updating the total amount required and the percentage of the starting balance used.
- **Solution:** Ensure that the API call to BYBIT correctly fetches the token price at the specified date and time. Debug the code to confirm that the calculations involving position size and leverage are accurate.

### 3. Calibri Font Issue
- **Issue:** The Calibri font specified in the CSS is not being applied consistently across all pages.
- **Solution:** Review the CSS file to confirm that the Calibri font is correctly defined and linked. Check for potential conflicts with other styles that might be overriding the font settings.

## Planned Features

### 1. Chart for Total Trade Value
- **Description:** Implement a chart to visualize the total value of trades made with certain pairings.
- **Suggested Tool:** Consider using charting libraries such as [Chart.js](https://www.chartjs.org/) or [Plotly](https://plotly.com/python/) for dynamic and interactive charts.

### 2. PnL Updates
- **Description:** Add functionality to calculate and display Profit and Loss (PnL) on the View Trades page.
- **Suggested Implementation:** Integrate logic to update and display PnL based on trades and the starting balance, ensuring real-time accuracy.

### 3. User Login Page
- **Description:** Implement a login system to allow users to have personalized settings and data.
- **Suggested Tool:** Utilize Django's built-in authentication system to handle user login, registration, and session management.

### 4. Strategies Page
- **Description:** Create a dedicated page where users can input, save, and manage their trading strategies.
- **Suggested Implementation:** Use Django forms and dropdown components to allow users to select and apply strategies when adding new trades.
