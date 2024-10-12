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

    # Select date and value columns
    date_column = st.selectbox("Select the date column", df.columns)
    value_column = st.selectbox("Select the value column", df.columns)

    # Convert the selected date column to datetime
    df[date_column] = pd.to_datetime(df[date_column])
    df.set_index(date_column, inplace=True)

    # Check for numeric values
    if not pd.api.types.is_numeric_dtype(df[value_column]):
        st.error("The selected value column must be numeric.")
    else:
        # Handle missing values
        if df[value_column].isnull().any():
            fill_option = st.radio("Missing values found. Choose how to handle them:", 
                                    ("Drop rows", "Fill with mean", "Fill with zero"))
            if fill_option == "Drop rows":
                df = df.dropna(subset=[value_column])
            elif fill_option == "Fill with mean":
                df[value_column] = df[value_column].fillna(df[value_column].mean())
            elif fill_option == "Fill with zero":
                df[value_column] = df[value_column].fillna(0)

        # Plot customization options
        line_color = st.color_picker("Pick a line color", "#00f")
        show_markers = st.checkbox("Show markers")
        plot_type = st.selectbox("Select plot type", ["Line", "Bar", "Area"])

        # Plot the data
        st.write(f"Time Series Visualization of {value_column} over {date_column}")

        plt.figure(figsize=(10, 5))
        if plot_type == "Line":
            plt.plot(df[value_column], color=line_color, marker='o' if show_markers else '')
        elif plot_type == "Bar":
            plt.bar(df.index, df[value_column], color=line_color)
        elif plot_type == "Area":
            plt.fill_between(df.index, df[value_column], color=line_color)

        plt.title(f'Time Series of {value_column}')
        plt.xlabel(date_column)
        plt.ylabel(value_column)
        plt.grid()

        # Show the plot in Streamlit
        st.pyplot(plt)

        # Download option
        plt.savefig("plot.png")
        with open("plot.png", "rb") as file:
            st.download_button("Download Plot", file, "plot.png", "image/png")

    # Add descriptive statistics
    st.write("Descriptive Statistics:")
    st.write(df[value_column].describe())

# Add a footer
st.write("Upload a CSV file containing date and value columns to visualize the time series data.")
st.write("For more information, visit [GitHub](https://github.com/kellertree/csv_visualize).")
