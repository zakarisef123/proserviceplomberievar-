# -*- coding: utf-8 -*-
"""Communes desservies (une page commune + une page par prestation pour chacune).
`core=True` : commune principale (menu, pied de page, liens des pages de service).
`menu=True` : affichée aussi dans le menu « Zones ».
`delay` : délai indicatif en minutes depuis Vidauban, hors trafic ; `delay_todo=True` : chiffre à confirmer.
Ne jamais présenter un délai comme « garanti »."""

CITIES = [
    {
        "name": "Vidauban", "slug": "vidauban", "cp": "83550", "a": "à Vidauban", "de": "de Vidauban",
        "delay": 0, "core": True,
        "intro": "Notre base est à Vidauban : c'est ici que nous intervenons le plus vite, souvent dans l'heure. Centre du village, quartiers résidentiels, maisons de la plaine et domaines viticoles le long de l'Argens, nous connaissons les installations du secteur.",
        "context": "À Vidauban, le parc de logements mêle maisons de village anciennes, où l'on rencontre encore des canalisations vieillissantes, et villas plus récentes avec chauffe-eau, piscines et arrosage. Être sur place nous permet d'intervenir sans délai de route et de revenir facilement si une pièce doit être commandée.",
        "near": ["taradeau", "le-cannet-des-maures", "les-arcs-sur-argens", "le-muy", "la-garde-freinet", "le-thoronet"],
    },
    {
        "name": "Le Muy", "slug": "le-muy", "cp": "83490", "a": "au Muy", "de": "du Muy",
        "delay": 15, "core": True,
        "intro": "Le Muy fait partie de notre zone d'intervention, 24h/24 et 7j/7. Au pied du rocher de Roquebrune, la commune compte de nombreux lotissements et maisons individuelles que nous dépannons régulièrement.",
        "context": "Au Muy, beaucoup de maisons individuelles sont équipées de chauffe-eau électriques de grande capacité et de réseaux enterrés jusqu'au portail : les recherches de fuite après compteur et les remplacements de ballon y sont fréquents. L'accès rapide par la DN7 et l'autoroute A8 nous permet d'y être vite.",
        "near": ["vidauban", "les-arcs-sur-argens", "la-motte", "roquebrune-sur-argens", "puget-sur-argens", "trans-en-provence"],
    },
    {
        "name": "Les Arcs-sur-Argens", "slug": "les-arcs-sur-argens", "cp": "83460", "a": "aux Arcs-sur-Argens", "de": "des Arcs-sur-Argens",
        "delay": 15, "core": True,
        "intro": "Les Arcs-sur-Argens, avec son village médiéval et sa gare Les Arcs-Draguignan, fait partie de notre zone d'intervention, 24h/24 et 7j/7. Nous y intervenons aussi bien dans le vieux village que dans les quartiers résidentiels et les domaines viticoles.",
        "context": "Dans le village ancien des Arcs, les ruelles étroites et les maisons de village imposent souvent des réseaux d'évacuation anciens et encastrés : nous privilégions la détection précise avant d'ouvrir. Dans les quartiers plus récents, ce sont surtout les chauffe-eau, les WC et la robinetterie qui nous occupent.",
        "near": ["taradeau", "vidauban", "le-muy", "draguignan", "trans-en-provence", "lorgues"],
    },
    {
        "name": "Le Cannet-des-Maures", "slug": "le-cannet-des-maures", "cp": "83340", "a": "au Cannet-des-Maures", "de": "du Cannet-des-Maures",
        "delay": 15, "core": True,
        "intro": "Le Cannet-des-Maures, dans la plaine des Maures près de la jonction des autoroutes A8 et A57, fait partie de notre zone d'intervention, 24h/24 et 7j/7. Nous y dépannons particuliers, propriétaires de résidences secondaires et petites entreprises.",
        "context": "Au Cannet-des-Maures, les habitations sont souvent dispersées, avec des réseaux d'eau enterrés sur de longues distances et parfois un assainissement individuel : une fuite ou un bouchon peut se situer loin de la maison. Nous venons équipés pour chercher méthodiquement.",
        "near": ["le-luc", "vidauban", "le-thoronet", "les-mayons", "gonfaron", "la-garde-freinet"],
    },
    {
        "name": "Le Luc", "slug": "le-luc", "cp": "83340", "a": "au Luc", "de": "du Luc",
        "delay": 20, "core": True,
        "intro": "Le Luc (Le Luc-en-Provence), sur la DN7 entre Vidauban et Brignoles, fait partie de notre zone d'intervention, 24h/24 et 7j/7. Centre ancien, lotissements et zones d'activité : nous y intervenons tous les jours de l'année.",
        "context": "Au Luc, le centre ancien concentre des immeubles et maisons de ville aux colonnes d'évacuation communes, où les bouchons et les dégâts des eaux entre voisins sont fréquents. Dans les quartiers pavillonnaires, nous intervenons surtout sur les chauffe-eau, les fuites et la rénovation de salles de bain.",
        "near": ["le-cannet-des-maures", "gonfaron", "les-mayons", "le-thoronet", "vidauban", "pignans"],
    },
    {
        "name": "La Garde-Freinet", "slug": "la-garde-freinet", "cp": "83680", "a": "à La Garde-Freinet", "de": "de La Garde-Freinet",
        "delay": 20, "core": True,
        "intro": "Village perché au cœur du massif des Maures, La Garde-Freinet fait partie de notre zone d'intervention, 24h/24 et 7j/7. Nous y intervenons dans le village comme dans les maisons isolées de la forêt.",
        "context": "À La Garde-Freinet, beaucoup de maisons sont isolées, desservies par des pistes, avec des installations parfois anciennes et des résidences secondaires inoccupées une partie de l'année. Une fuite peut y passer inaperçue longtemps : nous conseillons de couper l'eau au départ et de faire vérifier l'installation avant la saison.",
        "near": ["vidauban", "le-cannet-des-maures", "les-mayons", "grimaud", "le-muy", "sainte-maxime"],
    },
    {
        "name": "Gonfaron", "slug": "gonfaron", "cp": "83590", "a": "à Gonfaron", "de": "de Gonfaron",
        "delay": 25, "core": True,
        "intro": "Gonfaron, village provençal au pied du massif des Maures, fait partie de notre zone d'intervention, 24h/24 et 7j/7. Nous y assurons les dépannages urgents comme les travaux de plomberie planifiés.",
        "context": "À Gonfaron, entre maisons de village et villas en périphérie, nous intervenons aussi bien pour des fuites sur des réseaux anciens que pour le remplacement de chauffe-eau entartrés, l'eau étant calcaire dans le secteur.",
        "near": ["le-luc", "les-mayons", "pignans", "le-cannet-des-maures", "la-garde-freinet", "vidauban"],
    },
    {
        "name": "Draguignan", "slug": "draguignan", "cp": "83300", "a": "à Draguignan", "de": "de Draguignan",
        "delay": 25, "core": True, "delay_todo": True,
        "intro": "Draguignan, sous-préfecture de la région, fait partie de notre zone d'intervention, 24h/24 et 7j/7. Centre historique autour de la tour de l'Horloge, quartiers résidentiels, immeubles et maisons individuelles : nous y intervenons 7j/7.",
        "context": "À Draguignan, nous intervenons beaucoup en appartement : colonnes d'évacuation communes, dégâts des eaux entre voisins, chauffe-eau en placard. Dans ces situations, nous fournissons les éléments nécessaires au constat amiable et coordonnons si besoin avec le syndic.",
        "near": ["trans-en-provence", "flayosc", "les-arcs-sur-argens", "lorgues", "la-motte", "taradeau"],
    },
    # ---- Communes secondaires (page commune uniquement)
    {
        "name": "Taradeau", "slug": "taradeau", "cp": "83460", "a": "à Taradeau", "de": "de Taradeau",
        "delay": 10, "core": False,
        "intro": "Taradeau, petit village viticole entre Vidauban et Les Arcs, est à une dizaine de minutes de notre base : c'est l'une des communes où nous arrivons le plus vite.",
        "context": "À Taradeau, nous intervenons dans le village et dans les maisons et domaines alentour, souvent alimentés par de longues canalisations enterrées. Fuites après compteur, chauffe-eau et débouchages représentent l'essentiel de nos interventions.",
        "near": ["vidauban", "les-arcs-sur-argens", "lorgues", "le-thoronet"],
    },
    {
        "name": "Lorgues", "slug": "lorgues", "cp": "83510", "a": "à Lorgues", "de": "de Lorgues",
        "delay": 20, "core": False,
        "intro": "Lorgues, village provençal réputé pour sa collégiale et ses ruelles, fait partie de notre zone d'intervention, 24h/24 et 7j/7.",
        "context": "À Lorgues, les maisons de village anciennes et les nombreuses bastides en campagne demandent des interventions adaptées : réseaux anciens, chauffe-eau éloignés, fosses et évacuations longues.",
        "near": ["taradeau", "le-thoronet", "les-arcs-sur-argens", "draguignan", "flayosc"],
    },
    {
        "name": "Le Thoronet", "slug": "le-thoronet", "cp": "83340", "a": "au Thoronet", "de": "du Thoronet",
        "delay": 20, "core": False,
        "intro": "Le Thoronet, connu pour son abbaye cistercienne, fait partie de notre zone d'intervention, 24h/24 et 7j/7. Nous y dépannons les habitants du village et des hameaux alentour.",
        "context": "Au Thoronet, l'habitat est dispersé et souvent entouré de nature : canalisations enterrées, puits, arrosage et chauffe-eau sont les sujets les plus courants de nos interventions.",
        "near": ["le-cannet-des-maures", "le-luc", "lorgues", "vidauban", "taradeau"],
    },
    {
        "name": "Les Mayons", "slug": "les-mayons", "cp": "83340", "a": "aux Mayons", "de": "des Mayons",
        "delay": 25, "core": False,
        "intro": "Les Mayons, petit village du massif des Maures, fait partie de notre zone d'intervention, 24h/24 et 7j/7. Nous y intervenons malgré l'éloignement, avec un délai annoncé au téléphone.",
        "context": "Aux Mayons, les maisons isolées et les résidences secondaires sont nombreuses : fuites non détectées pendant l'absence des occupants et chauffe-eau à remplacer sont des interventions fréquentes.",
        "near": ["gonfaron", "le-luc", "le-cannet-des-maures", "la-garde-freinet"],
    },
    {
        "name": "Trans-en-Provence", "slug": "trans-en-provence", "cp": "83720", "a": "à Trans-en-Provence", "de": "de Trans-en-Provence",
        "delay": 20, "core": False,
        "intro": "Trans-en-Provence, traversée par la Nartuby, fait partie de notre zone d'intervention, 24h/24 et 7j/7, entre Les Arcs, La Motte et Draguignan.",
        "context": "À Trans-en-Provence, nous intervenons dans le vieux village comme dans les quartiers résidentiels : débouchages, recherche de fuite et remplacement de chauffe-eau sont nos demandes les plus fréquentes.",
        "near": ["draguignan", "la-motte", "les-arcs-sur-argens", "le-muy"],
    },
    {
        "name": "La Motte", "slug": "la-motte", "cp": "83920", "a": "à La Motte", "de": "de La Motte",
        "delay": 20, "core": False,
        "intro": "La Motte, commune viticole entre Le Muy et Draguignan, fait partie de notre zone d'intervention, 24h/24 et 7j/7.",
        "context": "À La Motte, l'habitat est majoritairement composé de maisons individuelles avec jardin : canalisations enterrées, arrosage, chauffe-eau de grande capacité et salles de bain à rénover.",
        "near": ["le-muy", "trans-en-provence", "draguignan", "les-arcs-sur-argens"],
    },
    {
        "name": "Flayosc", "slug": "flayosc", "cp": "83780", "a": "à Flayosc", "de": "de Flayosc",
        "delay": 30, "core": False,
        "intro": "Flayosc, village perché à l'ouest de Draguignan, fait partie de notre zone d'intervention, 24h/24 et 7j/7. Le délai exact vous est communiqué lors de l'appel.",
        "context": "À Flayosc, entre village ancien et nombreuses villas sur les collines, nous intervenons pour les fuites, les débouchages, les chauffe-eau et les projets de rénovation.",
        "near": ["draguignan", "lorgues", "trans-en-provence"],
    },
    {
        "name": "Roquebrune-sur-Argens", "slug": "roquebrune-sur-argens", "cp": "83520", "a": "à Roquebrune-sur-Argens", "de": "de Roquebrune-sur-Argens",
        "delay": 25, "core": False,
        "intro": "Roquebrune-sur-Argens, de son village perché jusqu'au littoral des Issambres, fait partie de notre zone d'intervention, 24h/24 et 7j/7.",
        "context": "À Roquebrune-sur-Argens, nous intervenons dans les résidences principales comme dans les résidences secondaires et les copropriétés : fuites, dégâts des eaux, débouchages et chauffe-eau.",
        "near": ["le-muy", "puget-sur-argens", "frejus", "sainte-maxime"],
    },
    {
        "name": "Puget-sur-Argens", "slug": "puget-sur-argens", "cp": "83480", "a": "à Puget-sur-Argens", "de": "de Puget-sur-Argens",
        "delay": 25, "core": False,
        "intro": "Puget-sur-Argens, entre Le Muy et Fréjus le long de la DN7, fait partie de notre zone d'intervention, 24h/24 et 7j/7.",
        "context": "À Puget-sur-Argens, l'habitat pavillonnaire domine : recherches de fuite, chauffe-eau et installations sanitaires sont nos interventions les plus fréquentes.",
        "near": ["le-muy", "roquebrune-sur-argens", "frejus"],
    },
    {
        "name": "Fréjus", "slug": "frejus", "cp": "83600", "a": "à Fréjus", "de": "de Fréjus",
        "delay": 35, "core": False, "delay_todo": True,
        "intro": "Fréjus, de la vieille ville à Port-Fréjus, Fréjus-Plage, la Tour de Mare et Saint-Aygulf, jusqu'aux Issambres, fait partie de notre zone d'intervention, 24h/24 et 7j/7. Nous y intervenons sur rendez-vous et en urgence, avec un délai annoncé à l'appel.",
        "context": "À Fréjus, les appartements en copropriété et les résidences secondaires représentent une grande part de nos interventions : dégâts des eaux entre voisins, chauffe-eau, fuites et rénovation de salles de bain.",
        "near": ["puget-sur-argens", "saint-raphael", "roquebrune-sur-argens"],
    },
    {
        "name": "Saint-Raphaël", "slug": "saint-raphael", "cp": "83700", "a": "à Saint-Raphaël", "de": "de Saint-Raphaël",
        "delay": 40, "core": False, "delay_todo": True,
        "intro": "Saint-Raphaël, du centre-ville à Valescure, Boulouris, Agay et Anthéor, fait partie de notre zone d'intervention, 24h/24 et 7j/7. Pour les travaux planifiés comme pour les urgences, le délai vous est donné au téléphone.",
        "context": "À Saint-Raphaël, nous intervenons principalement en appartement et en villa : rénovation de salles de bain, remplacement de chauffe-eau et recherche de fuite.",
        "near": ["frejus", "puget-sur-argens", "roquebrune-sur-argens"],
    },
    {
        "name": "Sainte-Maxime", "slug": "sainte-maxime", "cp": "83120", "a": "à Sainte-Maxime", "de": "de Sainte-Maxime",
        "delay": 35, "core": False,
        "intro": "Sainte-Maxime, sur le golfe de Saint-Tropez, fait partie de notre zone d'intervention, 24h/24 et 7j/7. Nous y intervenons notamment pour les résidences secondaires.",
        "context": "À Sainte-Maxime, de nombreuses villas et appartements sont occupés une partie de l'année : vérification avant la saison, fuites découvertes au retour et chauffe-eau à remplacer sont des demandes fréquentes.",
        "near": ["grimaud", "le-muy", "roquebrune-sur-argens", "la-garde-freinet"],
    },
    {
        "name": "Grimaud", "slug": "grimaud", "cp": "83310", "a": "à Grimaud", "de": "de Grimaud",
        "delay": 35, "core": False,
        "intro": "Grimaud, du village perché à Port-Grimaud, fait partie de notre zone d'intervention, 24h/24 et 7j/7.",
        "context": "À Grimaud, nous intervenons dans les maisons de village, les villas et les résidences secondaires : fuites, chauffe-eau, débouchages et rénovations de salles de bain.",
        "near": ["la-garde-freinet", "sainte-maxime"],
    },
    {
        "name": "Pignans", "slug": "pignans", "cp": "83790", "a": "à Pignans", "de": "de Pignans",
        "delay": 30, "core": False,
        "intro": "Pignans, au pied de Notre-Dame-des-Anges, fait partie de notre zone d'intervention, 24h/24 et 7j/7.",
        "context": "À Pignans, nous intervenons pour les dépannages urgents et les travaux planifiés : fuites, débouchages, chauffe-eau et installation sanitaire.",
        "near": ["gonfaron", "le-luc"],
    },
    # Toulon et son agglomération (délais indicatifs à confirmer : "delay_todo")
    {
        "name": "Toulon", "slug": "toulon", "cp": "83000", "a": "à Toulon", "de": "de Toulon",
        "delay": 50, "core": True, "menu": True, "delay_todo": True,
        "intro": "Toulon, préfecture de la région, fait partie de notre zone d'intervention, 24h/24 et 7j/7. Nous intervenons dans tous les quartiers : Le Mourillon, Le Cap Brun, Le Port et le centre-ville, Pont-du-Las, Saint-Jean-du-Var, La Rode, Les Routes et Valbertrand.",
        "context": "À Toulon, une grande partie de nos interventions a lieu en appartement : immeubles anciens du centre et du Port aux colonnes d'évacuation communes, résidences du Mourillon et du Cap Brun, maisons de Saint-Jean-du-Var, de La Rode, des Routes ou de Valbertrand. Dégâts des eaux entre voisins, chauffe-eau en placard et débouchages sont nos demandes les plus fréquentes ; nous fournissons les éléments utiles au constat amiable et au syndic.",
        "near": ["la-valette-du-var", "la-garde", "la-seyne-sur-mer", "ollioules", "six-fours-les-plages", "hyeres"],
    },
    {
        "name": "La Seyne-sur-Mer", "slug": "la-seyne-sur-mer", "cp": "83500", "a": "à La Seyne-sur-Mer", "de": "de La Seyne-sur-Mer",
        "delay": 55, "core": False, "menu": True, "delay_todo": True,
        "intro": "La Seyne-sur-Mer, du centre-ville à Tamaris, aux Sablettes et à Mar-Vivo, fait partie de notre zone d'intervention, 24h/24 et 7j/7.",
        "context": "À La Seyne-sur-Mer, nous intervenons dans les immeubles du centre comme dans les villas de Tamaris et des Sablettes : fuites, dégâts des eaux, chauffe-eau et débouchages, avec un air marin qui use plus vite la robinetterie.",
        "near": ["toulon", "six-fours-les-plages", "ollioules"],
    },
    {
        "name": "La Garde", "slug": "la-garde", "cp": "83130", "a": "à La Garde", "de": "de La Garde",
        "delay": 45, "core": False, "menu": True, "delay_todo": True,
        "intro": "La Garde, entre Toulon et La Valette-du-Var, fait partie de notre zone d'intervention, 24h/24 et 7j/7.",
        "context": "À La Garde, entre le vieux village, les quartiers pavillonnaires et les résidences proches de l'université, nous intervenons surtout pour des fuites, des chauffe-eau et des installations sanitaires.",
        "near": ["la-valette-du-var", "toulon", "hyeres"],
    },
    {
        "name": "La Valette-du-Var", "slug": "la-valette-du-var", "cp": "83160", "a": "à La Valette-du-Var", "de": "de La Valette-du-Var",
        "delay": 45, "core": False, "menu": True, "delay_todo": True,
        "intro": "La Valette-du-Var, au pied du Coudon, fait partie de notre zone d'intervention, 24h/24 et 7j/7.",
        "context": "À La Valette-du-Var, l'habitat mêle maisons individuelles, résidences et commerces : recherches de fuite, chauffe-eau et débouchages sont nos interventions les plus fréquentes.",
        "near": ["la-garde", "toulon", "hyeres"],
    },
    {
        "name": "Hyères", "slug": "hyeres", "cp": "83400", "a": "à Hyères", "de": "d'Hyères",
        "delay": 45, "core": False, "menu": True, "delay_todo": True,
        "intro": "Hyères, de la vieille ville à Costebelle, L'Ayguade et la presqu'île de Giens, fait partie de notre zone d'intervention, 24h/24 et 7j/7.",
        "context": "À Hyères, de nombreuses villas et résidences secondaires sont occupées une partie de l'année : fuites découvertes au retour, chauffe-eau entartrés et rénovations de salle de bain sont des demandes fréquentes.",
        "near": ["la-garde", "la-valette-du-var", "toulon"],
    },
    {
        "name": "Six-Fours-les-Plages", "slug": "six-fours-les-plages", "cp": "83140", "a": "à Six-Fours-les-Plages", "de": "de Six-Fours-les-Plages",
        "delay": 60, "core": False, "menu": True, "delay_todo": True,
        "intro": "Six-Fours-les-Plages, du Brusc au Cap Sicié, fait partie de notre zone d'intervention, 24h/24 et 7j/7.",
        "context": "À Six-Fours-les-Plages, l'habitat est surtout pavillonnaire, avec beaucoup de résidences secondaires : fuites, chauffe-eau et installations sanitaires sont nos interventions les plus courantes.",
        "near": ["la-seyne-sur-mer", "ollioules", "toulon"],
    },
    {
        "name": "Ollioules", "slug": "ollioules", "cp": "83190", "a": "à Ollioules", "de": "d'Ollioules",
        "delay": 55, "core": False, "menu": True, "delay_todo": True,
        "intro": "Ollioules, entre Toulon et les gorges d'Ollioules, fait partie de notre zone d'intervention, 24h/24 et 7j/7.",
        "context": "À Ollioules, entre maisons de village et villas en périphérie, nous intervenons pour les dépannages urgents comme pour les travaux planifiés : fuites, débouchages, chauffe-eau et salle de bain.",
        "near": ["toulon", "la-seyne-sur-mer", "six-fours-les-plages"],
    },
]

