from data_input import DataInput
from report_generation import ReportGeneration
from analysis import Analysis
from error_handling import ErrorHandling
from visualization import Visualization

def main():
    print("Starting Carbon Footprint Monitoring Tool...")  # Debug print statement
    data_input = DataInput()
    print("Initialized DataInput class.")  # Debug print statement

    if not data_input.get_input():
        ErrorHandling.handle_error("Invalid input. Exiting...")
        return
    print("User input received.")  # Debug print statement

    data = data_input.get_data()
    print(f"Data collected: {data}")  # Debug print statement

    report_gen = ReportGeneration(data)
    print("Initialized ReportGeneration class.")  # Debug print statement
    report_gen.generate_report("reports/report1.pdf")
    print("Report generated successfully.")  # Debug print statement

    analysis = Analysis(data)
    print("Initialized Analysis class.")  # Debug print statement
    analysis.generate_visualizations()
    print("Visualizations generated successfully.")  # Debug print statement

    historical_data = [
        {'energy_consumption': 400, 'travel': 150, 'waste_production': 45},
        {'energy_consumption': 450, 'travel': 160, 'waste_production': 50},
        {'energy_consumption': 500, 'travel': 200, 'waste_production': 55}
    ]
    analysis.trend_analysis(historical_data)
    print("Trend analysis completed.")  # Debug print statement

    Visualization.plot_pie_chart(data, "Carbon Footprint Distribution", "reports/pie_chart.png")
    print("Pie chart generated successfully.")  # Debug print statement

if __name__ == "__main__":
    main()