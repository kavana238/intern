import pandas as pd
 
usernames = pd.Series([' Alice ', 'bob', ' CHARLIE '])

cleaned_usernames = usernames.str.strip().str.lower()
print(cleaned_usernames)

contains_a = cleaned_usernames.str.contains('a')
print(contains_a)
