# Introduction
Ceci est un document contenant des solutions que nous avons tenté de vous montrer pendant la formation, c'est une liste non exhaustive des problèmes les plus accessibles,
si cela vous intéresse il existe d'autres solutions en ligne.



# Première étape de l'investigation : Exploration du site

La première phase de l'investigation consiste à parcourir le site web et à interagir avec lui de manière manuelle. À ce stade, il n'est pas nécessaire d'activer des outils comme BurpSuite ou d'autres outils d'interception de trafic. En naviguant directement sur l'application, vous pouvez déjà recueillir des informations importantes.

## Ce que vous pouvez chercher :

- **Identification des points d'entrée** : Explorez les différentes pages du site pour identifier les formulaires de saisie, les champs de recherche, les interfaces de connexion, etc.
- **Recherche d'informations sensibles** : Pendant votre navigation, soyez attentif aux informations qui peuvent sembler sensibles ou exposées. Par exemple, il est courant que certaines applications laissent des informations telles que des adresses email dans les messages d'erreur ou dans le code source de la page.
- **Analyse du code source** : Inspectez le code source HTML des pages pour détecter des commentaires, des variables JavaScript ou des liens qui pourraient révéler des informations sensibles ou des points d'entrée pour des attaques.
- **Découverte de l'adresse mail de l'administrateur** : Une première découverte courante pourrait être l'adresse email de l'administrateur, qui peut apparaître dans le code source, dans les pages de contact, ou dans les réponses d'erreur. Cette information pourrait être utile pour de futures étapes de l'investigation.

## Pourquoi cette étape est importante ?

Bien que cette exploration initiale semble basique, elle permet de collecter des informations essentielles sans avoir besoin d'outils spécialisés. L'objectif ici est de mieux comprendre l'architecture du site, de repérer d'éventuelles failles de sécurité évidentes et de recueillir des données qui pourraient être utilisées plus tard dans l'investigation.

Cette phase d'interaction manuelle peut être un premier pas pour repérer des pistes intéressantes avant de passer à des outils plus avancés.

# Deuxième partie de l'investigation : Connexion au compte administrateur et au compte de Bender via manipulation de requêtes SQL

## Objectif

Dans cette étape de l'investigation, l'objectif est de se connecter d'abord au **compte administrateur**, puis au **compte de Bender**, en manipulant les requêtes SQL envoyées au serveur. Vous apprendrez à exploiter des vulnérabilités d'injection SQL pour contourner l'authentification et accéder à des comptes non autorisés. 

Vous pouvez utiliser **Burp Suite** pour intercepter les requêtes et analyser le trafic HTTP, ou manipuler directement les champs du formulaire de connexion pour effectuer l'injection SQL.

## Étape 1 : Connexion au compte administrateur

1. **Accédez à la page de connexion** :
   - Ouvrez le site vulnérable.
   - Identifiez les champs de connexion, notamment le champ pour l'**email** et le **mot de passe**.

2. **Injection SQL pour contourner l'authentification** :
   - Dans le champ **email** ou **mot de passe**, vous allez injecter un payload SQL pour contourner la validation des informations d'identification. Par exemple :
     ```sql
     admin' OR '1'='1
     ```
   - Ce payload modifie la requête SQL envoyée au serveur de manière à ce que la condition `'1'='1` soit toujours vraie, vous permettant ainsi de vous connecter en tant qu'administrateur.

3. **Utilisation de Burp Suite pour intercepter la requête** (optionnel) :
   - Activez **Burp Suite** et configurez-le pour intercepter le trafic HTTP.
   - Soumettez le formulaire de connexion avec le payload injecté. Burp Suite vous permettra de capturer la requête et de l'analyser en détail avant de l'envoyer au serveur.
   - Modifiez la requête si nécessaire pour affiner l'injection SQL et valider votre accès.

## Étape 2 : Connexion au compte de Bender

Après avoir réussi à vous connecter en tant qu'administrateur, la prochaine étape consiste à accéder au **compte de Bender**. 

1. **Accédez à l'interface d'administration ou à la page des utilisateurs** :
   - Il faudra d'abord trouvé l'adresse mail de Bender qui est similaire à celle de l'administrateur d'ailleurs.

