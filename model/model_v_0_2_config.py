import pandas as pd
from src.custom_types import Metadata

LEARNING_RATE = 0.001
MAX_EPOCHS = 100
PATIENCE = 50
VERSION_MAJOR = "0"
VERSION_MINOR = "2"
DATA_DIR = "data/processed/v_0_1"
DATA_FILENAME_MAP = {
    "AC": {"filename": "AC_1995_2022.csv", "metadata": "AC_1995_2022_metadata.json"},
    "BDO": {"filename": "BDO_1995_2022.csv", "metadata": "BDO_1995_2022_metadata.json"},
    "JFC": {"filename": "JFC_1995_2022.csv", "metadata": "JFC_1995_2022_metadata.json"},
    "MAXS": {"filename": "MAXS_1995_2022.csv", "metadata": "MAXS_1995_2022_metadata.json"},
    "FB": {"filename": "FB_1995_2022.csv", "metadata": "FB_1995_2022_metadata.json"},
    "URC": {"filename": "URC_1995_2022.csv", "metadata": "URC_1995_2022_metadata.json"},
    "BPI": {"filename": "BPI_1995_2022.csv", "metadata": "BPI_1995_2022_metadata.json"},
    "TEL": {"filename": "TEL_1995_2022.csv", "metadata": "TEL_1995_2022_metadata.json"},
    "SM": {"filename": "SM_1995_2022.csv", "metadata": "SM_1995_2022_metadata.json"},
    "SMC": {"filename": "SMC_1995_2022.csv", "metadata": "SMC_1995_2022_metadata.json"},
    "2GO": {"filename": "2GO_1995_2022.csv", "metadata": "2GO_1995_2022_metadata.json"},
    "ALI": {"filename": "ALI_1995_2022.csv", "metadata": "ALI_1995_2022_metadata.json"},
    "CEB": {"filename": "CEB_1995_2022.csv", "metadata": "CEB_1995_2022_metadata.json"},
    "AP": {"filename": "AP_1995_2022.csv", "metadata": "AP_1995_2022_metadata.json"},
    "FGEN": {"filename": "FGEN_1995_2022.csv", "metadata": "FGEN_1995_2022_metadata.json"},
    "NOW": {"filename": "NOW_1995_2022.csv", "metadata": "NOW_1995_2022_metadata.json"},
    "PGOLD": {"filename": "PGOLD_1995_2022.csv", "metadata": "PGOLD_1995_2022_metadata.json"},
    "FNI": {"filename": "FNI_1995_2022.csv", "metadata": "FNI_1995_2022_metadata.json"},
    "MBC": {"filename": "MBC_1995_2022.csv", "metadata": "MBC_1995_2022_metadata.json"},
    "MB": {"filename": "MB_1995_2022.csv", "metadata": "MB_1995_2022_metadata.json"},
    "MBT": {"filename": "MBT_1995_2022.csv", "metadata": "MBT_1995_2022_metadata.json"},
    "MEG": {"filename": "MEG_1995_2022.csv", "metadata": "MEG_1995_2022_metadata.json"},
    "RRHI": {"filename": "RRHI_1995_2022.csv", "metadata": "RRHI_1995_2022_metadata.json"},
    "TBGI": {"filename": "TBGI_1995_2022.csv", "metadata": "TBGI_1995_2022_metadata.json"},
    "PX": {"filename": "PX_1995_2022.csv", "metadata": "PX_1995_2022_metadata.json"},
}
TRAINING_SET = ["AC", "BDO", "FB", "MAXS"]
TEST_SET = [
    "JFC",  # Food, Beverage & Tobacco
    "SM",  # Holding Firms
    "ALI",  # Property
    "BPI",  # Banks
    "TEL",  # Telecommunications
    "NOW",  # Information Technology
    "CEB",  # Transportation Services
    "AP",  # Electricity, Energy, Power & Water
    "FNI",  # Mining
    "PGOLD",  # Retail
    "MBC",  # Media
]
VALIDATION_SET = [
    "URC",  # Food, Beverage & Tobacco
    "SMC",  # Holding Firms
    "MEG",  # Property
    "MBT",  # Banks
    # Telecommunications - None, as I plan to use GLO in training set
    "TBGI",  # Information Technology
    "2GO",  # Transportation Services
    "FGEN",  # Electricity, Energy, Power & Water
    "PX",  # Mining
    "RRHI",  # Retail
    "MB",  # Media
]
MODELS_DIR = "model"
LOAD_BASELINE_MODEL = True
BASELINE_MODEL_FILENAME = "v_0_1/model.h5"
TRAINING_SET_PREPROCESSING = [
    ("Volume", ["z-score"]),
]
LOSS_FUNCTION = "mean_squared_error"
METRICS = ["mean_absolute_error"]


def df_windowed_to_index_x_y(df: pd.DataFrame, metadata: Metadata):
    """
    Converts the windowed dataframe to a dataframe with the
    dates as the index and the features and targets as columns.
    """

    window_size = metadata["window_size"]
    feature_size = len(metadata["features"])
    windowed_cols = metadata["windowed_cols"]
    target_cols = metadata["target_cols"]
    index_col = metadata["index_col"]
    index_data = df[index_col].values
    feature_data = df[windowed_cols].values
    feature_data = feature_data.reshape(len(df), window_size, feature_size)
    target_data = df[target_cols].values

    return index_data, feature_data, target_data


GET_INDEX_X_Y = df_windowed_to_index_x_y