CITY_BY_SLUG = {c["slug"]: c for c in CITIES}

# Délai dans les textes : « {delai} » est remplacé par « environ N minutes » d'après "delay",
# pour que le chiffre ne soit à modifier qu'à un seul endroit.
for _c in CITIES:
    for _k in ("intro", "context"):
        _c[_k] = _c[_k].replace("{delai}", "environ %d minutes" % _c["delay"])

TRADE = "plombier"
CONTEXTS = {
    "littoral": [
        "{a}, beaucoup de logements sont des résidences secondaires ou des villas avec piscine et arrosage automatique : une fuite peut couler des semaines avant d'être découverte. Nous intervenons aussi bien pour la recherche de fuite que pour remettre en route un chauffe-eau à l'arrivée des vacances.",
        "Sur le littoral, l'eau est calcaire et les installations travaillent fort en été. {a}, nous remplaçons souvent des chauffe-eau entartrés, des robinetteries usées et des flexibles fatigués, et nous débouchons les canalisations des appartements et locations saisonnières.",
        "{a}, entre appartements de vacances, villas et maisons de famille, nos interventions vont de la fuite sous évier au dégât des eaux entre voisins. Pour les propriétaires absents, nous pouvons intervenir en lien avec un gardien ou une agence, avec photos et facture à l'appui.",
    ],
    "ville": [
        "{a}, beaucoup de logements sont en immeuble, avec des colonnes d'eau et d'évacuation communes : un bouchon ou une fuite chez un voisin peut vite toucher plusieurs appartements. Nous localisons l'origine et fournissons le rapport utile au syndic et aux assureurs.",
        "Entre immeubles anciens du centre et quartiers résidentiels, les installations {de} sont très variées. Nous intervenons sur les canalisations vieillissantes, les chauffe-eau de petite capacité des appartements et les WC bouchés, à toute heure.",
        "{a}, les dégâts des eaux en copropriété sont fréquents. Nous recherchons la fuite sans casse inutile, réparons et remettons les justificatifs demandés pour le constat amiable et l'assurance.",
    ],
    "rural": [
        "{a}, beaucoup de maisons sont anciennes, en pierre, parfois isolées, avec un assainissement individuel et des canalisations qui ont vécu. En hiver, le gel peut faire éclater un tuyau exposé : coupez l'eau au compteur et appelez-nous, nous intervenons même loin du village.",
        "Dans l'arrière-pays, l'eau est souvent calcaire et les réseaux longs. {a}, nous intervenons pour des fuites enterrées, des chauffe-eau entartrés et des évacuations bouchées dans les maisons de village comme dans les fermes et résidences secondaires.",
    ],
    "plaine": [
        "{a}, le parc mêle maisons de village anciennes et lotissements plus récents, avec des réseaux d'eau enterrés jusqu'au portail : recherches de fuite après compteur, remplacements de chauffe-eau et débouchages font partie de nos interventions courantes.",
        "L'eau est calcaire dans le secteur {de} : les chauffe-eau s'entartrent et la robinetterie s'use plus vite. Nous dépannons, remplaçons et conseillons sur l'entretien, en plus des urgences de fuite et de débouchage.",
        "{a}, nous intervenons dans le centre ancien comme dans les quartiers pavillonnaires et les mas en périphérie : fuites, WC bouchés, chauffe-eau en panne ou rénovation de salle de bain, avec un prix annoncé avant de partir.",
    ],
}


