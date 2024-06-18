# Description: Command line Python script to load multiple dataframes into pandasGUI for analysis
import pandas as pd
from pandasgui import show
import sys

def load_dataframe(file_path, delimiter):
    try:
        # Load file into a DataFrame
        df = pd.read_csv(file_path, sep=delimiter, dtype=str, encoding='utf-8')
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading DataFrame from {file_path}: {e}")
        sys.exit(1)

def main():
    # Check if file path arguments are provided
    if len(sys.argv) < 2 or len(sys.argv) > 5:
        print("Usage: python script.py <file_path1> [<file_path2> <file_path3> <file_path4>]")
        sys.exit(1)

    file_paths = sys.argv[1:]

    dataframes = {}
    for file_path in file_paths:
        # Prompt user for delimiter
        delimiter = input(f"Enter the delimiter used in the file {file_path} (, | tab, etc...): ")
        # Load DataFrame with specified delimiter
        try:
            df = load_dataframe(file_path, delimiter)
            dataframes[file_path] = df
        except Exception as e:
            print(f"Error loading DataFrame from {file_path} with specified delimiter: {e}")
            sys.exit(1)

    # Show DataFrames using PandasGUI
    show(**dataframes)

if __name__ == "__main__":
    main()
