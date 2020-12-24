# regular expression wild cards
import re

validtion = r'(?P<first_half>^[a-z0-9]+)([\._]?)([a-z0-9]+)([@])([a-z0-9]+)(\.)(?P<dns>com|net|mn)'

email = 'some.text@mail.com'

x = re.search(validtion, email, re.IGNORECASE)

print(x.group('dns'))


senteces = 'name BoB name john'

print(re.sub(r'[a-zA-Z]', '1', senteces))
