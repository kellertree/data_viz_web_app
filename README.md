# CSV to Time Series Visualization App

## Overview
The CSV to Time Series Visualization App is a web application built using Streamlit that allows users to upload CSV files and create interactive time series visualizations. This app is designed for data analysts, researchers, and anyone interested in visualizing time-based data effortlessly.

## Features
- **Easy CSV Upload**: Users can upload their CSV files directly through the web interface.
- **Interactive Visualizations**: Generate time series plots based on user-selected date and value columns.
- **Data Preview**: View a preview of the uploaded data before visualization.
- **Input Validation**: Ensure that the selected value column is numeric and handle missing values effectively.
- **Plot Customization**: Customize visualizations by choosing line color, plot type (line, bar, area), and whether to show markers.
- **Descriptive Statistics**: Display basic statistics of the selected value column for better insights.
- **Downloadable Plots**: Users can download the generated plots as image files.

## Technologies Used
- **Python**: The programming language used to develop the app.
- **Streamlit**: A Python library for creating web applications easily.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For generating visualizations.

## Installation
### Prerequisites
Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Clone the Repository
Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/kellertree/csv_visualize.git
```

### Install Required Packages
Navigate to the project directory and install the required packages:
```bash
cd csv_visualize
pip install -r requirements.txt
```

### Run the Application
Start the Streamlit app using the following command:
```bash
streamlit run app.py
```

Now, you can access the application in your web browser at `http://localhost:8501`.

## Future Enhancements
- Additional visualization types (e.g., histograms, scatter plots).
- Enhanced user interface features and design improvements.

