import os
import re

pages = {
    'confidentialité.html': {
        'title': 'Politique de Confidentialité - Africa Dev',
        'description': 'Politique de confidentialité d\'Africa Dev - Découvrez comment nous protégeons vos données.',
        'keywords': 'confidentialité, politique, protection des données, RGPD',
        'url': 'https://yoursite.com/confidentialité.html',
        'og_image': 'https://yoursite.com/og-image.jpg'
    },
    'option.html': {
        'title': 'Bienvenue sur Africa Dev',
        'description': 'Explorez les options et modules de formation disponibles sur Africa Dev.',
        'keywords': 'options, modules, formation, apprentissage',
        'url': 'https://yoursite.com/option.html',
        'og_image': 'https://yoursite.com/og-image.jpg'
    },
    'developement web.html': {
        'title': 'Développement Web - Africa Dev',
        'description': 'Apprenez le développement web avec nos cours complets. HTML, CSS, JavaScript et bien plus.',
        'keywords': 'développement web, programmation, HTML, CSS, JavaScript',
        'url': 'https://yoursite.com/developement-web.html',
        'og_image': 'https://yoursite.com/og-image.jpg'
    },
    'groupe chat.html': {
        'title': 'Notre Groupe Chat - Africa Dev',
        'description': 'Rejoignez notre groupe chat pour discuter et partager avec la communauté Africa Dev.',
        'keywords': 'groupe chat, communauté, discussion, interaction',
        'url': 'https://yoursite.com/groupe-chat.html',
        'og_image': 'https://yoursite.com/og-image.jpg'
    },
    'marketing digital.html': {
        'title': 'Marketing Digital - Africa Dev',
        'description': 'Maîtrisez les stratégies de marketing digital pour développer votre présence en ligne.',
        'keywords': 'marketing digital, stratégie marketing, SEO, réseaux sociaux',
        'url': 'https://yoursite.com/marketing-digital.html',
        'og_image': 'https://yoursite.com/og-image.jpg'
    },
    'transformation digital.html': {
        'title': 'Transformation Digitale - Africa Dev',
        'description': 'Découvrez comment transformer votre entreprise à l\'ère numérique avec Africa Dev.',
        'keywords': 'transformation digitale, transformation numérique, innovations technologiques',
        'url': 'https://yoursite.com/transformation-digital.html',
        'og_image': 'https://yoursite.com/og-image.jpg'
    }
}

def create_head_content(page_info):
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{page_info['description']}">
  <meta name="keywords" content="{page_info['keywords']}">
  <meta name="author" content="Africa Dev Team">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{page_info['url']}">
  <!-- Open Graph -->
  <meta property="og:title" content="{page_info['title']}">
  <meta property="og:description" content="{page_info['description']}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{page_info['url']}">
  <meta property="og:image" content="{page_info['og_image']}">
  <meta property="og:locale" content="fr_FR">
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{page_info['title']}">
  <meta name="twitter:description" content="{page_info['description']}">
  <meta name="twitter:image" content="{page_info['og_image']}">
  <title>{page_info['title']}</title>
  <link rel="stylesheet" href="Styles.CSS">
</head>
"""

for filename, page_info in pages.items():
    filepath = os.path.join('/workspaces/Africa-Dev', filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the closing </head> tag
    head_end = content.find('</head>')
    if head_end == -1:
        print(f"No </head> found in {filename}")
        continue
    
    # Find the opening <head> tag
    head_start = content.find('<head>')
    if head_start == -1:
        head_start = content.find('<head ')
    
    if head_start == -1:
        print(f"No <head> found in {filename}")
        continue
    
    # Replace from <!DOCTYPE to </head>
    new_content = content[:content.find('<!DOCTYPE')]
    new_content += create_head_content(page_info)
    new_content += content[head_end + 7:]  # +7 for len('</head>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✓ Updated: {filename}")

print("\nAll HTML files have been updated with SEO metadata!")
