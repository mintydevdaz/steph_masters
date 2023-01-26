import os

import openpyxl
import pandas as pd


def main():
    # Open File Directory
    path = "/Users/darrenchung/Downloads/Rainfall data - BoM"
    directory = os.listdir(path)

    # Iterate through each file.
    count = 0
    for d in directory:
        try:
            # Open as Pandas DataFrame
            df = pd.read_csv(f"{path}/{d}")

            # Construct new filename and end path. Save as Excel file.
            new_filename = d[:17]
            end_path = "/Users/darrenchung/Downloads/BOM_Rainfall Data_EXCEL/"
            i = f"{end_path}{new_filename}.xlsx"

            # Save file to end path
            df.to_excel(i, index=False, engine="openpyxl")
            count += 1

        # Ignores hidden DS.store file
        except UnicodeDecodeError:
            continue

    print(f"Files saved: {count}")


if __name__ == "__main__":
    main()
