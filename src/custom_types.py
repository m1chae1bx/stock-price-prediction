from typing import Dict, List, TypedDict


class Metadata(TypedDict):
    types: Dict[str, str]
    window_size: int
    features: List[str]
    windowed_cols: List[str]
    target_cols: List[str]
    index_col: str
