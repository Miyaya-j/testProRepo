import random
import string
'''
创建随机验证码
python3中String模块ascii_letters和digits方法，其中ascii_letters是生成所有字母，从a-z和A-Z,digits是生成所有数字0-9.
在Python中，string.punctuation将给出所有的标点符号。
用法： string.punctuation
参数：由于它不是函数，因此不带任何参数。
返回值：返回所有标点符号。
注意：确保导入字符串库函数以便使用string.punctuation
random.sample:从序列中选择元素的k长度的新列表。
'''
total = string.ascii_letters + string.digits + string.punctuation
length = 16
password = "".join(random.sample(total, length))
print(password)
