import netCDF4 as nc


def main():
    f = "/Users/darrenchung/Downloads/IMOS_aggregation_20230123T034522Z.nc"
    ds = nc.Dataset(f, "r")

    dct = ds.__dict__
    # for k, v in dct.items():
    #     print(f"{k}: {v}")

    print(ds.variables.values())


if __name__ == "__main__":
    main()
