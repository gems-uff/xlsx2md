import pandas as pd
import sys

file = sys.argv[1]
df = pd.read_excel(file, "Cronograma", keep_default_na=False)

print('{: style="border-collapse: collapse; width: 100%; text-align: center;" border="1"}')
print('| Data | Atividade | Entrega')
print('|---')

for index, row in df.iterrows():
    date = pd.to_datetime(row['Data'], errors='coerce').strftime('%d/%m/%Y')
    activity = row['Atividade']
    task = row['Entrega']

    if not pd.isnull(activity) and activity.strip():
        if activity.startswith(('Prova', 'Segunda chamada', 'Verificação suplementar')):
            color = 'blue'
        elif activity.startswith(('Apresentação de trabalho', 'Vista de prova')):
            color = 'green'
        elif activity.startswith('Sem aula'):
            color = 'red'
        else:
            color = None

        if color:
            print(f'| {date} | <span style="color:{color}">{activity}</span> | {task}')
        else:
            print(f'| {date} | Aula | {task}')