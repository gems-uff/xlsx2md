import pandas as pd
import sys

file = sys.argv[1]
df = pd.read_excel(file, "Cronograma", keep_default_na=False)

print('{: style="border-collapse: collapse; width: 100%; text-align: center;" border="1"}')
print('| Data | Atividade | Entrega')
print('|---')

previous = None
for index, row in df.iterrows():
    date = pd.to_datetime(row['Data'], errors='coerce').strftime('%d/%m/%Y')
    activity = row['Atividade']
    task = row['Entrega']

    if not pd.isnull(activity) and activity.strip():
        # Blue for exams
        if activity.startswith(('Prova', 'Segunda chamada', 'Verificação suplementar')):
            color = 'blue'
        # Green for assignment presentations
        elif activity.startswith('Apresentações de trabalhos'):
            color = 'green'
        # Black for activities that should not be highlighted, but should be shown
        elif activity.startswith('Apresentações de artigos'):
            color = 'black'
        # Red for optional activities and no class
        elif activity.startswith(('Sem aula', 'Vista de prova', 'Vista de avaliações')):
            color = 'red'
        else:
            color = None

        current = {
            'date': date, 
            'activity': f'<span style="color:{color}">{activity}</span>' if color else 'Aula', 
            'task': task
        }

        if previous:
            if current['date'] == previous['date']:
                if current['activity'] != previous['activity']:
                    current['activity'] = f'{previous["activity"]} <br/> { current["activity"]}'
                if current['task'] != previous['task']:
                    current['task'] = f'{previous["task"]} <br/> { current["task"]}'
            else:
                print(f'| {previous["date"]} | {previous["activity"]} | {previous["task"]}')
        
        previous = current

print(f'| {previous["date"]} | {previous["activity"]} | {previous["task"]}')
