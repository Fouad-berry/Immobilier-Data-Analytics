# immobilier-data-analysis

## Problématique

Analyse des indicateurs immobiliers par commune en France, avec un focus sur l'année 2024 (possibilité d'étendre à la période 2014-2024). Quelles sont les tendances, les villes les plus dynamiques, et quelles recommandations business peut-on en tirer ?

## Méthode
- Collecte et nettoyage des données (dataset "Indicateurs immobiliers par commune et par année (2014–2024)" de data.gouv.fr)
- Ajout du nom des communes via correspondance code INSEE
- Analyses statistiques et visualisations (tendances, top villes, KPIs)
- Préparation d'une base PostgreSQL pour exploitation BI
- Création d'un dashboard Power BI

## Livrables
- Notebook Python (nettoyage, analyses, graphiques)
- Base PostgreSQL prête pour BI
- Dashboard Power BI (KPI, cartes, évolutions)
- Dataset nettoyé (communesdvf2024_clean.csv)
- Ce README

## Insights & Recommandations business
- Évolution du prix moyen au m² par année (focus 2024, ou sur toute la période)
- Top 10 des villes les plus chères (année 2024 ou toutes années)
- Dataset nettoyé prêt à l'emploi pour Power BI
- *(À compléter après analyse approfondie)*


## Lancement du projet

1. (Recommandé) Créer un environnement virtuel Python :
	```bash
	python3 -m venv .venv
	source .venv/bin/activate  # Sous Windows : .venv\Scripts\activate
	```

2. Installer les dépendances Python :
	```bash
	pip install -r requirements.txt
	```

3. Ouvrir le notebook dans VS Code ou Jupyter :
	- Aller dans le dossier `notebooks/`
	- Ouvrir `01_exploration_nettoyage.ipynb`

4. Exécuter les cellules du notebook une à une :
	- Le notebook va charger, nettoyer, enrichir et analyser les données.
	- Un fichier `communesdvf2024_clean.csv` sera généré dans `data/`.

5. (Optionnel) Ouvrir Power BI Desktop :
	- Importer `communesdvf2024_clean.csv` depuis le dossier `data/`
	- Créer le dashboard, puis sauvegarder le fichier `.pbix` dans le dossier `dashboard/`
