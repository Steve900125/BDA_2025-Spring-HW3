# debug_mv_all.py
import pandas as pd
from Markowitz import Helper

helper = Helper()
std_paths = [
    "./Answer/mv_list_0.pkl",
    "./Answer/mv_list_1.pkl",
    "./Answer/mv_list_2.pkl",
    "./Answer/mv_list_3.pkl",
]

for idx, path in enumerate(std_paths):
    std = pd.read_pickle(path)
    your = helper.mv_list[idx][0]  # 取第 idx 組權重 DataFrame
    diff = (std - your).abs()
    mismatches = diff[diff > 1e-6].stack().reset_index()
    mismatches.columns = ["Date", "Asset", "Diff"]
    if mismatches.empty:
        print(f"MV variant {idx} ✓ all match")
    else:
        print(f"MV variant {idx} ✗ mismatches (前 5 筆)：")
        print(mismatches.head(), "\n")
