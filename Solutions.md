# Introduction
Les exercices que nous vous avons proposés sont pour la plupart abordables pour des débutants
Nous vous encourageons à utiliser les solutions qu'en cas de gros blocage.

C'est une liste non exhaustive des problèmes les plus accessibles,
si cela vous intéresse il existe d'autres solutions en ligne.


# Solutions

## 1. Trouvez la page du scoreboard

- on peut simplement faire une inspection du code source de la page web et chercher avec "CTRL + F" un href ou le mot score
- on peut aussi le chercher dans l'onglet source de l'inspecteur, ou on peut tenter un "CTRL + F" global notamment sur "path" qui nous donne souvent les chemins
- une idée élégante est de chercher le path de pages que l'on connait déjà car elles seront proches du path du scoreboard 



## 2. Faire renvoyer une erreur SQL via le formulaire de login
- simplement en mettant un caractère spécial dans le champ username ou password

## 3. Se connecter en tant qu'un autre user genre Bender

- on procède à une injection SQL classique dans le formulaire de login on met username à bender@jui-ce.shop' --  et on laisse le password vide




## 4. Se connecter en tant qu'admin 

- on procède à une injection SQL classique dans le formulaire de login
- on met username à ' OR 1=1 --  et on laisse le password vide


## 5. Faire en sorte que le chatbot offre des réductions
- on lui dit coupon et on le spam et il finit par craquer 

## 6 faire un "customer feedback" avec 0 étoiles
- on peut utiliser reqbin.com pour faire une requête POST vers l'endpoint  http://localhost:3000/api/Feedbacks/
pour le body de la requête on met {"UserId":1,"captchaId":9,"captcha":"1","comment":"fff (admin@juice-sh.op)","rating":0}

ou autre cela se trouve en faisant un essaie et en regardant la requete.

apparemment il existe une solution plus facile qui consiste à modifier l'ui mais ~~j'ai pas trouvé~~ je préfère la mienne.


## 7 Trouver un dom-based xss avec alert("xss")
- dans le champ de recherche on peut simplement taper <iframe src="javascript:alert('xss');"></iframe>

## 8 trouver la page de métriques
- on peut trouver au pif
- on peut nous indique dans le scoreboard que les métriques sont lues par prometheus en lisant sa doc on voit le /metrics utile comme "endpoint" des métriques.



## 9 trouver le fichier confidentiel
 On peut utiliser zaproxy ou dirb pour aller chercher des endpoints cachés.
il s'agit de acquisation.md mais pleins d'autres documents sont alors accessibles. 

## 10 faire s'afficher la photo de chat de Bjoern
On remarque simplement l'url et on se rend compte qu'il y a des # dans l'encoding, ce n'est pas normal un # est là pour faire des ancres.
On remplace les # par des %23 et on obtient l'url valide. C'est la valeur qu'on aurait eu si on avait encodé l'url avec encode l'url correctement.


##11.


## Se connecter en admin par une méthode bruteforce 
### en créant son propre script Python et avec une liste de mots de passe courants


```python
import requests
from requests.structures import CaseInsensitiveDict

url = "http://127.0.0.1:3000/rest/user/login"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"






file_path = 'fourni/best1050.txt'

with open(file_path, 'r') as file:
    file_content = ''
    line = file.readline()
    
    while line:
        line = file.readline()

        data = '{"email": "admin@juice-sh.op", "password": "' + line.strip() +'"}'
        print(line) 
        print(data)
        r = requests.post(url, headers=headers, data=data, timeout=10)
        if r.status_code == 200:
            print("Success with password:", line.strip())
            break



# Basic
print(r.status_code)
print(r.text)

# JSON body (if response is JSON)
try:
    print(r.json())
except ValueError:
    print("Response not JSON")

# Full debug: headers and raw bytes
print("Response headers:", r.headers)
print("Raw bytes:", r.content)
```
### avec Burp Suite Intruder et une liste de mots de passe courants
#### Étape 1 : Configuration de Burp Suite pour intercepter la requête

