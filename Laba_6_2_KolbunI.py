from typing import TypeVar, Generic, Iterator


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

    @property
    def discount(self):
        discount = 0
        if self.is_reg:
            discount += 0.1
        if self.accident_num == 0:
            discount += 0.1
        if self.driving_experience >= 3:
            discount += 0.1
        if self.driving_experience >= 10:
            discount += 0.05
        return 1 - discount


T = TypeVar('T')


class TypedArray(Generic[T]):
    def __init__(self, init: T):
        self.array = [init]
        self.type = type(init)

    def add(self, elem: T) -> None:
        if type(elem) is not self.type:
            raise TypeError('Value type incorrect')
        self.array.append(elem)

    def __iter__(self) -> Iterator[T]:
        return iter(self.array)

    def __len__(self) -> int:
        return len(self.array)

    def __getitem__(self, key) -> T:
        return self.array[T]


model = ['Suzuki Swift', 'Opel', 'KIA', 'Audi']
body_type = ['hatchback', 'sedan', 'SUV', 'two-door']
price = [1000, 2000, 6000, 3000]

if __name__ == '__main__':
    car1 = Car('sedan', 'BMW', 10000)
    t1 = TypedArray(car1)
    for m, b, p in zip(model, body_type, price):
        t1.add(Car(m, b, p))

    print('CARS THAT ARE AVAILABLE')
    for el in t1:
        print(el.model, el.body_type, el.price)

    driving_experience, accident_num, partnership_months = map(float, input("Enter your driving experience, number of "
                                                                 "accidents, partnership months: ").split(","))
    customer = Customer(driving_experience, accident_num, partnership_months)
    # print(customer.is_reg)
    max_price = float(input("Enter max price that you can afford: "))
    available = filter(lambda x: x.price*customer.discount <= max_price, t1)
    sum = 0
    for el in available:
        print(el.model, el.body_type, f'{el.price*customer.discount:.2f}')