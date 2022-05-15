import random
import string
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
number = string.digits
symbols = "!@#$%^&*()_-+={[}]|:;'<>?/"
generate = lower_case + upper_case + number +symbols
pass_length = 12
password_gen = "".join(random.sample(generate , pass_length))
password = "Your Generated password is: " + password_gen
print(password)