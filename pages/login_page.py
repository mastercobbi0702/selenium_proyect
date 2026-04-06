from playwright.sync_api import Page, expect

class LoginPage:
    """ Page object para la clase Login. Aquí se encapsulan selectores y acciones para la página de login"""

    URL = '/login'

    def __init__(self, page: Page):
        self.page = page

        #Localizadores

        self.input_usuario = page.locator("#user-name")
        self.input_password = page.locator("#password")
        self.btn_login = page.locator("#login-button")
        self.msg_error = page.locator("[data-test='error']")

        #Acciones

        def navegar(self):
            self.page.goto(self.URL)

        def iniciar_sesion(self, usuario:str, password:str):
            self.input_usuario.fill(usuario)
            self.input_password.fill(password)
            self.btn_login.click()

        def verificar_error_contiene(self, texto:str):
            expect(self.msg_error).to_contain_text(texto)

        def obtener_mensaje_error(self) -> str:
            return self.msg_error.inner_text()

        def verificar_titulo_pagina(self):
            expect(self.page).to_have_title("Swag Labs")
        