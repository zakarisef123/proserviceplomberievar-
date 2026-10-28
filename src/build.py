# -*- coding: utf-8 -*-
"""Générateur du site PRO SERVICE 83.

Usage : python3 src/build.py
Produit le site statique complet dans ./public (pages, sitemap.xml, robots.txt, llms.txt…).
Aucune dépendance externe.
"""
import html
import json
import os
import shutil
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(__file__))
import data_business as B  # noqa: E402
from data_cities import CITIES, CITY_BY_SLUG  # noqa: E402
from data_guides import GUIDES  # noqa: E402
from data_services import SERVICES, SERVICE_ICONS, ASSURANCE_PAGE  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "public")
SRC_ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
TODAY = date.today().isoformat()
SITE = B.SITE_URL.rstrip("/")
ASSET_VERSION = TODAY.replace("-", "")

SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}
CORE_CITIES = [c for c in CITIES if c["core"]]
PAGES = []  # (chemin, priorité) pour le sitemap


def esc(s):
    return html.escape(s, quote=True)


def strip_tags(s):
    import re
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


def abs_url(path):
    return SITE + path


def city_path(c):
    return "/plombier-%s/" % c["slug"]


def combo_path(s, c):
    return "/%s-%s/" % (s["combo"], c["slug"])


def service_path(s):
    return "/%s/" % s["slug"]


def guide_path(g):
    return "/conseils/%s/" % g["slug"]


def delay_label(c):
    return "sur place" if c["delay"] == 0 else "~%d min" % c["delay"]


def delay_sentence(c):
    if c["delay"] == 0:
        return "Notre base est à Vidauban : nous y intervenons sans délai de route, souvent dans l'heure."
    return "Depuis notre base de Vidauban, comptez environ %d minutes pour arriver %s, hors trafic. Le délai précis vous est donné au moment de l'appel." % (c["delay"], c["a"])


def delay_txt(c):
    return "Basé à Vidauban" if c["delay"] == 0 else "À ~%d min de Vidauban" % c["delay"]


# ---------------------------------------------------------------- icônes
PHONE_SVG = '<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M6.6 10.8c1.5 3 3.9 5.4 6.9 6.9l2.3-2.3c.3-.3.7-.4 1.1-.2 1.2.4 2.5.6 3.9.6.6 0 1 .4 1 1V21c0 .6-.4 1-1 1C10.6 22 2 13.4 2 3c0-.6.4-1 1-1h4.2c.6 0 1 .4 1 1 0 1.4.2 2.7.6 3.9.1.4 0 .8-.2 1.1L6.6 10.8Z" {paint}/></svg>'


def phone_icon(size=16, filled=False):
    paint = 'fill="currentColor"' if filled else 'stroke="currentColor" stroke-width="1.8"'
    return PHONE_SVG.format(s=size, paint=paint)


def svc_icon(key, size=24):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" aria-hidden="true">%s</svg>' % (size, size, SERVICE_ICONS[key])


LOGO_SVG = '<svg class="logo-mark" viewBox="0 0 40 40" fill="none" aria-hidden="true"><path d="M20 3 L33 20 L20 37 L7 20 Z" fill="#4a2a86"/><path d="M20 3 L33 20 L20 37 Z" fill="#f37b1e"/></svg>'


# ---------------------------------------------------------------- données structurées
def business_schema():
    area = [{"@type": "City", "name": c["name"], "postalCode": c["cp"]} for c in CITIES]
    area.append({"@type": "AdministrativeArea", "name": "Var (83)"})
    address = {
        "@type": "PostalAddress",
        "addressLocality": B.BASE_CITY,
        "postalCode": B.BASE_CP,
        "addressRegion": B.REGION,
        "addressCountry": "FR",
    }
    if B.ADDRESS_STREET:
        address["streetAddress"] = B.ADDRESS_STREET
    data = {
        "@context": "https://schema.org",
        "@type": "Plumber",
        "@id": SITE + "/#entreprise",
        "name": B.NAME,
        "description": "Artisan plombier basé à Vidauban (Var). Dépannage plomberie 24h/24 et 7j/7 : fuite d'eau, recherche de fuite, débouchage, chauffe-eau, canalisations, installation sanitaire et rénovation de salle de bain.",
        "url": SITE + "/",
        "telephone": B.PHONE_TEL,
        "email": B.EMAIL,
        "image": SITE + "/assets/og-image.png",
        "logo": SITE + "/assets/logo-512.png",
        "priceRange": "€€",
        "currenciesAccepted": "EUR",
        "foundingDate": str(B.SINCE),
        "address": address,
        "geo": {"@type": "GeoCoordinates", "latitude": B.GEO[0], "longitude": B.GEO[1]},
        "areaServed": area,
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "00:00", "closes": "23:59",
        }],
        "knowsAbout": ["Plomberie", "Recherche de fuite", "Débouchage de canalisation", "Chauffe-eau",
                       "Installation sanitaire", "Rénovation de salle de bain", "Dégât des eaux"],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Prestations de plomberie",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"], "url": abs_url(service_path(s))}}
                for s in SERVICES
            ],
        },
    }
    same_as = [u for u in [B.GOOGLE_BUSINESS_URL] + list(B.SAME_AS) if u]
    if same_as:
        data["sameAs"] = same_as
    if B.SIRET:
        data["identifier"] = {"@type": "PropertyValue", "propertyID": "SIRET", "value": B.SIRET}
    return data


def breadcrumb_schema(crumbs):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": abs_url(path)}
            for i, (name, path) in enumerate(crumbs)
        ],
    }


def faq_schema(faq):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in faq
        ],
    }


def service_schema(name, desc, path, area_name, price_min=None):
    data = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": name,
        "serviceType": name,
        "description": desc,
        "url": abs_url(path),
        "provider": {"@id": SITE + "/#entreprise"},
        "areaServed": {"@type": "City" if area_name != "Var (83)" else "AdministrativeArea", "name": area_name},
        "availableChannel": {"@type": "ServiceChannel", "servicePhone": B.PHONE_TEL},
    }
    if price_min:
        data["offers"] = {"@type": "Offer", "priceCurrency": "EUR",
                          "priceSpecification": {"@type": "PriceSpecification", "minPrice": price_min, "priceCurrency": "EUR"}}
    return data


# ---------------------------------------------------------------- gabarit
NAV = [
    ("Prestations", "/prestations/"),
    ("Zones", "/zones-intervention/"),
    ("Tarifs", "/tarifs/"),
    ("Conseils", "/conseils/"),
    ("À propos", "/a-propos/"),
    ("Contact", "/contact/"),
]


def head(title, desc, path, schemas, og_type="website", noindex=False):
    canonical = abs_url(path)
    schema_tags = "\n".join(
        '<script type="application/ld+json">%s</script>' % json.dumps(s, ensure_ascii=False, separators=(",", ":"))
        for s in schemas
    )
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large, max-snippet:-1"
    verif = ""
    if B.GOOGLE_SITE_VERIFICATION:
        verif += '<meta name="google-site-verification" content="%s">\n' % esc(B.GOOGLE_SITE_VERIFICATION)
    if B.BING_SITE_VERIFICATION:
        verif += '<meta name="msvalidate.01" content="%s">\n' % esc(B.BING_SITE_VERIFICATION)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canonical}">
{verif}<meta name="geo.region" content="FR-83">
<meta name="geo.placename" content="{esc(B.BASE_CITY)}">
<meta name="geo.position" content="{B.GEO[0]};{B.GEO[1]}">
<meta name="ICBM" content="{B.GEO[0]}, {B.GEO[1]}">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="{esc(B.NAME)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#4a2a86">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">

<!-- Google tag (gtag.js) + Consent Mode v2 -->
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  (function(){{
    /* Consentement par défaut : refusé tant que le visiteur n'a pas choisi (CNIL / RGPD) */
    var c = null; try {{ c = JSON.parse(localStorage.getItem('ps83-consent')); }} catch(e) {{}}
    var ok = c && (Date.now() - c.t) < 182*24*3600*1000;
    var ads = ok && c.ads ? 'granted' : 'denied';
    var perso = ok && c.ads && c.perso ? 'granted' : 'denied';
    gtag('consent', 'default', {{ad_storage:ads, ad_user_data:ads, ad_personalization:perso, analytics_storage:ads, functionality_storage:'granted', security_storage:'granted', wait_for_update:500}});
    gtag('set', 'ads_data_redaction', ads === 'denied');
    gtag('set', 'url_passthrough', true);
  }})();
  gtag('js', new Date());
  gtag('config', '{B.GTAG_ID}');
</script>
<script async src="https://www.googletagmanager.com/gtag/js?id={B.GTAG_ID}"></script>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css?v={ASSET_VERSION}">
{schema_tags}
</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
"""


def header(path):
    links = "".join(
        '<a href="%s"%s>%s</a>' % (href, ' aria-current="page"' if path.startswith(href) else "", label)
        for label, href in NAV
    )
    mlinks = "".join('<a href="%s">%s</a>' % (href, label) for label, href in [("Accueil", "/"), ("Urgence 24h/24", "/plombier-urgence-24h-var/")] + NAV)
    return f"""<header class="site">
  <div class="wrap headbar">
    <a class="logo" href="/" aria-label="{B.NAME}, accueil">
      {LOGO_SVG}
      <span class="logo-text"><span class="l1" style="display:block">Pro Service</span><span class="l2" style="display:block">PLOMBIER 83</span></span>
    </a>
    <nav class="main" aria-label="Navigation principale">{links}</nav>
    <a href="tel:{B.PHONE_TEL}" class="call-pill">
      {phone_icon(16)}
      <span class="dot dot-pulse"></span>
      <span class="txt">{B.PHONE}</span>
    </a>
    <button class="menu-btn" type="button" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="mobile-nav">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
    </button>
  </div>
  <nav class="mobile-nav" id="mobile-nav" aria-label="Navigation mobile">{mlinks}</nav>
</header>
<main id="contenu">
"""


def footer(form_anchor="#devis"):
    svc_links = "".join('<li><a href="%s">%s</a></li>' % (service_path(s), esc(s["short"])) for s in SERVICES)
    svc_links += '<li><a href="/%s/">%s</a></li>' % (ASSURANCE_PAGE["slug"], ASSURANCE_PAGE["name"])
    city_links = "".join('<li><a href="%s">Plombier %s</a></li>' % (city_path(c), esc(c["name"])) for c in CORE_CITIES)
    city_links += '<li><a href="/zones-intervention/">Toutes les communes</a></li>'
    return f"""</main>
<footer class="site">
  <div class="wrap">
    <div class="foot-cols">
      <div>
        <a class="logo" href="/">{LOGO_SVG.replace('class="logo-mark"', 'class="logo-mark" width="34" height="34"')}<span class="logo-text"><span class="l2">{B.NAME}</span></span></a>
        <p class="foot-about">Artisan plombier indépendant basé à <b>Vidauban</b> depuis {B.SINCE}. Dépannage <b>24h/24 et 7j/7</b> dans le centre Var : fuite, débouchage, chauffe-eau, sanitaire, salle de bain.</p>
        <p class="foot-about"><a href="tel:{B.PHONE_TEL}"><b>{B.PHONE}</b></a><br><a href="mailto:{B.EMAIL}">{B.EMAIL}</a></p>
      </div>
      <div><h2>Prestations</h2><ul>{svc_links}</ul></div>
      <div><h2>Zones d'intervention</h2><ul>{city_links}</ul></div>
      <div><h2>Informations</h2><ul>
        <li><a href="/tarifs/">Tarifs</a></li>
        <li><a href="/a-propos/">À propos &amp; engagements</a></li>
        <li><a href="/conseils/">Conseils plomberie</a></li>
        <li><a href="/faq/">Questions fréquentes</a></li>
        <li><a href="/contact/">Contact &amp; devis</a></li>
        <li><a href="/plan-du-site/">Plan du site</a></li>
      </ul></div>
    </div>
    <div class="foot-bottom">
      <span>© {date.today().year} {B.NAME} — Artisan plombier indépendant, Vidauban (83550), Var.</span>
      <span><a href="/mentions-legales/">Mentions légales</a> · <a href="/politique-confidentialite/">Confidentialité</a> · <button type="button" data-consent="open">Cookies</button></span>
    </div>
  </div>
