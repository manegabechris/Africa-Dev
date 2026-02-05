import os
import re

print("\n" + "="*60)
print("🔍 VALIDATION SEO - GOOGLE SEARCH CONSOLE")
print("="*60 + "\n")

# Check robots.txt
print("✓ FICHIERS CRITIQUES:")
files_critical = ['robots.txt', 'sitemap.xml', '.htaccess', '.htaccess']
for fname in files_critical:
    if os.path.exists(f'/workspaces/Africa-Dev/{fname}'):
        print(f"  ✅ {fname} - Trouvé")
    else:
        print(f"  ❌ {fname} - MANQUANT")

print("\n✓ FICHIERS SUPPORT:")
files_support = ['schema.json', 'feed.xml', 'BingSiteAuth.xml', 'google-site-verification.txt']
for fname in files_support:
    if os.path.exists(f'/workspaces/Africa-Dev/{fname}'):
        print(f"  ✅ {fname} - Trouvé")
    else:
        print(f"  ❌ {fname} - MANQUANT")

print("\n✓ DOCUMENTATION:")
docs = ['GSC_REQUIREMENTS_CHECKLIST.md', 'CONFIG_FINAL.md']
for fname in docs:
    if os.path.exists(f'/workspaces/Africa-Dev/{fname}'):
        print(f"  ✅ {fname} - Trouvé")
    else:
        print(f"  ❌ {fname} - MANQUANT")

# Check HTML files
print("\n✓ VALIDATION DES FICHIERS HTML:")
html_files = [
    'index.html', 'chat.html', 'inscription.html', 'information.html',
    'confidentialité.html', 'option.html', 'developement web.html',
    'groupe chat.html', 'marketing digital.html', 'transformation digital.html'
]

meta_checks = {
    'charset': '<meta charset="UTF-8">',
    'viewport': 'name="viewport"',
    'description': 'name="description"',
    'robots': 'name="robots"',
    'og:title': 'property="og:title"',
    'og:description': 'property="og:description"',
    'og:url': 'property="og:url"',
    'og:image': 'property="og:image"',
    'canonical': 'rel="canonical"',
    'schema': 'application/ld+json'
}

all_checks_passed = True
for html_file in html_files:
    filepath = f'/workspaces/Africa-Dev/{html_file}'
    if not os.path.exists(filepath):
        print(f"\n  ⚠️  {html_file} - MANQUANT")
        all_checks_passed = False
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    checks_passed = 0
    checks_total = len(meta_checks)
    
    for check_name, check_string in meta_checks.items():
        if check_string.lower() in content.lower():
            checks_passed += 1
    
    percentage = (checks_passed / checks_total) * 100
    status = "✅" if percentage == 100 else "⚠️ "
    
    print(f"  {status} {html_file}: {checks_passed}/{checks_total} ({int(percentage)}%)")
    
    if percentage < 100:
        all_checks_passed = False
        for check_name, check_string in meta_checks.items():
            if check_string.lower() not in content.lower():
                print(f"       ❌ Manque: {check_name}")

print("\n" + "="*60)
if all_checks_passed:
    print("✅ TOUS LES ÉLÉMENTS SEO SONT EN PLACE!")
else:
    print("⚠️  CERTAINS ÉLÉMENTS MANQUENT - Vérifiez ci-dessus")
print("="*60 + "\n")

# Check robots.txt content
print("✓ CONTENU ROBOTS.TXT:")
try:
    with open('/workspaces/Africa-Dev/robots.txt', 'r') as f:
        robots_content = f.read()
        if 'User-agent: *' in robots_content:
            print("  ✅ User-agent configuré")
        if 'Sitemap:' in robots_content:
            print("  ✅ Sitemap référencé")
        if 'Disallow:' in robots_content:
            print("  ✅ Exclusions configurées")
except:
    print("  ❌ Erreur lors de la lecture")

# Check sitemap.xml
print("\n✓ CONTENU SITEMAP.XML:")
try:
    with open('/workspaces/Africa-Dev/sitemap.xml', 'r') as f:
        sitemap_content = f.read()
        urls = len(re.findall(r'<loc>', sitemap_content))
        print(f"  ✅ {urls} URLs trouvées dans le sitemap")
except:
    print("  ❌ Erreur lors de la lecture")

print("\n" + "🎯 PROCHAINES ÉTAPES:" + "\n")
print("1. Remplacez 'yoursite.com' par votre domaine dans:")
print("   - robots.txt")
print("   - sitemap.xml")
print("   - Tous les fichiers HTML (balises canonical, og:url, etc.)")
print("\n2. Obtenez votre code de vérification Google:")
print("   - Allez sur https://search.google.com/search-console")
print("   - Remplacez 'YOUR_GOOGLE_VERIFICATION_CODE'")
print("\n3. Créez l'image OG (1200×630px):")
print("   - Sauvegardez comme 'og-image.jpg'")
print("   - Mettez à jour les URLs og:image si nécessaire")
print("\n4. Soumettez dans Google Search Console:")
print("   - Vérifiez votre domaine")
print("   - Soumettez le sitemap.xml")
print("   - Vérifiez la couverture (onglet 'Couverture')")
print("\n" + "="*60 + "\n")

