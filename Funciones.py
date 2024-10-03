

import os
import pandas as pd

def cargar_archivos(carpeta='data', archivos=['game_play_by_play_E2023.csv', 'game_pregame_teams_comparison_E2023.csv', 'game_report_E2023.csv', 'game_stats_E2023.csv','player_boxscore_stats_E2023.csv', 'player_stats_advanced_accumulated_E2023.csv','standings_E2023_28.csv','team_boxscore_stats_E2023.csv','team_stats_advanced_per_game_E2023.csv'], delimiter='\,'):
    """
    Carga cuatro archivos .txt desde la carpeta especificada.

    Args:
        carpeta (str): Carpeta donde están almacenados los archivos .txt.
        archivos (list): Lista de nombres de archivos .txt a cargar.
        delimiter (str): Delimitador que separa los valores en los archivos. Por defecto, es tabulación '\t'.

    Returns:
        dict: Un diccionario con los nombres de archivos como claves y los DataFrames como valores.
    """
    datos = {}
    
    for archivo in archivos:
        ruta = os.path.join(carpeta, archivo)
        try:
            # Leer el archivo .txt en un DataFrame de pandas
            df = pd.read_csv(ruta, delimiter=delimiter)
            datos[archivo] = df
            print(f"Archivo {archivo} cargado correctamente.")
        except Exception as e:
            print(f"Error al cargar {archivo}: {e}")
    
    return datos

# Ejemplo de uso
# Cargar los archivos archivo1.txt, archivo2.txt, archivo3.txt y archivo4.txt desde la carpeta 'data'
archivos=['game_play_by_play_E2023.csv', 'game_pregame_teams_comparison_E2023.csv', 'game_report_E2023.csv', 'game_stats_E2023.csv','player_boxscore_stats_E2023.csv', 'player_stats_advanced_accumulated_E2023.csv','standings_E2023_28.csv','team_boxscore_stats_E2023.csv','team_stats_advanced_per_game_E2023.csv']
datos = cargar_archivos(carpeta='data', archivos=archivos, delimiter=',')  # Cambia el delimitador si es necesario
