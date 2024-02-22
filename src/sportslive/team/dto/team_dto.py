class TeamRequestDTO:
    def __init__(self, request_data):
        self._data = request_data

    @property
    def names(self):
        return self._data.getlist('names')

    @property
    def logos(self):
        return self._data.getlist('logos')

class FakeTeamRequestDTO:
    def __init__(self, request_data):
        self._data = request_data

    @property
    def names(self):
        return self._data.get('names')

    @property
    def logos(self):
        return self._data.get('logos')

class TeamMakeDTO:
    def __init__(self, name: str, logo) -> None:
        self.name = name
        self.logo = logo