import streamlit as st
from PIL import Image
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
from pylab import rcParams
import matplotlib.pyplot as plt

import os   
      
      
# Your combined function
def display_notebook():

        # Display the project overview
        st.markdown("""
            # Project Overview
        
        In the rapidly evolving landscape of the technology sector, investor sentiment and market dynamics can significantly impact stock trading volumes. Apple Inc., as a leading technology company, has experienced notable fluctuations in its stock trading volume, particularly with a marked increase post-2020. This project aims to unravel the underlying causes of these volume changes and to forecast future movements in response to emerging trends and product developments. The challenge lies in accurately modeling these complex market behaviors and predicting how upcoming innovations, such as 'Apple Vision' and proprietary advancements in AI, may affect investor activity and trading patterns. A comprehensive understanding of these factors is crucial for investors and financial analysts seeking to optimize investment strategies. Utilizing historical stock price data, we will embark on a data-driven journey to extract insights and patterns through exploratory data analysis (EDA). Our endeavor will involve the development and optimization of predictive models, including ARIMA and SARIMA, both with and without the integration of exogenous variables, to forecast critical stock indicators such as opening and closing prices, as well as the volume of stocks traded.

        ## Key Objectives:

        - Conduct an exploratory data analysis (EDA) to uncover trends, seasonal patterns, and anomalies within the historical stock data of Apple.
        - Develop ARIMA and SARIMA models to capture the intrinsic time series characteristics and assess the impact of external factors on stock performance.
        - Evaluate the models' predictive accuracy on the test data using RMSE, ensuring the reliability and robustness of the forecasts.
        - Explore the practical implications of the forecasting results for investment strategies and market participation.
        
        ## My Work Summary:
        
        - Analyzed historical stock data, revealing a substantial increase in trading volume post-2020, coinciding with Apple's strategic market movements and global economic shifts
        - Implemented ARIMA and SARIMAX statistical models to identify patterns and seasonality in historical stock trading volumes.
        - Investigated market trends and product launches, linking heightened trading activity to key events such as Apple's stock split and the company's pivot to services and wearables.
        - Achieved an error rate of less than 2% compared to average trading volumes, demonstrating the model's strong predictive performance in a real-world scenario.
        - Interpreted diagnostic plots for model validation and optimized model configurations based on AIC for improved forecast precision.
        - Attained robust model evaluation metrics, with an RMSE of 3187.89 and a MAPE of 14.16%, reflecting high predictive accuracy.
        - Predicted future volume increases by synthesizing data with anticipated product releases, including "Apple Vision" and new AI advancements, positioning Apple at the forefront of innovation.
        - Utilized real-time data from Alpha Vantage API and SARIMAX modeling, incorporating external factors to refine forecasts and provide data-driven insights for investment strategies.
        
        ## Key Insights:
        
        - The 2020 stock split significantly augmented trading volume, enhancing Apple's market liquidity and accessibility to a broader range of investors. 
        - Upcoming product launches, bolstered by Apple's venture into AR/VR and AI technologies, are projected to sustain investor interest and amplify trading volumes through 2024. 
        - In-depth research and analysis underscore the importance of aligning stock volume trends with corporate growth milestones and broader industry trends for accurate forecasting.
        
        
        For a detailed exploration of the project, including the Jupyter notebooks, code, and datasets, please visit our [GitHub repository](https://github.com/joyboy5477/TimeSeriesForecasting/blob/main/appleStockAnalysis.ipynb).
        
        ---
           
        """)

 # Initialize your Alpha Vantage API key
API_KEY = 'KA1DZ9DAVS60XC5E'

def fetch_stock_data(symbol):
    # ts = TimeSeries(key=API_KEY, output_format='pandas')
    # data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
    data = pd.read_csv("applestock.csv", parse_dates=['date'], index_col='date')
    return data

def display_volume_analysis(data):
    st.subheader("Volume Analysis")
    rcParams['figure.figsize']= 15,8
    data.plot();
    plt.grid()

    # Convert the index to datetime to manipulate easily
    data.index = pd.to_datetime(data.index)

    # Date range selector
    start_date, end_date = st.select_slider(
        "Select date range for volume analysis:",
        options=data.index,
        value=(data.index.min(), data.index.max())
    )
    
    # Filter data based on selection
    filtered_data = data.loc[start_date:end_date]

    # Plotting
    st.line_chart(filtered_data['5. volume'])


