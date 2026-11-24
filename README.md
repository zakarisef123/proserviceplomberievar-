# PROSERVICE 83 — site web du plombier à Vidauban (Var)

Site statique multipage, optimisé pour le référencement local (SEO) et pour les assistants IA (llms.txt).

## Structure

```
src/
  build.py            générateur du site (Python 3, sans dépendance)
  data_business.py    URL du site, identité légale (Kbis), assurances, médiateur, tarifs, Google Ads, avis
  data_services.py    les 7 prestations (textes, FAQ, prix)
  data_cities.py      les 29 communes principales (textes écrits à la main) + génération des 124 autres
  data_communes_var.py les 153 communes du Var (INSEE) : code postal, secteur, voisines, délai estimé
  data_guides.py      les guides pratiques (rubrique Conseils)
  assets/             CSS, JS, favicon, images
  make_images.js      régénère les PNG (og-image, logo, favicon) avec Playwright
  make_webp.py        crée les variantes WebP des photos (assets/img/webp/, nécessite Pillow)
public/               site généré, publié tel quel (ne pas modifier à la main)
netlify.toml          configuration Netlify (dossier publié, en-têtes)
```

## Modifier le site

1. Modifier les textes dans `src/data_*.py`.
2. Régénérer : `python3 src/build.py` (après un changement de photo : `python3 src/make_webp.py` d'abord).
   La fin du build liste les informations encore « À compléter » (mentions légales, tarifs, conversions, délais).
3. Commiter `src/` **et** `public/`, puis pousser.

## Pages générées (380 pages indexables)

- Accueil, Prestations, Zones d'intervention, Tarifs, À propos, FAQ, Contact, Conseils, Plan du site
- 7 pages de service + 1 page « dégât des eaux & assurance »
- 153 pages d'accueil locales « Plombier + commune » : une par commune du Var, avec toutes les sections de l'accueil
  (héros, urgence, tarifs, services, charte, garanties, étapes, assureurs, zones, conseils, FAQ, formulaire)
- 203 pages « service + commune » (7 services × 29 communes)
- 7 guides pratiques
- Mentions légales, confidentialité (noindex), 404

Chaque page affiche la section « Un plombier proche de chez vous » avec le temps d'arrivée pour chaque commune
(délais modifiables dans `src/data_cities.py`).

## Fonctionnalités

Menus déroulants, héros avec photo, bandeau de confiance défilant, bandeau « Une urgence plomberie ? »,
encart « Facture détaillée acceptée par votre assureur », cartes de service avec photo et boutons
« Appeler / Demander un devis », fenêtre « Demander un devis » (formulaire `devis-express`),
garanties, « Nous pouvons aussi vous aider pour », bandeau d'appel, page `/merci/` (conversion Google Ads),
case de consentement RGPD sur les formulaires. Galerie de chantiers prête : remplir `REALISATIONS`
dans `src/data_business.py` avec des photos de chantiers du Var (dossier `src/assets/chantiers/`).

## Cookies

Bandeau « Tout accepter / Tout refuser / Personnaliser » relié au Google Consent Mode v2
(refus par défaut, choix conservé 6 mois). Code : `src/assets/main.js` et la fonction `head()` de `src/build.py`.

## Fichiers SEO / IA

- `sitemap.xml` : toutes les pages indexables
- `robots.txt` : ouvert aux moteurs et aux robots IA (GPTBot, ClaudeBot, PerplexityBot, Google-Extended…)
- `llms.txt` et `llms-full.txt` : résumé et contenu complet pour les modèles de langage
- Données structurées JSON-LD : Plumber (LocalBusiness), Service, FAQPage, BreadcrumbList, Article

## Formulaires

Trois formulaires (`devis`, `rappel`, `devis-express`) envoyés par **FormSubmit** directement par e-mail à `FORM_EMAIL`
(`src/data_business.py`). Après envoi, le visiteur arrive sur `/merci/` (conversion Google Ads).
**Première mise en ligne** : envoyer une demande test, puis cliquer sur le lien « Activate Form » reçu par e-mail.

## À compléter

Dans `src/data_business.py` :
- `SITE_URL` : l'adresse du site (https://pro-service83.com) (sert aux URL canoniques, au sitemap, à robots.txt et à llms.txt)
- `SIRET`, `ADDRESS_STREET`, `RESPONSABLE_PUBLICATION` : obligatoires dans les mentions légales
- `GOOGLE_SITE_VERIFICATION`, `BING_SITE_VERIFICATION` : codes de validation Search Console / Bing Webmaster Tools
- `ASSURANCE_DECENNALE` : passer à `True` si l'entreprise a une décennale et une RC pro à jour
- `GOOGLE_BUSINESS_URL`, `GOOGLE_REVIEW_URL`, `SAME_AS` : fiche Google, lien « laisser un avis », autres profils


## Avis clients

La section « Avis » n'apparaît que si `REVIEWS` (dans `src/data_business.py`) contient des avis réels,
chacun avec le lien vers sa source (fiche Google, etc.).

## Design

Thème « Noir & bleu » : anthracite + bleu vif (#1fa2ff), titres en Space Grotesk, texte en Inter.
Le thème est en fin de `src/assets/style.css`. Logo : badge rond bleu « 24/7 » avec le symbole du métier
(`LOGO_SVG` dans `src/build.py`, `src/assets/favicon.svg`) ; les PNG se régénèrent avec `node src/make_images.js`.

## Délais des 124 communes ajoutées

Les délais des communes ajoutées sont **estimés** (distance depuis Vidauban, relief) : à vérifier et corriger
dans `src/data_communes_var.py` (champ `delay`).

## Bandeaux de logos

Bandeau défilant des logos d'assureurs (`INSURERS` dans `src/data_business.py`, images dans `src/assets/assurances/`), avec une mention « logos cités à titre d'information, sans partenariat ».
