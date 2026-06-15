# 🐣 Smart Farm Incubator: IoT Simulation & Monitoring Pipeline

Une solution de bout en bout pour le monitoring de couveuses agricoles, basée sur une architecture micro-services conteneurisée. Ce projet simule des capteurs IoT transmettant des données de température et d'humidité via MQTT, traitées en temps réel par un pipeline de données Python, et stockées dans une base de données temporelle.

## 🛠 Architecture Technique
Le projet est orchestré avec **Docker Compose** pour une mise en place rapide et isolée :

* **Broker MQTT (Eclipse Mosquitto)** : Gestion asynchrone des flux de messages.
* **Pipeline de Données (Python)** : Service `bridge` qui transforme et injecte les messages MQTT dans la base de données.
* **Stockage (InfluxDB 2.7)** : Base de données optimisée pour les séries temporelles.
* **Simulation (Python)** : Génération automatique de données cohérentes (température, humidité, état des lampes) pour tester le système.
* **Visualisation (Grafana)** : Prêt à être configuré pour monitorer vos courbes en temps réel.

## 🚀 Mise en route

### Prérequis
* Docker & Docker Compose installés.

### Installation
1. Clonez ce dépôt.
2. Lancez l'environnement complet :
   ```bash
   docker-compose up -d
Le système est maintenant actif :

Le Simulateur envoie des données toutes les 5 secondes vers le topic ferme/couveuse/data.

Le Bridge intercepte ces messages et les persiste dans InfluxDB.

📊 Fonctionnalités
Isolation des services : Chaque composant tourne dans son propre conteneur.

Flexibilité : Ajout facile de nouveaux nœuds de capteurs via le broker MQTT.

Résilience : Gestion des redémarrages automatiques des services en cas de défaillance.

📁 Structure du projet
bridge.py : Logique d'abonnement MQTT et écriture InfluxDB.

simulator.py : Script de génération de données aléatoires.

docker-compose.yml : Orchestration de la stack.