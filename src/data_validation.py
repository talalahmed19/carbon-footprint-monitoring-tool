class DataValidation:
    @staticmethod
    def validate_data(data):
        if data['energy_consumption'] < 0 or data['travel'] < 0 or data['waste_production'] < 0:
            print("All input values must be non-negative.")  # Debug print statement
            return False
        return True