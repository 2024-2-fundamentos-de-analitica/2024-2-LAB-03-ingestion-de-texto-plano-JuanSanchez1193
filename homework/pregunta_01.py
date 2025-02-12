import pandas as pd
import re

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    file_path = 'files/input/clusters_report.txt'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    data = []
    current_cluster = None
    
    for line in lines[4:]:  
        line = line.rstrip()
        
        if not line:
            continue  
        
        match = re.match(r'\s*(\d+)\s+(\d+)\s+([\d,]+)\s*%', line)
        if match:
            cluster = int(match.group(1))
            cantidad_palabras = int(match.group(2))
            porcentaje = float(match.group(3).replace(',', '.'))
            palabras_clave = line[match.end():].strip()
            current_cluster = [cluster, cantidad_palabras, porcentaje, palabras_clave]
            data.append(current_cluster)
        elif current_cluster:
            current_cluster[3] += ' ' + line.strip()

    for i in range(len(data)):
        data[i][3] = re.sub(r'\s+', ' ', data[i][3].replace(',', ', ')).strip()
        if data[i][3].endswith('.'):
            data[i][3] = data[i][3][:-1]  
    df = pd.DataFrame(data, columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])

    return df

print(pregunta_01())

