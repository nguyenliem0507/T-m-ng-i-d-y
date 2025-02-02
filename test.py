from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time 


driver = webdriver.Chrome()
driver.maximize_window()


student_data_login = {
    'username': 'student1',
    'password': '@admin123'
}

student_data_reg = {
    'username': 'student2',
    'password': '@admin123',
    'fullname': 'John Doe',
    'dob': '13/01/2025',
    'gender': 'M',
    'phone': '0123456789',
    'email': 'testn@gmail.com',
    'new-phone': '0987654321',
    'new-email': 'test22@gmail.com'
}

tutor_data_login = {
    'username': 'tutor1',
    'password': '@admin123'
}

moderator_data_login = {
    'username': 'moderator1',
    'password': '@admin123'
}


def test_student(driver, data_reg, data_login, url = None):
    if not url:
        url = 'http://127.0.0.1:8000' 
    driver.get(url)
    time.sleep(0.5)

    try:
        # Test Register 
        driver.find_element(By.ID, 'register-tab').click()
        time.sleep(1)
        driver.find_element(By.ID, 'username').send_keys(data_reg.get('username'))
        driver.find_element(By.ID, 'password').send_keys(data_reg.get('password'))
        driver.find_element(By.ID, 'confirmPassword').send_keys(data_reg.get('password'))
        driver.find_element(By.ID, 'fullname').send_keys(data_reg.get('fullname'))
        driver.find_element(By.ID, 'birthdate').send_keys(data_reg.get('dob'))
        driver.find_element(By.ID, 'gender').send_keys(data_reg.get('gender'))
        driver.find_element(By.ID, 'phone').send_keys(data_reg.get('phone'))
        driver.find_element(By.ID, 'email').send_keys(data_reg.get('email'))
        driver.find_element(By.CLASS_NAME, "btn-success").click()
        time.sleep(0.5)
        
        # Test Login 
        driver.find_element(By.ID, 'loginUsername').send_keys(data_reg.get('username'))
        driver.find_element(By.ID, 'loginPassword').send_keys(data_reg.get('password'))
        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(0.5)

        # Test edit user info 
        driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/nav/div/a[1]').click()
        time.sleep(0.2)

        driver.find_element(By.ID, 'email-edited').send_keys(student_data_reg.get('new-phone'))
        driver.find_element(By.ID, 'phone-edited').send_keys(student_data_reg.get('new-email'))
        driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[1]/div/div[2]/form/button').click()
        time.sleep(0.5)

    except Exception as e:
        print(f"Error: {str(e)}")
        
    time.sleep(0.3)


def test_tutor(driver, data_login, url = None):
    if not url:
        url = 'http://127.0.0.1:8000'
    driver.get(url)
    time.sleep(0.5)
    try:
        # Test Login 
        driver.find_element(By.ID, 'loginUsername').send_keys(data_login.get('username'))
        driver.find_element(By.ID, 'loginPassword').send_keys(data_login.get('password'))
        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(0.5)
    except Exception as e:
        print(f'Error: {str(e)}')


def test_moderator(driver, data_login, url = None):
    if not url:
        url = 'http://127.0.0.1:8000'
    driver.get(url)
    time.sleep(3)

    try:
        # Test Login 
        driver.find_element(By.ID, 'loginUsername').send_keys(data_login.get('username'))
        driver.find_element(By.ID, 'loginPassword').send_keys(data_login.get('password'))
        driver.find_element(By.CLASS_NAME, 'btn-primary').click()
        time.sleep(0.5)
    except Exception as e:
        print(f"Error: {str(e)}")


def main():
    try:
        test_student(driver, student_data_reg, student_data_login, url = 'http://127.0.0.1:8000/student-login/')
        time.sleep(1)
        test_tutor(driver, tutor_data_login, url='http://127.0.0.1:8000/tutor-login/')
        time.sleep(1)
        test_moderator(driver, moderator_data_login, url='http://127.0.0.1:8000/moderator-login/')
    except Exception as e:
        print(f'Error: {str(e)}')
    finally:
        driver.quit()


if __name__ == '__main__':
    main()
