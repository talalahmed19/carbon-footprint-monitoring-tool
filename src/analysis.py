import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

class Analysis:
    def __init__(self, data):
        self.data = data
        print("Analysis class initialized.")  # Debug print statement

    def generate_summary(self):
        print("Generating summary.")  # Debug print statement
        return pd.DataFrame([self.data])

    def generate_visualizations(self):
        print("Generating visualizations.")  # Debug print statement
        df = self.generate_summary()

        plt.figure(figsize=(10, 5))
        df.plot(kind='bar', stacked=True)
        plt.title('Carbon Footprint Analysis')
        plt.xlabel('Activities')
        plt.ylabel('Values')
        plt.savefig('reports/visualization.png')
        print("Visualization saved as 'reports/visualization.png'.")  # Debug print statement
        plt.show()

    def trend_analysis(self, historical_data):
        df = pd.DataFrame(historical_data)
        trends = {}

        for col in df.columns:
            slope, intercept, r_value, p_value, std_err = linregress(range(len(df)), df[col])
            trends[col] = {'slope': slope, 'intercept': intercept, 'r_value': r_value,
                           'p_value': p_value, 'std_err': std_err}
            print(f"Trend analysis for {col}: {trends[col]}")  # Debug print statement

        return trends