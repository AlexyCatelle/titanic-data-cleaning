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

## K-Nearest Neighbors (KNN)

Le KNN prédit la classe d'un individu en fonction des classes de ses K plus proches voisins.

## Régression logistique

La régression logistique est un algorithme de classification permettant d'estimer la probabilité qu'un passager ait survécu.
Elle permet notamment d'étudier l'influence des différentes variables sur la probabilité de survie.

## Random Forest

Random Forest est un algorithme basé sur un ensemble d'arbres de décision.
Il combine plusieurs arbres afin d'obtenir une prédiction plus robuste et permet également d'étudier l'importance des variables dans les prédictions.

## 4. Comparaison des modèles

Trois modèles de classification ont été entraînés afin de prédire la survie des passagers du Titanic.

### Résultats

| Métrique | KNN | Régression logistique | Random Forest |
|---|---:|---:|---:|
| Accuracy Train | 86,22 % | 83,92 % | 84,83 % |
| Accuracy Test | 80,34 % | **80,52 %** | 79,82 % |
| Écart Train/Test | 5,88 pts | **3,40 pts** | 5,01 pts |

### Avantages et inconvénients

| Modèle | Avantages | Inconvénients |
|---|---|---|
| **KNN** | Simple à comprendre, capture les relations non linéaires. | Sensible à l'échelle des variables et au choix de K. |
| **Régression logistique** | Rapide, interprétable et fournit des probabilités. | Moins adaptée aux relations complexes et non linéaires. |
| **Random Forest** | Capture les interactions, gère les relations non linéaires et mesure l'importance des variables. | Plus difficile à interpréter et nécessite un réglage des hyperparamètres. |

### Conclusion

Les trois modèles obtiennent des performances relativement proches, avec une accuracy autour de 80 %.

La **régression logistique** obtient le meilleur score sur le jeu de test (80,52 %) et présente le plus faible écart entre les performances d'entraînement et de test. Elle offre donc le meilleur compromis parmi les résultats obtenus.

⚙️ Installation et utilisation

Prérequis

Python 3.10 ou supérieur

Jupyter Notebook

Git

1. Cloner le dépôt

git clone <URL_DU_DEPOT>

2. Accéder au projet

cd titanic-data-cleaning

3. Installer les dépendances

pip install -r requirements.txt

4. Lancer Jupyter Notebook

jupyter notebook

Vous pourrez ensuite ouvrir les notebooks et exécuter les différentes étapes du projet.

🛠️ Technologies utilisées

Python : langage de programmation.

Pandas : manipulation et nettoyage des données.

Matplotlib : visualisation des données.

Seaborn : visualisation statistique.

Scikit-learn : prétraitement, entraînement et évaluation des modèles.

re : Récupération des titres par RegEx

Jupyter Notebook : environnement de développement et d'analyse.

Git / GitHub : gestion de versions et collaboration.


📚 Sources et ressources

Dataset Titanic – Kaggle




