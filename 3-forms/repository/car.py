class CarsRepository:
    def __init__(self):
        self.cars = [
            {"id": 1, "name": "Toyota Camry", "year": 2020},
            {"id": 2, "name": "Honda Accord", "year": 2019},
            {"id": 3, "name": "Ford Mustang", "year": 2021},
            {"id": 4, "name": "Chevrolet Tahoe", "year": 2018},
            {"id": 5, "name": "BMW X5", "year": 2022},
            {"id": 6, "name": "Mercedes-Benz C-Class", "year": 2017},
            {"id": 7, "name": "Audi A4", "year": 2019},
            {"id": 8, "name": "Tesla Model S", "year": 2023},
            {"id": 9, "name": "Nissan Altima", "year": 2021},
            {"id": 10, "name": "Hyundai Sonata", "year": 2020},
            {"id": 11, "name": "Volkswagen Passat", "year": 2018},
            {"id": 12, "name": "Subaru Outback", "year": 2022},
            {"id": 13, "name": "Mazda CX-5", "year": 2019},
            {"id": 14, "name": "Porsche 911", "year": 2023},
            {"id": 15, "name": "Jeep Wrangler", "year": 2021},
            {"id": 16, "name": "Dodge Charger", "year": 2017},
            {"id": 17, "name": "Chevrolet Silverado", "year": 2020},
            {"id": 18, "name": "GMC Yukon", "year": 2019},
            {"id": 19, "name": "Honda CR-V", "year": 2021},
            {"id": 20, "name": "Ford Explorer", "year": 2023},
            {"id": 21, "name": "Toyota RAV4", "year": 2018},
            {"id": 22, "name": "Lexus RX", "year": 2022},
            {"id": 23, "name": "Cadillac Escalade", "year": 2023},
            {"id": 24, "name": "Jaguar F-Pace", "year": 2020},
            {"id": 25, "name": "Kia Sportage", "year": 2019},
            {"id": 26, "name": "Volvo XC90", "year": 2018},
            {"id": 27, "name": "Land Rover Range Rover", "year": 2021},
            {"id": 28, "name": "Ferrari 488", "year": 2022},
            {"id": 29, "name": "Lamborghini Urus", "year": 2023},
            {"id": 30, "name": "Maserati Levante", "year": 2020}
        ]

    def save(self, car):
        if "id" not in car or not car["id"]:
            car["id"] = self.get_new_id()
        self.cars.append(car)
        return car
    
    def get_new_id(self):
        return len(self.cars)+1

    def find(self, name):
        cars = []
        name = name.lower()
        for car in self.cars:
            # print(name, car['name'])
            if name in car["name"].lower():
                print(name, car['name'])
                cars.append(car)
        if len(cars) > 0:
            print(cars)
            return cars
        else:
            return False
    
    def get_all(self):
        return self.cars
    
repository = CarsRepository()
repository.find('toyota')