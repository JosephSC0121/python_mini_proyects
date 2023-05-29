# Convert JSON to CSV
This project is a simple Python script that converts data from a JSON file to a CSV file. It serves as a convenient tool for transforming data in a specific format.

# How It Works
The script follows the following steps:

1.Reads the input data from the input.json file.
2.Converts the JSON data into a Python dictionary using the json.loads() function.
3.Constructs a CSV string by joining the keys of the first dictionary object.
4.Iterates over each dictionary object in the data.
5.Appends a new line to the CSV string for each dictionary object, containing the values for the keys "Name", "age", and "birthyear".
6.Writes the CSV string to the output.csv file.

# Usage

Ensure that you have Python installed on your system.
Place the input data in the input.json file. The data should be in valid JSON format with a list of dictionary objects.
Run the script by executing the command python script.py in the terminal.
After successful execution, the converted data will be available in the output.csv file.
