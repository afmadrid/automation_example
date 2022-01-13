import logging

logger = logging.getLogger(name='test')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('logging_files/employee.log', mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class Employee:
    """A sample Employee class"""
    def __init__(self, first, last):
        self.first = first
        self.last = last
        logger.info(f'Created employee: {self.fullname} - {self.email}')

    @property
    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'
