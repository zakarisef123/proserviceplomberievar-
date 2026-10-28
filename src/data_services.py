# -*- coding: utf-8 -*-
"""Prestations proposées. Chaque service génère une page dédiée et une page par commune principale."""

SERVICES = [
    # ------------------------------------------------------------------ URGENCE
    {
        "slug": "plombier-urgence-24h-var",
        "combo": "plombier-urgence",
        "name": "Plombier urgence 24h/24",
        "short": "Urgence plomberie 24h/24",
        "icon": "bolt",
        "badge": "Urgence 24/7",
        "price_label": "Tarif annoncé avant déplacement",
        "price_min": None,
        "title": "Plombier urgence 24h/24 dans le Var — nuit, week-end, jours fériés",
        "meta": "Plombier d'urgence dans le Var 24h/24 et 7j/7 : fuite, dégât des eaux, WC bouché, chauffe-eau en panne. Tarif annoncé avant déplacement. ☎ 06 75 93 19 04",
        "h1": "Plombier d'urgence 24h/24 et 7j/7 dans le Var",
        "lead": "Fuite importante, dégât des eaux, WC bouché, plus d'eau chaude : un plombier vous répond <b>jour et nuit, week-end et jours fériés compris</b>, depuis Vidauban vers tout le centre Var.",
        "checks": ["Réponse immédiate au téléphone", "Prix annoncé avant de partir", "Facture pour l'assurance"],
        "card_desc": "Fuite, dégât des eaux, panne : un plombier joignable jour et nuit, week-end et jours fériés compris.",
        "card_checks": ["Disponible 7j/7", "Tarif confirmé avant déplacement"],
        "sections": [
            ("Quelles situations justifient un plombier en urgence ?",
             "<p>Toutes les pannes de plomberie ne se valent pas. Certaines peuvent attendre un rendez-vous en semaine, d'autres provoquent des dégâts en quelques minutes. Nous intervenons en priorité pour :</p>"
             "<ul><li><strong>Une fuite d'eau importante</strong> : tuyau percé, flexible éclaté, raccord qui cède, chauffe-eau qui fuit.</li>"
             "<li><strong>Un dégât des eaux</strong> chez vous ou chez le voisin du dessous, avec infiltration au plafond ou dans un mur.</li>"
             "<li><strong>Un WC bouché</strong> lorsqu'il n'y a qu'un seul WC dans le logement, ou une canalisation qui refoule.</li>"
             "<li><strong>Une panne de chauffe-eau</strong> : plus d'eau chaude, eau qui coule en continu par le groupe de sécurité.</li>"
             "<li><strong>Un robinet d'arrêt bloqué ou cassé</strong> qui empêche de couper l'eau.</li></ul>"
             "<p>Au téléphone, nous vous aidons à évaluer l'urgence. Si la situation peut attendre le lendemain sans risque, nous vous le disons : un déplacement de nuit coûte plus cher et nous préférons vous faire économiser cette dépense lorsqu'elle n'est pas nécessaire.</p>"),
            ("Les bons réflexes en attendant le plombier",
             "<ol><li><strong>Coupez l'eau</strong> au robinet d'arrêt de l'appareil concerné, ou au robinet général (souvent près du compteur, dans un regard extérieur ou sous l'évier).</li>"
             "<li><strong>Coupez l'électricité</strong> si l'eau approche des prises, d'un tableau électrique ou d'un appareil branché.</li>"
             "<li><strong>Coupez le chauffe-eau</strong> (disjoncteur dédié) s'il fuit ou si l'eau est coupée longtemps.</li>"
             "<li><strong>Épongez et protégez</strong> : serpillières, bassines, meubles surélevés.</li>"
             "<li><strong>Prenez des photos</strong> des dégâts : elles serviront pour votre déclaration à l'assurance.</li>"
             "<li><strong>Prévenez le voisin du dessous</strong> si vous êtes en appartement.</li></ol>"
             "<p>Vous ne trouvez pas le robinet d'arrêt ? Appelez-nous : nous vous guidons au téléphone pendant que le plombier est en route.</p>"),
            ("Plombier la nuit, le dimanche et les jours fériés",
             "<p>Une fuite ne prévient pas. C'est pourquoi la ligne <strong>06 75 93 19 04</strong> est joignable 24h/24, y compris le dimanche, les jours fériés et pendant les vacances. Les interventions de nuit, de week-end ou de jour férié peuvent faire l'objet d'un supplément horaire : <strong>il vous est toujours communiqué avant le déplacement</strong>, jamais découvert sur la facture.</p>"
             "<p>Ce fonctionnement transparent est l'inverse des pratiques que dénoncent régulièrement les associations de consommateurs dans le dépannage d'urgence. Vous savez ce que vous allez payer avant que le plombier ne prenne la route, et le prix est confirmé sur place avant tout travail.</p>"),
            ("Une intervention qui règle le problème, pas seulement le symptôme",
             "<p>En urgence, la priorité est de stopper la fuite et de sécuriser le logement. Mais nous ne repartons pas en laissant une réparation de fortune sans vous prévenir. Si une pièce doit être commandée ou si une réparation durable nécessite un second passage, nous vous l'expliquons clairement, avec un devis séparé.</p>"
             "<p>À la fin de l'intervention, vous recevez une <strong>facture détaillée</strong> (déplacement, main-d'œuvre, pièces) et, si besoin, un descriptif de la cause du sinistre pour votre assureur habitation.</p>"),
        ],
        "faq": [
            ("Combien coûte un plombier en urgence la nuit ou le dimanche ?", "Le prix dépend de la nature de l'intervention et de l'horaire. Un supplément peut s'appliquer la nuit, le week-end et les jours fériés : il vous est annoncé au téléphone avant le déplacement, puis le prix total est confirmé sur place avant de commencer."),
            ("En combien de temps un plombier peut-il arriver ?", "Depuis notre base de Vidauban, comptez environ 15 minutes pour Le Muy, Les Arcs ou Le Cannet-des-Maures, 20 minutes pour Le Luc et 25 minutes pour Draguignan, hors trafic. Le délai précis vous est donné au moment de l'appel."),
            ("Que faire si je n'arrive pas à couper l'eau ?", "Cherchez le robinet général près du compteur d'eau (regard extérieur, garage, placard technique). S'il est bloqué, ne forcez pas avec un outil : vous risquez de le casser. Appelez-nous, nous vous guidons au téléphone."),
            ("Intervenez-vous pour les dégâts des eaux pris en charge par l'assurance ?", "Oui. Nous recherchons l'origine de la fuite, la réparons et vous remettons une facture détaillée et un descriptif de la cause, utiles pour votre déclaration et le constat amiable dégât des eaux."),
        ],
        "combo_h1": "Plombier d'urgence 24h/24",
        "combo_title": "Plombier urgence {city} ({cp}) — 24h/24, 7j/7",
        "combo_meta": "Plombier d'urgence {a} 24h/24 et 7j/7 : fuite, dégât des eaux, WC bouché, chauffe-eau. {delay_txt}. Prix annoncé avant déplacement. ☎ 06 75 93 19 04",
        "combo_intros": [
            "Une fuite qui inonde la cuisine, un WC qui déborde, un chauffe-eau qui lâche un soir de week-end : {a}, vous pouvez joindre un plombier à toute heure au <b>06 75 93 19 04</b>. Nous partons de Vidauban et le délai d'arrivée vous est donné dès l'appel.",
            "Besoin d'un plombier tout de suite {a} ? Notre ligne est ouverte jour et nuit, dimanches et jours fériés compris. Vous décrivez la situation, on vous annonce le prix et le délai, puis un plombier part avec le matériel adapté.",
            "Habitants {de}, gardez ce numéro : <b>06 75 93 19 04</b>. En cas d'urgence plomberie, un artisan du secteur vous répond directement, sans plateforme ni centre d'appel, et intervient rapidement avec un prix annoncé à l'avance.",
        ],
        "combo_points": [
            "Fuite d'eau importante ou tuyau percé",
            "Dégât des eaux et infiltration chez le voisin",
            "WC bouché ou canalisation qui refoule",
            "Chauffe-eau en panne ou qui fuit",
            "Robinet d'arrêt cassé ou bloqué",
            "Flexible de robinet ou de lave-linge éclaté",
        ],
        "combo_tip": "En attendant notre arrivée, coupez l'eau au robinet général et, si l'eau approche d'une prise ou d'un appareil électrique, coupez aussi le courant au tableau. Prenez quelques photos : elles vous serviront pour l'assurance.",
    },
    # ------------------------------------------------------------------ FUITE
    {
        "slug": "recherche-de-fuite-var",
        "combo": "recherche-fuite",
        "name": "Fuite d'eau & recherche de fuite",
        "short": "Fuite d'eau",
        "icon": "drop",
        "badge": "Urgence 24/7",
        "price_label": "à partir de 79 €",
        "price_min": 79,
        "title": "Recherche de fuite et réparation de fuite d'eau dans le Var (83)",
        "meta": "Fuite d'eau dans le Var ? Recherche de fuite non destructive (visuelle, thermique, acoustique) et réparation dès 79 €. Rapport pour l'assurance. ☎ 06 75 93 19 04",
        "h1": "Recherche de fuite et réparation de fuite d'eau dans le Var",
        "lead": "Compteur qui tourne, tache au plafond, facture d'eau qui s'envole : nous <b>localisons la fuite sans casser inutilement</b> et la réparons proprement. Intervention à partir de 79 €.",
        "checks": ["Détection sans casse quand c'est possible", "Réparation durable", "Rapport utile à l'assurance"],
        "card_desc": "Détection et réparation de fuites (robinet, canalisation, WC, chauffe-eau) rapidement et proprement.",
        "card_checks": ["Recherche de fuite", "Sans casse quand possible"],
        "sections": [
            ("Les signes qui doivent vous alerter",
             "<p>Une fuite n'est pas toujours visible. Une canalisation encastrée ou enterrée peut perdre des centaines de litres avant que le moindre signe n'apparaisse. Soyez attentif à :</p>"
             "<ul><li>un <strong>compteur d'eau qui tourne</strong> alors que tous les robinets sont fermés ;</li>"
             "<li>une <strong>facture d'eau anormalement élevée</strong> ou un courrier de votre service des eaux signalant une surconsommation ;</li>"
             "<li>des <strong>taches d'humidité</strong>, auréoles, peinture qui cloque ou papier peint qui se décolle ;</li>"
             "<li>une <strong>odeur de moisi</strong> ou des moisissures dans un placard, derrière un meuble ou au bas d'un mur ;</li>"
             "<li>un <strong>bruit d'écoulement</strong> permanent, un WC qui coule en continu ;</li>"
             "<li>une <strong>baisse de pression</strong> ou une zone de sol anormalement humide dans le jardin.</li></ul>"
             "<div class=\"callout info\"><strong>Le test du compteur :</strong> fermez tous les robinets, relevez l'index du compteur, n'utilisez pas d'eau pendant une à deux heures et relevez-le de nouveau. S'il a bougé, il y a une fuite quelque part après le compteur.</div>"),
            ("Comment nous localisons la fuite",
             "<p>Casser un mur ou une dalle au hasard coûte cher et ajoute des travaux. Notre objectif est de trouver l'origine exacte de la fuite avant d'ouvrir quoi que ce soit. Selon la situation, nous combinons plusieurs méthodes :</p>"
             "<ul><li><strong>Contrôle visuel et méthodique</strong> des équipements : robinetterie, raccords, mécanisme de chasse d'eau, groupe de sécurité, siphons, joints.</li>"
             "<li><strong>Détection thermique</strong> : une caméra infrarouge met en évidence les différences de température, très utile pour suivre une canalisation d'eau chaude ou de chauffage au sol.</li>"
             "<li><strong>Détection acoustique</strong> : l'écoute du bruit de l'eau qui s'échappe permet de localiser une fuite sur une canalisation sous pression.</li>"
             "<li><strong>Isolement des réseaux</strong> et lecture du compteur pour déterminer quelle partie de l'installation est concernée.</li></ul>"
             "<p>Une fois la fuite localisée, nous vous expliquons ce que nous avons trouvé et ce qu'il faut faire, avec le prix, avant d'intervenir.</p>"),
            ("La réparation",
             "<p>Selon l'origine, la réparation peut aller du simple remplacement d'un joint ou d'un flexible à la reprise d'une portion de canalisation (cuivre, PER, multicouche ou PVC). Nous utilisons des pièces de qualité et privilégions les solutions durables plutôt que les réparations provisoires. Quand l'ouverture d'un mur ou d'un sol est inévitable, elle est limitée au strict nécessaire.</p>"),
            ("Fuite d'eau, assurance et facture d'eau",
             "<p>Une fuite qui provoque un dégât des eaux est généralement couverte par votre assurance multirisque habitation, selon votre contrat. Nous vous remettons une <strong>facture détaillée</strong> et un <strong>descriptif de la cause et de la localisation de la fuite</strong>, les documents que demandent les assureurs.</p>"
             "<p>Si la fuite se trouve sur une canalisation après le compteur, la <strong>loi Warsmann</strong> permet en outre de faire plafonner votre facture d'eau, à condition de fournir une attestation de réparation d'une entreprise de plomberie dans le mois qui suit l'information par votre service des eaux. <a href=\"/conseils/fuite-apres-compteur-loi-warsmann/\">Lire notre guide sur la loi Warsmann</a>.</p>"),
        ],
        "faq": [
            ("Combien coûte une recherche de fuite ?", "La réparation d'une fuite démarre autour de 79 € en journée. Une recherche de fuite plus poussée (fuite encastrée, enterrée ou sous dalle) est chiffrée au cas par cas, toujours avant intervention."),
            ("La recherche de fuite est-elle prise en charge par l'assurance ?", "Beaucoup de contrats multirisques habitation prennent en charge la recherche de fuite lorsqu'elle est liée à un dégât des eaux. Vérifiez votre contrat : nous fournissons les justificatifs nécessaires (facture détaillée, cause et localisation)."),
            ("Faut-il casser le mur pour trouver une fuite ?", "Pas forcément. Les méthodes thermique et acoustique permettent souvent de localiser la fuite précisément, ce qui limite l'ouverture au strict nécessaire."),
            ("Mon WC coule en permanence, est-ce une fuite ?", "Oui, et elle peut représenter plusieurs dizaines de mètres cubes par an. C'est souvent le mécanisme de chasse ou le joint de clapet qu'il faut remplacer, une réparation rapide."),
        ],
        "combo_h1": "Recherche et réparation de fuite d'eau",
        "combo_title": "Recherche de fuite {city} ({cp}) — fuite d'eau dès 79 €",
        "combo_meta": "Fuite d'eau {a} ? Recherche de fuite sans casse inutile et réparation dès 79 €. Justificatifs pour l'assurance. {delay_txt}. ☎ 06 75 93 19 04",
        "combo_intros": [
            "Compteur qui tourne, auréole au plafond, facture d'eau qui grimpe : {a}, nous localisons l'origine de la fuite avec méthode, puis nous la réparons, à partir de 79 €.",
            "Une fuite d'eau {a} doit être traitée vite : elle abîme les murs, les sols et votre budget. Nous intervenons depuis Vidauban pour trouver la fuite sans casser inutilement et la réparer durablement.",
            "Vous suspectez une fuite dans votre maison ou votre appartement {a} ? Avant d'ouvrir un mur, nous cherchons. Contrôle des équipements, détection thermique ou acoustique : l'objectif est de trouver la fuite du premier coup.",
        ],
        "combo_points": [
            "Fuite sous évier, lavabo ou baignoire",
            "WC qui coule en continu",
            "Fuite sur canalisation encastrée ou enterrée",
            "Fuite au groupe de sécurité du chauffe-eau",
            "Infiltration au plafond, chez vous ou chez le voisin",
            "Surconsommation d'eau inexpliquée",
        ],
        "combo_tip": "Faites le test du compteur avant notre arrivée : fermez tous les robinets, notez l'index, attendez une heure sans utiliser d'eau. S'il a bougé, la fuite est confirmée et ce relevé nous aide à la localiser plus vite.",
    },
    # ------------------------------------------------------------------ DEBOUCHAGE
    {
        "slug": "debouchage-canalisation-var",
        "combo": "debouchage",
        "name": "Débouchage WC & canalisation",
        "short": "Débouchage",
        "icon": "pipe",
        "badge": "Rapide",
        "price_label": "à partir de 99 €",
        "price_min": 99,
        "title": "Débouchage WC, évier et canalisation dans le Var — dès 99 €",
        "meta": "Débouchage WC, évier, douche, baignoire et canalisation dans le Var, 7j/7. Matériel professionnel, sans produits agressifs, dès 99 €. ☎ 06 75 93 19 04",
        "h1": "Débouchage WC, évier et canalisation dans le Var",
        "lead": "WC bouché, évier qui ne se vide plus, douche qui stagne, odeurs d'égout : nous débouchons <b>avec du matériel professionnel et sans produits agressifs</b>. Intervention à partir de 99 €.",
        "checks": ["Matériel adapté à chaque bouchon", "Sans produits corrosifs", "Garantie sur l'intervention"],
        "card_desc": "WC, évier, douche, canalisation bouchée. Intervention rapide avec matériel adapté.",
        "card_checks": ["Sans produits agressifs", "Garantie sur l'intervention"],
        "sections": [
            ("Tous types de bouchons",
             "<ul><li><strong>Débouchage WC</strong> : papier en excès, lingettes, objets tombés dans la cuvette, tartre accumulé.</li>"
             "<li><strong>Débouchage évier de cuisine</strong> : graisses figées, résidus alimentaires, marc de café.</li>"
             "<li><strong>Débouchage douche, baignoire et lavabo</strong> : cheveux, savon, calcaire.</li>"
             "<li><strong>Débouchage de canalisation et de colonne</strong> : évacuations communes, descentes, collecteurs.</li>"
             "<li><strong>Canalisations extérieures et regards</strong> : racines, terre, dépôts.</li></ul>"),
            ("Notre méthode : le bon outil pour le bon bouchon",
             "<p>Un bouchon ne se traite pas de la même façon dans un WC, dans un siphon de lavabo ou à plusieurs mètres dans une canalisation enterrée. Nous commençons par identifier où se trouve le bouchon et de quoi il est fait, puis nous utilisons l'outil adapté : pompe à déboucher professionnelle, démontage et nettoyage du siphon, furet manuel ou motorisé pour atteindre les bouchons profonds.</p>"
             "<p>Lorsque la canalisation est très encrassée sur une grande longueur, un curage plus important peut être nécessaire : nous vous l'expliquons et vous donnons le prix avant de le réaliser.</p>"
             "<div class=\"callout\"><strong>Évitez la soude caustique et l'acide.</strong> Ces produits attaquent les joints et les canalisations, surtout les anciennes, et rendent l'intervention du plombier dangereuse s'ils stagnent dans le tuyau. Si vous en avez déjà versé, dites-le nous au téléphone.</div>"),
            ("Pourquoi vos canalisations se bouchent",
             "<p>Les causes les plus fréquentes sont les <strong>lingettes</strong> (même « biodégradables », elles ne se désagrègent pas assez vite), les <strong>graisses de cuisson</strong> qui figent en refroidissant, les <strong>cheveux</strong> et, dans le Var, le <strong>calcaire</strong> qui réduit progressivement le diamètre intérieur des tuyaux. Une pente insuffisante ou une canalisation mal dimensionnée peuvent aussi expliquer des bouchons à répétition : dans ce cas, nous vous proposons une solution pour régler le problème à la source.</p>"),
            ("Conseils pour éviter les bouchons",
             "<ul><li>Ne jetez ni lingettes, ni cotons, ni protections hygiéniques dans les WC.</li>"
             "<li>Versez les graisses de cuisson refroidies dans un pot, pas dans l'évier.</li>"
             "<li>Installez une grille sur la bonde de douche pour retenir les cheveux.</li>"
             "<li>Une fois par mois, faites couler de l'eau très chaude dans les évacuations de cuisine.</li></ul>"),
        ],
        "faq": [
            ("Combien coûte un débouchage de WC ?", "Un débouchage démarre à partir de 99 €. Le prix exact dépend de l'emplacement du bouchon et du matériel nécessaire ; il est confirmé avant intervention."),
            ("Intervenez-vous le week-end pour un WC bouché ?", "Oui, 7j/7. Si c'est votre seul WC, la situation est considérée comme une urgence."),
            ("Le débouchage est-il garanti ?", "Oui, l'intervention est garantie. Si le bouchon revient rapidement, nous recherchons la cause de fond (pente, canalisation abîmée, dépôt de calcaire)."),
            ("Puis-je utiliser un produit déboucheur avant votre venue ?", "Nous le déconseillons : les produits corrosifs abîment les canalisations et compliquent l'intervention. Une ventouse peut être essayée sans risque."),
        ],
        "combo_h1": "Débouchage WC, évier et canalisation",
        "combo_title": "Débouchage {city} ({cp}) — WC, évier, canalisation dès 99 €",
        "combo_meta": "Débouchage WC, évier, douche et canalisation {a}, 7j/7. Matériel professionnel, sans produits agressifs, dès 99 €. {delay_txt}. ☎ 06 75 93 19 04",
        "combo_intros": [
            "WC bouché, évier qui déborde, douche qui ne se vide plus : {a}, nous débouchons vos canalisations avec du matériel professionnel, sans produits corrosifs, à partir de 99 €.",
            "Une canalisation bouchée {a} ne se règle pas toujours à la ventouse. Pompe professionnelle, démontage du siphon, furet manuel ou motorisé : nous choisissons l'outil adapté au bouchon.",
            "Vous cherchez un débouchage rapide {a} ? Nous intervenons 7j/7 depuis Vidauban pour les WC, éviers, lavabos, douches, baignoires et canalisations, avec un prix confirmé avant de commencer.",
        ],
        "combo_points": [
            "Débouchage WC et toilettes",
            "Débouchage évier de cuisine",
            "Débouchage douche, baignoire, lavabo",
            "Canalisation ou colonne bouchée",
            "Odeurs d'égout et évacuation lente",
            "Regard et canalisation extérieure",
        ],
        "combo_tip": "Avant notre arrivée, n'utilisez pas de soude caustique ni d'acide : ces produits abîment les canalisations et rendent le débouchage plus délicat. Une ventouse peut être tentée sans risque.",
    },
    # ------------------------------------------------------------------ CHAUFFE-EAU
    {
        "slug": "chauffe-eau-var",
        "combo": "chauffe-eau",
        "name": "Chauffe-eau : dépannage & remplacement",
        "short": "Chauffe-eau",
        "icon": "heater",
        "badge": "Pose soignée",
        "price_label": "sur devis",
        "price_min": None,
        "title": "Chauffe-eau dans le Var : dépannage, remplacement, installation",
        "meta": "Plus d'eau chaude ? Dépannage, remplacement et installation de chauffe-eau électrique ou thermodynamique dans le Var. Devis gratuit. ☎ 06 75 93 19 04",
        "h1": "Dépannage, remplacement et installation de chauffe-eau dans le Var",
        "lead": "Plus d'eau chaude, eau tiède, fuite au groupe de sécurité, ballon qui disjoncte : nous <b>dépannons ou remplaçons votre chauffe-eau</b>, électrique ou thermodynamique, avec un devis gratuit et détaillé.",
        "checks": ["Diagnostic de la panne", "Conseil sur la capacité", "Garantie pièces et main-d'œuvre"],
        "card_desc": "Remplacement, dépannage et installation de chauffe-eau électrique ou thermodynamique.",
        "card_checks": ["Pose soignée", "Garantie pièces et MO"],
        "sections": [
            ("Les pannes de chauffe-eau les plus courantes",
             "<ul><li><strong>Plus d'eau chaude du tout</strong> : résistance hors service, thermostat défaillant, sécurité déclenchée, problème d'alimentation électrique ou de contacteur heures creuses.</li>"
             "<li><strong>Eau tiède ou qui refroidit vite</strong> : ballon entartré, résistance recouverte de calcaire, thermostat mal réglé.</li>"
             "<li><strong>Fuite au groupe de sécurité</strong> : quelques gouttes pendant la chauffe sont normales, un écoulement continu ne l'est pas.</li>"
             "<li><strong>Le chauffe-eau fait disjoncter</strong> : résistance ou câblage endommagé, à faire contrôler rapidement.</li>"
             "<li><strong>Cuve qui fuit</strong> : la cuve est percée par la corrosion, le remplacement du ballon est alors nécessaire.</li></ul>"
             "<p>Nous diagnostiquons la panne et vous disons honnêtement s'il vaut mieux réparer ou remplacer, en fonction de l'âge du ballon et du coût de la réparation.</p>"),
            ("Remplacement et installation de chauffe-eau",
             "<p>Nous installons des <strong>chauffe-eau électriques</strong> (verticaux, horizontaux, muraux ou sur socle) et des <strong>chauffe-eau thermodynamiques</strong>, plus économes à l'usage. La pose comprend la dépose de l'ancien appareil, le raccordement eau froide et eau chaude, un groupe de sécurité neuf, le raccordement à l'évacuation et la mise en service.</p>"
             "<h3>Quelle capacité choisir ?</h3>"
             "<div class=\"table-scroll\"><table><thead><tr><th>Foyer</th><th>Capacité indicative</th></tr></thead><tbody>"
             "<tr><td>1 personne</td><td>50 à 100 litres</td></tr>"
             "<tr><td>2 personnes</td><td>100 à 150 litres</td></tr>"
             "<tr><td>3 à 4 personnes</td><td>200 litres</td></tr>"
             "<tr><td>5 personnes et plus</td><td>250 à 300 litres</td></tr></tbody></table></div>"
             "<p>Ces valeurs sont indicatives : le nombre de salles de bain, la présence d'une baignoire et vos habitudes comptent aussi. Nous vous conseillons la capacité adaptée, sans surdimensionner.</p>"),
            ("Eau calcaire : entretenir son chauffe-eau dans le Var",
             "<p>Dans une grande partie du Var, l'eau est calcaire. Le tartre se dépose sur la résistance et au fond de la cuve, ce qui augmente la consommation électrique et raccourcit la durée de vie du ballon. Pour le préserver :</p>"
             "<ul><li>faites manœuvrer le groupe de sécurité une fois par mois quelques secondes ;</li>"
             "<li>faites détartrer le ballon et contrôler l'anode tous les deux à trois ans ;</li>"
             "<li>réglez le thermostat autour de 55 à 60 °C, un bon compromis entre hygiène et entartrage.</li></ul>"
             "<p><a href=\"/conseils/eau-calcaire-var-plomberie/\">Lire notre guide sur l'eau calcaire dans le Var</a>.</p>"),
        ],
        "faq": [
            ("Combien coûte le remplacement d'un chauffe-eau ?", "Le prix dépend de la capacité, du type d'appareil (électrique ou thermodynamique) et de l'accessibilité. Nous établissons un devis gratuit et détaillé avant toute pose."),
            ("Quelle est la durée de vie d'un chauffe-eau ?", "Un chauffe-eau électrique dure en moyenne 10 à 15 ans, parfois moins avec une eau très calcaire et sans entretien."),
            ("Mon groupe de sécurité goutte, est-ce grave ?", "Quelques gouttes pendant la chauffe sont normales : c'est la dilatation de l'eau. Un écoulement permanent indique un groupe de sécurité défectueux ou une pression trop élevée, à faire vérifier."),
            ("Pouvez-vous intervenir en urgence si je n'ai plus d'eau chaude ?", "Oui, nous intervenons 7j/7. Si la panne nécessite une pièce spécifique, nous vous indiquons le délai et une solution provisoire lorsque c'est possible."),
        ],
        "combo_h1": "Dépannage et remplacement de chauffe-eau",
        "combo_title": "Chauffe-eau {city} ({cp}) — dépannage et remplacement",
        "combo_meta": "Plus d'eau chaude {a} ? Dépannage, remplacement et installation de chauffe-eau électrique ou thermodynamique. Devis gratuit. {delay_txt}. ☎ 06 75 93 19 04",
        "combo_intros": [
            "Plus d'eau chaude {a} ? Résistance, thermostat, groupe de sécurité ou cuve percée : nous trouvons l'origine de la panne et vous disons franchement s'il vaut mieux réparer ou remplacer.",
            "Remplacement de cumulus, installation d'un chauffe-eau thermodynamique, fuite au groupe de sécurité : nous intervenons {a} avec un devis gratuit et détaillé.",
            "Votre chauffe-eau {a} fait des siennes ? Eau tiède, disjonction, écoulement continu : nous dépannons et remplaçons les chauffe-eau électriques et thermodynamiques de toutes marques.",
        ],
        "combo_points": [
            "Plus d'eau chaude ou eau tiède",
            "Fuite au groupe de sécurité",
            "Chauffe-eau qui fait disjoncter",
            "Remplacement de ballon électrique",
            "Installation de chauffe-eau thermodynamique",
            "Détartrage et entretien",
        ],
        "combo_tip": "Si votre chauffe-eau fuit, coupez son disjoncteur au tableau électrique puis fermez l'arrivée d'eau froide du ballon. Ne laissez pas un chauffe-eau sous tension s'il a été vidé.",
    },
    # ------------------------------------------------------------------ SANITAIRE
    {
        "slug": "installation-sanitaire-var",
        "combo": "installation-sanitaire",
        "name": "Installation sanitaire & robinetterie",
        "short": "Installation sanitaire",
        "icon": "tap",
        "badge": "Sur devis",
        "price_label": "sur devis",
        "price_min": None,
        "title": "Installation sanitaire dans le Var : WC, lavabo, douche, robinetterie",
        "meta": "Pose et remplacement de WC (suspendu ou au sol), lavabo, évier, douche, baignoire, mitigeur et robinetterie dans le Var. Devis gratuit. ☎ 06 75 93 19 04",
        "h1": "Installation sanitaire et robinetterie dans le Var",
        "lead": "Remplacement de WC, pose d'un WC suspendu, nouveau lavabo, douche, mitigeur thermostatique : nous installons vos équipements <b>proprement, dans les règles de l'art</b>, avec un devis gratuit et détaillé.",
        "checks": ["Conseil sur le choix du matériel", "Pose soignée et propre", "Devis gratuit et détaillé"],
        "card_desc": "Pose de WC, lavabo, douche, baignoire, robinetterie. Rénovation complète possible.",
        "card_checks": ["Conseil personnalisé", "Travail soigné"],
        "sections": [
            ("Ce que nous installons",
             "<ul><li><strong>WC</strong> : remplacement de WC au sol, pose de WC suspendu avec bâti-support, WC broyeur, remplacement de mécanisme de chasse.</li>"
             "<li><strong>Lavabos, vasques et éviers</strong> : pose, remplacement, raccordement des évacuations.</li>"
             "<li><strong>Douches et baignoires</strong> : receveur, colonne de douche, remplacement de baignoire par une douche.</li>"
             "<li><strong>Robinetterie</strong> : mitigeur, mitigeur thermostatique, robinet de cuisine, robinet d'arrêt, réducteur de pression.</li>"
             "<li><strong>Électroménager</strong> : raccordement de lave-linge et de lave-vaisselle (arrivée et évacuation).</li></ul>"),
            ("Bien choisir ses équipements",
             "<p>Nous vous conseillons en fonction de votre usage, de votre budget et de votre installation existante. Quelques exemples :</p>"
             "<ul><li>un <strong>mitigeur thermostatique</strong> sous la douche évite les variations de température, un vrai confort et une sécurité pour les enfants ;</li>"
             "<li>un <strong>WC suspendu</strong> facilite le ménage et gagne un peu de place, mais demande un bâti-support et un mur adapté ;</li>"
             "<li>une <strong>chasse d'eau à double débit</strong> réduit sensiblement la consommation d'eau ;</li>"
             "<li>en eau calcaire, des <strong>mousseurs démontables</strong> facilitent l'entretien de la robinetterie.</li></ul>"
             "<p>Vous pouvez fournir votre matériel ou nous laisser le fournir : dans tous les cas, nous vous indiquons ce qui est compatible avec votre installation.</p>"),
            ("Une pose propre, dans les règles de l'art",
             "<p>Chaque installation est réalisée avec des raccords et des joints de qualité, un contrôle d'étanchéité systématique et des évacuations correctement raccordées et ventilées. Nous protégeons les sols, évacuons les anciens équipements et laissons la pièce propre.</p>"),
        ],
        "faq": [
            ("Combien coûte le remplacement d'un WC ?", "Le prix dépend du type de WC (au sol, suspendu, broyeur) et de l'état des raccordements existants. Nous établissons un devis gratuit et détaillé avant les travaux."),
            ("Puis-je fournir moi-même le matériel ?", "Oui. Nous vérifions simplement qu'il est compatible avec votre installation et vous prévenons si une pièce complémentaire est nécessaire."),
            ("Combien de temps dure la pose d'un WC suspendu ?", "Comptez généralement une journée, habillage compris, selon la configuration de la pièce."),
            ("Intervenez-vous pour un simple robinet qui fuit ?", "Oui, aucune intervention n'est trop petite. Le remplacement d'une cartouche ou d'un mitigeur est souvent réalisé en moins d'une heure."),
        ],
        "combo_h1": "Installation sanitaire et robinetterie",
        "combo_title": "Installation sanitaire {city} — WC, lavabo, douche, robinet",
        "combo_meta": "Pose et remplacement de WC, lavabo, douche, baignoire, mitigeur et robinetterie {a}. Conseil, pose soignée, devis gratuit. ☎ 06 75 93 19 04",
        "combo_intros": [
            "Remplacer un WC, poser un lavabo, changer un mitigeur ou installer une douche {a} : nous vous conseillons sur le matériel et réalisons une pose propre et durable.",
            "Vous rénovez ou remplacez un équipement {a} ? WC au sol ou suspendu, vasque, évier, robinetterie thermostatique : nous installons, raccordons et contrôlons l'étanchéité.",
            "Pour vos travaux d'installation sanitaire {a}, nous établissons un devis gratuit et détaillé, puis nous intervenons à la date convenue, en laissant la pièce propre.",
        ],
        "combo_points": [
            "Remplacement de WC, pose de WC suspendu",
            "Pose de lavabo, vasque et évier",
            "Mitigeur et robinetterie thermostatique",
            "Receveur et colonne de douche",
            "Raccordement lave-linge et lave-vaisselle",
            "Remplacement de mécanisme de chasse",
        ],
        "combo_tip": "Pour un devis précis, envoyez-nous quelques photos de la pièce et des raccordements existants (arrivées d'eau, évacuation) : nous pourrons vous conseiller avant même de nous déplacer.",
    },
    # ------------------------------------------------------------------ CANALISATION
    {
        "slug": "reparation-canalisation-var",
        "combo": "reparation-canalisation",
        "name": "Réparation & remplacement de canalisation",
        "short": "Dépannage canalisation",
        "icon": "wrench",
        "badge": "Dépannage",
        "price_label": "à partir de 89 €",
        "price_min": 89,
        "title": "Réparation et remplacement de canalisation dans le Var — dès 89 €",
        "meta": "Canalisation percée, évacuation lente, odeurs d'égout, vieux tuyaux en plomb : réparation et remplacement de canalisations dans le Var dès 89 €. ☎ 06 75 93 19 04",
        "h1": "Réparation et remplacement de canalisations dans le Var",
        "lead": "Tuyau percé, évacuation qui fuit, odeurs d'égout, vieilles canalisations à remplacer : nous <b>diagnostiquons sur place et proposons une solution durable</b>, à partir de 89 €.",
        "checks": ["Diagnostic sur place", "Solutions durables", "Tous matériaux : cuivre, PER, multicouche, PVC"],
        "card_desc": "Réparation ou remplacement de canalisations, problèmes d'évacuation, odeurs, etc.",
        "card_checks": ["Diagnostic sur place", "Solutions durables"],
        "sections": [
            ("Nos interventions sur les canalisations",
             "<ul><li><strong>Réparation de tuyau percé ou fissuré</strong> : cuivre, PER, multicouche, acier galvanisé.</li>"
             "<li><strong>Remplacement de canalisations anciennes</strong>, notamment les tuyaux en plomb encore présents dans certaines maisons anciennes.</li>"
             "<li><strong>Évacuations PVC</strong> : fuites, raccords décollés, pentes insuffisantes, reprise de descentes.</li>"
             "<li><strong>Odeurs d'égout</strong> : siphon désamorcé, ventilation absente, joint défectueux.</li>"
             "<li><strong>Création et modification de réseaux</strong> pour une cuisine, une salle d'eau ou une buanderie.</li></ul>"),
            ("D'où viennent les odeurs d'égout ?",
             "<p>Une odeur d'égout dans une salle de bain ou une cuisine vient le plus souvent d'un <strong>siphon qui s'est vidé</strong> (appareil peu utilisé, évaporation en été), d'un <strong>joint de WC défectueux</strong> ou d'une <strong>ventilation des chutes</strong> absente ou bouchée. Dans un logement peu occupé, faire couler l'eau régulièrement dans chaque évacuation suffit souvent. Si l'odeur persiste, nous recherchons la cause et la corrigeons.</p>"),
            ("Les tuyaux en plomb : faut-il les remplacer ?",
             "<p>Les canalisations d'eau potable en plomb ne sont plus installées depuis longtemps mais subsistent dans certains logements anciens. Le plomb peut se dissoudre dans l'eau, en particulier quand elle stagne. Les autorités sanitaires recommandent de les remplacer. Nous remplaçons ces tronçons par des matériaux actuels (cuivre, PER ou multicouche) et vous conseillons, en attendant, de laisser couler l'eau quelques instants avant de la boire après une longue stagnation.</p>"),
            ("Notre façon de travailler",
             "<p>Nous commençons toujours par un diagnostic sur place : état des canalisations, matériau, accessibilité, cause de la panne. Vous recevez ensuite une proposition claire, avec le prix, et le choix entre une réparation ponctuelle et une reprise plus complète lorsque cela se justifie. Nous ne remplaçons pas ce qui peut être réparé durablement.</p>"),
        ],
        "faq": [
            ("Combien coûte la réparation d'une canalisation ?", "Les interventions démarrent à partir de 89 €. Le prix dépend du matériau, de l'accessibilité et de la longueur à reprendre ; il est confirmé avant intervention."),
            ("Pourquoi mon évacuation se vide-t-elle lentement ?", "Le plus souvent à cause d'un début de bouchon (graisses, cheveux, calcaire) ou d'une pente insuffisante. Un débouchage ou une reprise de pente règle le problème."),
            ("Peut-on réparer une canalisation encastrée sans tout casser ?", "Souvent oui : après localisation précise de la fuite, l'ouverture est limitée à la zone concernée. Dans certains cas, un nouveau passage apparent ou en doublage est plus judicieux."),
            ("Remplacez-vous les canalisations de toute une maison ?", "Oui, nous réalisons la reprise complète d'un réseau d'alimentation ou d'évacuation, sur devis détaillé."),
        ],
        "combo_h1": "Réparation et remplacement de canalisation",
        "combo_title": "Canalisation {city} ({cp}) — réparation, fuite, odeurs dès 89 €",
        "combo_meta": "Canalisation percée, évacuation lente, odeurs d'égout {a} : réparation et remplacement de canalisations dès 89 €. {delay_txt}. ☎ 06 75 93 19 04",
        "combo_intros": [
            "Tuyau percé, évacuation qui fuit, odeurs d'égout {a} : nous diagnostiquons sur place et proposons une réparation durable, à partir de 89 €.",
            "Vos canalisations {a} montrent des signes de faiblesse ? Fuites à répétition, vieux tuyaux en plomb ou en acier, évacuation lente : nous réparons ou remplaçons, cuivre, PER, multicouche ou PVC.",
            "Nous intervenons {a} sur tous les réseaux d'alimentation et d'évacuation : réparation d'urgence, reprise de pente, remplacement de tronçons, création de nouvelles arrivées.",
        ],
        "combo_points": [
            "Tuyau percé ou raccord qui fuit",
            "Évacuation lente ou qui refoule",
            "Odeurs d'égout dans la maison",
            "Remplacement de tuyaux en plomb",
            "Reprise d'évacuations PVC",
            "Nouvelles arrivées d'eau",
        ],
        "combo_tip": "Une odeur d'égout dans une pièce peu utilisée vient souvent d'un siphon qui s'est vidé par évaporation. Faites couler un peu d'eau dans chaque évacuation : si l'odeur persiste, appelez-nous.",
    },
    # ------------------------------------------------------------------ SALLE DE BAIN
    {
        "slug": "renovation-salle-de-bain-var",
        "combo": "renovation-salle-de-bain",
        "name": "Rénovation de salle de bain",
        "short": "Rénovation salle de bain",
        "icon": "bath",
        "badge": "Rénovation",
        "price_label": "sur devis",
        "price_min": None,
        "title": "Rénovation de salle de bain dans le Var — douche italienne, PMR",
        "meta": "Rénovation complète ou partielle de salle de bain dans le Var : remplacement baignoire par douche, douche à l'italienne, salle de bain PMR. Devis détaillé gratuit. ☎ 06 75 93 19 04",
        "h1": "Rénovation de salle de bain dans le Var",
        "lead": "Remplacer une baignoire par une douche, créer une douche à l'italienne, adapter la salle de bain pour un senior : nous menons votre <b>rénovation de A à Z</b>, plomberie, carrelage et robinetterie compris.",
        "checks": ["Visite et devis détaillé gratuits", "Un seul interlocuteur", "Chantier propre"],
        "card_desc": "Rénovation complète ou partielle de salle de bain : plomberie, carrelage, robinetterie.",
        "card_checks": ["Devis détaillé", "Travail propre"],
        "sections": [
            ("Vos projets de salle de bain",
             "<ul><li><strong>Remplacement de baignoire par une douche</strong>, avec receveur extra-plat pour un accès facilité.</li>"
             "<li><strong>Douche à l'italienne</strong> de plain-pied, avec étanchéité sous carrelage.</li>"
             "<li><strong>Salle de bain adaptée</strong> aux seniors et aux personnes à mobilité réduite : accès sans marche, barres d'appui, siège de douche, WC surélevé.</li>"
             "<li><strong>Rénovation complète</strong> : dépose, reprise des réseaux, carrelage et faïence, meuble vasque, WC suspendu, robinetterie.</li>"
             "<li><strong>Rafraîchissement partiel</strong> : changement du meuble vasque, de la robinetterie ou de la paroi de douche.</li></ul>"),
            ("Comment se déroule une rénovation",
             "<ol><li><strong>Visite</strong> : nous prenons les mesures, regardons l'état des réseaux et discutons de vos envies et de votre budget.</li>"
             "<li><strong>Devis détaillé</strong> : chaque poste est chiffré (dépose, plomberie, carrelage, fournitures, évacuation des gravats).</li>"
             "<li><strong>Planning</strong> : nous fixons ensemble les dates et la durée du chantier, en prévoyant si besoin une solution pour que vous puissiez vous laver pendant les travaux.</li>"
             "<li><strong>Travaux</strong> : protection des accès, chantier rangé chaque soir, contrôle d'étanchéité.</li>"
             "<li><strong>Réception</strong> : nous vérifions tout avec vous avant de clore le chantier.</li></ol>"),
            ("Ce qui fait une salle de bain durable",
             "<p>Une belle salle de bain qui fuit au bout de deux ans est un échec. Nous accordons une attention particulière à ce qui ne se voit pas : <strong>l'étanchéité</strong> sous le carrelage et autour du receveur, <strong>la pente</strong> des évacuations, la <strong>ventilation</strong> de la pièce pour éviter l'humidité, et l'accès aux éléments techniques (vannes, siphons) pour l'entretien futur.</p>"),
        ],
        "faq": [
            ("Combien coûte la rénovation d'une salle de bain ?", "Tout dépend de la surface, des équipements et des finitions choisies. Après une visite gratuite, nous vous remettons un devis détaillé poste par poste."),
            ("Combien de temps durent les travaux ?", "Le remplacement d'une baignoire par une douche prend généralement quelques jours ; une rénovation complète, une à trois semaines selon l'ampleur."),
            ("Peut-on faire une douche à l'italienne partout ?", "Pas toujours : il faut pouvoir créer une pente d'évacuation suffisante. Lorsque ce n'est pas possible, un receveur extra-plat offre un résultat très proche."),
            ("Gérez-vous aussi le carrelage ?", "Oui, la rénovation inclut la plomberie, le carrelage et la robinetterie : vous avez un seul interlocuteur pour l'ensemble du chantier."),
        ],
        "combo_h1": "Rénovation de salle de bain",
        "combo_title": "Rénovation salle de bain {city} — douche italienne, PMR",
        "combo_meta": "Rénovation de salle de bain {a} : baignoire remplacée par une douche, douche à l'italienne, aménagement PMR. Visite et devis détaillé gratuits. ☎ 06 75 93 19 04",
        "combo_intros": [
            "Vous voulez transformer votre salle de bain {a} ? Douche à l'italienne, remplacement de baignoire, meuble vasque, WC suspendu : nous gérons plomberie, carrelage et robinetterie.",
            "Pour une rénovation de salle de bain {a}, nous commençons par une visite gratuite, puis un devis détaillé poste par poste. Un seul interlocuteur du début à la fin du chantier.",
            "Salle de bain vieillissante, baignoire difficile d'accès, besoin d'adapter la pièce à un senior : nous rénovons votre salle de bain {a} avec un soin particulier pour l'étanchéité.",
        ],
        "combo_points": [
            "Remplacement de baignoire par une douche",
            "Douche à l'italienne",
            "Salle de bain senior et PMR",
            "Meuble vasque et robinetterie",
            "WC suspendu",
            "Carrelage et faïence",
        ],
        "combo_tip": "Pour préparer la visite, notez ce qui vous gêne dans votre salle de bain actuelle et rassemblez quelques photos d'inspiration : cela nous aide à vous proposer un projet qui vous ressemble, dans votre budget.",
    },
]