2. **Injection SQL pour se connecter au compte de Bender** :
   - Dans le formulaire de connexion pour Bender, vous pouvez à nouveau utiliser une injection SQL pour vous connecter directement en tant que Bender. Par exemple, utilisez un payload comme :
     ```sql
     bender' OR '1'='1
     ```
   - Cela permettra de contourner l'authentification et de vous connecter au compte de Bender, même si vous ne connaissez pas son mot de passe.

3. **Utilisation de Burp Suite pour intercepter et analyser la requête** :
   - Si vous utilisez **Burp Suite**, vous pouvez intercepter et analyser la requête envoyée lors de la tentative de connexion au compte de Bender. Cela vous permettra de voir comment la requête SQL est envoyée et d'adapter votre payload en conséquence.

## Pourquoi cette étape est cruciale ?

Les attaques par injection SQL sont parmi les vulnérabilités les plus courantes et les plus dangereuses dans les applications web. Les participants apprendront ainsi à identifier ces vulnérabilités et à comprendre les conséquences des failles d'authentification.

## Résumé des étapes

- **Objectif** : Se connecter aux comptes administrateur et Bender en exploitant des failles d'injection SQL.
- **Méthode** :
  - Injection SQL dans les champs de saisie du formulaire de connexion.
  - Utilisation de **Burp Suite** pour intercepter et analyser les requêtes HTTP (optionnel).
  - Manipulation des données envoyées au serveur pour contourner les mécanismes d'authentification.

# Troisième étape de l'investigation : Connexion au compte administrateur en utilisant Burp Suite Intruder

## Objectif

Dans cette étape, vous allez utiliser **Burp Suite Intruder** pour effectuer une attaque par force brute sur le formulaire de connexion, en tentant de deviner le mot de passe du compte **administrateur** à partir d'une liste de mots de passe populaires (fichier `best1050.txt`). Cette étape met en évidence les vulnérabilités liées à l'authentification, en particulier l'utilisation de mots de passe faibles pour des comptes avec des privilèges importants.

## Étape 1 : Configuration de Burp Suite pour intercepter la requête

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

## Étape 2 : Configuration de l'attaque par force brute

1. **Définir la liste des mots de passe** :
   - Téléchargez le fichier de liste de mots de passe `best1050.txt`. Ce fichier contient une série de mots de passe couramment utilisés, classés par fréquence.
   - Dans Burp Suite, configurez Intruder pour utiliser cette liste de mots de passe dans l’attaque de force brute. Cela permettra de tester plusieurs mots de passe populaires pour trouver celui du compte administrateur.

2. **Lancer l'attaque avec Burp Suite Intruder** :
   - Configurez Intruder pour envoyer la requête avec chaque mot de passe de la liste `best1050.txt`.
   - L'attaque par force brute va maintenant tenter d'envoyer différentes combinaisons de mots de passe au serveur pour tenter de se connecter avec un mot de passe valide pour l'administrateur.

## Étape 3 : Analyser les résultats

