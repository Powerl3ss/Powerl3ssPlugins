# Plugins Dalamud de Powerl3ss

Une seule ligne à ajouter dans Dalamud pour accéder à tous mes plugins pour Final Fantasy XIV.

## Installation

1. En jeu, tape `/xlsettings` → onglet **Experimental**.
2. Dans **Custom Plugin Repositories**, colle ce lien, coche **Enabled**, clique sur **+** puis **Save** :

   ```
   https://raw.githubusercontent.com/Powerl3ss/Powerl3ssPlugins/main/repo.json
   ```

3. Tape `/xlplugins` et installe les plugins que tu veux.

## Plugins

| Plugin | Description |
| --- | --- |
| [DailyToDo](https://github.com/Powerl3ss/DailyTodo) | Une liste de tâches journalières et hebdomadaires en HUD, entièrement configurable. |
| [DPSmeter](https://github.com/Powerl3ss/DPSmeter) | Tes dégâts et ceux de ton groupe en direct, dans un HUD configurable. |
| [MiniRadar](https://github.com/Powerl3ss/MiniRadar) | Les joueurs autour de toi sur la minimap : amis, compagnie et autres, chacun sa couleur. |
| [BetterChat](https://github.com/Powerl3ss/BetterChat) | Un chat moderne à la place du chat du jeu : onglets, recherche, liens cliquables, mentions. |

## Passer de l'ancien lien au nouveau

Un plugin installé reste rattaché au lien depuis lequel il a été installé. Pour passer au lien unique :

1. Ajoute le nouveau lien et retire les anciens liens de chaque plugin.
2. Désinstalle chaque plugin, puis réinstalle-le depuis `/xlplugins`.

## Ajouter un plugin

Ajoute son dépôt dans `plugins.txt`. Le dépôt doit publier un `repo.json` à la racine de sa branche `main`.

`repo.json` est généré automatiquement toutes les 15 minutes environ : ne le modifie pas à la main.
