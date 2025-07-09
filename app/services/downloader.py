# KRX 자동 다운로드 (Selenium)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import shutil
from datetime import datetime

DOWNLOAD_DIR = os.path.abspath("data")

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    prefs = {
        "download.default_directory": DOWNLOAD_DIR,
        "download.prompt_for_download": False,
        "directory_upgrade": True
    }
    options.add_experimental_option("prefs", prefs)
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def download_krx_valuation():
    driver = setup_driver()
    print("[*] KRX 사이트 접속 중...")
    driver.get("http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MD0101")
    time.sleep(2)

    # [시장별] → [주식] → [전종목시세] 선택
    driver.get("http://data.krx.co.kr/contents/MDC/MAIN/main/index.cmd")
    time.sleep(1)

    # 실제 데이터 페이지로 바로 진입
    driver.get("http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=110")
    time.sleep(1)

    # 투자지표 > [전체] 선택
    driver.execute_script("fnSearch('ALL')")
    time.sleep(3)

    # 엑셀 다운로드 클릭
    print("[*] 다운로드 중...")
    excel_btn = driver.find_element(By.CSS_SELECTOR, "a.btn-excel")
    excel_btn.click()
    time.sleep(5)

    driver.quit()

    # 최신 다운로드 파일명 탐색
    for file in os.listdir(DOWNLOAD_DIR):
        if file.endswith(".xls") or file.endswith(".xlsx"):
            timestamp = datetime.now().strftime("%Y%m%d")
            new_filename = f"market_valuation_{timestamp}.xlsx"
            shutil.move(os.path.join(DOWNLOAD_DIR, file), os.path.join(DOWNLOAD_DIR, new_filename))
            print(f"[+] 파일 저장 완료: {new_filename}")
            return new_filename

    raise FileNotFoundError("엑셀 파일 다운로드 실패 😭")

if __name__ == "__main__":
    download_krx_valuation()
