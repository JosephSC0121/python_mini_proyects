## Area under curve

This project is a Python script for calculating the area under a curve and generating a LaTeX report with the results and a plot of the curve.

### Dependencies

Make sure you have the following dependencies installed:

- `sympy`
- `numpy`
- `matplotlib`
- `pylatex`

You can install them using `pip` with the following command:

```pip install sympy numpy matplotlib pylatex```


### How It Works

The script performs the following steps:

1. Accepts user input for the variable, function, lower limit, and upper limit of integration.
2. Calculates the area under the curve using SymPy.
3. Generates a plot of the curve and shades the area under the curve using Matplotlib.
4. Saves the plot as an image.
5. Creates a LaTeX document using the `pylatex` package.
6. Adds sections and subsections to the document with the expression, integral, result, and plot.
7. Saves the LaTeX document as a PDF file.

### Usage

1. Ensure that you have the required dependencies installed.
2. Run the script by executing the command `python script.py` in the terminal.
3. Enter the variable (e.g., 'x'), the function (e.g., 'x**2'), the lower limit, and the upper limit when prompted.
4. The script will generate a PDF report with the calculated area and a plot of the curve.
5. The PDF file will be saved in the same directory as the script.


## Convert JSON TO CSV

This project is a simple Python script that converts data from a JSON file to a CSV file. It serves as a convenient tool for transforming data in a specific format.

### How It Works

The script follows the following steps:

1. Reads the input data from the `input.json` file.
2. Converts the JSON data into a Python dictionary using the `json.loads()` function.
3. Constructs a CSV string by joining the keys of the first dictionary object.
4. Adds a new line after the first line of the CSV string.
5. Iterates over each dictionary object in the data.
6. Appends a new line to the CSV string for each dictionary object, containing the values for the keys "Name", "age", and "birthyear".
7. Writes the CSV string to the `output.csv` file.

### Usage

1. Ensure that you have Python installed on your system.
2. Place the input data in the `input.json` file. The data should be in valid JSON format with a list of dictionary objects.
3. Run the script by executing the command `python script.py` in the terminal.
4. After successful execution, the converted data will be available in the `output.csv` file.






