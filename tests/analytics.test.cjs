const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const html = fs.readFileSync('_site-production/index.html', 'utf8');
const code = [...html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/g)].map(match => match[1]).find(script => script.includes('var measurementId'));
assert.ok(code, 'Production Analytics script exists');
for (const hostname of ['127.0.0.1', 'localhost', 'preview.example.org', 'junhyoung-chung.github.io', 'junhyoung-chung.github.io.example.org']) {
  const inserted = [];
  const context = {window: {location: {hostname}}, document: {createElement: () => ({}), head: {appendChild: script => inserted.push(script)}}};
  vm.runInNewContext(code, context);
  if (hostname === 'junhyoung-chung.github.io') {
    assert.equal(inserted.length, 1);
    assert.equal(inserted[0].src, 'https://www.googletagmanager.com/gtag/js?id=G-CH97FJJG6N');
    assert.equal(inserted[0].async, true);
    assert.equal(context.window.dataLayer.length, 2);
    assert.equal(context.window.dataLayer[1][0], 'config');
    assert.equal(context.window.dataLayer[1][1], 'G-CH97FJJG6N');
  } else {
    assert.equal(inserted.length, 0, `No tracking script on ${hostname}`);
    assert.equal(context.window.dataLayer, undefined);
  }
}
console.log('PASS: GA4 loads once on the production hostname; local/preview/lookalike hosts are not tracked');
