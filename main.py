from loguru import logger
import pandas as pd
from bank_class import Bank

logger.add('log_file.log', rotation='10 MB')


# df = pd.read_csv('E:\\bank_details.csv', sep=';')
# df = Bank
# A = [Bank(a.name, a.age, a.gender, a.username, a.password) for a in df.itertuples()]

chandu = Bank(name='chandu', age=25, gender='male', username='cha', password='hello')

# user.show_user_details()