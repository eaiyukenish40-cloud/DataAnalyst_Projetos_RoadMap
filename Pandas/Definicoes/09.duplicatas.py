# %%

import pandas as pd

# Dictionary of 15 people (keys -> id, values -> dict with name and surename)
people = {
	1:  {"name": "Alice",    "surename": "Smith",     "salary": 4800.0},
	2:  {"name": "Bruno",    "surename": "Garcia",    "salary": 5200.0},
	3:  {"name": "Carla",    "surename": "Silva",     "salary": 4300.0},
	4:  {"name": "Diego",    "surename": "Fernandez", "salary": 6100.0},
	5:  {"name": "Elena",    "surename": "Martins",   "salary": 3900.0},
	6:  {"name": "Felipe",   "surename": "Oliveira",  "salary": 4500.0},
	7:  {"name": "Gabriela", "surename": "Costa",     "salary": 4700.0},
	8:  {"name": "Hugo",     "surename": "Ribeiro",   "salary": 4100.0},
	9:  {"name": "Irene",    "surename": "Nogueira",  "salary": 3800.0},
	10: {"name": "Joao",     "surename": "Pereira",   "salary": 3600.0},
	11: {"name": "Karina",   "surename": "Almeida",   "salary": 5400.0},
	12: {"name": "Lucas",    "surename": "Moreira",   "salary": 4000.0},
	13: {"name": "Marina",   "surename": "Soares",    "salary": 4700.0},
	14: {"name": "Nicolas",  "surename": "Lima",      "salary": 5800.0},
	15: {"name": "Olivia",   "surename": "Araujo",    "salary": 4200.0},
}

# Create a DataFrame from the dict
df = pd.DataFrame.from_dict(people, orient='index')

# Add duplicates: duplicate rows for ids 3 and 7 and append first two rows again
df_duplicates = pd.concat([df, df.loc[[3, 7]], df.head(2)], ignore_index=True)

# %%
df_duplicates.drop_duplicates(keep='last')
# %%

df2 = df_duplicates.sort_values(by='salary', ascending=False).drop_duplicates(subset=["name","surename"], keep='first') 

# %%