# ---------------------------------------------------------------- les 153 communes de la région
# Les 29 communes ci-dessus ont des textes écrits à la main. Les autres communes de la région
# (data_communes_var.py) reçoivent une page d'accueil locale avec des textes construits à partir
# de leur secteur, de leur taille et de leurs voisines. Délais estimés : à confirmer.
from data_communes_var import COMMUNES_VAR  # noqa: E402

SECTORS = {
    "dracenie": ("la Dracénie", "de la Dracénie", "autour de Draguignan, de la plaine de l'Argens aux villages perchés du arrière-pays"),
    "coeur-du-var": ("la plaine des Maures", "de la plaine des Maures", "dans la plaine des Maures et la vallée de l'Aille, le long de l'A8 et de la DN7"),
    "golfe": ("le golfe de Saint-Tropez", "du golfe de Saint-Tropez", "entre les villages perchés des Maures et les stations balnéaires du golfe"),
    "esterel": ("l'agglomération Estérel Côte d'Azur", "de l'agglomération Estérel Côte d'Azur", "entre la basse vallée de l'Argens et le massif de l'Estérel"),
    "maures-littoral": ("le secteur Méditerranée Porte des Maures", "du secteur Méditerranée Porte des Maures", "entre les plages et le massif des Maures, de La Londe au Lavandou"),
    "toulon": ("la métropole toulonnaise", "de la métropole toulonnaise", "autour de la rade de Toulon, entre littoral, collines et plaine de La Crau"),
    "gapeau": ("la vallée du Gapeau", "de la vallée du Gapeau", "entre Toulon et Cuers, au pied des collines de Solliès"),
    "sud-sainte-baume": ("le Sud Sainte-Baume", "du Sud Sainte-Baume", "entre le littoral de Bandol et Sanary et les villages du Castellet et du Beausset"),
    "provence-verte": ("la Provence Verte", "de la Provence Verte", "autour de Brignoles et Saint-Maximin, entre vignes, forêts et collines"),
    "sainte-baume-nord": ("le pied de la Sainte-Baume", "du pied de la Sainte-Baume", "dans la haute vallée de l'Huveaune, à la limite des Bouches-du-Rhône"),
    "provence-verdon": ("la Provence Verdon", "de la Provence Verdon", "sur les plateaux et dans les villages ruraux entre Barjols et Rians"),
    "lacs-verdon": ("le secteur des lacs et gorges du Verdon", "du secteur des lacs et gorges du Verdon", "du lac de Sainte-Croix aux plateaux de l'Artuby"),
    "verdon-durance": ("la vallée du Verdon et de la Durance", "de la vallée du Verdon et de la Durance", "à la limite des Alpes-de-Haute-Provence"),
    "fayence": ("le pays de Fayence", "du pays de Fayence", "dans les villages perchés entre l'Estérel et les premiers plateaux, autour du lac de Saint-Cassien"),
}
SECTOR_KIND = {"golfe": "littoral", "esterel": "littoral", "maures-littoral": "littoral", "sud-sainte-baume": "littoral",
               "toulon": "ville", "fayence": "rural", "provence-verdon": "rural", "lacs-verdon": "rural",
               "verdon-durance": "rural", "sainte-baume-nord": "plaine", "provence-verte": "plaine",
               "gapeau": "plaine", "coeur-du-var": "plaine", "dracenie": "plaine"}


