# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "pandas",
#   "seaborn",
#   "matplotlib",
#   "scikit-learn",
# ]
# ///

# Import necessary libraries
import os  # For interacting with the operating system (e.g., file paths)
import sys  # For system-specific parameters and functions (e.g., exit codes)
import httpx  # For making HTTP requests to the API


import pandas as pd  # For data manipulation and analysis
import seaborn as sns  # For data visualization (statistical plotting)
import matplotlib.pyplot as plt  # For creating static, animated, and interactive visualizations
from sklearn.ensemble import IsolationForest  # For outlier detection
from sklearn.cluster import KMeans  # For clustering analysis
from sklearn.preprocessing import StandardScaler  # For scaling the data
from sklearn.impute import SimpleImputer  # For handling missing data

from dotenv import load_dotenv  # For loading environment variables from a .env file

# Load environment variables from .env file
load_dotenv()

# Constants for API URL and token
API_URL = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
API_TOKEN = os.environ.get("AIPROXY_TOKEN")  # Get the API token from environment variables

# Check if API_TOKEN is available; exit if not
if not API_TOKEN:
    print("Error: AIPROXY_TOKEN is not set in the environment.")
    sys.exit(1)

# Function to read CSV files
def read_csv_file(filename):
    try:
        return pd.read_csv(filename, encoding="utf-8")  # Try reading with UTF-8 encoding
    except UnicodeDecodeError:  # Handle the case when UTF-8 encoding fails
        print("Warning: UTF-8 encoding failed. Trying ISO-8859-1 (Latin-1).")
        return pd.read_csv(filename, encoding="ISO-8859-1")  # Try reading with ISO-8859-1 encoding

# Function to perform data analysis
def analyze_data(df):
    # Separate numeric and non-numeric columns
    numeric_df = df.select_dtypes(include=["number"])  # Select only numeric columns
    non_numeric_df = df.select_dtypes(exclude=["number"])  # Select non-numeric columns
    
    # Handle missing values for numeric columns (fill with mean values)
    numeric_imputer = SimpleImputer(strategy='mean')
    df[numeric_df.columns] = numeric_imputer.fit_transform(numeric_df)  # Apply imputer to numeric columns
    
    # Handle missing values for non-numeric columns (fill with most frequent values)
    non_numeric_imputer = SimpleImputer(strategy='most_frequent')
    df[non_numeric_df.columns] = non_numeric_imputer.fit_transform(non_numeric_df)  # Apply imputer to non-numeric columns

    # Create a dictionary with the analysis results
    analysis = {
        "summary": df.describe(include="all").to_dict(),  # Summary statistics of the dataset
        "missing_values": df.isnull().sum().to_dict(),  # Count missing values in each column
        "correlation": numeric_df.corr().to_dict(),  # Correlation matrix for numeric columns
        "outliers": detect_outliers(df),  # Outlier detection
        "clusters": cluster_analysis(df),  # Clustering analysis
    }
    return analysis

# Function to detect outliers using Isolation Forest
def detect_outliers(df):
    numeric_df = df.select_dtypes(include=["number"])  # Select numeric columns
    if numeric_df.empty:  # Check if there are no numeric columns
        return "No numeric data for outlier detection."
    clf = IsolationForest(contamination=0.05, random_state=42)  # Initialize Isolation Forest for outlier detection
    outliers = clf.fit_predict(numeric_df)  # Fit the model to the data and predict outliers
    return pd.Series(outliers).value_counts().to_dict()  # Count the number of outliers

# Function to perform clustering analysis using KMeans
def cluster_analysis(df):
    numeric_df = df.select_dtypes(include=["number"])  # Select numeric columns
    if numeric_df.shape[0] > 1 and numeric_df.shape[1] > 1:  # Check if there's enough data for clustering
        scaler = StandardScaler()  # Initialize the StandardScaler to normalize the data
        scaled_data = scaler.fit_transform(numeric_df.dropna())  # Scale the numeric data
        kmeans = KMeans(n_clusters=3, random_state=42)  # Initialize KMeans with 3 clusters
        clusters = kmeans.fit_predict(scaled_data)  # Fit the KMeans model and predict cluster assignments
        cluster_centroids = pd.DataFrame(kmeans.cluster_centers_, columns=numeric_df.columns)  # Get centroids of clusters
        cluster_summary = {
            "cluster_counts": pd.Series(clusters).value_counts().to_dict(),  # Count the number of points in each cluster
            "centroids": cluster_centroids.to_dict(orient="list")  # Convert centroids to dictionary
        }
        return cluster_summary
    return "Insufficient data for clustering."  # Return message if data is insufficient for clustering

