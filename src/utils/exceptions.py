class NoTextException(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.message = "Some text input is required."
