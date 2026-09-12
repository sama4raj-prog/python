class USA:
    def capital(self):
        print("Washington, D.C. is the capital of United States.")
    def language(self):
        print("English is our national language.")
    def type(self):
        print("USA is a developing country.")

class Bangladesh:
    def capital(self):
        print("Dhaka is the capital of Bangladesh.")
    def language(self):
        print("Bangla is our national language.")
    def type(self):
        print("Bangladesh is a developing country.")

class India:
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is our national language.")
    def type(self):
        print("India is a developing country.")

ind = India()
usa = USA()
bd = Bangladesh()

for country in ind,usa,bd:
    country.capital()
    country.language()
    country.type()