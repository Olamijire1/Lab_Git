#!/usr/bin/env python3
"""Save processed data to a file."""
import json


class ProcessDatatoFile:
    """Class to process data and save to a file."""

    def __init__(self):
        self.__data = []

    def add_data(self, value: list):
        """Add data to the list."""
        self.__data.extend(value)

    def process_data(self):
        """Process data and display results."""
        if self.__data:
            total = sum(self.__data)
            average = total / len(self.__data)
            max_value = max(self.__data)
            min_value = min(self.__data)

            print("Data:", self.__data)
            print("Total:", total)
            print("Average:", average)
            print("Maximum Value:", max_value)
            print("Minimum Value:", min_value)
            print("", end='\n\n')
            return {'data': self.__data, 'total': total, 'average': average, 'max': max_value, 'min': min_value}
        else:
            print("No data available. Please add data first.")

    def save_to_file(self):
        """Save data to a text file."""
        try:
            with open('data.json', 'r') as file:
                old_val = json.load(file)
        except FileNotFoundError:
            old_val = []
        with open('data.json', 'w') as file: 
            value = self.process_data()
            old_val.append(value)
            json.dump(old_val, file)
            print(f"Data saved to data.json .", end='\n\n')

    def load_from_file(self):
        """Load data from a text file."""
        try:
            with open("data.json", 'r') as file:
                data = json.load(file)
                for val in data:
                    for k, v in val.items():
                        print(f"{k}: {v}")
                    print("", end='\n\n')
                print("Data loaded successfully from data.json.", end='\n\n')
        except FileNotFoundError:
            print(f"File 'data.json' not found.")


if __name__ == "__main__":
    demo = ProcessDatatoFile()

    ans = input("Do you want to add data? (y/n): ")
    if ans == 'y':
        data_val = []
        while ans == 'y':
            try:
                data_val.append(int(input("Enter the value: ")))
                ans = input("Do you want to add data? (y/n): ")
            except ValueError:
                print("Please enter an integer value.")
                continue
        demo.add_data(data_val)
    else:
        print("No data added, running with default data.", end="\n\n")
        
    # Add data
    demo.add_data([1, 2, 7, 4, 95])

    # Process and display data
    demo.process_data()

    # Save data to a file
    demo.save_to_file()

    # load from the file
    demo.load_from_file()