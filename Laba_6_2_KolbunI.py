class Car:
    # тип кузова, марка, цена
    def __init__(self, body_type, model, price=1000):
        self.body_type = body_type
        self.model = model
        self.price = price


class Customer:
    # стаж вождения клиента, число аварий, времея сотрудничества с фирмой (в месяцах)
    def __init__(self, driving_experience, accident_num, partnership_months, is_regular_customer=False):
        self.driving_experience = driving_experience
        self.accident_num = accident_num
        self.partnership_months = partnership_months
        self.is_regular_customer = is_regular_customer

    @property
    def is_reg(self):
        if self.partnership_months >= 3:
            return True
        return False
