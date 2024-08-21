data1 = ['Desktop', 'Notes', 'Commands', 'React', 'Veu', 'Private', 'Excel File.doc']
data2 = ['desktop', 'notes', 'commands', 'react', 'veu', 'private', 'excelFile']

data1 = str(data1).replace(' ', '').replace('doc', '').replace('.','').lower()
data2 = str(data2).lower().replace(' ', '')
print(data1)
print(data2)

assert data1 == data2
