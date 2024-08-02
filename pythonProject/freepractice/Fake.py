import pandas as pd
from faker import Faker

# 创建对象
fake = Faker()

# 生成数据
fake.name()
fake.text()
fake.address()
fake.email()
fake.date()
fake.country()
fake.phone_number()
fake.random_number(digits=5)

# 创建Dataframe
fakeDataframe = pd.DataFrame(
    {'date2':[fake.date() for i in range(5)],
    'name2':[fake.name() for i in range(5)],
    'email':[fake.email() for i in range(5)],
    'text':[fake.text() for i in range(5)]
     }
)
print(fakeDataframe)


data={'语文': [95,5,65],
     '数学': [149,45,78],
     '英语': [120,35,99]}
fakeDataframe = pd.DataFrame(data, index=['Jerry','mark','john'])
print(fakeDataframe)