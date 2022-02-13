from loguru import logger

logger.add('log_file.log', rotation='10 MB')


class Car:
    def __init__(self, registration_no, fuel_type, brake_system, top_speed, mileage, company, model, variant, price):
        self.registration_no = registration_no
        self.fuel_type = fuel_type
        self.brake_system = brake_system
        self.top_speed = top_speed
        self.mileage = mileage
        self.company = company
        self.variant = variant
        self.model = model
        self.price = price

    def show_details(self):
        print(self.company, self.model)
        vehicle = input('What kind of vehicle is it?')
        logger.debug(f'This is a {vehicle}.')
        logger.info(f'It is made by {self.company} .')
        logger.info(f'The model is {self.model} .')
        logger.info(f'It is registered under the number {self.registration_no} .')
        logger.info(f'It uses one litre {self.fuel_type} to run {self.mileage} kilometres.')
        logger.info(f'It can reach a top speed of {self.top_speed} kms/hour and is powered by {self.brake_system} brakes.')
        logger.info(f'It is a {self.variant}.')
        logger.info(f'It costs $ {self.price}.')


class Bike(Car):
    def __init__(self, registration_no, fuel_type, brake_system, top_speed, mileage, company, model, variant, price, engine, horse_power):
        super().__init__(registration_no, fuel_type, brake_system, top_speed, mileage, company, model, variant, price)
        self.engine = engine
        self.horse_power = horse_power

    def bike_details(self):
        self.show_details()
        logger.info(f'It is powered by a {self.engine} cc Engine and has a Horse Power of {self.horse_power} BHP.')

