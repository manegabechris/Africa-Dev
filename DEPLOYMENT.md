# 🌐 GUIDE DE DÉPLOIEMENT - africa-dev.com

Pour que Google trouve votre site, **il DOIT être en ligne** (pas localhost).

---

## 🎯 3 OPTIONS DE DÉPLOIEMENT

### **OPTION 1: Vercel (⭐ Recommandé - GRATUIT)**

#### Pourquoi Vercel?
```
✅ Gratuit
✅ HTTPS automatique
✅ Déploiement en 1 clic
✅ Domaine custom (africa-dev.com)
✅ Performance excellente
```

#### Étapes:
```
1. Allez sur https://vercel.com
2. Cliquez "Sign up" avec GitHub
3. Sélectionnez votre repo "Africa-Dev"
4. Cliquez "Import"
5. Vercel déploie automatiquement!

URL temporaire: https://africa-dev.vercel.app
```

#### Ajouter votre domaine:
```
1. Allez à "Domains" dans Vercel
2. Cliquez "Add Domain"
3. Entrez: africa-dev.com
4. Vercel vous donne 2 choix:
   a) Changer vos serveurs DNS (RECOMMANDÉ)
   b) Ajouter des enregistrements CNAME
5. Suivez les instructions
6. Attendez 30 min - 24h (propagation DNS)
7. Voilà! Votre site est accessible
```

---

### **OPTION 2: Netlify (⭐ Aussi bon - GRATUIT)**

#### Étapes:
```
1. Allez sur https://netlify.com
2. Cliquez "Git with GitHub"
3. Autorisez Netlify
4. Sélectionnez: "Africa-Dev"
5. Cliquez "Deploy site"
6. Netlify déploie automatiquement!

URL: https://africa-dev.netlify.app
```

#### Ajouter domaine:
```
1. Allez à "Domain management"
2. Cliquez "Add custom domain"
3. Entrez: africa-dev.com
4. Changez vos serveurs DNS (si nécessaire)
5. Attendez la propagation DNS
```

---

### **OPTION 3: GitHub Pages (GRATUIT)**

#### Étapes:
```
1. Allez à "Settings" de votre repo
2. Cherchez "Pages" (à gauche)
3. Branch: "refactor/centralize-css-inline"
4. Sauvegardez
5. GitHub génère: https://manegabechris.github.io/Africa-Dev

URL: https://manegabechris.github.io/Africa-Dev
(Pas votre propre domaine, mais GRATUIT et HTTPS)
```

#### Ajouter domaine custom:
```
1. Dans "Pages", entrez: africa-dev.com
2. GitHub vous donne les serveurs DNS
3. Allez chez votre registrar (OVH, GoDaddy, etc.)
4. Changez les serveurs DNS
5. Attendez 24-48h
```

---

## 💳 ACHETER UN DOMAINE

Si vous n'avez pas africa-dev.com:

### **Endroits pour acheter (1-3€/an):**

| Site | Domaine gratuit? | Prix départ | Lien |
|------|-----------------|------------|------|
| **Namecheap** | OUI (.tk) | 1€/an | https://www.namecheap.com |
| **GoDaddy** | OUI (.tk) | 1€/an | https://www.godaddy.com |
| **OVH** | NON | 2€/an | https://www.ovh.com |
| **Amazon Route53** | NON | 12€/an | https://aws.amazon.com/route53 |

### **Je recommande: Namecheap**
```
1. Allez sur https://www.namecheap.com
2. Cherchez: "africa-dev.com"
3. Ajoutez au panier
4. Payez (~ 10€/an)
5. Revenez à Vercel/Netlify
6. Ajoutez le domaine custom
```

---

## 🔄 WORKFLOW DE DÉPLOIEMENT COMPLET

### **Avec Vercel (Recommandé):**

```
ÉTAPE 1: Préparer le code
  └─ Git push (déjà fait ✓)

ÉTAPE 2: Créer compte Vercel
  └─ https://vercel.com/sign-up

ÉTAPE 3: Importer projet
  └─ Sélectionnez Africa-Dev
  └─ Cliquez "Import"

ÉTAPE 4: Deployment auto
  └─ Vercel déploie automatiquement
  └─ URL: https://africa-dev.vercel.app

ÉTAPE 5: Ajouter domaine
  └─ Achetiez africa-dev.com (ou utilisez .tk gratuit)
  └─ Allez à "Domains" dans Vercel
  └─ Ajoutez: africa-dev.com
  └─ Changez DNS

ÉTAPE 6: Vérifier HTTPS
  └─ Allez à https://africa-dev.com
  └─ Vérifiez le cadenas ✅

ÉTAPE 7: Test final
  └─ Vérifiez https://africa-dev.com/robots.txt
  └─ Vérifiez https://africa-dev.com/sitemap.xml
  └─ Vérifiez https://africa-dev.com/index.html
```

---

## 🚨 VÉRIFICATION AVANT GOOGLE

Avant de soumettre à Google Search Console:

```
TESTEZ CES URLS:
  ☐ https://africa-dev.com          (ouvre?)
  ☐ https://africa-dev.com/         (ouvre?)
  ☐ https://africa-dev.com/index.html (ouvre?)
  ☐ https://africa-dev.com/robots.txt (télécharge?)
  ☐ https://africa-dev.com/sitemap.xml (ouvre?)

VÉRIFIEZ LE CODE:
  ☐ Pas d'erreur JavaScript (F12 → Console)
  ☐ Pas d'image brisée
  ☐ CSS chargé correctement
  ☐ Responsive sur mobile (F12 → Responsive mode)

VÉRIFIEZ LE HTTPS:
  ☐ URL commence par https:// (pas http://)
  ☐ Cadenas dans la barre d'adresse ✅
  ☐ Certificat SSL valide
```

---

## ⚡ REDÉPLOYER APRÈS CHANGEMENTS

Si vous modifiez le code plus tard:

```
VERCEL:
  1. git push origin refactor/centralize-css-inline
  2. Vercel redéploie automatiquement
  3. C'est tout! (no manual steps)

NETLIFY:
  1. git push origin refactor/centralize-css-inline
  2. Netlify détecte et redéploie
  3. C'est tout!

GITHUB PAGES:
  1. git push origin refactor/centralize-css-inline
  2. GitHub redéploie automatiquement
  3. C'est tout!
```

---

## 🆘 TROUBLESHOOTING

### **Problème: Site ne se charge pas**
```
Vérifications:
  ☐ Allez sur https://africa-dev.com
  ☐ Vérifiez qu'il y a le cadenas (https://)
  ☐ Attendez 5-10 minutes (déploiement en cours)
  ☐ Videz le cache (Ctrl+Shift+Suppr)
  ☐ Vérifiez dans les logs de votre déploiement
```

### **Problème: Fichiers manquants (404)**
```
Si .htaccess ou d'autres fichiers manquent:
  1. Vérifiez qu'ils sont dans le repo
  2. Vérifiez que git est synchronisé (git status)
  3. Déploiement utilise les fichiers du repo
  4. Si toujours manquant, uploadez manuellement
```

### **Problème: robots.txt ou sitemap ne chargent pas**
```
S'ils ne chargent pas:
  1. Vérifiez qu'ils existent: git ls-files robots.txt
  2. Vérifiez que le serveur ne les bloque pas
  3. Test avec curl: curl https://africa-dev.com/robots.txt
  4. Si .htaccess cause problème, commentez les rules
```

### **Problème: SSL/HTTPS ne fonctionne pas**
```
Vercel/Netlify génèrent SSL automatiquement:
  ☐ Attendez 5 minutes après déploiement
  ☐ Rafraîchissez F5
  ☐ Si toujours pas: check les logs
  ☐ Support Vercel/Netlify peut aider
```

---

## 📋 CHECKLIST DE DÉPLOIEMENT

```
PRÉ-DÉPLOIEMENT:
☐ Code testé localement
☐ Tous les changements dans Git
☐ Pas d'erreurs console (F12)

DÉPLOIEMENT:
☐ Crée compte Vercel/Netlify
☐ Connecte ton repo GitHub
☐ Déploiement réussi (pas d'erreurs)
☐ Site accessible (https://url)

POST-DÉPLOIEMENT:
☐ Acheté domaine africa-dev.com
☐ Domaine pointe vers le site
☐ HTTPS fonctionne (cadenas ✓)
☐ robots.txt accessible
☐ sitemap.xml accessible

GOOGLE:
☐ Domaine prêt pour soumettre
☐ Google Search Console peut vérifier
☐ Sitemap peut être soumis
```

---

## 💡 MA RECOMMANDATION

```
CHOIX #1: Vercel ⭐⭐⭐
  Pros:  Gratuit, HTTPS, domaine custom, deployment auto
  Cons:  Besoin domaine payant
  
CHOIX #2: Netlify ⭐⭐⭐
  Pros:  Gratuit, HTTPS, domaine custom, facile
  Cons:  Besoin domaine payant
  
CHOIX #3: GitHub Pages ⭐⭐
  Pros:  Gratuit, HTTPS, pas besoin de compte
  Cons:  URL moins belle (github.io), domaine custom compliqué

JE RECOMMANDE: Vercel + Domaine payant (10€/an)
  = Meilleur rapport coût/performance
  = Seul vrai coût: domaine
  = Automatique en tout
```

---

## 🚀 COMMENCEZ MAINTENANT!

**Choix rapide:**

```
Vous voulez gratuit + facile?
  → Vercel ou Netlify avec domaine gratuit .tk

Vous voulez meilleur domaine?
  → Vercel + Namecheap (10€/an)

Vous êtes impatient?
  → GitHub Pages (immédiat, 0€)
```

**Allez-y! C'est votre seul blocage avant Google!** 🚀

---

**Besoin d'aide?** Demandez-moi:
- Vous bloquez à quel endroit?
- Quelle plateforme choisissez-vous?
- Je peux vous aider step-by-step!
