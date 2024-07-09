from selenium import webdriver
from selenium.webdriver.common.by import By
import sys


def test_scores_service(url):
    driver = webdriver.Chrome()
    driver.get(url)
    score = driver.find_element(By.XPATH, '//*[@id="score"]')
    score_text = score.text
    print(f"Score: {score_text}")
    if score_text.isdigit():
        score_to_int = int(score_text)
        return 1 <= score_to_int <= 1000
    else:
        return False

def main_function(url):
    if test_scores_service(url):
        return sys.exit(0)
    else:
        return sys.exit(-1)
