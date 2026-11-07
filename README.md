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
| [DPSmeter](https://github.com/Powerl3ss/DPSmeter) | Tes dégâts et ceux de ton groupe en direct, dans un HUD configurable. |
| [MiniRadar](https://github.com/Powerl3ss/MiniRadar) | Les joueurs autour de toi sur la minimap : amis, compagnie et autres, chacun sa couleur. |
| [BetterChat](https://github.com/Powerl3ss/BetterChat) | Un chat moderne à la place du chat du jeu : onglets, recherche, liens cliquables, mentions. |

## Passer de l'ancien lien au nouveau

Un plugin installé reste rattaché au lien depuis lequel il a été installé. Pour passer au lien unique :

1. Ajoute le nouveau lien et retire les anciens liens de chaque plugin.
2. Désinstalle chaque plugin, puis réinstalle-le depuis `/xlplugins`.

## Ajouter un plugin

1. Ajoute son dépôt dans `plugins.txt`. Il doit publier un `repo.json` à la racine de sa branche `main`.
2. Ajoute le secret `PLUGINS_REPO_TOKEN` dans ce dépôt, puis copie l'étape `Notify shared plugin repository` à la fin de son workflow de build.

## Mise à jour de `repo.json`

`repo.json` est généré automatiquement : ne le modifie pas à la main.

Chaque plugin prévient ce dépôt dès qu'il publie une version. Un passage planifié toutes les 15 minutes environ sert de filet de sécurité. Tu peux aussi lancer **Run workflow** dans l'onglet **Actions**.

Le secret `PLUGINS_REPO_TOKEN` est un token GitHub limité à ce dépôt, avec la permission **Contents** en lecture et écriture. Quand il expire, crée-en un nouveau et remplace le secret dans chaque plugin.
