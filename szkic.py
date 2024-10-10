from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Ścieżka do WebDrivera (upewnij się, że ścieżka jest poprawna)
PATH = "ścieżka/do/chromedriver"

# Funkcja logowania
def log_in(driver, username, password):
    # Otwórz stronę czatu
    driver.get("https://czateria.interia.pl")
    
    # Poczekaj, aż strona się w pełni załaduje
    time.sleep(5)

    # Znajdź i kliknij przycisk "Zaloguj się"
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Zaloguj się')]"))
    )
    login_button.click()

    # Poczekaj na formularz logowania
    time.sleep(2)

    # Wprowadź dane logowania
    username_input = driver.find_element(By.NAME, "login")
    password_input = driver.find_element(By.NAME, "password")

    username_input.send_keys(username)
    password_input.send_keys(password)

    # Wyślij formularz logowania
    password_input.send_keys(Keys.RETURN)

    # Poczekaj, aż strona się zaloguje
    time.sleep(5)

# Funkcja do nasłuchiwania wiadomości i odpowiadania
def chat_with_users(driver):
    # Wejdź do pokoju czatu (upewnij się, że poprawnie identyfikujesz pokój)
    # room_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Wejdź do pokoju')]")
    # room_button.click()

    # Znajdź pole tekstowe czatu
    chat_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "form-control"))
    )

    # Główna pętla nasłuchująca wiadomości i wysyłająca odpowiedzi
    while True:
        try:
            # Znajdź wiadomości użytkowników
            messages = driver.find_elements(By.CLASS_NAME, "message-class")  # Zaktualizuj selektor w zależności od strony

            # Przetwarzanie każdej wiadomości
            for message in messages:
                user_message = message.text
                print(f"Użytkownik napisał: {user_message}")

                # Prosta logika odpowiedzi
                if "hej" in user_message.lower():
                    reply = "Cześć! Jak się masz?"
                elif "co robisz" in user_message.lower():
                    reply = "Rozmawiam na czacie :)"
                elif "pa" in user_message.lower() or "bye" in user_message.lower():
                    reply = "Do zobaczenia!"
                else:
                    reply = "Ciekawe! Powiedz mi więcej."

                # Wprowadzenie odpowiedzi do okna czatu
                chat_input.send_keys(reply)
                chat_input.send_keys(Keys.RETURN)

                # Poczekaj chwilę przed kolejną wiadomością
                time.sleep(2)

        except Exception as e:
            print(f"Coś poszło nie tak: {e}")
            break

# Główna funkcja bota
def main():
    # Inicjalizacja WebDrivera
    driver = webdriver.Chrome(PATH)

    # Dane logowania (zastąp swoimi prawdziwymi danymi)
    username = "TwojaNazwaUżytkownika"
    password = "TwojeHasło"

    try:
        # Logowanie na czateria
        log_in(driver, username, password)

        # Nasłuchiwanie i odpowiadanie na wiadomości
        chat_with_users(driver)
    finally:
        # Zakończ działanie przeglądarki po zakończeniu rozmowy
        driver.quit()

if __name__ == "__main__":
    main()
