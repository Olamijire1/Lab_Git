# ProcessDatatoFile Python Script

## Overview

This Python script defines a class, `ProcessDatatoFile`, which is designed to process numerical data, calculate statistics (total, average, maximum, and minimum values), and save the processed data to a JSON file. The script also provides functionality to load data from the file.

## Usage

1. **Add Data:**
   - Run the script, and it will prompt you to add data.
   - You can add data interactively by entering integer values when prompted.

2. **Default Data:**
   - If you choose not to add data interactively, the script will run with default data `[1, 2, 7, 4, 95]`.

3. **Process and Display Data:**
   - The script processes and displays the total, average, maximum, and minimum values of the provided data.

4. **Save Data to File:**
   - The processed data is saved to a JSON file named `data.json`.
   - If the file already exists, the script appends the new data to the existing content.

5. **Load Data from File:**
   - The script provides an option to load and display previously saved data from the `data.json` file.

## Running the Script

- Ensure that Python 3 is installed on your system.
- Run the script by executing the following command in the terminal:

  ```
  $ python3 process_data.py
  ```
- or
   ```
   $ ./process_data.py
   ```

## Dependencies

- The script uses the `json` module, which is a standard library in Python.

## Notes

- If the `data.json` file does not exist, it will be created when saving data for the first time.
- The script handles user input errors by prompting for valid integer values.
- Feel free to modify the script to suit your specific requirements.
```