# st.title("Apple Inc. (AAPL) Stock Volume Analysis")

#     # Fetch AAPL stock data
# data = fetch_stock_data('AAPL')

#     # Display data head
# st.write("Data Head:")
# st.dataframe(data.head())

#     # Display interactive volume analysis
# display_volume_analysis(data)



# Create sidebar
st.sidebar.title("Topics")
topic = st.sidebar.radio(
    'Select a topic:',
    ('View Jupyter Notebook', 'Introduction', 'Basics of Time Series', 'Components of Time Series', 'Types of Time Series', 'Different models in TSF', 'Test in Forecasting', 'ARIMA Model')
)

# Display Content Based on Topic Selection
if topic == 'View Jupyter Notebook':
    display_notebook()

elif topic == 'Introduction':
        #Add a Title and Introduction to Your App
    st.title('Time Series Forecasting Tutorial')

    st.write("""
    Welcome to the Time Series Forecasting Tutorial! This interactive web app will guide you through the fundamentals of time series analysis and forecasting.
    """)

    st.header('Introduction')
    st.write('Here we will introduce the basics of time series forecasting...')

elif topic == 'Basics of Time Series':
    st.header('What is Time Series?')
    st.write('A time series is a sequence of observations taken sequentially in time')

    st.header('What is Time Series Forecasting?')
    st.write('Time series forecasting uses information regarding historical values and associated patterns to predict future activity. Most often, this relates to trend analysis, cyclical fluctuation analysis, and issues of seasonality')

    st.header('Why Time Series Forecasting is important?')
    st.write('It is important because it helps us anticipate trends, make informed decisions, optimize resources, manage risks, and evaluate performance.')
    st.write('By analyzing time-ordered data, we gain insights, set goals, and plan for the future. Time series forecasting is applicable in various domains and supports real-time monitoring and decision-making. Every business operated under Risk and Uncertainty.')

# Add similar blocks for each topic...
    
elif topic == "Components of Time Series":
        st.header("What is TSF (Time Series Forecasting) is made of?")
        st.write("A time series is a sequence of data points typically measured at successive points in time, spaced at uniform time intervals. Time series forecasting is made up of several key components such as Trend, Seasonality, Cyclic patterns, Irregular component (Noise), and Level")
        
        st.header("What are this components?")
        st.markdown("""
                **Trend**: The long-term progression of the series. A trend can be increasing (upward), decreasing (downward), or stable (horizontal). It represents the general pattern of the data over time.

                **Seasonality**: The pattern that repeats at regular intervals over time, such as daily, weekly, monthly, or quarterly. Seasonality can be caused by various factors like weather, holidays, and school terms.

                **Cyclic patterns**: These are fluctuations observed at irregular intervals, longer than seasonal effects. Cycles are often related to economic conditions, such as business cycles that last several years.

                **Irregular component (Noise)**: After we extract level, trend, seasonality/cyclicity, what is left is noise. Noise is a completely random fluctuation in the data.

                **Level**: Any time series will have a base line. To this base line we add different components to form a complete time series. This base line is known as level..
    """)
        
        st.header("Lets See this component in Diagram")
        image_path = 'components.png' 
        st.image(image_path, caption='Components of Time Series', use_column_width=True)

        st.markdown("""
                 NOTE : It's important to note that not all time series will exhibit all four components. Some may only have a trend and residual component, while others may have all components present.""")
                 
elif topic == "Types of Time Series":
     st.header("What is TS Decomposition?")
     st.write("Time series decomposition is a statistical method used to break down a time series into its constituent components. Two types of decompostion namely Additive Decomposition and  Multiplicative Decomposition")

     st.markdown("""
            ### What is Additive Decomposition?

            **Definition**:  
            In an additive time series, the components add together to make the time series data. Here seasonal variation is roughly constant over time.
            **Formula**:  
            `Y_t = T_t + S_t + R_t`

            
            ### What is Multiplicative Decomposition?

            **Definition**:  
            In a multiplicative time series, the components multiply together to make the time series data. Here  seasonal variation changes proportional to the level of the time series
            **Formula**:  
            `Y_t = T_t * S_t * R_t`
                 
            Where:
            - `Y_t` is the data at time `t`,
            - `T_t` is the trend component at time `t`,
            - `S_t` is the seasonal component at time `t`, and
            - `R_t` is the residual (or irregular) component at time `t`.
            """)

