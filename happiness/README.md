# Analysis of Global Happiness and Socioeconomic Factors

## Data Summary

The analysis covers a dataset containing 2,363 entries with information about socio-economic factors and their correlation with happiness across 165 countries. The key attributes in the dataset include:

- **Country name:** Top country: Argentina (18 occurrences)
- **Year:** Ranges from 2005 to 2023, with an average year of 2014.76
- **Life Ladder:** Mean value of 5.48, with a minimum of 1.281 and a maximum of 8.019
- **Log GDP per capita:** Average value of 9.40, ranging from 5.527 to 11.676
- **Social support:** Mean value of 0.81, with values ranging from 0.228 to 0.987
- **Healthy life expectancy at birth:** Average is 63.40 years, ranging from 6.72 to 74.6 years
- **Freedom to make life choices:** Mean of 0.75, covering minimum and maximum values from 0.228 to 0.985
- **Generosity:** Very low mean value (0.00009772), with a minimum of -0.34 and maximum of 0.7
- **Perceptions of corruption:** Average is 0.74, with a range of 0.035 to 0.983
- **Positive affect and Negative affect:** Average positive affect is 0.65, while negative affect averages at 0.27.

### Missing Values
No missing data points were identified in any of the attributes, indicating a clean dataset for analysis.

### Correlation Matrix
The correlation matrix reveals several interesting relationships:

- **Life Ladder** shows a strong positive correlation with **Log GDP per capita (0.78)**, **Social support (0.72)**, and **Healthy life expectancy (0.71)**.
- **Freedom to make life choices** has a moderate positive correlation with **Life Ladder (0.54)** and **Social support (0.40)**.
- Notably, **Perceptions of corruption** negatively correlate with **Life Ladder (-0.43)**.
- The weak correlations with the year indicate that happiness factors are relatively stable over time.

## Key Trends and Patterns

- The strong correlations among socio-economic factors suggest that improvements in GDP and social support could lead to increases in the perceived quality of life.
- Interestingly, lower perceptions of corruption seem to correlate with higher life satisfaction, suggesting a potential area for policy intervention.
- The **Generosity** attribute shows negligible impact, indicating that altruism may not have a direct influence on life satisfaction.

## Anomalies and Outliers

- **Outlier Detection** identified 1,119 outliers (1 being positive and -1 negative). Anomalies in happiness scores can indicate regions with unique socio-political contexts affecting life satisfaction.

### Potential Causes of Detected Outliers
Outliers may arise from extreme poverty, war-torn areas, or regions with exceptionally high levels of GDP and social support, affecting overall happiness differently.

## Clustering Analysis

Three clusters were identified:

- **Cluster 1 (1,113 entries):** Represents countries with favorable conditions—high GDP, significant social support, and high healthy life expectancy.
- **Cluster 2 (835 entries):** Middle-ground countries with moderate indicators.
- **Cluster 0 (415 entries):** Countries exhibiting low life satisfaction metrics.

### Business Implications
- Understanding cluster characteristics can help organizations targeting regions for development work and investment. For example, focusing resources on Cluster 0 may yield high returns in terms of improved living conditions.

## Recommendations for Future Analysis

- **Additional Data Collection:** Gathering data on political stability, crime rates, and education levels could enhance understanding of life satisfaction.
- **Hypothesize Missing Values:** Although there are currently no missing values, ongoing data collection should account for behavioral variance and demographic shifts.
- **Longitudinal Study Design:** Future studies should take a longitudinal approach to track how changes in socio-economic conditions impact happiness over time.

## Conclusion

This analysis illustrates significant trends linking happiness, wealth, social support, and health. The insights derived from clustering and correlation can inform both governmental policy and business strategies, suggesting a need for targeted actions in countries lagging in happiness metrics. By leveraging these insights, stakeholders can prioritize interventions to improve life satisfaction and social welfare across various regions.

## Attachments
Please refer to the following charts for a visual representation of our findings:
- **Correlation Matrix:** ![correlation_matrix.png](correlation_matrix.png)
- **Year Distribution:** ![year_distribution.png](year_distribution.png)
- **Life Ladder Distribution:** ![Life Ladder_distribution.png](Life Ladder_distribution.png)
- **Log GDP per Capita Distribution:** ![Log GDP per capita_distribution.png](Log GDP per capita_distribution.png)
- **Social Support Distribution:** ![Social support_distribution.png](Social support_distribution.png)
- **Healthy Life Expectancy at Birth Distribution:** ![Healthy life expectancy at birth_distribution.png](Healthy life expectancy at birth_distribution.png)
- **Freedom to Make Life Choices Distribution:** ![Freedom to make life choices_distribution.png](Freedom to make life choices_distribution.png)
- **Generosity Distribution:** ![Generosity_distribution.png](Generosity_distribution.png)
- **Perceptions of Corruption Distribution:** ![Perceptions of corruption_distribution.png](Perceptions of corruption_distribution.png)
- **Positive Affect Distribution:** ![Positive affect_distribution.png](Positive affect_distribution.png)
- **Negative Affect Distribution:** ![Negative affect_distribution.png](Negative affect_distribution.png)

This comprehensive approach allows for better decision-making related to socio-economic interventions globally.