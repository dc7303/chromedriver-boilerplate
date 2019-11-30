import sys
import os
import atexit

from logger import setup_custom_logger
from chromedriver import generate_chrome, close_chrome


if __name__ == '__main__':
    logger = setup_custom_logger('main.py')
    logger.debug('Run crawler!!!!')
    PROJECT_DIR = str(os.path.dirname(os.path.abspath(__file__)))
    DOWNLOAD_DIR = f'{PROJECT_DIR}'

platform = sys.platform
driver_path = f'{PROJECT_DIR}/lib/webDriver/'
if platform == 'darwin':
    logger.debug('System platform : Darwin')
    driver_path += 'chromedriverMac'
elif platform == 'linux':
    logger.debug('System platform : Linux')
    driver_path += 'chromedriverLinux'
else:
    logger.error(f'[{sys.platform}] not supported. This library support only Linux, Darwin.')
    raise Exception()

# 크롬 드라이버 인스턴스 생성    
chrome = generate_chrome(
    driver_path=driver_path,
    headless=True,
    download_path=DOWNLOAD_DIR)
atexit.register(close_chrome(chrome))       # 스크립트 종료전 무조건 크롬 종료