1. **Observer la réponse du serveur** :
   - Une fois l'attaque lancée, Burp Suite vous montrera les réponses du serveur pour chaque tentative de mot de passe.
   - En fonction de la réponse (par exemple, un message d'erreur différent ou un code de statut HTTP spécifique), vous pourrez identifier quel mot de passe a permis de réussir la connexion. Si un mot de passe valide est trouvé, vous aurez accès au compte administrateur.

2. **Identification du mot de passe vulnérable** :
   - L'attaque de force brute montre l'importance de la complexité des mots de passe. Un mot de passe simple et couramment utilisé (comme un mot de passe de la liste `best1050.txt`) peut facilement être deviné par un attaquant utilisant cette méthode.

## Pourquoi cette étape est importante ?

Cette étape met en lumière les dangers des mots de passe faibles, en particulier pour les comptes avec des privilèges élevés (comme le compte administrateur). Même si l'email et le nom d'utilisateur sont protégés, un mot de passe faible peut facilement permettre à un attaquant d'accéder à des comptes sensibles. Ainsi, il est necessaire d'avoir une politique de mots de passes robustes pour une site web.

## Résumé des étapes

- **Objectif** : Se connecter au compte administrateur en utilisant Burp Suite Intruder et une liste de mots de passe (`best1050.txt`).
- **Méthode** :
  - Interception de la requête de connexion via Burp Suite.
  - Configuration de Burp Suite Intruder pour envoyer des requêtes de force brute avec la liste de mots de passe.
  - Analyse des réponses du serveur pour identifier un mot de passe valide.

# Quatrième étape de l'investigation : Accéder à des informations sensibles (Sensitive Data Exposure)

## Objectif

L'objectif de cette étape est d'illustrer la notion d'**exposition de données sensibles** (Sensitive Data Exposure) en essayant d'accéder à des informations que vous ne devriez pas voir en tant qu'utilisateur ordinaire. Cela peut inclure des données confidentielles comme des informations personnelles, des mots de passe, des clés d'API, des données bancaires ou des fichiers sensibles qui sont mal protégés sur le site. Cette étape met en évidence l'importance de sécuriser les données sensibles pour éviter qu'elles ne soient exposées à des utilisateurs non autorisés.

## Étape 1 : Exploration des pages et des répertoires

1. **Explorer les URL et les paramètres de l'application** :
   - Commencez par explorer l'application web comme un utilisateur normal. Allez sur les pages accessibles sans authentification et examinez les URL.
   - Recherchez des paramètres sensibles dans l'URL, tels que des identifiants utilisateur, des tokens, ou d'autres informations qui pourraient vous permettre d'accéder à des données sensibles si elles sont mal protégées.

2. **Manipulation des URL et accès à des zones non protégées** :
   - Tentez de manipuler les URL en modifiant certains paramètres ou en accédant à des ressources protégées par des règles d'accès non strictes.
   - Essayez de deviner des chemins ou des fichiers qui pourraient contenir des informations sensibles, comme `/admin/config`, `/user/data`, ou `/backup`, ou `/ftp`.

## Étape 2 : Inspection des réponses du serveur

1. **Analyser les réponses du serveur** :
   - Observez attentivement les réponses du serveur lors de vos tentatives d'accès. Si le serveur renvoie des informations qui ne sont pas normalement accessibles, cela peut indiquer une vulnérabilité d'exposition de données sensibles.
   - Par exemple, vous pourriez obtenir des détails sur des utilisateurs, des fichiers de configuration contenant des mots de passe en texte clair, ou des données sensibles comme des numéros de carte de crédit ou des informations bancaires.

2. **Rechercher des fichiers de configuration mal sécurisés** :
   - Vérifiez si des fichiers de configuration importants (par exemple, des fichiers de configuration du serveur, des clés API ou des bases de données) sont accessibles sans restrictions appropriées.
   - Par exemple, si des fichiers comme `config.php`, `.env` ou `backup.tar.gz` sont présents dans les répertoires publics ou accessibles via l'URL, cela peut constituer une grave exposition de données sensibles.

## Étape 3 : Accès aux données sensibles (exemple avec un fichier de sauvegarde)

1. **Explorer les répertoires accessibles** :
   - Si l'application met à disposition des répertoires de sauvegarde ou des répertoires non protégés par une authentification stricte, explorez-les à la recherche de fichiers sensibles.
   - Par exemple, si un fichier de sauvegarde (comme `backup.zip` ou `database.sql`) est accessible, vous pourriez y trouver des informations sensibles telles que des identifiants, des mots de passe, des données personnelles, etc.

2. **Téléchargement de fichiers sensibles** :
   - Si vous trouvez un fichier qui semble contenir des données sensibles, téléchargez-le (si possible) et examinez-le pour vérifier qu'il contient des informations confidentielles qui ne devraient pas être accessibles à un utilisateur non autorisé.
   - Vérifiez le contenu de ces fichiers pour identifier des données sensibles comme des mots de passe non cryptés, des informations personnelles des utilisateurs, ou d'autres secrets.

## Étape 4 : Identification de la vulnérabilité d'exposition de données sensibles

1. **Exposition de données sensibles dans les réponses HTTP** :
   - Parfois, des informations sensibles peuvent être renvoyées directement dans les réponses HTTP, par exemple dans des cookies, des en-têtes HTTP ou des pages d'erreur. 
   - Si vous trouvez des informations sensibles dans ces réponses, cela démontre que les données ne sont pas correctement protégées et sont exposées de manière involontaire.

2. **Réflexion sur la sécurité des données sensibles** :
   - L'objectif de cette étape est de démontrer comment des données sensibles peuvent être exposées à des utilisateurs non autorisés, souvent à cause de mauvaises configurations ou de mauvaises pratiques de sécurité.
   - Une fois que vous avez trouvé des données sensibles, il est important de réfléchir à la manière dont elles devraient être protégées, par exemple en utilisant le cryptage des données sensibles, en mettant en place des contrôles d'accès stricts, ou en validant correctement les permissions d'accès à certains fichiers.

### Pourquoi cette étape est importante ?

L'exposition de données sensibles est une vulnérabilité critique qui peut entraîner des conséquences graves, telles que le vol d'identité, la fraude financière, ou la compromission de systèmes sensibles. Les entreprises doivent être conscientes des risques associés à l'exposition non intentionnelle de données sensibles et mettre en œuvre des mécanismes de sécurité solides pour protéger ces informations.

Les bonnes pratiques pour éviter l'exposition de données sensibles incluent :
- **Chiffrement des données sensibles** en transit (SSL/TLS) et au repos (base de données cryptées).
- **Contrôles d'accès stricts** pour limiter les utilisateurs autorisés à accéder à des données sensibles.
- **Mise en œuvre de l'authentification forte** pour les utilisateurs qui accèdent à des informations sensibles.
- **Validation des permissions** et sécurisation des répertoires et fichiers sensibles pour empêcher leur accès non autorisé.

## Résumé des étapes

- **Objectif** : Identifier et accéder à des données sensibles qui ne devraient pas être visibles pour un utilisateur ordinaire.
- **Méthode** :
  - Exploration des URL et manipulation des paramètres pour accéder à des répertoires ou fichiers sensibles.
  - Inspection des réponses du serveur pour détecter la présence d'informations sensibles.
  - Téléchargement de fichiers sensibles ou accès à des fichiers mal sécurisés (par exemple, sauvegardes, fichiers de configuration).
  - Analyse des risques d'exposition de données sensibles et réflexion sur les mesures de sécurité nécessaires.

# Cinquième étape de l'investigation : Contourner les restrictions de téléchargement avec Poison Null Byte

## Objectif

Dans cette étape, nous allons tenter de contourner la restriction qui empêche le téléchargement de certains fichiers, en utilisant une technique appelée **Poison Null Byte**. Cette méthode nous permet de manipuler l'URL pour contourner la restriction de type de fichier et accéder à des informations sensibles qui étaient autrement bloquées.

## Étape 1 : Analyser le problème de téléchargement

Lorsque vous tentez de télécharger le fichier **`package.json.bak`** situé dans le répertoire **`/ftp/`**, vous obtenez une erreur **403 - Forbidden**, ce qui signifie que le serveur interdit l'accès à ce fichier. Le message d'erreur indique également que seuls les fichiers avec les extensions **.md** et **.pdf** sont autorisés au téléchargement.

## Étape 2 : Comprendre la technique du Poison Null Byte

Le **Poison Null Byte** est un exploit basé sur un caractère spécial appelé **byte nul** (noté **`%00`** dans les URL). Ce caractère est un **terminateur de chaîne** dans de nombreux systèmes et langages de programmation. Cela signifie que lorsqu'un byte nul est rencontré, le système considère que la chaîne de caractères (comme un nom de fichier ou une URL) se termine à cet endroit.

En insérant un Poison Null Byte dans le nom du fichier que nous tentons de télécharger, nous pouvons tromper le serveur. Le Poison Null Byte va forcer le serveur à **ignorer la partie de l'extension du fichier après ce caractère**. Par exemple, en ajoutant un Poison Null Byte après **`package.json`**, le serveur pourrait ne voir que **`package.json`**, mais avec une extension autorisée comme **`.md`**.

## Étape 3 : Appliquer l'encodage URL au Poison Null Byte

Dans une URL, un Poison Null Byte (qui est normalement écrit **`%00`**) doit être encodé pour être correctement transmis. Le Poison Null Byte encodé en URL est **`%2500`**.

## Étape 4 : Manipuler l'URL pour contourner la restriction

Pour contourner la restriction de téléchargement des fichiers, modifions l'URL de la manière suivante :

1. L'URL initiale pour télécharger le fichier **`package.json.bak`** serait quelque chose comme :

    ```
    http://10.10.90.39/ftp/package.json.bak
    ```

2. Pour contourner la restriction des extensions, nous allons ajouter le Poison Null Byte encodé en URL **`%2500`** à la fin du nom du fichier, puis ajouter une extension **`.md`** à la fin. Cela donnera :

    ```
    http://10.10.90.39/ftp/package.json.bak%2500.md
    ```

## Étape 5 : Télécharger le fichier

En accédant à l'URL modifiée, le serveur va traiter le nom du fichier comme **`package.json.md`** au lieu de **`package.json.bak`**, car le Poison Null Byte force le serveur à ignorer la partie après le byte nul. Le fichier sera alors téléchargé avec l'extension **`.md`**, qui est autorisée, même si l'extension réelle du fichier est **`.bak`**.

## Pourquoi cette méthode fonctionne-elle ?

Cette méthode fonctionne grâce au comportement des **terminateurs de chaîne** dans de nombreux systèmes de fichiers et langages de programmation. Le byte nul **`%00`** est utilisé pour signaler la fin de la chaîne de caractères, ce qui permet de tronquer l'URL à ce point précis. En encodant ce byte nul en **`%2500`** (l'encodage URL du byte nul), nous pouvons manipuler l'URL de manière à faire en sorte que le serveur ignore la partie du nom de fichier après le Poison Null Byte, contournant ainsi les restrictions de téléchargement.

