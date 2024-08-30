## Addressing Current Issues

1. **Update `token_pairings.py`**
   - **Issue:** The `Update_token_pairings.py` script is not updating `token_pairings.py` as expected.
   - **Solution:** Check the path in `Update_token_pairings.py` and ensure it is correct. Verify that `token_pairings.py` exists in the specified location.

2. **Calculating Total Amount Required & Percentage**
   - **Issue:** The total amount required and percentage of the starting balance used are not updating correctly.
   - **Solution:** Ensure that the API call to BYBIT is correctly fetching the token price at the specified date and time. Debug the code to verify that the position size and leverage are properly used in the calculation.

## Adding Planned Features

1. **Chart for Total Trade Value**
   - **Description:** Implement a chart to visualize the total value of trades made with certain pairings.
   - **Suggestion:** Use a charting library such as [Chart.js](https://www.chartjs.org/) or [Plotly](https://plotly.com/python/).

2. **PnL Updates**
   - **Description:** Add functionality to calculate and display Profit and Loss (PnL) on the View Trades page.
   - **Suggestion:** Implement logic to update and show PnL based on trades and starting balance.

3. **User Login Page**
   - **Description:** Integrate a login system for user personalization.
   - **Suggestion:** Use a user authentication library like [Flask-Login](https://flask-login.readthedocs.io/en/latest/) for Flask or Django's built-in authentication system.

4. **Strategies Page**
   - **Description:** Create a page where users can input and save their trading strategies.
   - **Suggestion:** Implement a dropdown menu for users to select their strategies when adding trades. This can be achieved using forms and dropdown components in your framework of choice.
