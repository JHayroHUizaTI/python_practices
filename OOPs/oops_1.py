class person:
    # Constructor
    def __init__(self, name, old):
        """
        New person being created...!!!
        """
        self.name = name
        self.edad = old

    def walk(self):
        print(f"{self.name} you're walking")

    def running(self):
        print(f"{self.name} you're running")

    def __str__(self):
        """
        Retornarme una cadena de texto
        """
        return f"La persona se llama {self.name} y su edad es {self.edad}"


person1 = person("jhayro", 24)

print(person1)
