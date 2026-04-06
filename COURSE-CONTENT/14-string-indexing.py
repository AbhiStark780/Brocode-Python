# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start :  end : step]
#               start index is inclusive (i.e character at this index is included)
#               end index is exclusive (i.e chartacter at this index is not included)

credit_number = "1234-5678-9012-3456"

# print(credit_number[0])
# print(credit_number[:4]) starting from 0 index to index 3 (not 4 because end index is exclusive)

# print(credit_number[5:9])
# print(credit_number[5:]) python assumes and include all the characters upto the end

# print(credit_number[-1]) this allows to access the elements in reverse order

# print(credit_number[::2]) this will include every third character of the string

# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")

# EXERCISE print the credit card number in reverse
credit_number = credit_number[-1::]
print(credit_number)

# EXERCISE to mask the email address of a user

user_email = "abhishek.tipiria@gmail.com"
mask_email = user_email[0] + "*" * (len(user_email)-11) + user_email[-11::1]
print(mask_email)