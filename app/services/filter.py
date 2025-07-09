# 필터링 로직 (PER/PBR/ROE 기준)

import pandas as pd
import glob
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def get_latest_excel_file():
    files = glob.glob(os.path.join(DATA_DIR, "*.xlsx"))
    latest_file = max(files, key=os.path.getctime)
    return latest_file

def get_filtered_stocks(per_max=10, pbr_max=1, roe_min=10):
    filepath = get_latest_excel_file()
    df = pd.read_excel(filepath)

    df = df[['종목명', '종목코드', 'PER', 'PBR', 'ROE', '시가총액']].copy()

    # 숫자 변환
    for col in ['PER', 'PBR', 'ROE']:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    filtered = df[
        (df['PER'] < per_max) &
        (df['PBR'] < pbr_max) &
        (df['ROE'] > roe_min)
    ].dropna()

    return filtered.to_dict(orient="records")
