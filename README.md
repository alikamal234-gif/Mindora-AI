# Mindora AI
### Prédiction du risque de santé mentale chez les étudiants

## 1. Présentation du projet

Mindora AI est un projet de Machine Learning qui vise à analyser les facteurs associés au bien-être et au risque de santé mentale chez les étudiants à partir d'un jeu de données.

Le projet consiste à développer un système de classification supervisée capable de classer les observations en trois catégories :

- Low
- Medium
- High

L'objectif est d'expérimenter différents modèles de classification, de comparer leurs performances et de développer une application interactive permettant de visualiser les résultats.

> **Important :** Ce projet est strictement pédagogique. Le modèle ne constitue pas un outil de diagnostic ou de dépistage clinique. Il ne doit pas être utilisé pour prendre des décisions concernant les étudiants.

---

## 2. Dataset

**Source :** [Student Mental Health Risk Prediction Dataset](https://www.kaggle.com/datasets/maqdadali/mental-health-risk-prediction-dataset-students)

Le dataset contient des informations concernant les étudiants, notamment :

- Informations générales : âge, genre et année d'étude.
- Habitudes quotidiennes : sommeil, activité physique et alimentation.
- Habitudes numériques : temps d'écran et utilisation des réseaux sociaux.
- Facteurs académiques : GPA et taux de présence.
- Facteurs personnels : soutien familial et stress financier.
- Historique de santé mentale.

**Variable cible :** `Mental_Health_Risk`

---

# 3. Étapes de réalisation

## Étape 1 — Chargement et analyse exploratoire des données (EDA)

### Objectif
Comprendre la structure du dataset, identifier les problèmes de qualité des données et analyser les relations entre les variables.

### Tâches à réaliser

- [x] Charger le dataset.
- [x] Examiner les dimensions du dataset.
- [x] Consulter les types de données.
- [x] Produire les statistiques descriptives.
- [x] Vérifier les valeurs manquantes.
- [x] Vérifier les doublons.
- [ ] Identifier les incohérences dans les données.
- [ ] Détecter les valeurs aberrantes.
- [x] Analyser la distribution de la variable cible.
- [x] Étudier les distributions des variables numériques et catégorielles.
- [x] Analyser les relations entre les variables explicatives et la cible.
- [ ] Examiner les corrélations entre les variables.
- [ ] Identifier les variables les plus associées à la variable cible.
- [ ] Rédiger une conclusion de l'analyse exploratoire.

**Livrable :** Notebook `01_eda.ipynb` contenant les analyses, visualisations et conclusions.

---

## Étape 2 — Transformation et préparation des données

### Objectif
Préparer les données pour l'entraînement des modèles tout en évitant le Data Leakage.

### 2.1. Nettoyage des données

- [x] Nettoyer les noms des colonnes.
- [x] Supprimer les doublons.
- [ ] Vérifier les valeurs incohérentes.
- [ ] Justifier les décisions de nettoyage.

### 2.2. Séparation des données

- [x] Séparer les variables explicatives `X` de la variable cible `Y`.
- [x] Supprimer `Student_ID` des variables utilisées pour l'entraînement.
- [x] Diviser les données en :
  - 80 % pour l'entraînement.
  - 20 % pour le test.
- [x] Utiliser `stratify` pour préserver la distribution des classes.

### 2.3. Prétraitement

- [x] Identifier les variables numériques.
- [x] Identifier les variables catégorielles.
- [x] Imputer les valeurs manquantes numériques.
- [x] Imputer les valeurs manquantes catégorielles.
- [x] Encoder les variables catégorielles avec `OneHotEncoder`.
- [x] Normaliser les variables numériques avec `MinMaxScaler`.
- [x] Regrouper les transformations dans un `ColumnTransformer`.
- [x] Intégrer le prétraitement dans un `Pipeline`.
- [ ] Vérifier le traitement des valeurs aberrantes.
- [ ] Étudier le déséquilibre des classes.
- [ ] Appliquer SMOTE ou une autre méthode uniquement si cela est justifié.

**Livrables :**
- `src/data/cleaning.py`
- `src/features/preprocessing.py`

---

## Étape 3 — Entraînement et comparaison des modèles

### Objectif
Entraîner plusieurs modèles de classification et comparer leurs performances sur les mêmes données.

### Modèles expérimentés

- [x] Decision Tree Classifier.
- [x] Support Vector Classifier (SVC).
- [x] K-Nearest Neighbors (KNN).

### Métriques d'évaluation

- [x] Accuracy.
- [x] Precision.
- [x] Recall.
- [x] F1-score.
- [x] Confusion Matrix.
- [x] Matthews Correlation Coefficient (MCC).
- [ ] ROC-AUC si pertinent pour le problème multiclasse.

### Résultats préliminaires

| Modèle | Accuracy | F1 Macro | MCC |
|---|---:|---:|---:|
| Decision Tree | 60.25 % | 0.60 | 0.4036 |
| SVC | 62.25 % | 0.63 | 0.4363 |
| KNN | 48.00 % | 0.47 | 0.2195 |

**Meilleur modèle provisoire : SVC**

Ces résultats sont préliminaires et devront être confirmés après optimisation et validation croisée.

### Tâches restantes

- [x] Entraîner les trois modèles.
- [x] Comparer leurs résultats.
- [x] Identifier le modèle le plus prometteur.
- [ ] Analyser les erreurs de classification.
- [ ] Visualiser les résultats dans des graphiques comparatifs.

**Livrables :**
- `src/models/training.py`
- `src/models/evaluation.py`

---

## Étape 4 — Optimisation et évaluation finale

### Objectif
Améliorer les performances des modèles et sélectionner le modèle le plus adapté au problème.

### Tâches à réaliser

- [ ] Sélectionner les modèles les plus prometteurs.
- [ ] Appliquer `GridSearchCV` ou `RandomizedSearchCV`.
- [ ] Optimiser les hyperparamètres du SVC.
- [ ] Comparer les performances avant et après optimisation.
- [ ] Utiliser Cross-Validation pour évaluer la stabilité des modèles.
- [ ] Sélectionner le modèle final.
- [ ] Évaluer le modèle optimisé sur le jeu de test indépendant.
- [ ] Générer la matrice de confusion finale.
- [ ] Analyser les erreurs de prédiction.
- [ ] Présenter les limites du modèle.
- [ ] Justifier le choix du modèle final.
- [ ] Sauvegarder le pipeline complet au format `.joblib`.

**Livrable :**

`models/best_model.joblib`

Le fichier doit contenir le pipeline complet, incluant le prétraitement et le modèle entraîné.

---

## Étape 5 — Orchestration avec Airflow et application Streamlit

### 5.1. Orchestration avec Apache Airflow

**Objectif :** Automatiser les différentes étapes du pipeline Machine Learning.

### Tâches à réaliser

- [ ] Configurer Apache Airflow.
- [ ] Créer un DAG pour le projet.
- [ ] Ajouter une tâche de préparation des données.
- [ ] Ajouter une tâche de prétraitement.
- [ ] Ajouter une tâche d'entraînement.
- [ ] Ajouter une tâche d'évaluation.
- [ ] Définir les dépendances entre les tâches.
- [ ] Configurer l'exécution planifiée du DAG.
- [ ] Vérifier le suivi des exécutions.
- [ ] Gérer les erreurs éventuelles.

**Livrable :** `dags/mindora_pipeline.py`

### 5.2. Application Streamlit

**Objectif :** Développer une interface interactive permettant de consulter les résultats du modèle et de tester des prédictions.

### Fonctionnalités

- [ ] Créer la page d'accueil.
- [ ] Présenter le projet et ses objectifs.
- [ ] Afficher les performances du modèle.
- [ ] Afficher les graphiques d'évaluation.
- [ ] Afficher la matrice de confusion.
- [ ] Créer un formulaire de saisie des caractéristiques.
- [ ] Charger le modèle sauvegardé.
- [ ] Effectuer une prédiction avec le modèle.
- [ ] Afficher la catégorie prédite : Low, Medium ou High.
- [ ] Gérer les entrées incorrectes et les erreurs.
- [ ] Ajouter un avertissement sur les limites et l'utilisation pédagogique du modèle.

**Livrable :** `app/app.py`

---

# 4. Architecture du projet

```text
MINDORA-AI/
│
├── data/
│   └── raw/
│       └── students_mental_health.csv
│
├── notebooks/
│   └── 01_eda.ipynb
│
├── src/
│   ├── data/
│   │   ├── loading.py
│   │   └── cleaning.py
│   │
│   ├── features/
│   │   └── preprocessing.py
│   │
│   ├── models/
│   │   ├── training.py
│   │   └── evaluation.py
│   │
│   └── utils/
│       └── helpers.py
│
├── models/
│   └── best_model.joblib
│
├── dags/
│   └── mindora_pipeline.py
│
├── app/
│   └── app.py
│
├── analyse/
│   ├── figures/
│   └── reports/
│
├── config/
│   └── config.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

---

# 5. Technologies utilisées

| Domaine | Technologies |
|---|---|
| Langage | Python |
| Manipulation des données | Pandas, NumPy |
| Visualisation | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Prétraitement | ColumnTransformer, Pipeline |
| Optimisation | GridSearchCV, RandomizedSearchCV |
| Gestion des modèles | Joblib |
| Application interactive | Streamlit |
| Orchestration | Apache Airflow |
| Conteneurisation | Docker, Docker Compose |
| Versionnement | Git, GitHub |

---

# 6. Livrables finaux

- [ ] Dépôt Git organisé et documenté.
- [ ] Notebook complet d'analyse exploratoire.
- [ ] Scripts Python structurés.
- [ ] Code source organisé dans `data/`, `dags/`, `notebooks/`, `src/`, `models/` et `app/`.
- [ ] Fichier `requirements.txt`.
- [ ] Modèle entraîné et pipeline sérialisés (`.joblib`).
- [ ] DAG Airflow fonctionnel.
- [ ] Application Streamlit fonctionnelle.
- [ ] Dockerfile et docker-compose.yml.
- [ ] README complet.
- [ ] Résultats des évaluations et conclusions.

---

# 7. Planning du projet

| Période | Travail prévu |
|---|---|
| 09/11/2026 | Chargement, nettoyage et EDA |
| 10/11/2026 | Prétraitement et préparation des données |
| 11/11/2026 | Entraînement et comparaison des modèles |
| 12/11/2026 | Optimisation et évaluation finale |
| 13/11/2026 | Airflow et développement Streamlit |
| 14/11/2026 | Tests, documentation et finalisation |

**Date limite de rendu :** 14/11/2026 à 23h59.

**Date de soutenance :** 16/11/2026.

---

# 8. Préparation à la soutenance

Durée totale : 45 minutes.

| Partie | Durée | Contenu |
|---|---:|---|
| Présentation | 10 min | Présentation du projet et démonstration de l'application |
| Analyse du code | 10 min | Explication de l'architecture, du preprocessing et des modèles |
| Mise en situation | 20 min | Tests de l'application et cas d'utilisation proposés par le jury |
| Code Review | 5 min | Questions techniques et justification des choix |

---

## 9. Conclusion

Mindora AI couvre les principales étapes d'un projet de Machine Learning supervisé : de l'analyse exploratoire des données jusqu'à la mise à disposition d'une application interactive.

Le projet met l'accent sur la qualité des données, la prévention du Data Leakage, la comparaison des modèles, l'optimisation des performances, la reproductibilité et la documentation.

**L'objectif final est de fournir un prototype fonctionnel, documenté et techniquement justifié, dans un cadre strictement pédagogique.**