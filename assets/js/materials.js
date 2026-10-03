(function () {
  'use strict';
  var panel = document.getElementById('material-preview');
  if (!panel) return;
  var triggers = Array.from(document.querySelectorAll('.js-preview'));
  var frameContainer = panel.querySelector('.preview-frame');
  var status = document.getElementById('preview-status');
  var current = null;

  function safePDFURL(value) {
    try {
      var url = new URL(value, window.location.href);
      var local = url.origin === window.location.origin && /^https?:$/.test(url.protocol);
      return (url.protocol === 'https:' || local) && !url.username && !url.password ? url.href : null;
    } catch (_) { return null; }
  }

  function closePreview() {
    frameContainer.replaceChildren();
    panel.hidden = true;
    triggers.forEach(function (trigger) { trigger.setAttribute('aria-expanded', 'false'); });
    status.textContent = 'Preview closed.';
    if (current) current.focus({preventScroll: true});
    current = null;
  }

  triggers.forEach(function (trigger) {
    trigger.addEventListener('click', function (event) {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || event.button !== 0) return;
      var url = safePDFURL(trigger.href);
      if (!url) { event.preventDefault(); return; }
      event.preventDefault();
      current = trigger;
      triggers.forEach(function (item) { item.setAttribute('aria-expanded', String(item.dataset.previewId === trigger.dataset.previewId)); });
      panel.querySelector('#preview-title').textContent = trigger.dataset.previewTitle;
      panel.querySelector('.preview-caption').textContent = trigger.dataset.previewCaption;
      panel.querySelector('.preview-original').href = url;
      var frame = document.createElement('iframe');
      frame.title = trigger.dataset.previewTitle + ' — PDF preview';
      frame.referrerPolicy = 'no-referrer';
      frame.src = url;
      frameContainer.replaceChildren(frame);
      panel.hidden = false;
      status.textContent = 'Preview opened for ' + trigger.dataset.previewTitle + '.';
      panel.querySelector('.preview-close').focus({preventScroll: true});
      panel.scrollIntoView({behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start'});
    });
  });
  panel.querySelector('.preview-close').addEventListener('click', closePreview);
  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && !panel.hidden) closePreview();
  });
}());
