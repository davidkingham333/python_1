import requests
import urllib.parse
import os


class Lib:
    def __init__(self, author, name):
        self.author = author
        self.name = name

    def __str__(self):
        return f"Author: {self.author}, Name: {self.name}"

    def get_ISBN(self):
            
            try:
                with open('python','api_key.txt') as f:
                    api_key = f.read().strip()
            except ValueError:
                print("api_key not found")



            encoded_name = urllib.parse.quote(self.name)
            encoded_author = urllib.parse.quote(self.author)
            
            
            
            url = f"https://www.googleapis.com/books/v1/volumes?q={encoded_author}+{encoded_name}&key={api_key}"

            try:
                # Odeslání GET požadavku na API
                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json()
                    print(data)
                    # Kontrola, zda existují výsledky
                    if "items" in data and len(data["items"]) > 0:
                        # Vyhledání ISBN (13 pokud dostupné)
                        for identifier in data["items"][0]["volumeInfo"].get("industryIdentifiers", []):
                            if identifier["type"] == "ISBN_13":
                                return identifier["identifier"]
                    return "ISBN nebylo nalezeno."
                else:
                    return f"Chyba: {response.status_code}"

            except Exception as e:
                return f"Došlo k chybě: {str(e)}"


author = input("Zadejte jméno autora: ")
name = input("Zadejte název knihy: ")

# Vytvoření instance a vyhledání ISBN
book = Lib(author=author, name=name)
isbn = book.get_ISBN()
print(f"ISBN pro knihu '{book.name}' od autora '{book.author}': {isbn}")
