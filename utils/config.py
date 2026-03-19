from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://demo.saucedemo.com")
    USERNAME = os.getenv("USERNAME", "standard_user")
    PASSWORD = os.getenv("PASSWORD", "secret_sauce")
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "true")   
    SLOW_MO = int(os.getenv("SLOW_MO", 0))