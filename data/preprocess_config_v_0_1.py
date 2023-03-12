import pandas as pd
from custom_types import Metadata

DATA_VERSION_MAJOR = 0
DATA_VERSION_MINOR = 1
RAW_DATA_DIR = "data/raw"
RAW_DATA_FILENAMES = [
    # "JFC_1995_2022.csv",
    # "AC_1995_2022.csv",
    # "BDO_1995_2022.csv",
    # "BPI_1995_2022.csv",
    # "SMC_1995_2022.csv",
    # "SM_1995_2022.csv",
    # "URC_1995_2022.csv",
    # "TEL_1995_2022.csv",
    # "MAXS_1995_2022.csv",
    # "PIZZA_1995_2022.csv",
    # "FB_1995_2022.csv",
    # "AUB_1995_2022.csv",
    # "CEB_1995_2022.csv",
    # "GLO_1995_2022.csv",
    # "2GO_1995_2022.csv",
    # "ACEN_1995_2022.csv",
    # "ALI_1995_2022.csv",
    # "AP_1995_2022.csv",
    # "DMC_1995_2022.csv",
    # "FGEN_1995_2022.csv",
    # "GMA7_1995_2022.csv",
    # "ICT_1995_2022.csv",
    # "MEG_1995_2022.csv",
    # "MPI_1995_2022.csv",
    # "SECB_1995_2022.csv",
    # "SMPH_1995_2022.csv",
    # "PAL_1995_2022.csv",
    # "MONDE_1995_2022.csv",
    # "JGS_1995_2022.csv",
    # "PGOLD_1995_2022.csv",
    # "FNI_1995_2022.csv",
    # "NOW_1995_2022.csv",
    # "MBC_1995_2022.csv",
    # "MBT_1995_2022.csv",
    # "TBGI_1995_2022.csv",
    # "PX_1995_2022.csv",
    # "RRHI_1995_2022.csv",
    # "MB_1995_2022.csv",
    # "DITO_1995_2022.csv",
    # "SCC_1995_2022.csv",
    # "MER_1995_2022.csv",
    "SEVN_1995_2022.csv",
]
OUTPUT_DIR = "data/processed"
WINDOW_SIZE = 6
FEATURES = [
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
]
TARGET_COLS = [
    "Close",
]
INDEX_COL = "Date"
REF_COLS = TARGET_COLS + [INDEX_COL]


def transform_data(df: pd.DataFrame):
    df["Date"] = df["Date"].astype("datetime64[ns]")
    df["Open"] = df["Open"].str.replace(",", "").astype("float32")
    df["High"] = df["High"].str.replace(",", "").astype("float32")
    df["Low"] = df["Low"].str.replace(",", "").astype("float32")
    df["Close"] = df["Close"].str.replace(",", "").astype("float32")
    df["Volume"] = df["Volume"].str.replace(",", "").astype("float32")
    return df


def create_windowed_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a windowed dataset from a dataframe.
    """

    df_windowed = pd.DataFrame()
    for i in range(WINDOW_SIZE, 0, -1):
        for col in FEATURES:
            col_name = f"{col}_t-{i}"
            df_windowed[col_name] = df[col].shift(i)
    for col in REF_COLS:
        col_name = f"{col}_t"
        df_windowed[col_name] = df[col]

    df_windowed = df_windowed.iloc[WINDOW_SIZE:]

    return df_windowed


def create_metadata(df: pd.DataFrame):
    metadata: Metadata = {
        "types": {},
        "window_size": WINDOW_SIZE,
        "features": FEATURES,
        "windowed_cols": [],
        "target_cols": [],
        "index_col": "",
    }
    for ref_col in REF_COLS:
        if ref_col in TARGET_COLS:
            metadata["target_cols"].append(f"{ref_col}_t")
        if ref_col == INDEX_COL:
            metadata["index_col"] = f"{ref_col}_t"
    for col in df.columns:
        dtype = df[col].dtype
        metadata["types"][col] = str(dtype)
        if col not in metadata["target_cols"] and col != metadata["index_col"]:
            metadata["windowed_cols"].append(col)

    return metadata


TRANSFORMS = [transform_data, create_windowed_dataset]
CREATE_METADATA = create_metadata