## Conclusion

Le Poison Null Byte est une technique puissante pour contourner les restrictions sur les types de fichiers téléchargés. Dans cette étape, vous avez vu comment cette technique permet de tromper le serveur et de télécharger un fichier normalement interdit, en exploitant une faiblesse dans la manière dont les systèmes traitent les chaînes de caractères et les extensions de fichiers.

Cela illustre l'importance de vérifier et de sécuriser correctement les mécanismes de validation des fichiers et des entrées utilisateurs afin d'éviter des vulnérabilités telles que l'**exploitation de données sensibles**.

# Sixième étape de l'investigation : Accéder au panier des autres utilisateurs et trouver une page administrative (Broken Access Control)

## Objectif

L'objectif de cette étape est de démontrer une vulnérabilité de **contrôle d'accès défectueux** (Broken Access Control). En interceptant une requête sur Burp Suite, nous allons tenter d'accéder au panier d'un autre utilisateur et découvrir une page administrative cachée. Cela illustre l'importance de mettre en place un contrôle d'accès rigoureux pour protéger les données et les fonctionnalités sensibles des utilisateurs.

## Étape 1 : Interception de la requête avec Burp Suite

1. **Configurer Burp Suite** :
   - Lancez **Burp Suite** et configurez-le pour intercepter le trafic HTTP/HTTPS entre votre navigateur et le serveur de l'application.
   - Assurez-vous que le proxy de Burp Suite est activé et que votre navigateur est configuré pour utiliser ce proxy.

