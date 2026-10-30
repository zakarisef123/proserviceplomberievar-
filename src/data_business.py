# -*- coding: utf-8 -*-
"""Informations sur l'entreprise. Modifier ici puis relancer `python3 src/build.py`."""

# Adresse publique du site (sans slash final). À remplacer par le nom de domaine définitif.
SITE_URL = "https://pro-service83plomberie.netlify.app"

NAME = "PRO SERVICE 83"
LEGAL_NAME = "PRO SERVICE 83"
TAGLINE = "Artisan plombier à Vidauban — dépannage 24h/24 dans le Var"
PHONE = "06 75 93 19 04"
PHONE_TEL = "+33675931904"
EMAIL = "proservice83@hotmail.fr"
BASE_CITY = "Vidauban"
BASE_CP = "83550"
REGION = "Provence-Alpes-Côte d'Azur"
DEPARTEMENT = "Var (83)"
GEO = (43.4272, 6.4319)  # Vidauban
SINCE = 2013
YEARS = "12+"
INTERVENTIONS = "4 380"
RATING = "4.8/5"
SATISFACTION = "97 %"

# Champs légaux : laisser vide pour ne pas les afficher. À compléter dès que possible
# (obligatoire dans les mentions légales d'un artisan).
SIRET = ""
ADDRESS_STREET = ""
RESPONSABLE_PUBLICATION = ""

# Assureurs habitation, mutuelles et banques-assureurs qui acceptent nos factures
# (nom affiché, fichier logo dans src/assets/assurances/).
INSURERS = [
    ('AXA', 'axa.jpg'),
    ('Allianz', 'allianz.png'),
    ('Generali', 'generali.png'),
    ('MAIF', 'maif.png'),
    ('MACIF', 'macif.png'),
    ('MAAF', 'maaf.png'),
    ('Matmut', 'matmut.png'),
    ('Groupama', 'groupama.png'),
    ('Gan Assurances', 'gan-assurances.png'),
    ('Amaguiz', 'amaguiz.png'),
    ('MACSF', 'macsf.png'),
    ('Direct Assurance', 'direct-assurance.png'),
    ('Leocare', 'leocare.png'),
    ('Covéa', 'covea.png'),
    ('Thélem assurances', 'thelem-assurances.png'),
    ('La MAE', 'la-mae.png'),
    ('Swiss Life', 'swiss-life.png'),
    ('Abeille Assurances', 'abeille-assurances.png'),
    ('AG2R La Mondiale', 'ag2r-la-mondiale.png'),
    ('MGEN', 'mgen.png'),
    ('Hiscox Assurances', 'hiscox-assurances.png'),
    ('April', 'april.png'),
    ("L'olivier Assurance", 'lolivier-assurance.png'),
    ('Assu 2000', 'assu-2000.png'),
    ('Euro Assurance', 'euro-assurance.png'),
    ('Acheel', 'acheel.png'),
    ('Lovys', 'lovys.png'),
    ('Luko', 'luko.png'),
    ('Sogessur', 'sogessur.png'),
    ('Crédit Agricole Assurances', 'credit-agricole-assurances.png'),
    ('Crédit Mutuel', 'credit-mutuel.png'),
    ('CIC Assurances', 'cic-assurances.png'),
    ('BNP Paribas', 'bnp-paribas.png'),
    ('Société Générale Assurances', 'societe-generale-assurances.png'),
    ('LCL', 'lcl.png'),
    ('Banque Populaire', 'banque-populaire.png'),
    ("Caisse d'Épargne", 'caisse-epargne.png'),
    ('La Banque Postale Assurances', 'la-banque-postale-assurances.png'),
]

GTAG_ID = "AW-18380568336"

# Afficher « Assurance décennale & RC professionnelle » : passer à True uniquement si
# l'entreprise est bien couverte (attestation à jour).
ASSURANCE_DECENNALE = False

# Photos de chantiers réalisés dans le Var (galerie + page Réalisations, masquées si vide).
# Déposer les photos dans src/assets/chantiers/ puis ajouter par exemple :
# {"image": "salle-de-bain-vidauban.jpg", "title": "Salle de bain rénovée à Vidauban",
#  "text": "Baignoire remplacée par une douche…", "service": "renovation-salle-de-bain-var"},
REALISATIONS = []

REVIEWS = [
    {"text": "Fuite sous l'évier un dimanche, plombier arrivé rapidement et prix respecté.",
     "name": "Camille R.", "city": "Vidauban", "stars": 5},
    {"text": "Remplacement de chauffe-eau propre et soigné, bon conseil.",
     "name": "Karim B.", "city": "Le Muy", "stars": 5},
    {"text": "Débouchage WC efficace, léger retard mais prévenu à l'avance.",
     "name": "Sophie L.", "city": "Draguignan", "stars": 4},
]

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

# Grille tarifaire selon l'heure (page d'accueil). Heure de Paris.
# Journée : lun-sam de RATE_DAY_START à RATE_EVENING_START ; soirée : lun-sam jusqu'à RATE_NIGHT_START ;
# nuit : de RATE_NIGHT_START à RATE_DAY_START, plus dimanches et jours fériés toute la journée.
RATE_DAY_START = 8
RATE_EVENING_START = 18
RATE_NIGHT_START = 22
# (identifiant, libellé, coefficient appliqué aux prix « à partir de »)
RATE_PERIODS = [
    ("jour", "Journée", 1.0),
    ("soir", "Soirée", 1.25),
    ("nuit", "Nuit, dimanche & jours fériés", 1.5),
]
