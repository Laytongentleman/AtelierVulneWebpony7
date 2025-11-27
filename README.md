# Ce document

Ce document fait office de support, qui va vous guider tout au long de l'atelier, n'hésitez pas à directement prendre des notes dessus 

Retrouvez les anciens et prochains ateliers sur le salon pony7 du discord de net7 ou sur la page des événements:
https://pony7.fr/evenements.html

# Introduction

Le **Juice Shop** est une application web vulnérable conçue pour aider à la sensibilisation à la sécurité informatique et à l'apprentissage des techniques de piratage éthique. Développée par le projet **OWASP** (Open Web Application Security Project), le Juice Shop simule une application de commerce en ligne vendant des jus de fruits. Cependant, contrairement aux applications de commerce électronique classiques, cette application est intentionnellement conçue avec de nombreuses failles de sécurité, qui permettent aux utilisateurs de tester et d'explorer les différentes vulnérabilités courantes que l'on peut rencontrer dans le développement web.

Les failles que l'on peut trouver dans Juice Shop incluent des attaques telles que l'injection SQL, la manipulation de sessions, l'élévation de privilèges, et bien d'autres. Cela en fait une ressource précieuse pour les développeurs, les testeurs de sécurité et les professionnels de l'informatique souhaitant renforcer leurs compétences en matière de sécurité des applications.


*En résumé : Juice-Shop est une application web vulnérable, on va s'entrainer à repérer et exploiter ses vulnérabilités dans un pédagogique.*

## Installation : 
3 solutions du plus au moins recommandé : 

- faites tourner Juice-Shop sur votre ordinateur en l'installant comme expliqué ici: 
https://github.com/juice-shop/juice-shop?tab=readme-ov-file#setup
0. choisissez l'installation docker elle marche mieux, bien qu'elle empeche certains challenge d'être validés ils ne nous concernent pas pour cet atelier
1. installez docker: sudo apt-get install docker-compose
2. lancez le daemon docker: sudo systemctl start docker
3. lancez docker run --rm -p 127.0.0.1:3000:3000 bkimminich/juice-shop
4. l'application tourne au http://localhost:3000/  (!) ne mettez pas de s au http

- utilisez notre instance le temps de l'atelier: 

1. connectez vous au partage de connexion "pony7"
2. je vous donnerai l'ip du site

- utilisez une l'instance publique : https://demo.owasp-juice.shop/ (prend du temps à démarrer et peut être instable, à utiliser en dernier recours)




# presentation de quelques failles
c'est la plus value de l'atelier qui va vous donner des bases à adapter sur le site.



# Guide proposé pour attaquer juice-shop  (Spoiler, pas nécessaire si vous êtes avancé ) 
Les informations qui suivent sont essentielles si vous n'avez jamais exploité de vulnérabilités Web. 
Si vous souhaitez continuer sans aide vous pouvez passer votre chemin.


## Un exemple de méthode d'investigation :

Nous vous conseillez dans un premier temps de parcourir le site web et d'interagir avec lui de manière manuelle.
En naviguant directement sur l'application, vous pouvez déjà recueillir des informations importantes.

Liste de choses que vous pouvez chercher :

- **Identification des points d'entrée** : Explorez les différentes pages du site pour identifier les formulaires de saisie, les champs de recherche, les interfaces de connexion, etc.
- **Recherche d'informations sensibles** : Pendant votre navigation, soyez attentif aux informations qui peuvent sembler sensibles ou exposées. Par exemple, il est courant que certaines applications laissent des informations telles que des adresses email dans les messages d'erreur ou dans le code source de la page.
- **Analyse du code source** : Inspectez le code source HTML des pages pour détecter des commentaires, des variables JavaScript ou des liens qui pourraient révéler des informations sensibles ou des points d'entrée pour des attaques.
- **Découverte de l'adresse mail de l'administrateur** : Une première découverte courante pourrait être l'adresse email de l'administrateur, qui peut apparaître dans le code source, dans les pages de contact, ou dans les réponses d'erreur. Cette information pourrait être utile pour de futures étapes de l'investigation.

Cette phase d'interaction manuelle peut être un premier pas pour repérer des pistes intéressantes avant de passer à des outils plus avancés.


## Mots de passe

Dans le cadre de l'exploitation des vulnérabilités de Juice Shop, il est parfois nécessaire de tester des mots de passe, en particulier lors des attaques de brute force ou de dictionnaire. Une liste de mots de passe fréquemment utilisée, appelée **best1050.txt**, est mise à disposition dans le répertoire Git du projet.

### Utilisation de la liste de mots de passe

Vous pouvez utiliser cette liste pour tester différentes combinaisons de mots de passe dans le cadre de vos tests de sécurité. Deux outils populaires pour ce type d'attaque sont **Hydra** et **Burp Suite**. Voici comment les utiliser :


1. **Burp Suite** : Si vous préférez une solution graphique, vous pouvez également utiliser Burp Suite pour effectuer une attaque par brute force. En utilisant la fonctionnalité de **Repetitions** ou en configurant un **Intruder**, vous pouvez tester les mots de passe de la liste `best1050.txt` contre l'application Juice Shop.

2. Il est tout à fait possible de faire son propre script.

3. Hydra




## Outils Recommandés

### outils simples
https://reqbin.com/ 
pour les requetes http 

https://beautifier.io/
pour rendre le javascript lisible

Burp Suite Community Edition

### Outils pour aller plus loin

Burp Suite Community Edition

mitmproxy

zaproxy


# Quetes recommandées (Spoiler, à lire si vous êtes à un point mort et que vous ne trouvez pas/plus de failles à exploiter): 

(!) on vous donne l'objectif mais faut souvent diviser en plusieurs étapes, et des fois ce n'est pas évident, il faut juste se chercher partout sur le site 




1. Trouvez la page du scoreboard 
2. Faire renvoyer une erreur SQL imprévue 
3. Exploiter une injection SQL pour se connecter en tant que Bender ou un autre utilisateur 
4. Exploiter une injection SQL pour se connecter en tant qu'admin 
5. Faire en sorte que le chatbot offre des réductions 
6. faire un "customer feedback" avec 0 étoiles 
7. Trouver un moyen de faire un dom-based xss avec alert('xss')
8. Trouver la page de métriques 
9. Trouver des fichiers confidentiels
10. faire s'afficher la photo du chat de Bjoern 
11. Se connecter au compte Admin sans injection sql
12. Réussir à se faire rediriger vers la page qui promeut leur crypto monnaie
13. supprimer les avis des utilisateurs en tant qu'admin
14. faire 10 customer feebacks en moins de 20 secondes
15. télécharger le fichier package-lock.json.bak
16. upload un fichier pdf 
17. upload un fichier de plus de 100 kb
18. XSS persistant
19. XSS réfléchi
20. Trouver un moyen d'accéder au panier d'un autre utilisateur 





# Pour aller plus loin 

- La plupart des failles que nous avons abordé sont des failles simples à exploiter et à repérer mais il 172 challenges dont beaucoup sont corrigés en ligne dont des difficiles sur ce site donc n'hésitez pas à continer et surtout à alterner avec d'autres mediums d'apprentissage.

# Conclusion

- Merci d'avoir suivi l'atelier, n'hésitez surtout pas à nous faire par des retours en présentiel et sinon sur le salon #pony7 du discord de net7
- Pour les thématiques des prochains ateliers vous pouvez voter ici: https://beta.framadate.org/polls/303f262513f757fb5e5a

- Si vous souhaitez à votre tour présenter un atelier, faites nous en part en mp discord ou sur le salon #pony7 du discord de net7.