1. **Accédez à la page de connexion** :
   - Comme dans les étapes précédentes, ouvrez le site vulnérable.
   - Localisez le formulaire de connexion où vous entrez votre **email** et **mot de passe**.

2. **Interceptez la requête de connexion** :
   - Activez **Burp Suite** et configurez-le pour intercepter les requêtes HTTP.
   - Soumettez un formulaire avec des informations valides (même si l'email et le mot de passe sont incorrects pour cette étape, l’objectif est simplement de capturer la requête).
   - Burp Suite interceptera la requête POST envoyée au serveur avec les données de connexion.

3. **Envoyez la requête à Intruder** :
   - Une fois la requête interceptée, envoyez-la à l'outil **Intruder** de Burp Suite pour automatiser l'attaque de force brute.
   - Dans l'onglet **Intruder**, identifiez la partie de la requête qui contient le **mot de passe** et sélectionnez cette zone comme **position à attaquer**.

#### Étape 2 : Configuration de l'attaque par force brute


1. **Définir la liste des mots de passe** :
   - Téléchargez le fichier de liste de mots de passe `best1050.txt`. Ce fichier contient une série de mots de passe couramment utilisés, classés par fréquence.
   - Dans Burp Suite, configurez Intruder pour utiliser cette liste de mots de passe dans l’attaque de force brute. Cela permettra de tester plusieurs mots de passe populaires pour trouver celui du compte administrateur.

2. **Lancer l'attaque avec Burp Suite Intruder** :
   - Configurez Intruder pour envoyer la requête avec chaque mot de passe de la liste `best1050.txt`.
   - L'attaque par force brute va maintenant tenter d'envoyer différentes combinaisons de mots de passe au serveur pour tenter de se connecter avec un mot de passe valide pour l'administrateur.

#### Étape 3 : Analyser les résultats

1. **Observer la réponse du serveur** :
   - Une fois l'attaque lancée, Burp Suite vous montrera les réponses du serveur pour chaque tentative de mot de passe.
   - En fonction de la réponse (par exemple, un message d'erreur différent ou un code de statut HTTP spécifique), vous pourrez identifier quel mot de passe a permis de réussir la connexion. Si un mot de passe valide est trouvé, vous aurez accès au compte administrateur.

2. **Identification du mot de passe vulnérable** :
   - L'attaque de force brute montre l'importance de la complexité des mots de passe. Un mot de passe simple et couramment utilisé (comme un mot de passe de la liste `best1050.txt`) peut facilement être deviné par un attaquant utilisant cette méthode.

## 12. Se faire rediriger qui promeut leur crypto

- simple ctrl+F redirect dans le main.js et on trouve la redirection vers le site de la crypto


## 13 
1. se connecter en tant qu'admin 
2. aller sur /administration 


## 

1. Analyser le problème de téléchargement

Lorsque vous tentez de télécharger le fichier **`package.json.bak`** situé dans le répertoire **`/ftp/`**, vous obtenez une erreur **403 - Forbidden**, ce qui signifie que le serveur interdit l'accès à ce fichier. Le message d'erreur indique également que seuls les fichiers avec les extensions **.md** et **.pdf** sont autorisés au téléchargement.

2. Comprendre la technique du Poison Null Byte

Le **Poison Null Byte** est un exploit basé sur un caractère spécial appelé **byte nul** (noté **`%00`** dans les URL). Ce caractère est un **terminateur de chaîne** dans de nombreux systèmes et langages de programmation. Cela signifie que lorsqu'un byte nul est rencontré, le système considère que la chaîne de caractères (comme un nom de fichier ou une URL) se termine à cet endroit.

En insérant un Poison Null Byte dans le nom du fichier que nous tentons de télécharger, nous pouvons tromper le serveur. Le Poison Null Byte va forcer le serveur à **ignorer la partie de l'extension du fichier après ce caractère**. Par exemple, en ajoutant un Poison Null Byte après **`package.json`**, le serveur pourrait ne voir que **`package.json`**, mais avec une extension autorisée comme **`.md`**.

3. : Appliquer l'encodage URL au Poison Null Byte

Dans une URL, un Poison Null Byte (qui est normalement écrit **`%00`**) doit être encodé pour être correctement transmis. Le Poison Null Byte encodé en URL est **`%2500`**.

4. : Manipuler l'URL pour contourner la restriction

Pour contourner la restriction de téléchargement des fichiers, modifions l'URL de la manière suivante :


5. L'URL initiale pour télécharger le fichier **`package.json.bak`** serait quelque chose comme :

    ```
    http://10.10.90.39/ftp/package.json.bak
    ```

6. Pour contourner la restriction des extensions, nous allons ajouter le Poison Null Byte encodé en URL **`%2500`** à la fin du nom du fichier, puis ajouter une extension **`.md`** à la fin. Cela donnera :

    ```
    http://10.10.90.39/ftp/package.json.bak%2500.md
    ```
7. Télécharger le fichier

En accédant à l'URL modifiée, le serveur va traiter le nom du fichier comme **`package.json.md`** au lieu de **`package.json.bak`**, car le Poison Null Byte force le serveur à ignorer la partie après le byte nul. Le fichier sera alors téléchargé avec l'extension **`.md`**, qui est autorisée, même si l'extension réelle du fichier est **`.bak`**.

8. Pourquoi cette méthode fonctionne-elle ?

Cette méthode fonctionne grâce au comportement des **terminateurs de chaîne** dans de nombreux systèmes de fichiers et langages de programmation. Le byte nul **`%00`** est utilisé pour signaler la fin de la chaîne de caractères, ce qui permet de tronquer l'URL à ce point précis. En encodant ce byte nul en **`%2500`** (l'encodage URL du byte nul), nous pouvons manipuler l'URL de manière à faire en sorte que le serveur ignore la partie du nom de fichier après le Poison Null Byte, contournant ainsi les restrictions de téléchargement.

9. Conclusion

Le Poison Null Byte est une technique puissante pour contourner les restrictions sur les types de fichiers téléchargés. Dans cette étape, vous avez vu comment cette technique permet de tromper le serveur et de télécharger un fichier normalement interdit, en exploitant une faiblesse dans la manière dont les systèmes traitent les chaînes de caractères et les extensions de fichiers.

Cela illustre l'importance de vérifier et de sécuriser correctement les mécanismes de validation des fichiers et des entrées utilisateurs afin d'éviter des vulnérabilités telles que l'**exploitation de données sensibles**.


## 1. DOM-based XSS (XSS basé sur le Document Object Model)

Le **DOM-based XSS** exploite l'environnement HTML et JavaScript côté client pour exécuter du code malveillant. Ce type d'attaque est déclenché lorsqu'une page web permet l'injection de données non filtrées dans le DOM (Document Object Model), souvent par l'intermédiaire des paramètres d'URL ou d'autres entrées de l'utilisateur.

### Exemple d'attaque DOM XSS

1. **Identifier la vulnérabilité** : Recherchez une page où des paramètres dans l'URL sont utilisés sans être correctement échappés dans le DOM. Par exemple, une page qui prend un paramètre tel que **`?user=<username>`** et l'affiche directement dans le DOM sans validation.
   
2. **Injection de JavaScript malveillant** : Vous pouvez injecter du JavaScript dans l'URL comme suit :
http://10.10.90.39/page?user=<script>alert('XSS')</script>

3. **Exécution du script malveillant** : Lorsque la page est chargée avec ce paramètre, le code JavaScript injecté sera exécuté dans le navigateur de la victime, déclenchant une alerte **`XSS`**.

## 2. Persistent XSS (XSS persistant côté serveur)

Le **Persistent XSS** (ou XSS stocké) se produit lorsque du code JavaScript malveillant est envoyé au serveur et stocké, puis exécuté chaque fois que la page contenant le script est consultée. Cela peut se produire lorsque les données envoyées par l'utilisateur (comme les commentaires d'un blog ou les messages d'un forum) ne sont pas correctement nettoyées avant d'être stockées.

### Exemple d'attaque Persistent XSS

1. **Identifier un champ de saisie vulnérable** : Cherchez un formulaire de soumission de données (comme un champ de commentaire, un champ de message, ou un champ de recherche) où l'utilisateur peut entrer du texte qui sera ensuite affiché sans validation ni nettoyage.

2. **Injection du script malveillant** : Dans un champ de saisie, vous pouvez soumettre un commentaire comme :
<script>alert('Persistent XSS')</script>


3. **Accéder à la page contenant le script** : Après avoir soumis le commentaire, si la page qui affiche les commentaires n'échappe pas correctement le contenu, chaque utilisateur qui visite cette page verra le script exécuté automatiquement, affichant l'alerte **`Persistent XSS`**.

## 3. Reflected XSS (XSS réfléchi côté client)

Le **Reflected XSS** se produit lorsque du code malveillant est injecté dans une page via une entrée utilisateur, mais la page est immédiatement renvoyée au client sans être correctement filtrée ou échappée. Cela se produit souvent lorsqu'un paramètre de recherche est renvoyé dans le résultat de la page, par exemple.

### Exemple d'attaque Reflected XSS

1. **Identifier un champ de recherche vulnérable** : Cherchez un formulaire de recherche ou un paramètre d'URL où vous pouvez soumettre des entrées qui sont ensuite directement affichées sur la page, sans validation appropriée.

2. **Injection du script malveillant** : Vous pouvez soumettre une recherche avec un script injecté, par exemple :
http://10.10.90.39/search?q=<script>alert('Reflected XSS')</script>


3. **Exécution du script malveillant** : Lorsque la page de résultats de recherche est renvoyée avec le paramètre **`q`**, le script malveillant est exécuté dans le navigateur de l'utilisateur, déclenchant l'alerte **`Reflected XSS`**.

## Pourquoi ces attaques fonctionnent-elles ?

- **DOM XSS** : L'attaque DOM XSS fonctionne lorsque le JavaScript côté client manipule directement les données fournies par l'utilisateur sans les valider, ce qui permet d'exécuter du code malveillant dans le contexte de la page.

- **Persistent XSS** : Cette attaque fonctionne lorsque le serveur accepte et stocke des données malveillantes (sans nettoyage) qui sont ensuite affichées pour tous les utilisateurs. Ainsi, le script malveillant est exécuté chaque fois que la page est visitée.

- **Reflected XSS** : Cette attaque se produit lorsque les données fournies par l'utilisateur sont immédiatement réintégrées dans la page sans validation appropriée. Le script malveillant est exécuté dès que la page est renvoyée avec l'input de l'utilisateur.

## Conclusion

Ces trois types d'attaques XSS illustrent différentes façons dont un attaquant peut injecter et exécuter du JavaScript malveillant dans un site web. Chaque type d'attaque exploite une faille dans la gestion des données utilisateur, qu'il s'agisse de l'environnement HTML, du stockage côté serveur ou du traitement immédiat des données côté client.

Les bonnes pratiques pour éviter les attaques XSS comprennent :
- **Validation et échappement des entrées utilisateur** : Toujours valider et nettoyer les données envoyées par l'utilisateur avant de les utiliser dans l'application (que ce soit dans l'HTML, l'URL ou le code JavaScript).
- **Utilisation des en-têtes de sécurité** : Mettre en place des en-têtes HTTP de sécurité tels que **Content-Security-Policy (CSP)** pour limiter le type de contenu JavaScript autorisé à s'exécuter.
- **Encodage des données** : Lorsque vous affichez des données utilisateur, assurez-vous qu'elles sont correctement encodées pour empêcher l'exécution de code malveillant.

Cela permet de protéger les utilisateurs contre l'exécution de scripts malveillants et de renforcer la sécurité des applications web.





