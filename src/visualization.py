import matplotlib.pyplot as plt

class Visualization:
    @staticmethod
    def plot_pie_chart(data, title, filename):
        labels = list(data.keys())
        sizes = list(data.values())
        
        # Debug print statements
        print(f"Labels: {labels}")
        print(f"Sizes: {sizes}")

        # Check if data is not empty
        if not labels or not sizes:
            print("No data available to plot pie chart.")
            return

        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title(title)
        plt.savefig(filename)
        print(f"Pie chart saved as {filename}")  # Debug print statement
        plt.show()