</footer>

<a href="tel:{B.PHONE_TEL}" class="float-call" aria-label="Appeler {B.NAME}">{phone_icon(24, True)}</a>
<div class="mobile-bar">
  <a href="tel:{B.PHONE_TEL}" class="btn btn-orange">{phone_icon(18, True)} Appeler</a>
  <a href="{form_anchor}" class="btn btn-purple">Devis gratuit</a>
</div>

<div class="consent" id="consent" role="dialog" aria-labelledby="consent-title">
  <h2 id="consent-title">Vos choix en matière de cookies</h2>
  <p>Avec votre accord, nous utilisons des cookies Google Ads pour mesurer les appels et demandes de devis issus de nos annonces. Aucun cookie publicitaire n'est déposé sans votre accord, et le site fonctionne dans tous les cas. Votre choix est conservé 6 mois et modifiable à tout moment via le lien « Cookies » en bas de page. <a href="/politique-confidentialite/">En savoir plus</a></p>
  <div class="consent-prefs" id="consent-prefs" hidden>
    <label class="toggle"><input type="checkbox" checked disabled><span><b>Cookies nécessaires</b> — mémorisation de votre choix. Toujours actifs.</span></label>
    <label class="toggle"><input type="checkbox" id="c-ads"><span><b>Mesure publicitaire (Google Ads)</b> — savoir quelles annonces génèrent des appels et des demandes de devis.</span></label>
    <label class="toggle"><input type="checkbox" id="c-perso"><span><b>Personnalisation des annonces</b> — vous montrer des annonces adaptées sur les services Google.</span></label>
  </div>
  <div class="row">
    <button type="button" class="btn btn-purple" data-consent="granted">Tout accepter</button>
    <button type="button" class="btn btn-purple" data-consent="denied">Tout refuser</button>
    <button type="button" class="btn btn-outline" data-consent="custom" id="consent-custom">Personnaliser</button>
  </div>
</div>

<script src="/assets/main.js?v={ASSET_VERSION}" defer></script>
</body>
</html>
"""


def write_page(path, content, priority="0.6", sitemap=True):
    target = os.path.join(OUT, path.strip("/"), "index.html") if path != "/" else os.path.join(OUT, "index.html")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)
    if sitemap:
        PAGES.append((path, priority))


# ---------------------------------------------------------------- blocs réutilisables
def crumbs_html(crumbs):
    parts = []
    for i, (name, path) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            parts.append('<span aria-current="page">%s</span>' % esc(name))
        else:
            parts.append('<a href="%s">%s</a><span class="sep">›</span>' % (path, esc(name)))
    return '<nav class="crumbs" aria-label="Fil d\'Ariane">%s</nav>' % "".join(parts)


def page_hero(crumbs, h1, lead, checks=None, badge=None):
    checks_html = ""
    if checks:
        checks_html = '<div class="hero-checks">%s</div>' % "".join(
            '<div class="check-row"><span class="check-circle gr">✓</span>%s</div>' % esc(c) for c in checks)
    badge_html = ""
    if badge:
        badge_html = '<div class="pill avail-badge" style="margin:18px 0 0"><span class="dot dot-pulse"></span><span>%s</span></div>' % badge
    return f"""<section class="page-hero">
  <div class="wrap">
    {crumbs_html(crumbs)}
    {badge_html}
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    <div class="actions">
      <a href="tel:{B.PHONE_TEL}" class="btn btn-orange">{phone_icon(18, True)} {B.PHONE}</a>
      <a href="#devis" class="btn btn-ghost">Demander un devis gratuit</a>
    </div>
    {checks_html}
  </div>
