# Disclaimer
Les exercices que nous vous avons proposés sont pour la plupart abordables pour des débutants
Nous vous encourageons à les utiliser qu'en cas de gros blocage.

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








