class MenuItem:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"MenuItem(name='{self.name}', description='{self.description}')"
