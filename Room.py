class Room:
    def __init__(self, room_id, name, building):
        self.room_id = room_id
        self.name = name
        self.building = building

    def __str__(self):
        return (
            f"Room ID: {self.room_id}\n"
            f"Room Name: {self.name}\n"
            f"Building: {self.building}"
        )
