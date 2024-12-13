# AutoAnalysis Project

## Overview

This project provides an automated data analysis tool that reads a CSV dataset, performs various analyses, generates visualizations, and narrates findings in a markdown format. It uses Python libraries such as Pandas, Scikit-learn, Seaborn, and Matplotlib for data manipulation, machine learning, and visualizations.

### Key Features:
- **Data Cleaning:** Automatically handles missing values in numeric and non-numeric columns.
- **Outlier Detection:** Uses Isolation Forest to identify outliers in numeric data.
- **Clustering Analysis:** Performs clustering using KMeans algorithm on numeric data.
- **Visualizations:** Generates correlation matrix, distribution plots, and missing values heatmaps.
- **Reports:** Narrates findings and insights in a detailed `README.md` format.

---

## Requirements

To run this script, ensure you have the following Python libraries installed:

```bash
pip install -r requirements.txt
