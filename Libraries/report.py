from pytest_expect import expect

class Report:
    def __init__(self):
        pass

    __step_no = 1
    __step_active = False

    @staticmethod
    def reset_step_count():
        Report.__step_no = 1
        Report.__step_active = False

    @staticmethod
    def comment(string):
        for i in ('Tear Down', 'Test Case', 'Pre Condition'):
            if string.find(i) != -1:
                Report.__step_active = False
                break
        ident = '     ' + ' ' * len(str(Report.__step_no)) + '  '
        ident = ident if Report.__step_active else ''
        print(ident + string)

    @staticmethod
    def step(string=''):
        if not string:
            print('Step ' + str(Report.__step_no))
            Report.__step_no += 1
        else:
            print('Step ' + str(Report.__step_no) + ': ' + string)
            Report.__step_no += 1
        Report.__step_active = True

    @staticmethod
    def verify(actual, expected, fail_string):
        assert actual == expected, 'Step ' + str(Report.__step_no) + ': ' + fail_string
