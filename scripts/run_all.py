# 다운로드 + 필터 자동 실행 스크립트

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.downloader import download_krx_valuation
from app.services.filter import get_filtered_stocks


print("sys.path:", sys.path)
print("cwd:", os.getcwd())

# 자동 다운로드
filename = download_krx_valuation()

# 결과 필터링
filtered = get_filtered_stocks()
print(f"\n🔥 필터링된 종목 수: {len(filtered)}개")
for stock in filtered:
    print(stock)
