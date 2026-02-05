#!/bin/bash

# Domaine à remplacer
DOMAIN="africa-dev.com"

echo "🔄 Remplacement du domaine par: $DOMAIN"
echo "================================"

# Remplacer dans robots.txt
sed -i "s|yoursite.com|$DOMAIN|g" robots.txt
echo "✓ robots.txt mis à jour"

# Remplacer dans sitemap.xml
sed -i "s|yoursite.com|$DOMAIN|g" sitemap.xml
echo "✓ sitemap.xml mis à jour"

# Remplacer dans tous les fichiers HTML
for file in *.html; do
    sed -i "s|yoursite.com|$DOMAIN|g" "$file"
    echo "✓ $file mis à jour"
done

# Remplacer dans schema.json
sed -i "s|yoursite.com|$DOMAIN|g" schema.json
echo "✓ schema.json mis à jour"

# Remplacer dans feed.xml
sed -i "s|yoursite.com|$DOMAIN|g" feed.xml
echo "✓ feed.xml mis à jour"

# Remplacer dans BingSiteAuth.xml
sed -i "s|yoursite.com|$DOMAIN|g" BingSiteAuth.xml 2>/dev/null || echo "○ BingSiteAuth.xml (pas de domaine)"

echo ""
echo "✅ Tous les fichiers ont été mis à jour avec: $DOMAIN"