def _pop(n):
    n = int(round(n, -2)) if n >= 1000 else int(round(n, -1))
    return "{:,}".format(n).replace(",", " ")


def _intro(r, i):
    lab, lab_de, desc = SECTORS[r["sector"]]
    p = _pop(r["pop"])
    if r["pop"] >= 15000:
        first = [
            "%s, avec ses quelque %s habitants, est l'une des principales villes %s. Nous y intervenons 24h/24 et 7j/7, en centre-ville comme dans les quartiers résidentiels." % (r["name"], p, lab_de),
            "Avec environ %s habitants, %s est l'une des grandes communes de la région. Un artisan %s s'y déplace jour et nuit, week-ends et jours fériés compris." % (p, r["name"], TRADE),
        ][i % 2]
    elif r["pop"] >= 3000:
        first = [
            "%s (%s), commune %s d'environ %s habitants, fait partie de notre zone d'intervention, jour et nuit, 7j/7." % (r["name"], r["cp"], lab_de, p),
            "Nous intervenons %s (%s), commune d'environ %s habitants, pour les urgences comme pour les travaux planifiés, 24h/24 et 7j/7." % (r["a"], r["cp"], p),
        ][i % 2]
    else:
        first = [
            "Même dans un village comme %s (environ %s habitants), vous joignez directement un artisan %s de la région. Nous intervenons dans le village et les hameaux alentour, 24h/24 et 7j/7." % (r["name"], p, TRADE),
            "%s, petite commune %s d'environ %s habitants, fait partie de notre zone d'intervention. Village, hameaux ou maisons isolées : nous nous déplaçons jour et nuit." % (r["name"], lab_de, p),
        ][i % 2]
    where = ("La commune se trouve à environ %d km de notre base de Vidauban, dans %s, %s." % (r["km"], lab, desc)) if r["km"] >= 3 else ""
    return (first + " " + where).strip()


