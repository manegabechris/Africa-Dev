const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

function waitFor(predicate, timeout = 2000) {
  const start = Date.now();
  return new Promise((resolve, reject) => {
    (function poll() {
      try {
        if (predicate()) return resolve();
      } catch (e) {}
      if (Date.now() - start > timeout) return reject(new Error('timeout'));
      setTimeout(poll, 20);
    })();
  });
}

function loadOptionDOM() {
  const html = fs.readFileSync(path.resolve(__dirname, '../option.html'), 'utf8');
  const dom = new JSDOM(html, { runScripts: 'dangerously', resources: 'usable', url: 'http://localhost/' });
  return dom;
}

test('search finds "developpement" (accent-insensitive) and protects navigation for anonymous users then allows when logged in', async () => {
  const dom = loadOptionDOM();
  const { window } = dom;

  // wait for scripts to run
  await waitFor(() => window.document.readyState === 'complete' || window.document.getElementById('search-input'));

  // ensure anonymous
  window.localStorage.removeItem('currentUser');
  // perform search (no accents)
  const input = window.document.getElementById('search-input');
  input.value = 'developpement';
  input.dispatchEvent(new window.Event('input', { bubbles: true }));

  // wait for results
  await waitFor(() => window.document.getElementById('search-results').children.length >= 1);
  const results = window.document.getElementById('search-results');
  expect(results.children.length).toBeGreaterThan(0);

  // move focus into list with ArrowDown
  input.dispatchEvent(new window.KeyboardEvent('keydown', { key: 'ArrowDown', bubbles: true }));
  await waitFor(() => window.document.activeElement && window.document.activeElement.tagName === 'LI');
  const active = window.document.activeElement;
  expect(active.tagName).toBe('LI');

  // Press Enter while anonymous -> should show toast (no navigation)
  active.dispatchEvent(new window.KeyboardEvent('keydown', { key: 'Enter', bubbles: true }));

  const toast = window.document.getElementById('toast');
  await waitFor(() => toast.style.display === 'block');
  expect(toast.textContent).toMatch(/Connectez-vous/i);

  // Now simulate login
  window.localStorage.setItem('currentUser', JSON.stringify({ username: 'tester', name: 'Tester' }));
  // update UI (function defined by the page)
  if (typeof window.updateUserUI === 'function') window.updateUserUI();

  // Press Enter again to navigate
  active.dispatchEvent(new window.KeyboardEvent('keydown', { key: 'Enter', bubbles: true }));

  // Expect the location changed to the target page (file name includes 'developement web.html')
  await waitFor(() => /developement web\.html$/.test(window.location.href));
  expect(window.location.href).toMatch(/developement web\.html$/);
});