</section>
"""


def strip_band():
    items = [
        ('<path d="M12 2 4 5v6c0 5 3.4 8.7 8 11 4.6-2.3 8-6 8-11V5l-8-3Z" stroke="currentColor" stroke-width="1.8"/>', "Factures acceptées par les assurances"),
        ('<circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.8"/><path d="M12 7v5l3.5 2" stroke="currentColor" stroke-width="1.8"/>', "Disponible 24h/24 et 7j/7"),
        ('<path d="M4 6h16M4 12h16M4 18h10" stroke="currentColor" stroke-width="1.8"/>', "Prix annoncé avant intervention"),
        ('<path d="M3 12h4l3-8 4 16 3-8h4" stroke="currentColor" stroke-width="1.8"/>', "Artisan local depuis %d" % B.SINCE),
    ]
    inner = "".join('<div class="strip-item"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true">%s</svg>%s</div>' % (p, t) for p, t in items)
    return '<div class="strip"><div class="wrap strip-grid">%s</div></div>\n' % inner


def service_options(selected=None):
    names = [s["short"] for s in SERVICES] + ["Dégât des eaux / assurance", "Autre demande"]
    return "".join('<option%s>%s</option>' % (" selected" if n == selected else "", esc(n)) for n in names)


def city_options(selected=None):
    opts = ['<option value="">Choisir…</option>']
    opts += ['<option%s>%s</option>' % (" selected" if c["name"] == selected else "", esc(c["name"])) for c in CITIES]
    opts.append("<option>Autre commune du Var</option>")
    return "".join(opts)


def contact_section(path, title="Besoin d'un plombier maintenant ?", service=None, city=None):
    """Formulaire de devis complet (Netlify Forms : « devis »), présent en bas de chaque page."""
    return f"""<section class="contact" id="devis">
  <div class="wrap contact-grid">
    <div>
      <div class="pill pill-orange">Contact &amp; devis gratuit</div>
      <h2>{title}</h2>
      <p class="lead">Pour une urgence, l'appel reste le plus rapide : un plombier vous répond directement. Pour une demande de devis, remplissez le formulaire, nous vous rappelons rapidement (sous 1 h en journée).</p>
      <div class="contact-info">
        <div class="cinfo">
          <div class="icon-sq">{phone_icon(18)}</div>
          <div><b><a href="tel:{B.PHONE_TEL}">{B.PHONE}</a></b><span>Ligne directe, 24h/24 et 7j/7</span></div>
        </div>
        <div class="cinfo">
          <div class="icon-sq"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4 6h16v12H4z" stroke="currentColor" stroke-width="1.8"/><path d="M4 7l8 6 8-6" stroke="currentColor" stroke-width="1.8"/></svg></div>
          <div><b><a href="mailto:{B.EMAIL}">{B.EMAIL}</a></b><span>Devis et demandes non urgentes</span></div>
        </div>
        <div class="cinfo">
          <div class="icon-sq">{svc_icon("shield", 18)}</div>
          <div><b>Vidauban &amp; tout le centre Var</b><span>Diagnostic téléphonique et devis gratuits</span></div>
        </div>
      </div>
    </div>
    <form class="quote" name="devis" method="POST" data-netlify="true" netlify-honeypot="adresse-web" action="/contact/">
      <input type="hidden" name="form-name" value="devis">
      <input type="hidden" name="page" value="{esc(path)}">
      <p class="hp"><label>Ne pas remplir : <input name="adresse-web" tabindex="-1" autocomplete="off"></label></p>
      <div class="frow-2">
        <div class="frow">
          <label for="d-nom">Nom *</label>
          <input id="d-nom" name="nom" type="text" required autocomplete="name" placeholder="Votre nom">
        </div>
        <div class="frow">
          <label for="d-tel">Téléphone *</label>
          <input id="d-tel" name="telephone" type="tel" required autocomplete="tel" placeholder="06 00 00 00 00">
        </div>
      </div>
      <div class="frow-2">
        <div class="frow">
          <label for="d-email">E-mail</label>
          <input id="d-email" name="email" type="email" autocomplete="email" placeholder="vous@exemple.fr">
        </div>
        <div class="frow">
          <label for="d-ville">Commune</label>
          <select id="d-ville" name="commune">{city_options(city)}</select>
        </div>
      </div>
      <div class="frow-2">
        <div class="frow">
          <label for="d-service">Type de besoin</label>
          <select id="d-service" name="besoin">{service_options(service)}</select>
        </div>
        <div class="frow">
          <label for="d-urgence">Urgence</label>
          <select id="d-urgence" name="urgence"><option>Urgent (aujourd'hui)</option><option>Dans la semaine</option><option>Pas urgent / projet</option></select>
        </div>
      </div>
      <div class="frow">
        <label for="d-msg">Message</label>
        <textarea id="d-msg" name="message" rows="3" placeholder="Décrivez rapidement la situation"></textarea>
      </div>
      <button type="submit" class="btn btn-orange">Envoyer ma demande</button>
      <p class="form-status" role="status"></p>
      <p class="form-note">En urgence, appelez directement le {B.PHONE}. Vos données servent uniquement à vous recontacter. <a href="/politique-confidentialite/" style="text-decoration:underline">Confidentialité</a></p>
    </form>
  </div>
</section>
"""


def quick_form(path, service=None, city=None, title="Rappel rapide"):
    """Formulaire court (Netlify Forms : « rappel »), dans la colonne latérale des pages de service."""
    return f"""<div class="side-card" id="rappel">
  <h2>{title}</h2>
  <p style="color:var(--gray-600)">Laissez votre numéro, un plombier vous rappelle au plus vite.</p>
  <form class="quote" name="rappel" method="POST" data-netlify="true" netlify-honeypot="adresse-web" action="/contact/" style="padding:0">
    <input type="hidden" name="form-name" value="rappel">
    <input type="hidden" name="page" value="{esc(path)}">
    <p class="hp"><label>Ne pas remplir : <input name="adresse-web" tabindex="-1" autocomplete="off"></label></p>
    <div class="frow"><label for="r-nom">Nom *</label><input id="r-nom" name="nom" type="text" required autocomplete="name" placeholder="Votre nom"></div>
    <div class="frow"><label for="r-tel">Téléphone *</label><input id="r-tel" name="telephone" type="tel" required autocomplete="tel" placeholder="06 00 00 00 00"></div>
    <div class="frow"><label for="r-ville">Commune</label><select id="r-ville" name="commune">{city_options(city)}</select></div>
    <div class="frow"><label for="r-besoin">Besoin</label><select id="r-besoin" name="besoin">{service_options(service)}</select></div>
    <button type="submit" class="btn btn-orange">Être rappelé</button>
    <p class="form-status" role="status"></p>
  </form>
</div>
"""


def call_card(price=None, extra=""):
    price_html = '<div class="price-big">%s</div>' % esc(price) if price else ""
    return f"""<div class="side-card dark">
  <h2>Urgence ? Appelez</h2>
  {price_html}
  <p>Un plombier vous répond directement, 24h/24 et 7j/7. Prix annoncé avant le déplacement.</p>
  <a href="tel:{B.PHONE_TEL}" class="btn btn-orange">{phone_icon(18, True)} {B.PHONE}</a>
  {extra}
</div>
"""


def faq_block(faq, title="Questions fréquentes", sub=None, cls="alt", anchor="faq"):
    items = "".join(
        '<details class="faq-item"%s><summary>%s <span class="plus" aria-hidden="true">+</span></summary><div class="faq-a"><p>%s</p></div></details>'
        % (" open" if i == 0 else "", esc(q), a) for i, (q, a) in enumerate(faq))
    sub_html = "<p>%s</p>" % sub if sub else ""
    return f"""<section class="{cls}" id="{anchor}">
  <div class="wrap">
    <div class="sec-head">
      <div class="pill pill-lav sec-badge">FAQ</div>
      <h2>{title}</h2>
      {sub_html}
    </div>
    <div class="faq-list">{items}</div>
  </div>
</section>
"""


def process_section(title="De l'appel à la réparation"):
    steps = [
        ("Appel &amp; diagnostic", "Vous décrivez le problème, nous estimons le type d'intervention et vous annonçons une fourchette de prix, gratuitement."),
        ("Départ", "Un plombier part avec le matériel adapté. Vous connaissez l'heure d'arrivée estimée."),
        ("Devis sur place", "Le prix est confirmé et validé avec vous avant de commencer. Vous restez libre de refuser."),
        ("Intervention &amp; garantie", "Réparation propre, facture détaillée remise, utile pour votre assurance. Travaux garantis."),
    ]
    items = "".join('<div class="proc-item"><div class="n">%d</div><h3>%s</h3><p>%s</p></div>' % (i + 1, t, d) for i, (t, d) in enumerate(steps))
    return f"""<section class="process">
  <div class="wrap">
    <div class="sec-head">
      <div class="pill pill-orange sec-badge">Déroulé</div>
      <h2>{title}</h2>
      <p>Quatre étapes claires, pour un tarif annoncé avant toute intervention.</p>
    </div>
    <div class="proc-list">{items}</div>
  </div>
</section>
"""


def insurers_section(cls=""):
    tiles = "".join('<span class="insurer">%s</span>' % esc(n) for n in B.INSURERS)
    return f"""<section class="{cls}" id="assurances">
  <div class="wrap">
    <div class="sec-head">
      <div class="pill pill-green sec-badge">{svc_icon("shield", 15)}Assurance habitation</div>
      <h2>Nos factures sont acceptées par votre assurance</h2>
      <p>En cas de dégât des eaux ou de recherche de fuite, nos clients se font rembourser auprès de leur assureur habitation, notamment :</p>
    </div>
    <div class="insurers">{tiles}</div>
    <p class="ins-note">Nous remettons une facture détaillée et un descriptif de la cause de la fuite, les justificatifs demandés par les assureurs. Remboursement selon les garanties et franchises de votre contrat. <a href="/{ASSURANCE_PAGE['slug']}/" style="color:var(--purple-700);font-weight:600;text-decoration:underline">Dégât des eaux : comment ça marche ?</a></p>
  </div>
</section>
"""


def reviews_section(cls="", city=None):
    reviews = B.REVIEWS
    cards = "".join(
        '<div class="testi"><div class="stars" aria-label="%d étoiles sur 5">%s</div><p>« %s »</p><div class="who"><span class="av">%s</span>%s — %s</div></div>'
        % (r["stars"], "★" * r["stars"] + "☆" * (5 - r["stars"]), esc(r["text"]),
           "".join(w[0] for w in r["name"].replace(".", "").split()), esc(r["name"]), esc(r["city"]))
        for r in reviews)
    review_btn = ""
    if B.GOOGLE_REVIEW_URL:
        review_btn = '<div class="center" style="margin-top:28px"><a class="btn btn-outline" href="%s" target="_blank" rel="noopener">Laisser un avis sur Google</a></div>' % esc(B.GOOGLE_REVIEW_URL)
    return f"""<section class="{cls}" id="avis">
  <div class="wrap">
    <div class="sec-head">
      <div class="pill pill-lav sec-badge">Avis clients</div>
      <h2>Ce que disent nos clients</h2>
      <p>Note moyenne de {B.RATING} et {B.SATISFACTION} de clients satisfaits sur plus de {B.INTERVENTIONS} interventions depuis {B.SINCE}.</p>
    </div>
    <div class="testi-grid">{cards}</div>
    {review_btn}
  </div>
</section>
"""


def services_grid(city=None):
    cards = []
    for s in SERVICES:
        href = combo_path(s, city) if city else service_path(s)
        title = s["short"] + (" " + city["a"] if city else "")
        checks = "".join('<div class="check-row"><span class="check-circle la">✓</span>%s</div>' % esc(c) for c in s["card_checks"])
        cards.append(f"""<article class="svc-card">
  <div class="svc-top"><div class="icon-sq pu">{svc_icon(s["icon"])}</div><span class="pill {'pill-orange' if 'Urgence' in s['badge'] or s['badge'] == 'Dépannage' else 'pill-lav'}">{esc(s["badge"])}</span></div>
  <h3><a href="{href}">{esc(title)}</a></h3>
  <p class="desc">{esc(s["card_desc"])}</p>
  <div class="svc-checks">{checks}</div>
  <div class="svc-foot"><span class="svc-price">{esc(s["price_label"])}</span><a class="more" href="{href}">En savoir plus →</a></div>
</article>""")
    return '<div class="svc-grid">%s</div>' % "".join(cards)


def stats_block():
    stats = [
        ('<path d="M3 17 9 11 13 15 21 7M21 7h-5M21 7v5" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>', B.YEARS, "Années d'expérience", "Depuis %d" % B.SINCE),
        ('<path d="M12 3.5 14.6 9.1 20.5 9.9 16.2 14 17.3 20 12 17.1 6.7 20 7.8 14 3.5 9.9 9.4 9.1Z" stroke="#fff" stroke-width="1.6" stroke-linejoin="round"/>', B.INTERVENTIONS, "Interventions réalisées", "Note moyenne " + B.RATING),
        ('<circle cx="12" cy="12" r="9" stroke="#fff" stroke-width="1.8"/><path d="M12 7v5l3.5 2" stroke="#fff" stroke-width="1.8"/>', "24/7", "Disponibilité", "Nuits, week-ends, fériés"),
        ('<path d="M12 2 4 5v6c0 5 3.4 8.7 8 11 4.6-2.3 8-6 8-11V5l-8-3Z" stroke="#fff" stroke-width="1.8"/><path d="M8.5 12l2.3 2.3L15.5 9.5" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>', B.SATISFACTION.replace(" ", "\u00a0"), "Clients satisfaits", "Taux de satisfaction"),
    ]
    items = "".join('<div class="stat"><div class="icon-sq"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" aria-hidden="true">%s</svg></div><b>%s</b><div class="lbl">%s</div><div class="sub">%s</div></div>' % s for s in stats)
    return '<div class="stats-card">%s</div>' % items


def zones_section(current=None, service=None, cls=""):
    """Section « Un plombier proche de chez vous » : toutes les communes avec le temps d'arrivée."""
    cities = sorted(CITIES, key=lambda c: (c["delay"], c["name"]))
    items = []
    for c in cities:
        href = combo_path(service, c) if service else city_path(c)
        label = ("%s %s" % (service["short"], c["name"])) if service else c["name"]
        items.append('<a href="%s"%s>%s <span class="d">%s</span></a>' % (
            href, ' class="current" aria-current="page"' if current and c["slug"] == current["slug"] else "", esc(label), delay_label(c)))
    return f"""<section class="zones {cls}" id="zones">
  <div class="wrap zones-inner">
    <div>
      <div class="pill pill-lav">Zone d'intervention</div>
      <h2>Un plombier proche de chez vous</h2>
      <p class="intro">Temps d'arrivée indicatifs depuis notre base de Vidauban, hors trafic. Le délai exact vous est confirmé au moment de l'appel.</p>
      <div class="zone-list">{"".join(items)}</div>
    </div>
    <div class="zone-note">
      <span class="pill pill-orange">Hors zone ?</span>
      <h3>On couvre tout le Var</h3>
      <p>Les délais ci-contre concernent le secteur autour de Vidauban. Pour les communes plus éloignées du Var, nous intervenons aussi : le délai précis est donné au téléphone, avant tout déplacement.</p>
      <a href="tel:{B.PHONE_TEL}" class="btn btn-purple">{phone_icon(18, True)} Vérifier mon secteur</a>
      <a href="/zones-intervention/" class="btn btn-outline">Toutes nos zones d'intervention</a>
    </div>
  </div>
</section>
"""


def zone_cards(cities, link_fn=city_path):
    return '<div class="zone-grid">%s</div>' % "".join(
        '<a class="zone-card" href="%s"><span>%s<small>%s</small></span><span class="d">%s</span></a>'
        % (link_fn(c), esc(c["name"]), c["cp"], delay_label(c)) for c in cities)


def guides_teaser(guides, title="Nos conseils de plombier", cls=""):
    cards = "".join(
        '<article class="post-card"><span class="pill pill-lav" style="align-self:flex-start">Guide pratique</span><h3><a href="%s">%s</a></h3><p>%s</p><a class="more" href="%s">Lire le guide →</a></article>'
        % (guide_path(g), esc(g["h1"]), esc(g["excerpt"]), guide_path(g)) for g in guides)
    return f"""<section class="{cls}">
  <div class="wrap">
    <div class="sec-head">
      <div class="pill pill-lav sec-badge">Conseils</div>
      <h2>{title}</h2>
    </div>
    <div class="cards-3">{cards}</div>
  </div>
</section>
"""


def trust_items():
    return [
        ("Prix annoncé avant de partir", "Diagnostic téléphonique gratuit et fourchette de prix avant tout déplacement, suppléments de nuit ou de week-end compris."),
        ("Devis validé avant les travaux", "Le prix est confirmé sur place et vous le validez avant que nous commencions. Vous restez libre de refuser."),
        ("Pas de travaux inutiles", "Si une réparation suffit, nous ne remplaçons pas. Si l'intervention peut attendre, nous vous le disons."),
        ("Facture détaillée", "Déplacement, main-d'œuvre et pièces détaillés : un document clair, accepté par les assureurs habitation."),
        ("Un artisan local, joignable en direct", "Pas de plateforme ni de centre d'appel : vous parlez directement à un plombier basé à Vidauban."),
        ("Travaux garantis", "Nos interventions sont garanties. En cas de souci, nous revenons."),
        ("Chantier propre", "Protection des sols, nettoyage en fin d'intervention et évacuation des anciennes pièces."),
        ("Ponctualité et transparence", "Un imprévu ? Nous vous prévenons à l'avance, avec un nouvel horaire."),
    ]


def trust_list_html():
    return '<ul class="trust-list">%s</ul>' % "".join(
        '<li><span class="check-circle gr">✓</span><div><b>%s</b><span class="t">%s</span></div></li>' % (t, d) for t, d in trust_items())


# ---------------------------------------------------------------- pages
HOME_FAQ = [
    ("Combien coûte une intervention de plombier ?", "Les tarifs démarrent à 79 € pour une fuite, 89 € pour une réparation de canalisation et 99 € pour un débouchage, en journée. Le prix exact dépend de l'intervention et de l'horaire ; il est toujours annoncé au téléphone et confirmé sur place avant les travaux. <a href=\"/tarifs/\">Voir nos tarifs</a>."),
    ("Intervenez-vous la nuit, le week-end et les jours fériés ?", "Oui, un plombier est joignable 24h/24 et 7j/7 au 06 75 93 19 04. Un supplément horaire peut s'appliquer la nuit, le week-end et les jours fériés : il vous est communiqué avant le déplacement."),
    ("Dans quelles communes intervenez-vous ?", "Nous sommes basés à Vidauban et intervenons dans tout le centre Var : Le Muy, Les Arcs-sur-Argens, Le Cannet-des-Maures, Le Luc, La Garde-Freinet, Gonfaron, Draguignan, Lorgues, Taradeau, Le Thoronet et au-delà. <a href=\"/zones-intervention/\">Voir toutes les communes</a>."),
    ("Le devis est-il gratuit ?", "Oui, le diagnostic téléphonique et le devis sur place sont gratuits et sans engagement."),
    ("Vos factures sont-elles acceptées par les assurances ?", "Oui. Nous remettons une facture détaillée et un descriptif de la cause de la fuite. Nos clients se font rembourser auprès de leur assureur habitation (Crédit Mutuel, Crédit Agricole, MAAF, MMA, GMF, Allianz, LCL, Société Générale, etc.), selon les garanties de leur contrat."),
    ("Faites-vous de la recherche de fuite ?", "Oui, nous réalisons la détection de fuite (visuelle, thermique ou acoustique selon le cas) puis la réparation, en limitant la casse au strict nécessaire."),
    ("En combien de temps arrivez-vous ?", "Depuis Vidauban, comptez environ 15 minutes pour Le Muy, Les Arcs ou Le Cannet-des-Maures, 20 minutes pour Le Luc ou La Garde-Freinet, 25 minutes pour Gonfaron ou Draguignan, hors trafic. Le délai précis est donné à l'appel."),
    ("Comment être sûr de ne pas tomber sur un plombier arnaqueur ?", "Exigez un prix avant le déplacement et un devis avant les travaux, méfiez-vous des faux documents « officiels » dans les boîtes aux lettres et préférez un artisan réellement local. <a href=\"/conseils/choisir-plombier-eviter-arnaques/\">Lire notre guide</a>."),
]


def build_home():
    path = "/"
    title = "Plombier Vidauban & Var 24h/24 — PRO SERVICE 83, dépannage 7j/7"
    desc = "Plombier à Vidauban et dans le Var, 24h/24 et 7j/7 : fuite d'eau, débouchage, chauffe-eau, canalisation, salle de bain. Prix annoncé avant intervention. ☎ 06 75 93 19 04"
    website = {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#site", "name": B.NAME, "url": SITE + "/", "inLanguage": "fr-FR", "publisher": {"@id": SITE + "/#entreprise"}}
    out = head(title, desc, path, [business_schema(), website, faq_schema(HOME_FAQ)])
    out += header(path)
    out += f"""<section class="hero">
  <div class="wrap hero-inner">
    <div class="pill avail-badge"><span class="dot dot-pulse"></span><span>Disponible maintenant · Intervention rapide</span></div>
    <h1>Votre plombier à Vidauban<br><span class="accent">et dans tout le Var, 24h/24</span></h1>
    <p class="lead">Fuite d'eau, débouchage, chauffe-eau, canalisation, salle de bain : <b>un artisan local vous répond en direct, jour et nuit, 7j/7.</b> Prix annoncé avant de partir.</p>
    <a href="tel:{B.PHONE_TEL}" class="hero-cta">
      <span class="num">{phone_icon(24, True)} {B.PHONE}</span>
      <span class="sub">Appel direct, disponible 24/7</span>
    </a>
    <a href="#devis" class="hero-devis">Ou demandez un devis gratuit</a>
    <div class="hero-checks">
      <div class="check-row"><span class="check-circle gr">✓</span>Diagnostic gratuit</div>
      <div class="check-row"><span class="check-circle gr">✓</span>Prix annoncé à l'avance</div>
      <div class="check-row"><span class="check-circle gr">✓</span>Travaux garantis</div>
      <div class="check-row"><span class="check-circle gr">✓</span>Factures acceptées par les assurances</div>
    </div>
  </div>
</section>
"""
    out += strip_band()
    out += f"""<section id="services">
  <div class="wrap">
    <div class="sec-head">
      <div class="pill pill-purple sec-badge">{svc_icon("shield", 15)}Services professionnels</div>
      <h2>Nos services de plomberie dans le Var</h2>
      <p>Un artisan plombier à votre service pour l'urgence comme pour les travaux, 24h/24 et 7j/7, de Vidauban à Draguignan.</p>
    </div>
    {services_grid()}
  </div>
</section>
<div class="alt" style="padding:0 0 10px"><div class="wrap">{stats_block()}</div></div>
<section class="alt">
  <div class="wrap text-block prose">
    <h2>Un plombier de confiance, installé à Vidauban depuis {B.SINCE}</h2>
    <p><strong>PRO SERVICE 83</strong> est une entreprise artisanale de plomberie basée à <strong>Vidauban</strong>, au cœur du Var. Depuis {B.SINCE}, nous dépannons et équipons les particuliers, propriétaires, locataires, gestionnaires de résidences secondaires et petites entreprises du centre Var : Le Muy, Les Arcs-sur-Argens, Le Cannet-des-Maures, Le Luc, La Garde-Freinet, Gonfaron, Draguignan et les communes voisines.</p>
    <p>Notre métier, c'est de régler vos problèmes de plomberie <strong>rapidement, proprement et au juste prix</strong>. Une fuite sous l'évier un dimanche, un WC bouché un soir de fête, un chauffe-eau qui lâche en plein hiver : vous joignez directement un plombier au <a href="tel:{B.PHONE_TEL}">{B.PHONE}</a>, sans plateforme ni centre d'appel. Il vous écoute, vous aide à sécuriser la situation et vous annonce une fourchette de prix <strong>avant</strong> de prendre la route.</p>
    <p>Nous intervenons sur l'ensemble de la plomberie de la maison : <a href="/recherche-de-fuite-var/">recherche et réparation de fuite</a>, <a href="/debouchage-canalisation-var/">débouchage de WC et de canalisations</a>, <a href="/chauffe-eau-var/">dépannage et remplacement de chauffe-eau</a>, <a href="/reparation-canalisation-var/">réparation de canalisations</a>, <a href="/installation-sanitaire-var/">installation sanitaire et robinetterie</a> et <a href="/renovation-salle-de-bain-var/">rénovation de salle de bain</a>. Pour les sinistres, nous fournissons les <a href="/{ASSURANCE_PAGE['slug']}/">justificatifs demandés par votre assurance</a>.</p>
    <p>Ce qui nous distingue ? Des engagements simples et tenus : un prix annoncé à l'avance, un devis validé avant les travaux, aucune intervention inutile et une facture détaillée. C'est ce qui nous vaut une note moyenne de {B.RATING} et la confiance de nombreux clients qui nous rappellent, et nous recommandent à leurs voisins.</p>
  </div>
</section>
<section id="pourquoi">
  <div class="wrap">
    <div class="sec-head">
      <div class="pill pill-lav sec-badge">{svc_icon("shield", 15)}Entreprise de confiance</div>
      <h2>Notre charte de confiance</h2>
      <p>Le dépannage d'urgence a mauvaise réputation. Nous avons choisi de faire l'inverse, et de l'écrire noir sur blanc.</p>
    </div>
    {trust_list_html()}
    <div class="center" style="margin-top:34px"><a class="btn btn-outline" href="/a-propos/">En savoir plus sur nous</a></div>
  </div>
</section>
"""
    out += process_section()
    out += insurers_section("alt")
    out += zones_section()
    out += reviews_section("alt")
    out += guides_teaser(GUIDES[:3])
    out += faq_block(HOME_FAQ, "Avant d'appeler : vos questions", cls="alt")
    out += contact_section(path)
    out += footer()
    write_page(path, out, "1.0")


def build_service(s, idx):
    path = service_path(s)
    crumbs = [("Accueil", "/"), ("Prestations", "/prestations/"), (s["name"], path)]
    schemas = [business_schema(), breadcrumb_schema(crumbs),
               service_schema(s["name"], strip_tags(s["lead"]), path, "Var (83)", s["price_min"]),
               faq_schema(s["faq"])]
    out = head(s["title"], s["meta"], path, schemas)
    out += header(path)
    out += page_hero(crumbs, s["h1"], s["lead"], s["checks"], badge="Disponible 24h/24 · 7j/7")
    sections = "".join("<h2>%s</h2>%s" % (h, body) for h, body in s["sections"])
    others = "".join('<li><a href="%s"><span>%s</span><span>→</span></a></li>' % (service_path(o), esc(o["short"])) for o in SERVICES if o is not s)
    city_chips = "".join('<a class="chip" href="%s">%s %s <span class="d">%s</span></a>' % (combo_path(s, c), esc(s["short"]), esc(c["name"]), delay_label(c)) for c in CORE_CITIES)
    other_chips = "".join('<a class="chip" href="%s">%s %s <span class="d">%s</span></a>' % (combo_path(s, c), esc(s["short"]), esc(c["name"]), delay_label(c)) for c in CITIES if not c["core"])
    related_guides = [g for g in GUIDES if s["slug"] in g["services"]]
    guides_html = ""
    if related_guides:
        guides_html = "<h2>Nos guides sur le sujet</h2><ul>%s</ul>" % "".join('<li><a href="%s">%s</a></li>' % (guide_path(g), esc(g["h1"])) for g in related_guides)
    out += f"""<section>
  <div class="wrap layout">
    <article class="prose">
      {sections}
      <h2>{esc(s["short"])} : où intervenons-nous ?</h2>
      <p>Nous intervenons depuis Vidauban dans tout le centre Var. Retrouvez le détail de notre intervention dans votre commune :</p>
      <div class="chips" style="margin-bottom:14px">{city_chips}</div>
      <p>Nous intervenons aussi dans les communes voisines : </p>
      <div class="chips">{other_chips}</div>
      {guides_html}
    </article>
    <aside class="side">
      {quick_form(path, service=s["short"], title="Rappel rapide : " + s["short"].lower())}
      {call_card(s["price_label"])}
      <div class="side-card"><h2>Nos autres prestations</h2><ul class="side-links">{others}</ul></div>
    </aside>
  </div>
</section>
"""
    out += zones_section(service=s, cls="alt")
    out += process_section()
    out += faq_block(s["faq"], "Questions fréquentes : " + s["short"].lower(), cls="")
    out += contact_section(path, "Un besoin en %s ?" % s["short"].lower(), service=s["short"])
    out += footer()
    write_page(path, out, "0.9")


def build_combo(s, c, si, ci):
    path = combo_path(s, c)
    v = (si + ci) % 3
    title = s["combo_title"].format(city=c["name"], cp=c["cp"])
    desc = s["combo_meta"].format(a=c["a"], delay_txt=delay_txt(c))
    h1 = "%s %s" % (s["combo_h1"], c["a"])
    lead = s["combo_intros"][v].format(a=c["a"], de=c["de"], city=c["name"])
    crumbs = [("Accueil", "/"), (s["name"], service_path(s)), ("%s %s" % (s["short"], c["name"]), path)]
    near = [CITY_BY_SLUG[n] for n in c["near"] if n in CITY_BY_SLUG]
    near_names = ", ".join(n["name"] for n in near[:5])
    # FAQ : délai local + deux questions du service (rotation) + communes voisines
    sf = s["faq"]
    faq = [
        ("En combien de temps intervenez-vous %s ?" % c["a"], delay_sentence(c) + " Pour une urgence, appelez le 06 75 93 19 04."),
        sf[v % len(sf)],
        sf[(v + 1) % len(sf)],
        ("Intervenez-vous aussi autour %s ?" % c["de"], "Oui, nous intervenons également à %s et dans tout le centre Var. <a href=\"/zones-intervention/\">Voir toutes nos zones</a>." % near_names),
    ]
    schemas = [business_schema(), breadcrumb_schema(crumbs),
               service_schema("%s %s" % (s["combo_h1"], c["a"]), strip_tags(lead), path, c["name"], s["price_min"]),
               faq_schema(faq)]
    out = head(title, desc, path, schemas)
    out += header(path)
    out += page_hero(crumbs, h1, lead, s["checks"], badge="%s · %s" % (delay_txt(c), "24h/24, 7j/7"))
    n = len(s["combo_points"])
    points = [s["combo_points"][(v * 2 + k) % n] for k in range(n)]
    points_html = "".join("<li>%s</li>" % esc(p) for p in points)
    other_services = "".join('<li><a href="%s"><span>%s %s</span><span>→</span></a></li>' % (combo_path(o, c), esc(o["short"]), esc(c["name"])) for o in SERVICES if o is not s)
    near_chips = "".join('<a class="chip" href="%s">%s %s</a>' % (combo_path(s, n), esc(s["short"]), esc(n["name"])) for n in near)
    first_section = s["sections"][0]
    out += f"""<section>
  <div class="wrap layout">
    <article class="prose">
      <h2>{esc(s["short"])} {c["a"]} : nos interventions</h2>
      <ul>{points_html}</ul>
      <h2>Un plombier proche de chez vous {c["a"]}</h2>
      <p>{esc(c["context"])}</p>
      <p>{delay_sentence(c)}</p>
      <div class="callout info"><strong>Notre conseil :</strong> {esc(s["combo_tip"])}</div>
      <h2>Prix et engagements</h2>
      <p>{"" if s["price_label"].lower().startswith("tarif") else "Tarif : "}<strong>{esc(s["price_label"])}</strong>. Le diagnostic téléphonique est gratuit, le prix est annoncé avant le déplacement et confirmé sur place avant les travaux. En fin d'intervention, vous recevez une facture détaillée, acceptée par les assureurs habitation pour vos démarches de remboursement. Les éventuels suppléments de nuit, de week-end ou de jour férié sont toujours annoncés à l'avance.</p>
      <h2>{first_section[0]}</h2>
      {first_section[1]}
      <p>Pour tout savoir sur cette prestation, consultez notre page <a href="{service_path(s)}">{esc(s["name"].lower())} dans le Var</a>, ou découvrez <a href="{city_path(c)}">toutes nos interventions de plombier {c["a"]}</a>.</p>
      <h2>Nous intervenons aussi autour {c["de"]}</h2>
      <div class="chips">{near_chips}</div>
    </article>
    <aside class="side">
      {quick_form(path, service=s["short"], city=c["name"], title="Rappel rapide " + c["a"])}
      {call_card(s["price_label"])}
      <div class="side-card"><h2>Autres services {c["a"]}</h2><ul class="side-links">{other_services}</ul></div>
    </aside>
  </div>
</section>
"""
    out += zones_section(current=c, service=s, cls="alt")
    out += faq_block(faq, "%s %s : vos questions" % (s["short"], c["a"]), cls="")
    out += contact_section(path, "%s %s : contactez-nous" % (s["short"], c["a"]), service=s["short"], city=c["name"])
    out += footer()
    write_page(path, out, "0.7" if c["core"] else "0.6")


def build_city(c):
    path = city_path(c)
    crumbs = [("Accueil", "/"), ("Zones d'intervention", "/zones-intervention/"), ("Plombier " + c["name"], path)]
    title = "Plombier %s (%s) — dépannage 24h/24, 7j/7 | %s" % (c["name"], c["cp"], B.NAME)
    desc = "Plombier %s (%s) : fuite d'eau, débouchage, chauffe-eau, canalisation, salle de bain. %s. Prix annoncé avant intervention. ☎ %s" % (c["a"], c["cp"], delay_txt(c), B.PHONE)
    near = [CITY_BY_SLUG[n] for n in c["near"] if n in CITY_BY_SLUG]
    faq = [
        ("Quel est le délai d'intervention d'un plombier %s ?" % c["a"], delay_sentence(c)),
        ("Intervenez-vous %s la nuit et le week-end ?" % c["a"], "Oui, nous intervenons 24h/24 et 7j/7, jours fériés compris. Un supplément peut s'appliquer la nuit, le week-end et les jours fériés : il vous est annoncé avant le déplacement."),
        ("Combien coûte un plombier %s ?" % c["a"], "Nos interventions démarrent à 79 € pour une fuite, 89 € pour une canalisation et 99 € pour un débouchage en journée. Le prix est annoncé au téléphone avant le départ et confirmé sur place. <a href=\"/tarifs/\">Voir nos tarifs</a>."),
        ("Vos factures sont-elles prises en charge par mon assurance ?", "Nous remettons une facture détaillée et un descriptif de la cause de la fuite, que nos clients transmettent à leur assureur habitation pour se faire rembourser, selon les garanties de leur contrat."),
        ("Quelles communes desservez-vous autour %s ?" % c["de"], "Nous intervenons notamment à %s, et dans tout le centre Var." % ", ".join(n["name"] for n in near)),
    ]
    schemas = [business_schema(), breadcrumb_schema(crumbs), faq_schema(faq)]
    out = head(title, desc, path, schemas)
    out += header(path)
    lead = "Fuite d'eau, débouchage, chauffe-eau, canalisation, installation sanitaire : un artisan plombier intervient <b>%s 24h/24 et 7j/7</b>, avec un prix annoncé avant de partir." % c["a"]
    out += page_hero(crumbs, "Plombier %s (%s)" % (c["a"], c["cp"]), lead, ["Diagnostic gratuit", "Prix annoncé à l'avance", "Factures acceptées par les assurances"], badge="%s · disponible 24h/24" % delay_txt(c))
    near_html = "".join('<a class="chip" href="%s">Plombier %s <span class="d">%s</span></a>' % (city_path(n), esc(n["name"]), delay_label(n)) for n in near)
    local_reviews = [r for r in B.REVIEWS if r["city"] == c["name"]]
    review_html = ""
    if local_reviews:
        r = local_reviews[0]
        review_html = '<div class="callout info"><strong>Avis client %s :</strong> « %s » — %s</div>' % (c["a"], esc(r["text"]), esc(r["name"]))
    out += f"""<section>
  <div class="wrap layout">
    <article class="prose">
      <h2>Votre plombier {c["a"]}</h2>
      <p>{esc(c["intro"])}</p>
      <p>{esc(c["context"])}</p>
      {review_html}
      <h2>Nos prestations de plomberie {c["a"]}</h2>
      <ul>
        <li><strong>Urgence plomberie 24h/24</strong> : fuite importante, dégât des eaux, WC bouché, panne de chauffe-eau.</li>
        <li><strong>Recherche et réparation de fuite</strong>, sans casse inutile, avec les justificatifs pour l'assurance.</li>
        <li><strong>Débouchage</strong> de WC, évier, douche, baignoire et canalisations.</li>
        <li><strong>Chauffe-eau</strong> : dépannage, remplacement, installation électrique ou thermodynamique.</li>
        <li><strong>Canalisations</strong> : réparation, remplacement de tuyaux anciens, odeurs d'égout.</li>
        <li><strong>Installation sanitaire</strong> : WC, lavabo, douche, mitigeur, robinetterie.</li>
        <li><strong>Rénovation de salle de bain</strong> : douche à l'italienne, remplacement de baignoire, aménagement PMR.</li>
      </ul>
      <h2>Pourquoi faire appel à nous {c["a"]} ?</h2>
      <p>Vous parlez directement à un artisan plombier installé à Vidauban, pas à une plateforme. Le diagnostic téléphonique est gratuit, le prix est annoncé avant le déplacement puis validé avec vous avant les travaux. Nous ne proposons que les interventions utiles et vous remettons une facture détaillée. Depuis {B.SINCE}, plus de {B.INTERVENTIONS} interventions et une note moyenne de {B.RATING}.</p>
      <h2>Communes voisines {c["de"]}</h2>
      <p>Nous intervenons aussi dans les communes proches :</p>
      <div class="chips">{near_html}</div>
    </article>
    <aside class="side">
      {quick_form(path, city=c["name"], title="Rappel rapide " + c["a"])}
      {call_card(None)}
    </aside>
  </div>
</section>
<section class="alt">
  <div class="wrap">
    <div class="sec-head">
      <div class="pill pill-purple sec-badge">Prestations</div>
      <h2>Nos services de plombier {c["a"]}</h2>
    </div>
    {services_grid(c)}
  </div>
</section>
"""
    out += zones_section(current=c)
    out += process_section()
    out += faq_block(faq, "Plombier %s : vos questions" % c["a"])
    out += contact_section(path, "Un plombier %s ? Contactez-nous" % c["a"], city=c["name"])
    out += footer()
    write_page(path, out, "0.8" if c["core"] else "0.7")


def build_prestations():
    path = "/prestations/"
    crumbs = [("Accueil", "/"), ("Prestations", path)]
    out = head("Prestations de plomberie dans le Var — PRO SERVICE 83",
               "Toutes nos prestations de plomberie dans le Var : urgence 24h/24, recherche de fuite, débouchage, chauffe-eau, canalisation, installation sanitaire, salle de bain.",
               path, [business_schema(), breadcrumb_schema(crumbs)])
    out += header(path)
    out += page_hero(crumbs, "Nos prestations de plomberie dans le Var", "De l'urgence de nuit au projet de salle de bain, <b>un seul artisan</b> pour toute la plomberie de votre logement, de Vidauban à Draguignan.", ["Devis gratuit", "Prix annoncé à l'avance", "Travaux garantis"])
    out += f"""<section><div class="wrap">{services_grid()}</div></section>
<section class="alt"><div class="wrap text-block prose">
  <h2>Dégât des eaux : nous gérons aussi le volet assurance</h2>
  <p>En cas de sinistre, nous recherchons l'origine de la fuite, la réparons et vous remettons les justificatifs attendus par votre assureur habitation. <a href="/{ASSURANCE_PAGE['slug']}/">Découvrir notre accompagnement dégât des eaux</a>.</p>
</div></section>
"""
    out += zones_section()
    out += process_section()
    out += contact_section(path)
    out += footer()
    write_page(path, out, "0.8")


def build_assurance():
    path = "/%s/" % ASSURANCE_PAGE["slug"]
    crumbs = [("Accueil", "/"), ("Prestations", "/prestations/"), (ASSURANCE_PAGE["name"], path)]
    faq = [
        ("Votre facture est-elle remboursée par mon assurance ?", "Nos factures sont acceptées par les assureurs habitation. Le remboursement dépend des garanties, plafonds et franchises de votre contrat : la recherche de fuite et les dommages causés par l'eau sont généralement couverts en cas de dégât des eaux."),
        ("Quels documents me remettez-vous ?", "Une facture détaillée (déplacement, recherche de fuite, réparation, pièces) et un descriptif de la cause et de la localisation de la fuite. Si la fuite est sur une canalisation après compteur, une attestation de réparation pour le plafonnement de la facture d'eau (loi Warsmann)."),
        ("Dans quel délai dois-je déclarer un dégât des eaux ?", "Sauf délai plus long prévu par votre contrat, vous disposez de 5 jours ouvrés à partir de la découverte du sinistre pour le déclarer à votre assureur."),
        ("Dois-je attendre l'expert pour faire réparer la fuite ?", "Non : vous devez faire cesser la fuite pour limiter les dégâts. Prenez des photos avant et conservez les pièces remplacées si possible. Pour les travaux d'embellissement, attendez en revanche l'accord de votre assureur."),
        ("Qui paie la recherche de fuite en appartement ?", "Avec la convention IRSI, pour les sinistres de moins de 5 000 € HT, c'est en principe l'assureur de l'occupant du local où les dégâts sont constatés qui organise et prend en charge la recherche de fuite, selon les contrats."),
    ]
    schemas = [business_schema(), breadcrumb_schema(crumbs),
               service_schema("Recherche de fuite et réparation après dégât des eaux", "Recherche de fuite, réparation et justificatifs pour l'assurance habitation dans le Var.", path, "Var (83)", 79),
               faq_schema(faq)]
    out = head("Plombier dégât des eaux & assurance dans le Var — factures acceptées",
               "Dégât des eaux dans le Var : recherche de fuite, réparation et justificatifs pour votre assurance (Crédit Mutuel, Crédit Agricole, MAAF, MMA, GMF, Allianz…). ☎ 06 75 93 19 04",
               path, schemas)
    out += header(path)
    out += page_hero(crumbs, "Plombier dégât des eaux : on s'occupe aussi des justificatifs pour l'assurance",
                     "Recherche de fuite, réparation, <b>facture détaillée et descriptif de la cause</b> : tout ce qu'il faut pour être remboursé par votre assurance habitation.",
                     ["Recherche de fuite sans casse inutile", "Facture détaillée", "Factures acceptées par les assurances"], badge="Disponible 24h/24 · 7j/7")
    out += f"""<section>
  <div class="wrap layout">
    <article class="prose">
      <h2>Ce que nous faisons pour vous en cas de dégât des eaux</h2>
      <ol>
        <li><strong>Mise en sécurité</strong> : coupure de l'eau, arrêt de la fuite, conseils pour limiter les dégâts.</li>
        <li><strong>Recherche de fuite</strong> : localisation précise de l'origine (visuelle, thermique ou acoustique), en limitant la casse.</li>
        <li><strong>Réparation</strong> durable de la fuite.</li>
        <li><strong>Justificatifs</strong> : facture détaillée, descriptif de la cause et de la localisation, attestation de réparation si nécessaire.</li>
      </ol>
      <p>Ces documents permettent à votre assureur d'instruire votre dossier rapidement. Nos clients les transmettent à leur assureur habitation pour se faire rembourser, selon les garanties de leur contrat.</p>
      <h2>Assureurs auprès desquels nos clients se font rembourser</h2>
      <p>Nos factures sont notamment acceptées par :</p>
      <div class="insurers" style="justify-content:flex-start;margin-bottom:18px">{"".join('<span class="insurer">%s</span>' % esc(n) for n in B.INSURERS)}</div>
      <p>Votre assureur n'est pas dans la liste ? Cela ne change rien : une facture détaillée d'un professionnel est le justificatif standard demandé par toutes les compagnies.</p>
      <h2>Les étapes côté assurance</h2>
      <ul>
        <li>Déclarez le sinistre dans les <strong>5 jours ouvrés</strong>.</li>
        <li>Remplissez un <strong>constat amiable dégât des eaux</strong> si un voisin, le propriétaire ou la copropriété sont concernés.</li>
        <li>Transmettez photos, facture du plombier et devis de remise en état.</li>
      </ul>
      <p>Tout est détaillé dans notre guide : <a href="/conseils/degat-des-eaux-assurance/">dégât des eaux, les démarches pour être bien remboursé</a>.</p>
      <h2>Et votre facture d'eau ?</h2>
      <p>Si la fuite était sur une canalisation après le compteur, votre facture d'eau peut être plafonnée grâce à la loi Warsmann, sur présentation d'une attestation de réparation d'un plombier. <a href="/conseils/fuite-apres-compteur-loi-warsmann/">En savoir plus</a>.</p>
    </article>
    <aside class="side">
      {quick_form(path, service="Dégât des eaux / assurance", title="Rappel rapide : dégât des eaux")}
      {call_card("Recherche de fuite dès 79 €")}
    </aside>
  </div>
</section>
"""
    out += zones_section(cls="alt")
    out += faq_block(faq, "Dégât des eaux et assurance : vos questions", cls="")
    out += contact_section(path, "Un dégât des eaux ? Contactez-nous", service="Dégât des eaux / assurance")
    out += footer()
    write_page(path, out, "0.9")


def build_zones():
    path = "/zones-intervention/"
    crumbs = [("Accueil", "/"), ("Zones d'intervention", path)]
    out = head("Zones d'intervention — plombier Vidauban, Draguignan, Le Muy, Le Luc… (Var)",
               "Plombier basé à Vidauban, intervention 24h/24 dans le centre Var : Le Muy, Les Arcs, Le Cannet-des-Maures, Le Luc, La Garde-Freinet, Gonfaron, Draguignan et plus.",
               path, [business_schema(), breadcrumb_schema(crumbs)])
    out += header(path)
    out += page_hero(crumbs, "Nos zones d'intervention dans le Var", "Basés à <b>Vidauban</b>, nous intervenons 24h/24 dans tout le centre Var. Délais indicatifs depuis notre base, hors trafic.", ["Artisan local", "Délai annoncé à l'appel", "7j/7"])
    rows = ""
    for c in CITIES:
        links = " · ".join('<a href="%s">%s</a>' % (combo_path(s, c), esc(s["short"])) for s in SERVICES)
        rows += '<tr><td><a href="%s"><strong>Plombier %s</strong></a></td><td>%s</td><td>%s</td><td>%s</td></tr>' % (city_path(c), esc(c["name"]), c["cp"], delay_label(c), links)
    out += f"""<section>
  <div class="wrap">
    <div class="sec-head"><h2>Communes principales</h2><p>Nous y intervenons tous les jours de l'année, pour l'urgence comme pour les travaux.</p></div>
    {zone_cards(CORE_CITIES)}
    <div class="sec-head" style="margin-top:56px"><h2>Autres communes desservies</h2></div>
    {zone_cards([c for c in CITIES if not c["core"]])}
  </div>
</section>
<section class="alt">
  <div class="wrap">
    <div class="sec-head"><h2>Toutes nos prestations, commune par commune</h2></div>
    <div class="table-scroll"><table class="prices"><thead><tr><th>Commune</th><th>Code postal</th><th>Délai</th><th>Prestations</th></tr></thead><tbody>{rows}</tbody></table></div>
    <p class="ins-note">Votre commune n'apparaît pas ? Nous couvrons tout le Var : appelez le {B.PHONE}, nous vous indiquons le délai.</p>
  </div>
</section>
"""
    out += contact_section(path)
    out += footer()
    write_page(path, out, "0.8")


def build_tarifs():
    path = "/tarifs/"
    crumbs = [("Accueil", "/"), ("Tarifs", path)]
    faq = [
        ("Le déplacement est-il payant ?", "Les éventuels frais de déplacement vous sont annoncés au téléphone, avant notre départ. Rien ne s'ajoute sur la facture sans votre accord."),
        ("Y a-t-il un supplément la nuit et le week-end ?", "Oui, un supplément horaire peut s'appliquer la nuit, le week-end et les jours fériés. Il vous est toujours communiqué avant le déplacement."),
        ("Le devis est-il gratuit ?", "Oui, le diagnostic téléphonique et le devis sur place sont gratuits et sans engagement."),
        ("Puis-je refuser le devis sur place ?", "Oui. Le prix est confirmé avant de commencer et vous restez libre de refuser."),
    ]
    out = head("Tarifs plombier dans le Var — prix fuite, débouchage, chauffe-eau",
               "Tarifs de plombier dans le Var : fuite dès 79 €, canalisation dès 89 €, débouchage dès 99 €. Devis gratuit, prix annoncé avant intervention, sans frais cachés.",
               path, [business_schema(), breadcrumb_schema(crumbs), faq_schema(faq)])
    out += header(path)
    out += page_hero(crumbs, "Nos tarifs de plombier dans le Var", "Des <b>prix clairs, annoncés avant le déplacement</b> et confirmés sur place avant les travaux. Pas de mauvaise surprise sur la facture.", ["Devis gratuit", "Sans frais cachés", "Facture détaillée"])
    rows = "".join('<tr><td><a href="%s"><strong>%s</strong></a></td><td>%s</td></tr>' % (service_path(s), esc(s["name"]), esc(s["price_label"])) for s in SERVICES)
    out += f"""<section>
  <div class="wrap layout">
    <article class="prose">
      <h2>Grille de prix indicative</h2>
      <div class="table-scroll"><table><thead><tr><th>Prestation</th><th>Prix</th></tr></thead><tbody>{rows}
        <tr><td><strong>Diagnostic téléphonique</strong></td><td>gratuit</td></tr>
        <tr><td><strong>Devis sur place</strong></td><td>gratuit, sans engagement</td></tr></tbody></table></div>
      <p>Prix en journée. Les interventions de nuit, de week-end et de jour férié peuvent faire l'objet d'un supplément, toujours annoncé avant le déplacement.</p>
      <h2>Ce qui fait varier le prix</h2>
      <ul>
        <li><strong>La nature de la panne</strong> : un joint ne se chiffre pas comme une canalisation encastrée.</li>
        <li><strong>L'accessibilité</strong> : canalisation derrière un coffrage, chauffe-eau en combles, regard enterré.</li>
        <li><strong>Les pièces</strong> : nous vous présentons les options (gamme, marque) avant de commander.</li>
        <li><strong>L'horaire</strong> : nuit, week-end et jours fériés.</li>
      </ul>
      <h2>Notre engagement prix</h2>
      <ol>
        <li>Au téléphone, vous décrivez le problème : nous annonçons une fourchette de prix.</li>
        <li>Sur place, nous confirmons le prix avant de commencer. Vous validez, ou vous refusez.</li>
        <li>En fin d'intervention, la facture correspond au prix validé, détaillée poste par poste.</li>
      </ol>
      <div class="callout info">Conformément à la réglementation sur le dépannage à domicile, un devis écrit détaillé vous est remis avant les travaux dont le montant estimé dépasse 150 € TTC.</div>
    </article>
    <aside class="side">
      {quick_form(path, title="Demander un prix")}
      {call_card(None)}
    </aside>
  </div>
</section>
"""
    out += insurers_section("alt")
    out += zones_section()
    out += faq_block(faq, "Questions sur nos tarifs")
    out += contact_section(path, "Obtenez votre devis gratuit")
    out += footer()
    write_page(path, out, "0.8")


def build_about():
    path = "/a-propos/"
    crumbs = [("Accueil", "/"), ("À propos", path)]
    out = head("À propos de PRO SERVICE 83 — artisan plombier à Vidauban depuis %d" % B.SINCE,
               "PRO SERVICE 83, artisan plombier indépendant installé à Vidauban (Var) depuis %d : notre histoire, nos engagements et notre charte de confiance." % B.SINCE,
               path, [business_schema(), breadcrumb_schema(crumbs)])
    out += header(path)
    out += page_hero(crumbs, "Un artisan plombier local, des engagements tenus", "PRO SERVICE 83 est une entreprise artisanale de plomberie installée à <b>Vidauban depuis %d</b>. Voici qui nous sommes et comment nous travaillons." % B.SINCE, ["%s ans d'expérience" % B.YEARS.replace("+", " +"), "%s interventions" % B.INTERVENTIONS, "Note moyenne %s" % B.RATING])
    out += f"""<section>
  <div class="wrap text-block prose">
    <h2>Notre histoire</h2>
    <p>PRO SERVICE 83 est né d'une idée simple : proposer aux habitants du centre Var un plombier <strong>joignable, honnête et efficace</strong>. Installés à Vidauban depuis {B.SINCE}, nous avons réalisé plus de {B.INTERVENTIONS} interventions, du simple joint qui fuit à la rénovation complète de salle de bain.</p>
    <p>Nous connaissons les installations du secteur : maisons de village aux canalisations anciennes, villas avec réseaux enterrés jusqu'au portail, résidences secondaires du massif des Maures, appartements de Draguignan aux colonnes communes. Et nous connaissons l'eau du Var, souvent calcaire, qui use les chauffe-eau et la robinetterie.</p>
    <h2>Pourquoi un artisan local change tout</h2>
    <p>Quand vous cherchez « plombier urgence » sur internet, beaucoup de numéros mènent à des plateformes nationales qui revendent votre appel à un intervenant parfois éloigné, avec des prix difficiles à prévoir. Avec nous, vous appelez directement le plombier qui va intervenir. Il connaît le secteur, il est proche, et il a tout intérêt à bien faire : sa réputation se joue ici, auprès de vos voisins.</p>
    <h2>Notre charte de confiance</h2>
  </div>
  <div class="wrap" style="margin-top:20px">{trust_list_html()}</div>
</section>
"""
    out += f'<div class="alt" style="padding:56px 0"><div class="wrap">{stats_block()}</div></div>'
    out += insurers_section()
    out += zones_section(cls="alt")
    out += reviews_section()
    out += contact_section(path)
    out += footer()
    write_page(path, out, "0.6")


def build_faq_page():
    path = "/faq/"
    crumbs = [("Accueil", "/"), ("FAQ", path)]
    groups = [("Général", HOME_FAQ)] + [(s["short"], s["faq"]) for s in SERVICES]
    all_faq = [qa for _, g in groups for qa in g]
    out = head("FAQ plombier Var — prix, délais, urgence, assurance | PRO SERVICE 83",
               "Toutes les réponses à vos questions de plomberie : prix, délais d'intervention, urgence de nuit, recherche de fuite, débouchage, chauffe-eau, assurance.",
               path, [business_schema(), breadcrumb_schema(crumbs), faq_schema(all_faq)])
    out += header(path)
    out += page_hero(crumbs, "Questions fréquentes", "Prix, délais, urgences, assurance : les réponses aux questions qu'on nous pose le plus souvent.")
    for i, (name, faq) in enumerate(groups):
        out += faq_block(faq, name, cls="alt" if i % 2 else "", anchor="faq-%d" % i)
    out += contact_section(path, "Votre question n'y est pas ? Écrivez-nous")
    out += footer()
    write_page(path, out, "0.6")


def build_contact():
    path = "/contact/"
    crumbs = [("Accueil", "/"), ("Contact", path)]
    out = head("Contact & devis gratuit — plombier PRO SERVICE 83, Vidauban (Var)",
               "Contactez PRO SERVICE 83 : 06 75 93 19 04, 24h/24 et 7j/7, ou demandez un devis gratuit en ligne. Plombier basé à Vidauban, intervention dans tout le Var.",
               path, [business_schema(), breadcrumb_schema(crumbs)])
    out += header(path)
    out += page_hero(crumbs, "Contact et devis gratuit", "Urgence : appelez le <b>%s</b>, 24h/24. Pour un devis, remplissez le formulaire ci-dessous, nous vous rappelons rapidement." % B.PHONE)
    out += contact_section(path, "Demandez votre devis gratuit")
    out += f"""<section>
  <div class="wrap text-block prose">
    <h2>Comment nous joindre</h2>
    <ul>
      <li><strong>Téléphone (24h/24, 7j/7)</strong> : <a href="tel:{B.PHONE_TEL}">{B.PHONE}</a></li>
      <li><strong>E-mail</strong> : <a href="mailto:{B.EMAIL}">{B.EMAIL}</a></li>
      <li><strong>Zone</strong> : Vidauban ({B.BASE_CP}) et tout le centre Var. <a href="/zones-intervention/">Voir nos zones</a></li>
    </ul>
    <h2>Pour un devis plus rapide</h2>
    <p>Indiquez votre commune, le type de besoin et, si possible, envoyez quelques photos par e-mail (fuite, équipement, pièce à rénover). Nous pourrons vous donner une estimation plus précise dès le premier échange.</p>
  </div>
</section>
"""
    out += footer()
    write_page(path, out, "0.7")


def build_guides():
    path = "/conseils/"
    crumbs = [("Accueil", "/"), ("Conseils", path)]
    out = head("Conseils plomberie — guides pratiques d'un plombier du Var",
               "Guides pratiques : fuite d'eau, WC bouché, chauffe-eau en panne, dégât des eaux et assurance, eau calcaire, loi Warsmann, éviter les arnaques au dépannage.",
               path, [business_schema(), breadcrumb_schema(crumbs)])
    out += header(path)
    out += page_hero(crumbs, "Conseils de plombier", "Nos guides pratiques pour réagir face à une panne, entretenir votre installation et éviter les mauvaises surprises.")
    out += guides_teaser(GUIDES, "Tous nos guides")
    out += zones_section(cls="alt")
    out += contact_section(path)
    out += footer()
    write_page(path, out, "0.6")
    for g in GUIDES:
        gp = guide_path(g)
        gcrumbs = crumbs + [(g["h1"], gp)]
        article = {
            "@context": "https://schema.org", "@type": "Article",
            "headline": g["h1"], "description": g["meta"], "inLanguage": "fr-FR",
            "mainEntityOfPage": abs_url(gp), "datePublished": TODAY, "dateModified": TODAY,
            "image": SITE + "/assets/og-image.png",
            "author": {"@type": "Organization", "name": B.NAME, "url": SITE + "/"},
            "publisher": {"@id": SITE + "/#entreprise"},
        }
        out = head(g["title"], g["meta"], gp, [business_schema(), breadcrumb_schema(gcrumbs), article], og_type="article")
        out += header(gp)
        out += page_hero(gcrumbs, g["h1"], esc(g["excerpt"]))
        svc_links = "".join('<li><a href="/%s/"><span>%s</span><span>→</span></a></li>' % (sl, esc(SERVICE_BY_SLUG[sl]["name"] if sl in SERVICE_BY_SLUG else ASSURANCE_PAGE["name"])) for sl in g["services"])
        others = "".join('<li><a href="%s"><span>%s</span><span>→</span></a></li>' % (guide_path(o), esc(o["h1"])) for o in GUIDES if o is not g)
        out += f"""<section>
  <div class="wrap layout">
    <article class="prose">
      <p class="meta-line">Par l'équipe {B.NAME}, artisan plombier à Vidauban · Mis à jour le {date.today().strftime("%d/%m/%Y")}</p>
      {g["body"]}
      <div class="callout"><strong>Besoin d'un plombier ?</strong> Nous intervenons 24h/24 et 7j/7 à Vidauban et dans tout le centre Var. Appelez le <a href="tel:{B.PHONE_TEL}">{B.PHONE}</a>.</div>
    </article>
    <aside class="side">
      {call_card(None)}
      <div class="side-card"><h2>Prestations liées</h2><ul class="side-links">{svc_links}</ul></div>
      <div class="side-card"><h2>Autres guides</h2><ul class="side-links">{others}</ul></div>
    </aside>
  </div>
</section>
"""
        out += contact_section(gp)
        out += footer()
        write_page(gp, out, "0.6")


def build_plan():
    path = "/plan-du-site/"
    crumbs = [("Accueil", "/"), ("Plan du site", path)]
    out = head("Plan du site — %s, plombier dans le Var" % B.NAME,
               "Plan du site de %s : toutes les prestations de plomberie, toutes les communes desservies et tous les guides pratiques." % B.NAME,
               path, [business_schema(), breadcrumb_schema(crumbs)])
    out += header(path)
    out += page_hero(crumbs, "Plan du site", "Toutes les pages du site, classées par thème.")
    def ul(items):
        return "<ul>%s</ul>" % "".join('<li><a href="%s">%s</a></li>' % (h, esc(t)) for t, h in items)
    main_pages = [("Accueil", "/"), ("Prestations", "/prestations/"), ("Zones d'intervention", "/zones-intervention/"),
                  ("Tarifs", "/tarifs/"), ("À propos", "/a-propos/"), ("Conseils", "/conseils/"), ("FAQ", "/faq/"),
                  ("Contact & devis", "/contact/"), ("Mentions légales", "/mentions-legales/"), ("Confidentialité", "/politique-confidentialite/")]
    svc = [(s["name"], service_path(s)) for s in SERVICES] + [(ASSURANCE_PAGE["name"], "/%s/" % ASSURANCE_PAGE["slug"])]
    cities = [("Plombier %s (%s)" % (c["name"], c["cp"]), city_path(c)) for c in CITIES]
    guides = [(g["h1"], guide_path(g)) for g in GUIDES]
    out += f"""<section><div class="wrap">
  <div class="sitemap-cols">
    <div><h2>Pages principales</h2>{ul(main_pages)}<h2 style="margin-top:24px">Guides pratiques</h2>{ul(guides)}</div>
    <div><h2>Prestations</h2>{ul(svc)}</div>
    <div><h2>Communes</h2>{ul(cities)}</div>
  </div>
</div></section>
<section class="alt"><div class="wrap">
  <div class="sec-head"><h2>Prestations par commune</h2></div>
  <div class="sitemap-cols">{"".join('<div><h2>%s</h2>%s</div>' % (esc(s["short"]), ul([("%s %s" % (s["short"], c["name"]), combo_path(s, c)) for c in CITIES])) for s in SERVICES)}</div>
</div></section>
"""
    out += footer("/contact/")
    write_page(path, out, "0.3")


def build_legal():
    path = "/mentions-legales/"
    crumbs = [("Accueil", "/"), ("Mentions légales", path)]
    lines = ["<li><strong>Raison sociale</strong> : %s</li>" % B.LEGAL_NAME,
             "<li><strong>Activité</strong> : artisan plombier, dépannage et travaux de plomberie</li>",
             "<li><strong>Adresse</strong> : %s%s %s, France</li>" % (B.ADDRESS_STREET + ", " if B.ADDRESS_STREET else "", B.BASE_CP, B.BASE_CITY),
             "<li><strong>Téléphone</strong> : %s</li>" % B.PHONE,
             "<li><strong>E-mail</strong> : %s</li>" % B.EMAIL]
    if B.SIRET:
        lines.append("<li><strong>SIRET</strong> : %s</li>" % B.SIRET)
    if B.RESPONSABLE_PUBLICATION:
        lines.append("<li><strong>Responsable de la publication</strong> : %s</li>" % B.RESPONSABLE_PUBLICATION)
    out = head("Mentions légales — %s" % B.NAME, "Mentions légales du site de %s, artisan plombier à Vidauban (Var)." % B.NAME, path, [breadcrumb_schema(crumbs)], noindex=True)
    out += header(path)
    out += page_hero(crumbs, "Mentions légales", "Informations légales relatives au site et à l'entreprise.")
    out += f"""<section><div class="wrap text-block prose">
  <h2>Éditeur du site</h2><ul>{"".join(lines)}</ul>
  <h2>Hébergement</h2><p>Netlify, Inc. — San Francisco, Californie, États-Unis — www.netlify.com</p>
  <h2>Propriété intellectuelle</h2><p>Les textes, illustrations et éléments graphiques de ce site sont la propriété de {B.NAME}, sauf mention contraire. Toute reproduction sans autorisation est interdite. Les noms des compagnies d'assurance cités appartiennent à leurs propriétaires respectifs et sont mentionnés à titre informatif.</p>
  <h2>Médiation de la consommation</h2><p>Conformément au Code de la consommation, en cas de litige non résolu, le client consommateur peut recourir gratuitement à un médiateur de la consommation, dont les coordonnées lui sont communiquées sur simple demande.</p>
  <h2>Données personnelles</h2><p>Voir notre <a href="/politique-confidentialite/">politique de confidentialité</a>.</p>
</div></section>
"""
    out += footer("/contact/")
    write_page(path, out, sitemap=False)

    path = "/politique-confidentialite/"
    crumbs = [("Accueil", "/"), ("Politique de confidentialité", path)]
    out = head("Politique de confidentialité — %s" % B.NAME, "Politique de confidentialité et de cookies du site de %s." % B.NAME, path, [breadcrumb_schema(crumbs)], noindex=True)
    out += header(path)
    out += page_hero(crumbs, "Politique de confidentialité", "Comment nous utilisons les informations que vous nous transmettez.")
    out += f"""<section><div class="wrap text-block prose">
  <h2>Données collectées</h2><p>Via nos formulaires, nous collectons les informations que vous saisissez : nom, téléphone, e-mail, commune, type de besoin et message. Elles servent uniquement à vous recontacter et à traiter votre demande. Elles ne sont ni vendues ni cédées.</p>
  <h2>Durée de conservation</h2><p>Les demandes sans suite sont supprimées au plus tard 3 ans après le dernier contact. Les factures sont conservées pendant la durée légale.</p>
  <h2>Cookies et mode de consentement</h2>
  <p>Lors de votre première visite, un bandeau vous permet de <strong>tout accepter</strong>, <strong>tout refuser</strong> ou de <strong>personnaliser</strong> vos choix. Tant que vous n'avez pas choisi, aucun cookie publicitaire n'est déposé.</p>
  <ul>
    <li><strong>Cookies nécessaires</strong> : mémorisation de votre choix dans votre navigateur. Toujours actifs.</li>
    <li><strong>Mesure publicitaire (Google Ads)</strong> : savoir quelles annonces génèrent des appels et des demandes de devis.</li>
    <li><strong>Personnalisation des annonces</strong> : affichage d'annonces adaptées sur les services Google.</li>
  </ul>
  <p>Le site utilise le mode de consentement de Google (Consent Mode v2) : si vous refusez, la balise Google n'enregistre aucun cookie publicitaire et n'envoie que des signaux anonymes, sans identifiant. Votre choix est conservé 6 mois, puis vous est redemandé. Vous pouvez le modifier à tout moment via le lien « Cookies » en bas de chaque page.</p>
  <h2>Vos droits</h2><p>Vous disposez d'un droit d'accès, de rectification, d'effacement et d'opposition sur vos données. Écrivez-nous à <a href="mailto:{B.EMAIL}">{B.EMAIL}</a>. Vous pouvez également saisir la CNIL (www.cnil.fr).</p>
</div></section>
"""
    out += footer("/contact/")
    write_page(path, out, sitemap=False)


def build_404():
    path = "/404/"
    out = head("Page introuvable — %s" % B.NAME, "Cette page n'existe pas.", "/", [], noindex=True)
    out += header(path)
    out += f"""<section class="page-hero"><div class="wrap">
  <h1>Page introuvable</h1>
  <p class="lead">Cette page n'existe pas ou a été déplacée. Besoin d'un plombier ? Appelez le <b>{B.PHONE}</b>.</p>
  <div class="actions"><a href="/" class="btn btn-orange">Retour à l'accueil</a><a href="/prestations/" class="btn btn-ghost">Nos prestations</a></div>
</div></section>
"""
    out += footer("/contact/")
    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
        f.write(out)


# ---------------------------------------------------------------- fichiers techniques
AI_BOTS = [
    "GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot", "anthropic-ai",
    "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot", "Applebot-Extended", "Bingbot",
    "DuckAssistBot", "MistralAI-User", "Meta-ExternalAgent", "Amazonbot", "CCBot", "cohere-ai", "YouBot",
]


def build_robots():
    lines = [
        "# robots.txt — %s, plombier à Vidauban (Var)" % B.NAME,
        "# Tout le site est ouvert aux moteurs de recherche et aux assistants IA.",
        "",
        "User-agent: *",
        "Allow: /",
        "Disallow: /404.html",
        "",
        "# Moteurs de recherche et assistants IA explicitement autorisés",
    ]
    for bot in ["Googlebot", "Googlebot-Image"] + AI_BOTS:
        lines += ["User-agent: %s" % bot]
    lines += ["Allow: /", "Disallow: /404.html", "",
              "Sitemap: %s/sitemap.xml" % SITE,
              "",
              "# Résumé du site pour les modèles de langage : %s/llms.txt" % SITE,
              "# Version complète : %s/llms-full.txt" % SITE, ""]
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def build_sitemap():
    urls = "".join(
        "<url><loc>%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>\n" % (abs_url(p), TODAY, pr)
        for p, pr in PAGES)
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)


def build_llms():
    summary = ("%s est un artisan plombier indépendant basé à Vidauban (83550, Var, France), en activité depuis %d. "
               "Il intervient 24h/24 et 7j/7 dans le centre Var pour les urgences et les travaux de plomberie : fuite d'eau et recherche de fuite, "
               "débouchage, chauffe-eau, canalisations, installation sanitaire et rénovation de salle de bain. Téléphone : %s." % (B.NAME, B.SINCE, B.PHONE))
    lines = ["# %s — Plombier à Vidauban et dans le Var" % B.NAME, "", "> " + summary, "",
             "Informations clés :",
             "- Téléphone (24h/24, 7j/7) : %s" % B.PHONE,
             "- E-mail : %s" % B.EMAIL,
             "- Base : %s (%s), %s" % (B.BASE_CITY, B.BASE_CP, B.DEPARTEMENT),
             "- Expérience : depuis %d, plus de %s interventions, note moyenne %s, %s de clients satisfaits" % (B.SINCE, B.INTERVENTIONS, B.RATING, B.SATISFACTION),
             "- Tarifs : fuite d'eau dès 79 €, réparation de canalisation dès 89 €, débouchage dès 99 €, chauffe-eau / installation sanitaire / salle de bain sur devis. Diagnostic téléphonique et devis gratuits. Supplément éventuel nuit, week-end et jours fériés annoncé avant le déplacement.",
             "- Engagements : prix annoncé avant le déplacement, devis validé avant les travaux, facture détaillée, travaux garantis.",
             "- Assurance : factures acceptées par les assureurs habitation (%s), selon les garanties du contrat." % ", ".join(B.INSURERS),
             "- Communes desservies : %s." % ", ".join("%s (%s, %s)" % (c["name"], c["cp"], delay_label(c)) for c in CITIES),
             "", "## Prestations", ""]
    for s in SERVICES:
        lines.append("- [%s](%s%s) : %s %s." % (s["name"], SITE, service_path(s), strip_tags(s["lead"]), s["price_label"][0].upper() + s["price_label"][1:] if s["price_label"].lower().startswith("tarif") else "Tarif : " + s["price_label"]))
    lines.append("- [Dégât des eaux & assurance](%s/%s/) : recherche de fuite, réparation et justificatifs pour l'assurance habitation." % (SITE, ASSURANCE_PAGE["slug"]))
    lines += ["", "## Zones d'intervention", ""]
    for c in CITIES:
        lines.append("- [Plombier %s (%s)](%s%s) : %s" % (c["name"], c["cp"], SITE, city_path(c), delay_sentence(c)))
    lines += ["", "Chaque prestation existe aussi en page dédiée par commune, selon le modèle %s/{prestation}-{commune}/ (ex. %s%s, %s%s). Liste complète : %s/plan-du-site/" % (
        SITE, SITE, combo_path(SERVICES[2], CITIES[1]), SITE, combo_path(SERVICES[0], CITIES[7]), SITE)]
    lines += ["", "## Guides pratiques", ""]
    for g in GUIDES:
        lines.append("- [%s](%s%s) : %s" % (g["h1"], SITE, guide_path(g), g["excerpt"]))
    lines += ["", "## Pages utiles", "",
              "- [Tarifs](%s/tarifs/) : grille de prix et engagement prix" % SITE,
              "- [À propos](%s/a-propos/) : histoire et charte de confiance" % SITE,
              "- [FAQ](%s/faq/) : questions fréquentes" % SITE,
              "- [Contact](%s/contact/) : téléphone, e-mail et formulaire de devis" % SITE,
              "", "## Optional", "",
              "- [Version complète pour les LLM](%s/llms-full.txt) : tout le contenu textuel du site" % SITE, ""]
    with open(os.path.join(OUT, "llms.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    # llms-full.txt : contenu intégral en texte brut
    full = ["# %s — contenu complet du site" % B.NAME, "", "> " + summary, "", "Site : %s/" % SITE, ""]
    full += ["## Charte de confiance", ""] + ["- %s : %s" % (t, d) for t, d in trust_items()] + [""]
    for s in SERVICES:
        full += ["## %s" % s["h1"], "", "URL : %s%s" % (SITE, service_path(s)), "Tarif : %s" % s["price_label"], "", strip_tags(s["lead"]), ""]
        for h, body in s["sections"]:
            full += ["### %s" % h, "", strip_tags(body.replace("</li>", "</li>\n").replace("</p>", "</p>\n")), ""]
        full += ["### Questions fréquentes", ""]
        for q, a in s["faq"]:
            full += ["Q : %s" % q, "R : %s" % strip_tags(a), ""]
    full += ["## Questions générales", ""]
    for q, a in HOME_FAQ:
        full += ["Q : %s" % q, "R : %s" % strip_tags(a), ""]
    full += ["## Zones d'intervention", ""]
    for c in CITIES:
        full += ["### Plombier %s (%s)" % (c["name"], c["cp"]), "", c["intro"], c["context"], delay_sentence(c), ""]
    for g in GUIDES:
        full += ["## %s" % g["h1"], "", "URL : %s%s" % (SITE, guide_path(g)), "", strip_tags(g["body"].replace("</p>", "</p>\n").replace("</li>", "</li>\n").replace("</h2>", "</h2>\n")), ""]
    with open(os.path.join(OUT, "llms-full.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(full))


def build_static():
    shutil.copytree(SRC_ASSETS, os.path.join(OUT, "assets"), dirs_exist_ok=True)
    for name in ("favicon.svg", "favicon-32.png", "apple-touch-icon.png"):
        src = os.path.join(SRC_ASSETS, name)
        if os.path.exists(src):
            shutil.copy(src, os.path.join(OUT, name))
    manifest = {
        "name": B.NAME + " — Plombier Var", "short_name": "PRO SERVICE 83", "lang": "fr",
        "start_url": "/", "display": "browser", "background_color": "#ffffff", "theme_color": "#4a2a86",
        "icons": [{"src": "/apple-touch-icon.png", "sizes": "180x180", "type": "image/png"},
                  {"src": "/assets/logo-512.png", "sizes": "512x512", "type": "image/png"}],
    }
    with open(os.path.join(OUT, "site.webmanifest"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    build_static()
    build_home()
    build_prestations()
    for i, s in enumerate(SERVICES):
        build_service(s, i)
    build_assurance()
    build_zones()
    for ci, c in enumerate(CITIES):
        build_city(c)
        for si, s in enumerate(SERVICES):
            build_combo(s, c, si, ci)
    build_tarifs()
    build_about()
    build_faq_page()
    build_contact()
    build_guides()
    build_plan()
    build_legal()
    build_404()
    build_robots()
    build_sitemap()
    build_llms()
    print("%d pages indexables générées dans %s" % (len(PAGES), OUT))


if __name__ == "__main__":
    main()
