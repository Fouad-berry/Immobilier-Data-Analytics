import pandas as pd

def load_main_dataset(path):
    """Charge le dataset immobilier principal."""
    return pd.read_csv(path)

def load_communes(path):
    """Charge le fichier de correspondance code INSEE <-> nom commune."""
    return pd.read_csv(path, sep=';')

def enrich_with_commune_name(df, communes):
    """Ajoute le nom de la commune au dataset principal."""
    return df.merge(communes[['CODGEO', 'LIBGEO']], left_on='INSEE_COM', right_on='CODGEO', how='left')

def clean_data(df):
    """Nettoie le dataset (suppression doublons, gestion valeurs manquantes)."""
    df = df.drop_duplicates()
    return df
