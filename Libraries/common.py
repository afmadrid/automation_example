class Common:
    def __init__(self):
        pass

    @staticmethod
    def is_number(string):
        try:
            float(string)
            return True
        except ValueError:
            return False
