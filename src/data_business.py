# -*- coding: utf-8 -*-
"""Informations sur l'entreprise. Modifier ici puis relancer `python3 src/build.py`.

Les champs laissés vides ne sont pas affichés sur le site ; la liste de ceux qui manquent
est rappelée à la fin de chaque build (« À compléter »)."""

# Adresse publique du site (sans slash final) : sert aux balises canonical, og:url, JSON-LD,
# sitemap.xml, robots.txt et llms.txt.
SITE_URL = "https://pro-service83.com"

# ---------------------------------------------------------------- identité (Kbis)
# NAME : nom affiché partout (titres, textes, JSON-LD « name »).
# LEGAL_NAME : dénomination exacte du Kbis (mentions légales, JSON-LD « legalName »).
# Orthographe exacte du Kbis : « PROSERVICE 83 ».
NAME = "PROSERVICE 83"
LEGAL_NAME = "PROSERVICE 83"
LEGAL_FORM = ""            # ex. "SASU au capital de 1 000 €" ou "Entreprise individuelle"
SIRET = ""                 # 14 chiffres, ex. "123 456 789 00012"
RCS_RM = ""                # ex. "RCS Draguignan 123 456 789" ou "RM 123 456 789 (CMA Var)"
TVA = ""                   # ex. "FR12 123456789"
ADDRESS_STREET = ""        # adresse du siège (rue), ex. "12 avenue de la Gare"
ADDRESS_CP = "83550"       # code postal du siège
ADDRESS_CITY = "Vidauban"  # commune du siège
DIRECTEUR_PUBLICATION = "" # ex. "Prénom Nom, gérant"

# Assurances professionnelles (laisser "" tant que l'attestation n'est pas fournie).
DECENNALE = {"assureur": "", "contrat": "", "zone": ""}
RC_PRO = {"assureur": "", "contrat": "", "zone": ""}

# Médiateur de la consommation (obligatoire pour un professionnel qui travaille avec des particuliers).
MEDIATEUR = {"nom": "", "site": ""}  # ex. {"nom": "CM2C", "site": "https://www.cm2c.net"}

TAGLINE = "Artisan plombier dans le Var (83) — dépannage 24h/24"
PHONE = "06 75 93 19 04"
PHONE_TEL = "+33675931904"
# Adresse e-mail publique (contact, JSON-LD).
EMAIL = "proservice83contact@gmail.com"
BASE_CITY = "Vidauban"
BASE_CP = "83550"
REGION = "Provence-Alpes-Côte d'Azur"
DEPARTEMENT = "Var (83)"
GEO = (43.4272, 6.4319)  # Vidauban
SINCE = 2013
YEARS = "12+"

# ---------------------------------------------------------------- Google Ads
GTAG_ID = "AW-18380568336"
# Google Tag Manager : balises de conversion Google Ads (événements clic_appel / envoi_formulaire).
GTM_ID = "GTM-54ZL3CHF"
# Libellés de conversion complets (« AW-…/LIBELLÉ »). Vide = aucune conversion envoyée.
# Conversions désormais envoyées par Google Tag Manager (GTM_ID ci-dessous) : laisser vides pour
# éviter le double comptage. Anciennes valeurs : call kUUYCLWxwfocEJDuxLxE / form BAvQCP2rjuAcEJDuxLxE.
CONV_CALL = ""   # clic sur un numéro (conversion secondaire)
CONV_FORM = ""   # formulaire envoyé (page /merci/)
# Appels depuis le site (numéro de transfert Google, durée minimale 60 s) : libellé de l'action
# « Appels vers un numéro de téléphone sur votre site Web », ex. "AW-18380568336/AbCdEf".
# Vide = numéro affiché tel quel, sans numéro de transfert.
CONV_CALL_FORWARDING = ""

# Afficher « Assurance décennale & RC professionnelle » : automatique dès que les deux
# assurances ci-dessus sont renseignées.
ASSURANCE_DECENNALE = bool(DECENNALE["assureur"] and RC_PRO["assureur"])

# Photos de chantiers réalisés dans le Var (galerie + page Réalisations, masquées si vide).
# Déposer les photos dans src/assets/chantiers/ puis ajouter par exemple :
# {"image": "salle-de-bain-vidauban.jpg", "title": "Salle de bain rénovée à Vidauban",
#  "text": "Baignoire remplacée par une douche…", "service": "renovation-salle-de-bain-var"},
REALISATIONS = []

