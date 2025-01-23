# 1 - Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Classe (Opcional)
class Teste_Produto():

    # 2.1 Atributos
    url = "https://www.saucedemo.com"                                               # endereço do site alvo

    # 2.2 Funções e Métodos
    def setup_method(self, method):                                                 # método de inicialização dos testes
        self.driver = webdriver.Edge()                                              # instancia o objeto do Selenium webdriver com o navegador(edge, chrome)
        self.driver.implicitly_wait(5)                                              # define o tempo de espera padrao por elementos em 5 segundos

    def teardown_method(self, method):                                              # encerra / destroi o objeto do selenium nwebdriver da memória
        self.driver.quit()


    def test_selecionar_produto(self):                                               # metodo de teste
        self.driver.get(self.url)                                                    # abre o navegador
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")      # escreve no campo user name
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")        # escreve a senha 