# elif topic == "Flow of Analysis":

#         st.markdown("""
#                     ### Flow of Analysis 
#                     - Import the required libraries
#                     - Read and understand the data
#                     - Exploratory Data Analysis
#                     - Data Preparation
#                     - Time Series Decomposition 
#                     - Build and Evaluate 
#                     - Time Series Forecast
            
#                     """)
        
elif topic == "Different models in TSF":
      st.header("Time Series Models")
      # Models descriptions using markdown
      st.markdown("""
        Here are some of the most common models used for time series forecasting:

        - **ARIMA (AutoRegressive Integrated Moving Average)**: A model that captures autocorrelation in data along with trends and non-seasonal patterns.

        - **Seasonal ARIMA (SARIMA)**: Builds on ARIMA by adding the ability to model seasonal effects.

        - **Exponential Smoothing (ES)**: Assigns exponentially decreasing weights to past observations.

        - **Prophet**: A flexible model that handles trends and seasonalities with ease, particularly useful for data with strong seasonal patterns.

        - **Machine Learning Models**: These include advanced algorithms like Random Forests, GBMs, and neural networks (RNNs, LSTMs) that can capture complex relationships in data.
        """)
      
    # Models descriptions using markdown
      st.header("Examples")
      st.markdown("""
        Below are brief examples of how each time series forecasting model operates:

        - **ARIMA (AutoRegressive Integrated Moving Average)**: 
        For example, an ARIMA model can forecast future stock prices by analyzing the past trends and fluctuations of the stock market.

        - **Seasonal ARIMA (SARIMA)**: 
        As an instance, SARIMA could predict electricity demand which has clear patterns depending on the season of the year.

        - **Exponential Smoothing (ES)**: 
        Imagine using ES to forecast retail sales by giving more importance to recent months' sales data when predicting future sales.

        - **Prophet**: 
        For instance, Prophet could be used to predict website traffic by accommodating special events like holidays or sales that have a known impact on traffic.

        - **Machine Learning Models**: 
        For example, a neural network might predict future currency exchange rates by learning from a vast array of economic indicators and their historical values.
        """)
      

elif topic == "Test in Forecasting":
      st.header("Why not Regression?")
      st.markdown("""
                Time series data is characterized by its sequential order, and often, observations are not independent of each other. This temporal dependency means that traditional regression models, which assume independence of observations, may not be directly applicable without modifications.

                """)
      st.header("What is the main CornerStone?")
      st.markdown("""
                Autocorrelation is main problem. In regression analysis assume that errors (residuals) between the observed and predicted values are not autocorrelated, meaning the error for one time point is not correlated with the error for another. However, in time series data, autocorrelation of residuals is common due to the sequential nature of the data. 
                ***How do we identify this ?***
                ***Answer : Using  diagnostic tests  such as 1.  Durbin-Watson  2. Augmented Dickey-Fuller***
                  """)
      
      st.header("What is Durbin- Watson test?")
      st.markdown("""
                The Durbin-Watson test is a statistical test used to detect the presence of autocorrelation at lag 1 in the residuals from a regression analysis. Autocorrelation refers to the similarity of observations as a function of the time lag between them. The test statistic ranges from 0 to 4, where:

                - A value of 2 indicates no autocorrelation.
                - A value less than 2 suggests positive autocorrelation.
                - A value more than 2 implies negative autocorrelation.
                  
                ##### Simple Example

                    Consider a very simple dataset where we have observed values (y) and we fit a regression model to predict these values based on some independent variables (x). After fitting the model, we calculate the residuals (the difference between the observed and predicted values).

                    Let's say our residuals are: [-1, 0.5, -0.5, 1]

                    To apply the Durbin-Watson test, we calculate the differences between successive residuals, square these differences, and sum them up. Then, we divide this sum by the sum of the squared residuals.

                
                ##### Test Statistic :
                   
                - DW Statistic ~ 2.0: Indicates no autocorrelation. This is the ideal scenario, suggesting that the residuals from your regression model are independent across observations.
                - DW Statistic < 2.0: Suggests positive autocorrelation. A value significantly less than 2 indicates that the residuals are positively correlated. This might occur in time series where the current value is similar to its previous values.
                - DW Statistic > 2.0: Indicates negative autocorrelation. A value significantly greater than 2 suggests that the residuals are negatively correlated, meaning the current value is likely to be dissimilar to its previous values.

                """)
                                
      st.header("What is Augmented Dickey-Fuller?")
      st.markdown("""
                The Augmented Dickey-Fuller (ADF) test is a type of statistical test called a unit root test. Its primary use is to help determine whether a time series is stationary, which means its statistical properties do not change over time. Stationarity is an important assumption in time series analysis.

                ##### Simple Example

                    Imagine we have a time series that represents the yearly average temperature of a city. To determine if this time series is stationary, we can use the ADF test.

                ##### Test Statistic : 
                  
                  - ADF Statistic < Critical Value(s): If the test statistic is less than the critical value(s), you reject the null hypothesis, suggesting the time series does not have a unit root and is stationary. 
                                                     This means the time series does not depend on time, making it suitable for many statistical methods.
                  - ADF Statistic > Critical Value(s): If the test statistic is greater than the critical value(s), you fail to reject the null hypothesis, suggesting the time series has a unit root and is non-stationary.
                                                     This means the statistical properties of the series change over time.
                
                ##### Thumb Rule for Application
                - Stationarity Check: Always start with checking for stationarity in your time series data. Use the ADF test for this purpose. If your data is non-stationary, consider differencing the series or transforming it to achieve stationarity.
                - Autocorrelation Check: After fitting a regression model, use the Durbin-Watson test to check for autocorrelation in the residuals. If significant autocorrelation is present, your model may not be adequately capturing the data's structure, and you might need to consider other models or add lagged terms of the dependent variable or other predictors to account for the autocorrelation.
""")


