# PRO SERVICE 83 — site web du plombier à Vidauban (Var)

Site statique multipage, optimisé pour le référencement local (SEO) et pour les assistants IA (llms.txt).

## Structure

```
src/
  build.py            générateur du site (Python 3, sans dépendance)
  data_business.py    coordonnées, chiffres clés, assureurs, avis, URL du site
  data_services.py    les 7 prestations (textes, FAQ, prix)
  data_cities.py      les 22 communes desservies (textes, délais, voisines)
  data_guides.py      les guides pratiques (rubrique Conseils)
  assets/             CSS, JS, favicon, images
  make_images.js      régénère les PNG (og-image, logo, favicon) avec Playwright
public/               site généré, publié tel quel (ne pas modifier à la main)
netlify.toml          configuration Netlify (dossier publié, en-têtes)
```

## Modifier le site

1. Modifier les textes dans `src/data_*.py`.
2. Régénérer : `python3 src/build.py`
3. Commiter `src/` **et** `public/`, puis pousser.

## Pages générées (101 pages indexables)

- Accueil, Prestations, Zones d'intervention, Tarifs, À propos, FAQ, Contact, Conseils
- 7 pages de service + 1 page « dégât des eaux & assurance »
- 22 pages « Plombier + commune »
- 56 pages « service + commune » (7 services × 8 communes principales)
- 7 guides pratiques
- Mentions légales, confidentialité (noindex), 404

## Fichiers SEO / IA

- `sitemap.xml` : toutes les pages indexables
- `robots.txt` : ouvert aux moteurs et aux robots IA (GPTBot, ClaudeBot, PerplexityBot, Google-Extended…)
- `llms.txt` et `llms-full.txt` : résumé et contenu complet pour les modèles de langage
- Données structurées JSON-LD : Plumber (LocalBusiness), Service, FAQPage, BreadcrumbList, Article

## Formulaires

Deux formulaires Netlify Forms : `devis` (bas de chaque page) et `rappel` (colonne latérale des pages de service et de commune).
Activer la détection des formulaires dans Netlify : *Project configuration → Forms → Enable form detection*,
puis ajouter une notification e-mail vers proservice83@hotmail.fr.

## À compléter

Dans `src/data_business.py` :
- `SITE_URL` : le nom de domaine définitif (sert aux URL canoniques, au sitemap, à robots.txt et à llms.txt)
- `SIRET`, `ADDRESS_STREET`, `RESPONSABLE_PUBLICATION` : obligatoires dans les mentions légales