def _context(r, i):
    opts = CONTEXTS[SECTOR_KIND[r["sector"]]]
    t = opts[i % len(opts)].format(a=r["a"], de=r["de"], name=r["name"])
    return t[0].upper() + t[1:]


_HAND = {c["slug"] for c in CITIES}
EXTRA_CITIES = []
for _i, _r in enumerate(COMMUNES_VAR):
    if _r["slug"] in _HAND:
        continue
    EXTRA_CITIES.append({
        "name": _r["name"], "slug": _r["slug"], "cp": _r["cp"], "a": _r["a"], "de": _r["de"],
        "delay": _r["delay"], "core": False, "extra": True, "estimated": True,
        "sector": _r["sector"], "pop": _r["pop"], "km": _r["km"],
        "intro": _intro(_r, _i), "context": _context(_r, _i),
        "near": _r["near"][:6],
    })
_SECT = {r["slug"]: r["sector"] for r in COMMUNES_VAR}
for _c in CITIES:
    _c.setdefault("sector", _SECT.get(_c["slug"], "dracenie"))
# Toutes les communes (pages d'accueil locales) ; CITIES reste la liste des 29 communes
# qui ont en plus une page par prestation.
ALL_CITIES = CITIES + EXTRA_CITIES
CITY_BY_SLUG = {c["slug"]: c for c in ALL_CITIES}
