import json
from typing import Any, Dict, List

import numpy as np
import pandas as pd
from src.custom_types import Metadata


def load_metadata(dir: str, filename: str) -> Metadata:
    """
    Loads the metadata from the given path.
    """
    with open(f"{dir}/{filename}") as f:
        metadata = json.load(f)

    return metadata


def load_preprocessed_data(dir: str, filename: str, metadata: Metadata):
    """
    Loads the preprocessed data from the given path and converts
    the columns to the correct data types based on the metadata.
    """
    df = pd.read_csv(f"{dir}/{filename}")

    types = metadata["types"]
    df = df.astype(types)

    return df


def merge_set(set: List[str], key: str, loaded_dataset: Dict[str, Dict[str, np.ndarray[Any, Any]]]):
    return np.concatenate(tuple(loaded_dataset[item][key] for item in set), axis=0)


def standardize(
    x: np.ndarray[str, Any], target_index: int, training_mean: np.float32, training_std: np.float32
):
    x[:, :, target_index] = (x[:, :, target_index] - training_mean) / training_std
    return x
