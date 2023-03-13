class Dialogue:
    def __init__(self, name, message):
        self.name = name
        self.message = message
    
    def get_file_lines(self):
        """Gets a list of each line of this dialogue."""
        return {"name": f"{self.name}.txt", "lines": [f"{self.message}"]}
