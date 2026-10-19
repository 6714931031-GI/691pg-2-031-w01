class Program:
    def __init__(self, program_id, name_th, name_en):
        self.program_id = program_id
        self.name_th = name_th
        self.name_en = name_en

    def __str__(self):
        return (
            f"Program ID: {self.program_id}\n"
            f"ชื่อหลักสูตร: {self.name_th}\n"
            f"Program Name: {self.name_en}"
        )

