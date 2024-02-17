# Bubble Sort Algorithm in Python

## Description
This Python script demonstrates the implementation of the bubble sort algorithm, a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

## Usage
1. Ensure you have Python installed on your system.
2. Clone or download the repository containing the script.
3. Run the script using Python by executing the command:

    ```bash
    python bubble_sort.py [arguments]
    ```
    
    Replace `[arguments]` with a list of alphanumeric characters (letters and numbers) separated by spaces. If no arguments are provided, the script will use the default list from the configuration file.

4. The script will output the sorted array.

## Configuration
The configuration file `config.json` contains the default list of numbers to be sorted when no arguments are provided.

## File Structure
- `bubble_sort.py`: The Python script containing the implementation of the bubble sort algorithm.
- `config.json`: Configuration file containing the default list of numbers.
- `README.md`: This README file providing information about the script.



## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



## Testing
To run tests for the script, you can use the `test_bubble_sort.py` script provided in the `tests/` directory. Before running the tests, ensure that your current directory is set to the `tests/` directory.

```bash
cd /path/to/your/bubble_sort_python
python -m tests.test_bubble_sort
```