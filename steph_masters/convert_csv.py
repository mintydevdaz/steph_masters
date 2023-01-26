import os
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

            # Construct new filename and end path. Save as CSV file.
            new_filename = d[:17]
            end_path = "/Users/darrenchung/Downloads/BOM_Rainfall Data_CSV/"
            i = f"{end_path}{new_filename}.csv"

            # Save file to end path
            df.to_csv(i, index=False)
            count += 1

        # Ignores hidden DS.store file
        except UnicodeDecodeError:
            continue

    print(f"Files saved: {count}")


if __name__ == "__main__":
    main()