# Page spéciale assurance / dégât des eaux (pas de déclinaison par commune)
ASSURANCE_PAGE = {
    "slug": "plombier-degat-des-eaux-assurance-var",
    "name": "Dégât des eaux & assurance",
}

SERVICE_ICONS = {
    "bolt": '<path d="M13 2 4 14h6l-1 8 9-12h-6l1-8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/>',
    "drop": '<path d="M12 3s-6 6.6-6 11a6 6 0 0 0 12 0c0-4.4-6-11-6-11Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/>',
    "pipe": '<path d="M4 8h8a4 4 0 0 1 4 4v8M4 8V5M4 8v3M16 20h-3M16 20h3" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/>',
    "heater": '<rect x="6" y="3" width="12" height="18" rx="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 9v4M10 21v1M14 21v1" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/>',
    "tap": '<path d="M5 9h9a3 3 0 0 1 3 3v2M8 9V6M5 6h6M17 17v1M17 20.5v.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/>',
    "wrench": '<path d="M14.7 6.3a4 4 0 0 0-5.2 5.2L4 17l3 3 5.5-5.5a4 4 0 0 0 5.2-5.2l-2.4 2.4-2.6-.6-.6-2.6 2.6-2.2Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>',
    "bath": '<path d="M3 12h18v2a5 5 0 0 1-5 5H8a5 5 0 0 1-5-5v-2ZM6 12V6a2 2 0 0 1 4 0M7 19l-1 2M17 19l1 2" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/>',
    "shield": '<path d="M12 2 4 5v6c0 5 3.4 8.7 8 11 4.6-2.3 8-6 8-11V5l-8-3Z" stroke="currentColor" stroke-width="1.8"/><path d="M8.5 12l2.3 2.3L15.5 9.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>',
}
