from data_validation import DataValidation

class DataInput:
    def __init__(self):
        self.data = {'energy_consumption': 0, 'travel': 0, 'waste_production': 0}
        print("DataInput class initialized.")  # Debug print statement

    def get_input(self):
        try:
            self.data['energy_consumption'] = float(input("Enter energy consumption (kWh): "))
            self.data['travel'] = float(input("Enter travel distance (km): "))
            self.data['waste_production'] = float(input("Enter waste production (kg): "))
        except ValueError as e:
            print(f"Invalid input: {e}")
            return False

        if not DataValidation.validate_data(self.data):
            print("Validation failed for the input data.")
            return False

        print("User input received.")  # Debug print statement
        return True

    def get_data(self):
        print("Returning collected data.")  # Debug print statement
        return self.data