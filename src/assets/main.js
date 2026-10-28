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

  /* Formulaires de devis (Netlify Forms, envoi en arrière-plan) */
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
        gtagReportConversion_Formulaire();
        btn.textContent = 'Demande envoyée ✓';
        btn.style.background = '#22a559';
        if(status){
          status.className = 'form-status ok';
          status.textContent = 'Merci ! Nous vous rappelons rapidement. En cas d’urgence, appelez le 06 75 93 19 04.';
        }
        form.reset();
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

  /* Consentement cookies (Google Consent Mode v2) */
  var KEY = 'ps83-consent';
  var banner = document.getElementById('consent');
  function read(){ try { return localStorage.getItem(KEY); } catch(e){ return null; } }
  function save(v){ try { localStorage.setItem(KEY, v); } catch(e){} }
  function apply(v){
    var g = v === 'granted' ? 'granted' : 'denied';
    gtag('consent', 'update', {ad_storage:g, ad_user_data:g, ad_personalization:g, analytics_storage:g});
  }
  var stored = read();
  if(stored){ apply(stored); } else if(banner){ banner.classList.add('show'); }
  document.querySelectorAll('[data-consent]').forEach(function(b){
    b.addEventListener('click', function(){
      var v = b.getAttribute('data-consent');
      if(v === 'open'){ if(banner){ banner.classList.add('show'); } return; }
      save(v); apply(v);
      if(banner){ banner.classList.remove('show'); }
    });
  });
})();
