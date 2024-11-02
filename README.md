# CSV to Time Series Visualization App

## Overview
The **CSV to Time Series Visualization App** is a web application built using Streamlit, designed to enable users—data analysts, researchers, and anyone working with time-based data—to upload CSV files and create interactive, customizable time series visualizations effortlessly.

## Features
- **Easy CSV Upload**: Upload CSV files directly through the app interface.
- **Interactive Visualizations**: Generate time series plots based on user-selected date and value columns.
- **Data Preview**: View the first few rows of the uploaded data to confirm selection.
- **Input Validation**: Ensures that the selected value column is numeric and handles missing values.
- **Plot Customization**: Customize line color, plot type (line, bar, or area), and marker visibility.
- **Descriptive Statistics**: Get basic statistics (mean, median, etc.) for the selected value column.
- **Downloadable Plots**: Download the generated plots as image files.

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: For creating a user-friendly web application.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For data visualization.

## Installation
### Prerequisites
Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

Install the necessary packages:
```bash
pip install streamlit pandas matplotlib
```

### Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/kellertree/csv_visualize.git
```

### Install Required Packages
Navigate to the project directory and install all required packages:
```bash
cd csv_visualize
pip install -r requirements.txt
```

## Running the Application
You can start the app by running the following command:
```bash
streamlit run app.py
```
This command will launch the application locally, and you can access it in your web browser at `http://localhost:8501`.

### Running with VS Code Terminal
You can also run the app from VS Code’s terminal. Just ensure you're in the project directory before running the `streamlit run` command.

## Future Enhancements
- Support for additional visualization types (e.g., histograms, scatter plots).
- User interface enhancements for improved usability and aesthetics.


