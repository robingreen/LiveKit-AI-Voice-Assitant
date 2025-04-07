0.explication youtube https://www.youtube.com/watch?v=DNWLIAK4BUY

1. **Créer l'environnement virtuel** :
   ```powershell
   python -m venv ai
   ```

2. **Activer l'environnement virtuel** :
   ```powershell
   .\ai\Scripts\Activate


la 

4. go to https://platform.openai.com/api-keys and copy your key

5. paste in the  .env  file in this repo SANS GUILEMMET NI ESPACE APRES LE SIGNE =

6. (deja fait) bash command pour créer un gitignore qui dira quoi ne pas envoyer (risque de vol d'api): 
   New-Item -Path .gitignore -ItemType File

7. (deja codé)taper .env dans ce gitignore pour que le programme ne divulge pas les clefs stockees dans .env

8. accder à mon livekit account https://cloud.livekit.io/ sur un ordi aller dans les 3 barres tout en bas et crer nouveau projet

9.  aller dans setting et creer une key livekit, utl ...tout ça et coller dans le .env

10. NE PAS TAPER RUN , mais faire en mode BASH :   
python main.py start               pour lancer le programme

11. aller a https://agents-playground.livekit.io/ et clique sur my first app

12 si il y a des serrur deconnect et reconnect sur le playground ci-mentionné

13 aaide toi d'une ia en lui donnant la base deja faite et certaines questions (cf pdf dans comment ca marche)


14 poour fermer le programme tape CTRL-C DEUX FOIS  et pour le lancer de nouveau :     python main.py start


Tu dois abords taper    python main.py start  pour activer l'agent, puis seulement aller sur  https://agents-playground.livekit.io/ en choisissant l'option myfirst app

# Note de test
Petite modification pour tester le push vers GitHub.