# Function to generate visualizations
def generate_visualizations(df, output_dir):
    charts = []  # Initialize list to store generated chart filenames
    numeric_df = df.select_dtypes(include=["number"])  # Select numeric columns

    # Correlation heatmap
    if numeric_df.shape[1] > 1:  # Only generate heatmap if there are multiple numeric columns
        plt.figure(figsize=(10, 6))  # Set figure size for heatmap
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")  # Create heatmap of correlation matrix
        plt.title("Correlation Matrix")  # Set the title of the heatmap
        plt.savefig(os.path.join(output_dir, "correlation_matrix.png"))  # Save heatmap to file
        charts.append("correlation_matrix.png")  # Add filename to charts list

    # Distribution plots for each numeric column
    for col in numeric_df.columns:
        plt.figure(figsize=(8, 5))  # Set figure size for distribution plot
        sns.histplot(numeric_df[col].dropna(), kde=True)  # Create histogram with KDE for the column
        plt.title(f"Distribution of {col}")  # Set the title of the plot
        filename = f"{col}_distribution.png"  # Generate filename for the plot
        plt.savefig(os.path.join(output_dir, filename))  # Save plot to file
        charts.append(filename)  # Add filename to charts list

    # Missing values heatmap
    if df.isnull().sum().any():  # Check if there are any missing values in the dataset
        plt.figure(figsize=(10, 6))  # Set figure size for missing values heatmap
        sns.heatmap(df.isnull(), cbar=False, cmap="viridis")  # Create heatmap of missing values
        plt.title("Missing Values Heatmap")  # Set the title of the heatmap
        filename = "missing_values_heatmap.png"  # Filename for missing values heatmap
        plt.savefig(os.path.join(output_dir, filename))  # Save heatmap to file
        charts.append(filename)  # Add filename to charts list

    return charts  # Return the list of chart filenames

# Function to send data to an LLM for narration
def send_to_llm(messages):
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",  # Authorization header with API token
        "Content-Type": "application/json",  # Content type for the API request
    }
    try:
        response = httpx.post(  # Send a POST request to the LLM API
            API_URL,
            json=messages,
            headers=headers,
            timeout=30.0  # Set a timeout of 30 seconds for the request
        )
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        return response.json()["choices"][0]["message"]["content"]  # Return the generated content from LLM
    except httpx.ReadTimeout:  # Handle read timeout exception
        print("Error: The request to the AI Proxy timed out. Try again later.")
        sys.exit(1)

# Function to narrate a story based on the analysis and charts
def narrate_story(analysis, charts, output_dir):
    prompt = f"""
    Create a README.md narrating this analysis:
    Data Summary: {analysis['summary']}
    Missing Values: {analysis['missing_values']}
    Correlation Matrix: {analysis['correlation']}
    Outlier Detection: {analysis['outliers']}
    Clustering Analysis: {analysis['clusters']}
    Attach these charts: {charts}.

    Key prompts to use:
    - Identify anomalies or surprising patterns from the analysis.
    - Suggest potential business decisions or insights based on clustering.
    - Explain why certain correlations are strong or weak.
    - Hypothesize causes for missing values and how to handle them.
    - Provide recommendations for future analysis or data collection.

    Additional Prompts:
    - What are the key trends or patterns in the dataset?
    - Summarize the structure and content of this dataset.
    - Suggest methods to handle missing data in this dataset.
    - Offer suggestions for enhancing the dataset's quality.
    """

    messages = [
        {"role": "system", "content": "You are a data analysis expert."},
        {"role": "user", "content": prompt},  # User's request
    ]
    narration = send_to_llm(messages)  # Send the prompt to the LLM for narration

    # Save the narration to a text file
    with open(os.path.join(output_dir, "narration.txt"), "w") as f:
        f.write(narration)  # Write the generated narration to a file

    print("Narration saved to 'narration.txt'")  # Confirmation message

# Main function to execute the entire workflow
def main(dataset_path, output_dir):
    df = read_csv_file(dataset_path)  # Read the dataset from the given path
    analysis = analyze_data(df)  # Analyze the data
    charts = generate_visualizations(df, output_dir)  # Generate visualizations
    narrate_story(analysis, charts, output_dir)  # Generate and save the story/narration

if __name__ == "__main__":
    # Ensure the dataset path and output directory are provided as arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <dataset_path> <output_dir>")
        sys.exit(1)
    
    dataset_path = sys.argv[1]  # Path to the dataset (CSV file)
    output_dir = sys.argv[2]  # Directory where output files will be saved

    if not os.path.exists(output_dir):  # Create the output directory if it doesn't exist
        os.makedirs(output_dir)

    main(dataset_path, output_dir)  # Run the main function
