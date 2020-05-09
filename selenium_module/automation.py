from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Baixar web driver do browser escolhido e colocar no PATH do sistema antes de executar o script
# Ou colocar web driver no mesmo lugar que o script
# https://selenium-python.readthedocs.io/installation.html#drivers

opcoes_chrome = Options()
opcoes_chrome.add_argument("--incognito")
opcoes_chrome.add_argument("--start-maximized")
# opcoes_chrome.add_argument("--headless")

driver = webdriver.Chrome(options=opcoes_chrome,
                          executable_path="./driver/chromedriver")
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

string_inserida = "Elemento encontrado!!"

user_message_input_text = driver.find_element_by_id("user-message")
user_message_input_text.send_keys(string_inserida)

user_message_btn = driver.find_element_by_css_selector(
    "form#get-input > button")
user_message_btn.click()

display_message_span = driver.find_element_by_id("display")
mensagem_texto_span = display_message_span.get_attribute("innerHTML")

if mensagem_texto_span != string_inserida:
    print("##Texto diferente")
else:
    print("->Texto certo!<-")

sum1_input_text = driver.find_element_by_id("sum1")
sum1_input_text.send_keys("700")

sum2_input_text = driver.find_element_by_id("sum2")
sum2_input_text.send_keys("77")

get_total_btn = driver.find_element_by_css_selector(
    "form#gettotal > button")
get_total_btn.click()

total_span = driver.find_element_by_id("displayvalue")
total_texto = total_span.get_attribute("innerHTML")

if int(total_texto) == 777:
    print("Soma correta!!")
else:
    print(f"Soma incorreta, valor encontrado: {total_texto}")

driver.close()
driver.quit()    