# Avis clients : uniquement des avis réels et vérifiables, avec le lien vers leur source
# (fiche Google, PagesJaunes…). La section « Avis » est masquée tant que la liste est vide.
# Exemple : {"text": "…", "name": "Prénom N.", "city": "Vidauban", "stars": 5,
#            "date": "2026-11", "source": "Google", "url": "https://maps.app.goo.gl/…"},
REVIEWS = []

# Référencement : codes de validation (laisser vide tant qu'ils ne sont pas fournis).
# Google Search Console : méthode « Balise HTML », copier uniquement la valeur de content="…".
GOOGLE_SITE_VERIFICATION = ""
# Bing Webmaster Tools : méthode « Balise meta », valeur de content="…".
BING_SITE_VERIFICATION = ""

# Fiche Google Business Profile (lien public) et lien direct « Laisser un avis ».
GOOGLE_BUSINESS_URL = ""
GOOGLE_REVIEW_URL = ""
# Autres profils officiels (Facebook, PagesJaunes, Instagram…), sous forme de liste d'URL.
SAME_AS = []

# ---------------------------------------------------------------- tarifs
# Tous les prix sont TTC. Grille selon l'heure (heure de Paris) :
# journée : lun-sam de RATE_DAY_START à RATE_EVENING_START ; soirée : lun-sam jusqu'à RATE_NIGHT_START ;
# nuit : de RATE_NIGHT_START à RATE_DAY_START ; dimanches et jours fériés : coefficient RATE_SUNDAY_COEF.
RATE_DAY_START = 8
RATE_EVENING_START = 18
RATE_NIGHT_START = 22
# (identifiant, libellé, coefficient appliqué aux prix « à partir de »)
RATE_PERIODS = [
    ("jour", "Journée", 1.0),
    ("soir", "Soirée", 1.25),
    ("nuit", "Nuit", 1.5),
]
RATE_SUNDAY_COEF = 1.5  # dimanches et jours fériés, toute la journée

# Déplacement : True = inclus dans les prix « à partir de » ; un nombre = prix TTC du déplacement ;
# None = pas encore renseigné (le site indique alors « annoncé au téléphone avant le départ »).
DEPLACEMENT = None
# Taux horaire de main-d'œuvre TTC (nombre) ; None = non affiché.
TAUX_HORAIRE = None

# Assureurs affichés dans le bandeau défilant (logos dans src/assets/assurances/).
# Logos cités à titre d'information : la facture détaillée est acceptée par les assureurs habitation.
INSURERS = [
    ('AXA', 'axa.jpg'), ('Allianz', 'allianz.png'), ('Generali', 'generali.png'), ('MAIF', 'maif.png'),
    ('MACIF', 'macif.png'), ('MAAF', 'maaf.png'), ('Matmut', 'matmut.png'), ('Groupama', 'groupama.png'),
    ('Gan Assurances', 'gan-assurances.png'), ('Amaguiz', 'amaguiz.png'), ('MACSF', 'macsf.png'),
    ('Direct Assurance', 'direct-assurance.png'), ('Leocare', 'leocare.png'), ('Covéa', 'covea.png'),
    ('Thélem assurances', 'thelem-assurances.png'), ('La MAE', 'la-mae.png'), ('Swiss Life', 'swiss-life.png'),
    ('Abeille Assurances', 'abeille-assurances.png'), ('AG2R La Mondiale', 'ag2r-la-mondiale.png'), ('MGEN', 'mgen.png'),
    ('Hiscox Assurances', 'hiscox-assurances.png'), ('April', 'april.png'), ("L'olivier Assurance", 'lolivier-assurance.png'),
    ('Assu 2000', 'assu-2000.png'), ('Euro Assurance', 'euro-assurance.png'), ('Acheel', 'acheel.png'), ('Lovys', 'lovys.png'),
    ('Luko', 'luko.png'), ('Sogessur', 'sogessur.png'), ('Crédit Agricole Assurances', 'credit-agricole-assurances.png'),
    ('Crédit Mutuel', 'credit-mutuel.png'), ('CIC Assurances', 'cic-assurances.png'), ('BNP Paribas', 'bnp-paribas.png'),
    ('Société Générale Assurances', 'societe-generale-assurances.png'), ('LCL', 'lcl.png'), ('Banque Populaire', 'banque-populaire.png'),
    ("Caisse d'Épargne", 'caisse-epargne.png'), ('La Banque Postale Assurances', 'la-banque-postale-assurances.png'),
]
