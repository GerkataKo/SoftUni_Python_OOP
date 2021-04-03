class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        """type: Heavy/Power"""
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    @property
    def used_memory(self):
        return sum([s.memory_consumption for s in self.software_components])

    @property
    def used_capacity(self):
        return sum([s.capacity_consumption for s in self.software_components])

    @property
    def available_memory(self):
        return self.memory - self.used_memory

    @property
    def available_capacity(self):
        return self.capacity - self.used_capacity

    def enough_capacity(self, software):
        return software.capacity_consumption <= self.available_capacity

    def enough_memory(self, software):
        return software.memory_consumption <= self.available_memory

    def install(self, software):
        if self.enough_memory(software) and self.enough_capacity(software):
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)
