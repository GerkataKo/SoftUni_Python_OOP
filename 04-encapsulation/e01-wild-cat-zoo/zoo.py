class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.animals = []
        self.workers = []
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

    def add_animal(self, animal, price):
        if len(self.animals) + 1 > self.__animal_capacity:
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) + 1 > self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        filtered_worker = [worker for worker in self.workers if worker.name == worker_name]
        if filtered_worker:
            self.workers.remove(filtered_worker[0])
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        amount_to_pay = sum([worker.salary for worker in self.workers])
        if amount_to_pay < self.__budget:
            self.__budget -= amount_to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        amount_to_pay = sum([animal.get_needs() for animal in self.animals])
        if amount_to_pay < self.__budget:
            self.__budget -= amount_to_pay
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]

        result = f"You have {len(self.animals)} animals" + "\n"
        result += f"----- {len(lions)} Lions:" + "\n"
        result += "{}".format('\n'.join([repr(l) for l in lions])) + "\n"
        result += f"----- {len(tigers)} Tigers:" + "\n"
        result += "{}".format('\n'.join([repr(t) for t in tigers])) + "\n"
        result += f"----- {len(cheetahs)} Cheetahs:" + "\n"
        result += "{}".format('\n'.join([repr(c) for c in cheetahs]))

        return result

    def workers_status(self):
        keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]

        result = f"You have {len(self.workers)} workers" + "\n"
        result += f"----- {len(keepers)} Keepers:" + "\n"
        result += "{}".format('\n'.join([repr(k) for k in keepers])) + "\n"
        result += f"----- {len(caretakers)} Caretakers:" + "\n"
        result += "{}".format('\n'.join([repr(c) for c in caretakers])) + "\n"
        result += f"----- {len(vets)} Vets:" + "\n"
        result += "{}".format('\n'.join([repr(v) for v in vets]))

        return result