2. **Naviguer sur le site en tant qu'utilisateur authentifié** :
   - Connectez-vous avec vos identifiants à l'application, puis ajoutez des articles à votre panier. Cela génère des requêtes HTTP/HTTPS qui seront envoyées au serveur.
   - Observez le trafic dans l'onglet **"Proxy"** de Burp Suite pour identifier la requête envoyée lors de l'ajout d'articles au panier.

3. **Capturer et analyser la requête** :
   - Repérez la requête qui contient des informations sur votre panier, généralement une requête **POST** ou **GET** avec un paramètre lié au panier (par exemple, `cart_id` ou `user_id`).
   - Inspectez cette requête pour repérer des informations sensibles, comme un identifiant de session, un identifiant utilisateur, ou un identifiant unique pour votre panier.

## Étape 2 : Manipuler la requête pour accéder au panier d'un autre utilisateur

1. **Modifier l'identifiant de l'utilisateur** :
   - Une fois que vous avez intercepté la requête du panier, vous pouvez modifier certains paramètres pour tenter d'accéder au panier d'un autre utilisateur.
   - Par exemple, si la requête contient un paramètre **`user_id`** ou **`cart_id`**, vous pouvez essayer de remplacer cet identifiant par celui d'un autre utilisateur.
   - Vous pouvez soit deviner l'identifiant d'un autre utilisateur (en l'extrayant de la page HTML ou d'une autre source), soit manipuler l'URL pour remplacer l'identifiant de l'utilisateur actuel.