elif topic == "ARIMA Model":
      st.header("What is ARIMA model?")
      st.markdown("""
                ## Understanding ARIMA Models and PDQ Parameters

                ARIMA, which stands for Autoregressive Integrated Moving Average, is a popular and widely used statistical method for time series forecasting. ARIMA models are capable of capturing a suite of different standard temporal structures in time series data.

                ### What is an ARIMA Model?

                ARIMA models are a class of statistical models for analyzing and forecasting time series data. They are used to describe and predict future points in the series based on past data. ARIMA is particularly suited for short to medium-term forecast models with data showing evidence of non-stationarity, where the mean and variance change over time.

                An ARIMA model is characterized by three primary parameters: (p, d, q), which are crucial to the behavior and efficacy of the ARIMA model.

                ### The PDQ Parameters Explained

                - **p (Autoregressive - AR term)**: Represents the number of lag observations included in the model. It's the part of the model that allows us to incorporate the effect of past values into our model. Essentially, it predicts the current value of the series based on its previous values. The 'p' parameter is identified by analyzing the Partial Autocorrelation Function (PACF) plot.

                - **d (Integrated - I term)**: Denotes the degree of differencing required to make the time series stationary. Differencing is the process of subtracting the current and previous observations. If the time series is already stationary, d=0. Otherwise, d corresponds to the number of differencing operations needed to stabilize the mean. The aim here is to remove trend and seasonality and make the series stationary.

                - **q (Moving Average - MA term)**: The size of the moving average window. It is the part of the model that allows us to incorporate the effect of past errors in the prediction equation. It represents the number of lagged forecast errors in the prediction equation. The 'q' parameter is identified by analyzing the Autocorrelation Function (ACF) plot.

                ### How to Choose PDQ Parameters?

                Choosing the right set of PDQ parameters is crucial for the ARIMA model's performance. This process typically involves:

                1. **Identification Stage**: Use plots of the data, ACF, and PACF to decide on the ARIMA model's orders (p, d, q).
                2. **Estimation and Testing**: Fit ARIMA models with different combinations of PDQ parameters, then use criteria like the Akaike Information Criterion (AIC) to compare the models.
                3. **Diagnostic Checking**: Once the model is fitted, check the residuals to ensure there are no patterns (meaning information that might be used for forecasting) left unexplained by the model.

                ### Implementing ARIMA in Python

                Python's `statsmodels` library provides the functionality to build ARIMA models easily. Users can specify their PDQ parameters directly or use automated techniques like `auto_arima` from the `pmdarima` library to find optimal parameters.

    
                """)
      