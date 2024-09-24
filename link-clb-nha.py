from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Khởi tạo tùy chọn cho trình duyệt Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Chạy trình duyệt ẩn
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Tạo Service cho ChromeDriver
service = Service(executable_path='C:/Users/HUYNH/Downloads/chromedriver-win64/chromedriver.exe')

# Khởi tạo trình duyệt Chrome với Service
driver = webdriver.Chrome(service=service, options=options)

# Mở trang web Premier League
driver.get("https://www.premierleague.com/tables")

# Chờ một chút để trang tải
time.sleep(5)

try:
    # Tìm bảng xếp hạng
    table = driver.find_element(By.CLASS_NAME, 'clubList')
    
    # Lưu dữ liệu vào file
    with open('bxh_ngoai_hang_anh.txt', 'w', encoding='utf-8') as file:
        clubs = table.find_elements(By.CLASS_NAME, 'clubList__club')
        for club in clubs:
            name = club.find_element(By.CLASS_NAME, 'name').text
            link = club.find_element(By.CLASS_NAME, 'clubList__link').get_attribute('href')
            file.write(f'{name}: {link}\n')

    print("Dữ liệu đã được ghi vào file bxh_ngoai_hang_anh.txt")
except Exception as e:
    print("Không thể tìm thấy bảng xếp hạng trong thời gian chờ.")
    print(e)

# Đóng trình duyệt
driver.quit()