2. **Rejouer la requête modifiée** :
   - Après avoir modifié la requête, envoyez-la à nouveau au serveur via Burp Suite et observez la réponse.
   - Si le contrôle d'accès est mal configuré, vous serez probablement capable d'accéder au panier d'un autre utilisateur, ce qui constitue une faille de sécurité.

## Étape 3 : Recherche d'une page administrative

1. **Explorer d'autres URL possibles** :
   - Pendant l'examen du trafic, cherchez des URL ou des paramètres qui pourraient vous conduire à une page administrative, comme **`/admin`**, **`/dashboard`**, **`/settings`**, ou des URL similaires.
   - Modifiez les paramètres de la requête pour tester l'accès à ces pages. Par exemple, si vous trouvez un paramètre comme **`user_id`**, essayez de remplacer cet identifiant par des valeurs spécifiques pour voir si vous pouvez accéder à des pages d'administration.

2. **Analyser les réponses du serveur** :
   - Si vous accédez à une page contenant des informations administratives, cela pourrait indiquer qu'il n'y a pas de contrôle d'accès approprié en place. Ces pages peuvent contenir des informations sensibles sur l'administration du site, comme la gestion des utilisateurs, les paramètres du système, ou les données confidentielles.

## Pourquoi cette méthode fonctionne-t-elle ?

Cette méthode exploite le manque de contrôle d'accès approprié, ce qui est un problème courant dans les applications web. Lorsqu'un contrôle d'accès est mal implémenté, il est possible de manipuler les paramètres dans les requêtes HTTP pour accéder à des ressources qui devraient être protégées, comme le panier d'un autre utilisateur ou une page administrative.

- **Contrôle d'accès défectueux** : Cela signifie qu'un utilisateur malveillant peut accéder à des ressources et données qui ne lui sont pas destinées, simplement en manipulant les paramètres de la requête.
- **Exploitation des identifiants** : Dans ce cas, le manque de vérification des permissions sur les requêtes permet à un utilisateur de visualiser ou de modifier les données d'un autre utilisateur.

## Conclusion

Cette étape illustre l'importance de la mise en place d'un **contrôle d'accès strict** sur toutes les ressources sensibles. Les contrôles d'accès doivent être vérifiés côté serveur pour s'assurer que chaque utilisateur n'a accès qu'à ses propres données et à celles pour lesquelles il a des autorisations spécifiques. Le contrôle d'accès doit être basé sur les rôles et les permissions, et il est crucial de ne jamais faire confiance aux paramètres envoyés par l'utilisateur (comme l'identifiant utilisateur ou l'identifiant du panier).

Les bonnes pratiques pour éviter le **Broken Access Control** incluent :
- Vérification des permissions sur le côté serveur pour chaque requête.
- Implémentation d'un contrôle d'accès basé sur les rôles (RBAC) pour déterminer les permissions des utilisateurs.
- Utilisation de mécanismes d'authentification forts pour garantir que les utilisateurs ne peuvent pas modifier ou intercepter les données des autres.

# Septième étape de l'investigation : Réaliser trois types d'attaques XSS

## Objectif

L'objectif de cette étape est d'illustrer trois types d'attaques **Cross-Site Scripting (XSS)** : **DOM-based XSS**, **Persistent XSS** et **Reflected XSS**. Ces attaques permettent d'injecter du code JavaScript malveillant dans les pages web visitées par d'autres utilisateurs. Elles peuvent être utilisées pour voler des informations sensibles, comme des cookies, ou manipuler le comportement des pages web.

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





