import xarray as xr


def main():

    ds = xr.open_dataset("/Users/darrenchung/Downloads/IMOS.nc")
    df = ds.to_dataframe()
    df.to_csv("/Users/darrenchung/Desktop/dataset.csv")


if __name__ == "__main__":
    main()
