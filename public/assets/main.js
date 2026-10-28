/* PRO SERVICE 83 — scripts partagés (menu mobile, formulaire, consentement cookies) */

/* Conversions Google Ads */
function gtagReportConversion_Appel(url) {
  gtag('event', 'conversion', {
    'send_to': 'AW-18380568336/kUUYCLWxwfocEJDuxLxE',
    'event_callback': function() {
      if (typeof(url) != 'undefined') {
        window.location = url;
      }
    }
  });
  return false;
}

function gtagReportConversion_Formulaire(url) {
  gtag('event', 'conversion', {
    'send_to': 'AW-18380568336/BAvQCP2rjuAcEJDuxLxE',
    'event_callback': function() {
      if (typeof(url) != 'undefined') {
        window.location = url;
      }
    }
  });
  return false;
}

(function(){
  /* Suivi des clics sur les numéros de téléphone */
  document.querySelectorAll('a[href^="tel:"]').forEach(function(a){
    a.addEventListener('click', function(){ gtagReportConversion_Appel(); });
  });

  /* Menu mobile */
  var btn = document.querySelector('.menu-btn');
  var mnav = document.getElementById('mobile-nav');
  if(btn && mnav){
    btn.addEventListener('click', function(){
      var open = mnav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  /* Fenêtre « Demander un devis » */
  var modal = document.getElementById('quote-modal');
  var lastFocus = null;
  function openModal(service){
    if(!modal){ return; }
    lastFocus = document.activeElement;
    var label = document.getElementById('quote-service-label');
    var input = document.getElementById('quote-service-input');
    if(label){ label.textContent = service; }
    if(input){ input.value = service; }
    var page = modal.querySelector('input[name="page"]');
    if(page){ page.value = location.pathname; }
    modal.classList.add('open');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    var first = document.getElementById('q-prenom');
    if(first){ first.focus(); }
  }
  function closeModal(){
    if(!modal){ return; }
    modal.classList.remove('open');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    if(lastFocus && lastFocus.focus){ lastFocus.focus(); }
  }
  document.querySelectorAll('.svc-quote').forEach(function(b){
    b.addEventListener('click', function(){ openModal(b.getAttribute('data-service') || 'Demande de devis'); });
  });
  var qc = document.getElementById('quote-close');
  if(qc){ qc.addEventListener('click', closeModal); }
  if(modal){ modal.addEventListener('click', function(e){ if(e.target === modal){ closeModal(); } }); }
  document.addEventListener('keydown', function(e){
    if(e.key === 'Escape' && modal && modal.classList.contains('open')){ closeModal(); }
  });

  /* Page merci : conversion « formulaire » */
  if(document.body.getAttribute('data-page') === 'merci'){ gtagReportConversion_Formulaire(); }

  /* Agrandissement des photos de chantiers */
  var shots = document.querySelectorAll('[data-lightbox]');
  if(shots.length && typeof HTMLDialogElement === 'function'){
    var d = document.createElement('dialog');
    d.className = 'lightbox';
    d.innerHTML = '<button type="button" class="lightbox-close" aria-label="Fermer">✕</button><img alt=""><p></p>';
    document.body.appendChild(d);
    var img = d.querySelector('img'), cap = d.querySelector('p');
    d.querySelector('.lightbox-close').addEventListener('click', function(){ d.close(); });
    d.addEventListener('click', function(e){ if(e.target === d){ d.close(); } });
    shots.forEach(function(a){
      a.addEventListener('click', function(e){
        e.preventDefault();
        img.src = a.getAttribute('href');
        img.alt = cap.textContent = a.getAttribute('data-caption') || '';
        d.showModal();
      });
    });
  }

  /* Formulaires de devis (Netlify Forms, envoi en arrière-plan puis page merci) */
  document.querySelectorAll('form.quote').forEach(function(form){
    form.addEventListener('submit', function(e){
      e.preventDefault();
      var btn = form.querySelector('button[type="submit"]');
      var status = form.querySelector('.form-status');
      var original = btn.textContent;
      btn.disabled = true;
      btn.textContent = 'Envoi en cours…';
      var body = new URLSearchParams(new FormData(form)).toString();
      fetch('/', {
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: body
      }).then(function(res){
        if(!res.ok){ throw new Error(res.status); }
        btn.textContent = 'Demande envoyée ✓';
        btn.style.background = '#22a559';
        window.location.href = '/merci/';
      }).catch(function(){
        btn.disabled = false;
        btn.textContent = original;
        if(status){
          status.className = 'form-status err';
          status.textContent = 'L’envoi a échoué. Appelez-nous au 06 75 93 19 04 ou écrivez à proservice83@hotmail.fr.';
        }
      });
    });
  });

  /* Consentement cookies (Google Consent Mode v2). Choix conservé 6 mois, puis redemandé. */
  var KEY = 'ps83-consent';
  var MAX_AGE = 182 * 24 * 3600 * 1000;
  var banner = document.getElementById('consent');
  var prefs = document.getElementById('consent-prefs');
  var customBtn = document.getElementById('consent-custom');
  var boxAds = document.getElementById('c-ads');
  var boxPerso = document.getElementById('c-perso');
  function read(){
    try {
      var c = JSON.parse(localStorage.getItem(KEY));
      return c && (Date.now() - c.t) < MAX_AGE ? c : null;
    } catch(e){ return null; }
  }
  function save(c){ try { localStorage.setItem(KEY, JSON.stringify(c)); } catch(e){} }
  function apply(c){
    var ads = c.ads ? 'granted' : 'denied';
    var perso = c.ads && c.perso ? 'granted' : 'denied';
    gtag('consent', 'update', {ad_storage:ads, ad_user_data:ads, ad_personalization:perso, analytics_storage:ads});
    gtag('set', 'ads_data_redaction', ads === 'denied');
  }
  function choose(ads, perso){
    var c = {ads: !!ads, perso: !!(ads && perso), t: Date.now()};
    save(c); apply(c);
    if(banner){ banner.classList.remove('show'); }
  }
  function open(){
    var c = read();
    if(boxAds){ boxAds.checked = !!(c && c.ads); }
    if(boxPerso){ boxPerso.checked = !!(c && c.perso); }
    if(banner){ banner.classList.add('show'); }
  }
  if(!read()){ open(); }
  if(boxPerso && boxAds){
    boxPerso.addEventListener('change', function(){ if(boxPerso.checked){ boxAds.checked = true; } });
    boxAds.addEventListener('change', function(){ if(!boxAds.checked){ boxPerso.checked = false; } });
  }
  document.querySelectorAll('[data-consent]').forEach(function(b){
    b.addEventListener('click', function(){
      var v = b.getAttribute('data-consent');
      if(v === 'open'){ open(); return; }
      if(v === 'granted'){ choose(true, true); return; }
      if(v === 'denied'){ choose(false, false); return; }
      if(v === 'custom'){
        if(prefs && prefs.hidden){
          prefs.hidden = false;
          customBtn.textContent = 'Enregistrer mes choix';
        } else {
          choose(boxAds && boxAds.checked, boxPerso && boxPerso.checked);
        }
      }
    });
  });
})();
