from loguru import logger


class User:
    def __init__(self, name, age, gender, username, password):
        self.name = name
        self.age = age
        self.gender = gender
        self.username = username
        self.password = password

    def show_user_details(self):
        logger.info('User details.')
        logger.info(f'Name: {self.name}')
        logger.info(f'Age: {self.age}')
        logger.info(f'Gender: {self.gender}')