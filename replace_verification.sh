#!/bin/bash

CODE="158265"

echo "🔐 Remplacement du code de vérification Google"
echo "=============================================="

# Remplacer dans tous les fichiers HTML
for file in *.html; do
    sed -i "s|YOUR_GOOGLE_VERIFICATION_CODE|$CODE|g" "$file"
    echo "✓ $file mis à jour"
done

echo ""
echo "✅ Code de vérification: $CODE"
echo ""
echo "⚠️  IMPORTANT: Vérifiez votre code dans index.html"
grep -n "google-site-verification" index.html
