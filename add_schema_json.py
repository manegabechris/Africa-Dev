import os

pages_schema = {
    'index.html': {
        'type': 'WebSite',
        'name': 'Africa Dev - Plateforme de Formation',
        'description': 'Plateforme de formation en ligne pour la transformation digitale et le développement web',
        'url': 'https://yoursite.com'
    },
    'chat.html': {
        'type': 'WebPage',
        'name': 'Chat Africa Dev',
        'description': 'Application de chat en temps réel pour la communauté Africa Dev',
        'url': 'https://yoursite.com/chat.html'
    },
    'inscription.html': {
        'type': 'WebPage',
        'name': 'Inscription - Africa Dev',
        'description': 'Formulaire d\'inscription pour rejoindre Africa Dev',
        'url': 'https://yoursite.com/inscription.html'
    },
    'information.html': {
        'type': 'WebPage',
        'name': 'Informations - Africa Dev',
        'description': 'En savoir plus sur Africa Dev',
        'url': 'https://yoursite.com/information.html'
    },
    'confidentialité.html': {
        'type': 'WebPage',
        'name': 'Politique de Confidentialité',
        'description': 'Politique de confidentialité d\'Africa Dev',
        'url': 'https://yoursite.com/confidentialité.html'
    },
    'option.html': {
        'type': 'WebPage',
        'name': 'Options - Africa Dev',
        'description': 'Les options et modules de formation',
        'url': 'https://yoursite.com/option.html'
    },
    'developement web.html': {
        'type': 'Course',
        'name': 'Cours de Développement Web',
        'description': 'Apprenez le développement web avec HTML, CSS et JavaScript',
        'url': 'https://yoursite.com/developement-web.html',
        'provider': 'Africa Dev'
    },
    'groupe chat.html': {
        'type': 'WebPage',
        'name': 'Groupe Chat',
        'description': 'Rejoignez notre groupe de discussion',
        'url': 'https://yoursite.com/groupe-chat.html'
    },
    'marketing digital.html': {
        'type': 'Course',
        'name': 'Cours de Marketing Digital',
        'description': 'Stratégies et techniques de marketing digital',
        'url': 'https://yoursite.com/marketing-digital.html',
        'provider': 'Africa Dev'
    },
    'transformation digital.html': {
        'type': 'Course',
        'name': 'Transformation Digitale',
        'description': 'Guide complet de la transformation digitale',
        'url': 'https://yoursite.com/transformation-digital.html',
        'provider': 'Africa Dev'
    }
}

def generate_schema(page_info):
    if page_info['type'] == 'Course':
        return f"""  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Course",
    "name": "{page_info['name']}",
    "description": "{page_info['description']}",
    "url": "{page_info['url']}",
    "provider": {{
      "@type": "Organization",
      "name": "{page_info.get('provider', 'Africa Dev')}",
      "url": "https://yoursite.com"
    }}
  }}
  </script>
"""
    else:
        return f"""  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "{page_info['type']}",
    "name": "{page_info['name']}",
    "description": "{page_info['description']}",
    "url": "{page_info['url']}"
  }}
  </script>
"""

for filename, page_info in pages_schema.items():
    filepath = os.path.join('/workspaces/Africa-Dev', filename)
    if not os.path.exists(filepath):
        print(f"Fichier non trouvé: {filepath}")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Trouver la position juste avant </head>
    head_end = content.rfind('</head>')
    if head_end == -1:
        print(f"Pas de </head> trouvé dans {filename}")
        continue
    
    # Insérer le schéma JSON
    schema = generate_schema(page_info)
    new_content = content[:head_end] + schema + content[head_end:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✓ Schéma JSON ajouté: {filename}")

print("\nSchéma JSON ajouté à tous les fichiers HTML!")
