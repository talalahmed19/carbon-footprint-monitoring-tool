from fpdf import FPDF

class ReportGeneration:
    def __init__(self, data):
        self.data = data
        self.pdf = FPDF()
        print("ReportGeneration class initialized.")  # Debug print statement

    def generate_report(self, filename):
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)
        self.pdf.cell(200, 10, txt="Carbon Footprint Report", ln=True, align='C')

        self.pdf.ln(10)
        self.pdf.cell(200, 10, txt=f"Energy Consumption: {self.data['energy_consumption']} kWh", ln=True)
        self.pdf.cell(200, 10, txt=f"Travel Distance: {self.data['travel']} km", ln=True)
        self.pdf.cell(200, 10, txt=f"Waste Production: {self.data['waste_production']} kg", ln=True)

        self.pdf.output(filename)
        print(f"Report generated: {filename}")