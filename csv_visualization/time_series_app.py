import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the title of the app
st.title("CSV to Time Series Visualization")

# File uploader to upload the CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the first few rows of the dataframe
    st.write("Data Preview:")
    st.write(df.head())

    # Ensure the date column is in datetime format
    date_column = st.selectbox("Select the date column", df.columns)
    value_column = st.selectbox("Select the value column", df.columns)

    # Convert the selected date column to datetime
    df[date_column] = pd.to_datetime(df[date_column])

    # Set the date column as the index
    df.set_index(date_column, inplace=True)

    # Plot the data
    st.write(f"Time Series Visualization of {value_column} over {date_column}")
    
    plt.figure(figsize=(10, 5))
    plt.plot(df[value_column])
    plt.title(f'Time Series of {value_column}')
    plt.xlabel(date_column)
    plt.ylabel(value_column)
    plt.grid()
    
    # Show the plot in Streamlit
    st.pyplot(plt)

# Add a footer
st.write("Upload a CSV file containing date and value columns to visualize the time series data.")
