# 📊 System Monitor - Monitoring Système en Python

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-macOS%20|%20Linux-lightgrey.svg)

Un script Python léger pour surveiller les ressources système (CPU, RAM, disque, réseau) et générer des rapports HTML visuels avec système d'alertes.

## 🎯 Objectif du projet

Ce projet a été développé dans le cadre de ma formation en **BTS CIEL option IR** pour démontrer mes compétences en :
- Scripting Python
- Monitoring système
- Automatisation de tâches
- Documentation technique

## ✨ Fonctionnalités

- ✅ Surveillance en temps réel du CPU
- ✅ Surveillance de la mémoire RAM
- ✅ Surveillance de l'espace disque
- ✅ Statistiques réseau
- ✅ Système d'alertes avec seuils configurables
- ✅ Génération de rapports HTML visuels
- ✅ Interface moderne et responsive

## 🛠️ Technologies utilisées

- **Python 3.8+**
- **psutil** : Bibliothèque pour la récupération d'informations système
- **HTML/CSS** : Pour les rapports visuels

## 📋 Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

## 🚀 Installation

### 1. Cloner le repository

```bash
git clone https://github.com/shireldsm/system-monitor.git
cd system-monitor
```

### 2. Installer les dépendances

```bash
pip3 install psutil
```

## 💻 Utilisation

### Lancement du script

```bash
python3 monitor.py
```

### Résultat

Le script va :
1. Analyser les ressources système
2. Afficher un résumé dans le terminal
3. Générer un fichier HTML avec le rapport détaillé

Exemple de sortie dans le terminal :
```
🔍 Analyse du système en cours...

📊 Résultats:
CPU: 45.2% ✅
RAM: 67.8% ✅
Disque: 72.3% ✅

✅ Rapport généré : system_report_20260123_143022.html
```

### Ouvrir le rapport

Double-cliquez sur le fichier HTML généré ou ouvrez-le avec votre navigateur :

```bash
open system_report_*.html
```

## ⚙️ Configuration

Les seuils d'alerte sont configurables dans le fichier `monitor.py` :

```python
SEUIL_CPU = 80      # Alerte si CPU > 80%
SEUIL_RAM = 85      # Alerte si RAM > 85%
SEUIL_DISQUE = 90   # Alerte si disque > 90%
```

## 📸 Captures d'écran

Le rapport HTML généré affiche :
- Des cartes pour chaque métrique (CPU, RAM, Disque, Réseau)
- Des barres de progression colorées
- Des alertes visuelles en rouge quand les seuils sont dépassés
- Un design moderne et responsive

## 🔄 Évolutions possibles

- [ ] Ajout d'une surveillance en continu (exécution toutes les X secondes)
- [ ] Envoi d'alertes par email
- [ ] Sauvegarde des historiques dans une base de données
- [ ] Interface web en temps réel
- [ ] Support multi-serveurs
- [ ] Graphiques d'évolution dans le temps

## 📝 Ce que j'ai appris

- Manipulation de bibliothèques Python (psutil)
- Génération dynamique de HTML avec Python
- Concepts de monitoring système
- Bonnes pratiques de documentation
- Utilisation de Git et GitHub

## 📚 Ressources

- [Documentation psutil](https://psutil.readthedocs.io/)
- [Documentation Python](https://docs.python.org/3/)

## 👨‍💻 Auteur

**Shirel Desmelliers**
- Formation : BTS CIEL IR
- GitHub : @shireldsm (https://github.com/shireldsm)
- LinkedIn : [Shirel Desmelliers](https://www.linkedin.com/in/shirel-desmelliers)

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

*Projet réalisé dans le cadre de mon portfolio technique pour une alternance en Systèmes et Réseaux*