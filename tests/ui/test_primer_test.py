from playwright.sync_api import sync_playwright

def test_titulo_pagina():
    with sync_playwright() as p:
        #Para iniciar el browser
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        #Navegamos a la pagina
        page.goto("https://www.saucedemo.com/")

        #Validamos que el titulo sea el correcto
        assert page.title() == "Swag Labs"

        #Tomamos un screenshot
        page.screenshot(path="screenshot.png")

        #Cerramos el browser
        browser.close()