# 🚢 Titanic – Analyse et prédiction de la survie des passagers

## 📌 Présentation du projet

Dans le cadre d'une mission de Data Science pour un musée maritime, ce projet a pour objectif d'analyser les données des passagers du Titanic afin de répondre à la problématique suivante :

**Quels facteurs ont réellement influencé les chances de survie des passagers du Titanic ?**

À partir du dataset Titanic issu de Kaggle, nous avons réalisé un travail complet de préparation des données, d'analyse exploratoire et de modélisation afin d'identifier les facteurs associés à la survie des passagers et de construire des modèles prédictifs.

## 🎯 Objectifs du projet

Le projet s'articule autour de quatre grandes étapes :

1. **Analyse exploratoire (EDA)** : comprendre la structure du dataset, étudier les distributions, les corrélations et identifier les premières tendances.
2. **Nettoyage et transformation** : traiter les valeurs manquantes, encoder les variables catégorielles et créer de nouvelles variables pertinentes.
3. **Modélisation** : entraîner plusieurs algorithmes de classification pour prédire la survie des passagers.
4. **Évaluation et comparaison** : comparer les performances des modèles à l'aide de différentes métriques de classification.

## 📂 Structure du projet

```text
titanic-data-cleaning/
│
├── .git/
│
├── csv/
│   ├── dataset-titanic.csv
│   ├── gender_submission.csv
│   ├── test.csv
│   ├── train_clean.csv
│   └── train.csv
│
├── dataset-titanic.csv
│
├── DTC.ipynb
├── exploration.ipynb
├── main.ipynb
├── model_KNN.ipynb
├── reglog.ipynb
│
└── requirements.txt
```

### Description des fichiers

| Fichier | Description |
|---|---|
| `csv/` | Dossier contenant les différents fichiers CSV du projet. |
| `train.csv` | Données d'entraînement d'origine. |
| `train_clean.csv` | Jeu de données après nettoyage et préparation. |
| `gender_submission.csv` | Fichier de soumission de référence fourni par Kaggle. |
| `exploration.ipynb` | Notebook consacré à l'analyse exploratoire. |
| `main.ipynb` | Notebook principal du projet. |
| `model_KNN.ipynb` | Entraînement et évaluation du modèle KNN. |
| `reglog.ipynb` | Entraînement et évaluation de la régression logistique. |
| `DTC.ipynb` | Notebook dédié à l'étude d'un modèle de classification. |
| `requirements.txt` | Liste des dépendances Python nécessaires au projet. |

## 🧹 1. Nettoyage et transformation des données

Le dataset initial présente plusieurs problèmes qui nécessitent un travail de préparation avant la modélisation.

Les principales opérations de préparation comprennent :

**Gestion des valeurs manquantes**
- Vérification des doublons
  
**Gestion des valeurs manquantes**
- Traitement des valeurs manquantes dans `Age` (environ 20 % des données).
- Suppression de la variable `Cabin`, qui comporte plus de 75 % de valeurs manquantes.
- Traitement des valeurs manquantes dans `Embarked`.

**Feature Engineering**

Création de nouvelles variables à partir des données existantes :
- Extraction du titre des passagers (`Mr`, `Mrs`, `Miss`, `Master`, etc.) depuis la colonne `Name`.
- Création d'une variable `IsAlone` permettant d'identifier les passagers voyageant seuls.

**Encodage des variables catégorielles**
- Encodage de `Sex`.
- Encodage de `Embarked` à l'aide pd.get_dummies().
- Encodage "title" avec pd.get_dummies()
- Encodage des éventuelles nouvelles variables catégorielles.

**Nettoyage final du dataset**
- Suppression des colonnes non pertinentes pour la prédiction

## 🔎 2. Analyse exploratoire des données (EDA)

La première étape consiste à comprendre les données disponibles et à identifier les variables susceptibles d'avoir une influence sur la survie.

Les principales analyses portent sur :

- Vérification des outliers
- Création d'un tableau de corrélation pour trouver les features avec le plus d'impact

Cette étape permet de formuler plusieurs hypothèses, notamment :
- Les femmes ont davantage survécu que les hommes.
- Les passagers de première classe ont bénéficié de meilleures chances de survie.
- Le prix du billet a une influence sur la survie

## 3. Création des modèles

Nous avons crée 3 modèles de classification entrainés et testés sur le même dataset df_clean :
- KNN : model_KNN.ipynb
- Logistic Regression : reglog.ipynb
- Random Forest :  DTC.ipynb

⚙️ Installation et utilisation

Prérequis

Python 3.10 ou supérieur

Jupyter Notebook

Git

1. Cloner le dépôt

git clone <URL_DU_DEPOT>

2. Accéder au projet

cd titanic-data-cleaning

3. Créer un environnement virtuel (recommandé)

python -m venv venv

Activation sous Windows :

venv\Scripts\activate

Activation sous Linux / macOS :

source venv/bin/activate

4. Installer les dépendances

pip install -r requirements.txt

5. Lancer Jupyter Notebook

jupyter notebook

Vous pourrez ensuite ouvrir les notebooks et exécuter les différentes étapes du projet.

🛠️ Technologies utilisées

Python : langage de programmation.

Pandas : manipulation et nettoyage des données.

NumPy : calcul numérique.

Matplotlib : visualisation des données.

Seaborn : visualisation statistique.

Scikit-learn : prétraitement, entraînement et évaluation des modèles.

Jupyter Notebook : environnement de développement et d'analyse.

Git / GitHub : gestion de versions et collaboration.

🎓 Compétences mobilisées

Ce projet permet notamment de travailler les compétences suivantes :

C34 – Nettoyage et transformation des données : gestion des valeurs manquantes, encodage des variables, feature engineering et réduction de dimensionnalité.

C39 – Analyse exploratoire des données : exploration statistique, visualisation, étude des corrélations et formulation d'hypothèses.

📚 Sources et ressources

Dataset Titanic – Kaggle

Documentation Pandas

Documentation Scikit-learn

Documentation Matplotlib

## 4. Comparaison des modèles


