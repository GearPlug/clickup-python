
from datetime import datetime, timedelta


class Response:
    def __init__(self, original) -> None:
        self.original = original

        if "application/json" in self.original.headers.get("Content-Type", ""):
            self.data = self.original.json()
        else:
            self.data = self.original.content

    def __repr__(self) -> str:
        return "<Response [{}]>".format(self.status_code)

    @property
    def status_code(self):
        return self.original.status_code