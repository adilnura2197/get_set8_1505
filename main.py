class Movie:
    cinema = "Magic Cinema"

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def show_info(self):
        print(f"Film: {self.title}")
        print(f"Yili: {self.year}")


m1 = Movie("Avatar", 2022)
m2 = Movie("Titanic", 1997)

m1.show_info()
print("----------")
m2.show_info()
