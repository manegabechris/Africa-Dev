# 🚀 GUIDE DE DÉPLOIEMENT - VERCEL & NETLIFY

**Status:** Prêt pour le déploiement ✅  
**Domaine:** africa-dev.com  
**Type:** Site statique  
**Date:** 5 février 2026

---

## 🎯 DÉPLOIEMENT RAPIDE - VERCEL (RECOMMANDÉ)

### Étape 1: Créer un compte Vercel

```
1. Allez sur: https://vercel.com/sign-up
2. Cliquez "Continue with GitHub"
3. Autorisez Vercel à accéder à vos repos
4. Complétez votre profil
```

### Étape 2: Importer votre projet

```
1. Allez sur: https://vercel.com/new
2. Cherchez: "manegabechris/Africa-Dev"
3. Cliquez "Import"
4. Framework: "Other" (site statique)
5. Root Directory: "." (racine)
6. Cliquez "Deploy"
→ Vercel déploie automatiquement! 🎉
```

**Votre URL temporaire:** `https://africa-dev.vercel.app`

### Étape 3: Ajouter votre domaine custom

```
1. Allez à "Domains" dans Vercel
2. Cliquez "Add Domain"
3. Entrez: africa-dev.com
4. Vercel vous donne 2 options:
   
   OPTION A: Changer les serveurs DNS (RECOMMANDÉ)
   ├─ Allez chez votre registrar (GoDaddy, Namecheap, etc.)
   ├─ Remplacez les serveurs DNS par ceux de Vercel
   ├─ Attendez 30 min - 24h (propagation)
   └─ Voilà! Domain est connecté ✓

   OPTION B: Ajouter enregistrement CNAME
   ├─ Ajoutez un enregistrement CNAME dans votre DNS
   ├─ Cible: cname.vercel-dns.com
   ├─ Attendez la propagation
   └─ Domaine connecté ✓
```

### Étape 4: Vérifier HTTPS

```
Vercel génère automatiquement un certificat SSL:
✅ https://africa-dev.com (cadenas vert)
✅ Certificat valide pour 1 an
✅ Renouelé automatiquement
```

### Étape 5: Modifier le code après le déploiement

```
Workflow:
1. git push origin refactor/centralize-css-inline
2. Vercel détecte le changement automatiquement
3. Vercel redéploie votre site
4. 1-2 minutes plus tard: changes sont en ligne! ✓

Pas besoin de faire quoi que ce soit d'autre!
```

---

## 🎯 DÉPLOIEMENT ALTERNATIVE - NETLIFY

Si vous préférez Netlify (aussi excellent):

### Étape 1: Créer un compte Netlify

```
1. Allez sur: https://netlify.com
2. Cliquez "Sign up"
3. Choisissez "GitHub"
4. Autorisez Netlify
5. Choisissez d'installer Netlify App ou pas
```

### Étape 2: Créer un nouveau site à partir du repo

```
1. Allez sur: https://app.netlify.com
2. Cliquez "Add new site"
3. Choisissez "Import an existing project"
4. Sélectionnez GitHub
5. Cherchez et sélectionnez: Africa-Dev
6. Configurez les settings:
   ├─ Build command: (laisser vide ou "echo 'Static site'")
   ├─ Publish directory: . (point)
   └─ Environment: aucune variable nécessaire
7. Cliquez "Deploy site"
→ Netlify déploie automatiquement! 🎉
```

**Votre URL temporaire:** `https://africa-dev.netlify.app`

### Étape 3: Ajouter votre domaine custom

```
1. Allez à "Domain management"
2. Cliquez "Add custom domain"
3. Entrez: africa-dev.com
4. Netlify vous donne les serveurs DNS
5. Allez chez votre registrar
6. Changez les serveurs DNS vers Netlify
7. Attendez 30 min - 24h (propagation)
```

### Étape 4: HTTPS automatique

```
✅ Netlify génère automatiquement un certificat SSL
✅ Renouvellement automatique annuel
✅ Cadenas vert = vous êtes connecté!
```

### Étape 5: Redéploiement automatique

```
Pareil que Vercel:
1. git push origin refactor/centralize-css-inline
2. Netlify redéploie automatiquement
3. 1-2 minutes = changes en ligne ✓
```

---

## 📊 COMPARAISON: VERCEL vs NETLIFY

| Aspect | Vercel | Netlify | Gagnant |
|--------|--------|---------|---------|
| **Gratuit** | ✅ Oui | ✅ Oui | Égal |
| **HTTPS** | ✅ Auto | ✅ Auto | Égal |
| **Domaine custom** | ✅ Oui | ✅ Oui | Égal |
| **Performance** | ⭐⭐⭐ | ⭐⭐⭐ | Égal |
| **Facilité** | ⭐⭐⭐ | ⭐⭐⭐ | Égal |
| **Support DNS** | ✅ Bon | ✅ Bon | Égal |
| **Speed** | ⚡ Rapide | ⚡ Rapide | Égal |

**Recommandation:** Vercel (légèrement plus moderne, UI plus claire)

---

## 🎁 FICHIERS DE CONFIGURATION FOURNIS

J'ai créé ces fichiers pour optimiser votre déploiement:

```
✅ vercel.json
   └─ Configuration optimisée pour Vercel
   └─ Headers de sécurité
   └─ Cache headers
   └─ Content-Type pour XML files

✅ netlify.toml
   └─ Configuration optimisée pour Netlify
   └─ Headers de sécurité
   └─ Cache headers
   └─ Content-Security-Policy

✅ .vercelignore
   └─ Fichiers à exclure du build Vercel

✅ .netlifyignore
   └─ Fichiers à exclure du build Netlify
```

Ces fichiers sont déjà configurés! Rien à faire de votre côté.

---

## 💾 PUSH VERS GITHUB (IMPORTANT!)

Avant de déployer, gérez les fichiers de configuration dans Git:

```bash
git add vercel.json netlify.toml .vercelignore .netlifyignore
git commit -m "chore: Add Vercel and Netlify configuration files"
git push origin refactor/centralize-css-inline
```

---

## 🔍 VÉRIFICATION PRÉ-DÉPLOIEMENT

Avant de déployer, vérifiez que tout est correct:

```
✅ Vérifications:
  ☐ index.html existe
  ☐ Tous les fichiers HTML sont présents
  ☐ robots.txt existe
  ☐ sitemap.xml existe
  ☐ Git est synchronisé
  ☐ Pas de fichiers .env locaux
  ☐ Pas d'erreurs console (F12)
```

Tout est bon! ✓

---

## 📱 APRÈS LE DÉPLOIEMENT

### Tester votre site

```
Vercel:
  → https://africa-dev.vercel.app

Netlify:
  → https://africa-dev.netlify.app

Avec votre domaine (une fois DNS propagé):
  → https://africa-dev.com
```

### Points à vérifier

```
✅ Site charge rapidement
✅ Pas d'erreur 404
✅ robots.txt accessible
✅ sitemap.xml accessible
✅ HTTPS avec cadenas ✓
✅ Responsive sur mobile
✅ Pas d'erreur console (F12)
```

---

## ⚠️ TROUBLESHOOTING

### Problème: "Build failed"

```
Solution:
  1. Allez dans "Deployments"
  2. Cliquez "View Logs"
  3. Vérifiez la raison de l'erreur
  4. Généralement: fichier manquant ou erreur de configuration
  5. Corrigez et pushez again
```

### Problème: Domaine ne se connecte pas

```
Solutions:
  1. Attendez la propagation DNS (10 min - 24h)
  2. Videz le cache: Ctrl+Shift+Suppr
  3. Vérifiez que les serveurs DNS ont bien changé
  4. Essayez: https://africa-dev.com (pas http://)
  5. Attendez 30 minutes, puis réessayez
```

### Problème: HTTPS ne fonctionne pas

```
Solutions:
  1. Attendez 5 minutes après le déploiement
  2. Rafraîchissez la page (F5)
  3. Si toujours pas: attendez 30 minutes
  4. Vérifiez dans "SSL" du dashboard
  5. Contact support si problème persiste
```

### Problème: "No such file or directory"

```
Vérifications:
  ☐ Chemin du fichier en minuscules
  ☐ Pas d'espaces dans les noms
  ☐ Fichiers existent dans le repo
  ☐ git push s'est bien fait
```

---

## 📞 SUPPORT

**Vercel Support:** https://vercel.com/support  
**Netlify Support:** https://support.netlify.com  
**Docs:** https://vercel.com/docs / https://docs.netlify.com

---

## ✅ CHECKLIST DE DÉPLOIEMENT

### Avant de commencer:
```
☐ Compte GitHub créé et repo Africa-Dev accessible
☐ Domaine africa-dev.com acheté (ou utiliser .tk gratuit)
☐ Compte registrar créé (GoDaddy, Namecheap, OVH, etc.)
```

### Vercel:
```
☐ Allez sur https://vercel.com/sign-up
☐ Connectez-vous avec GitHub
☐ Importez le repo Africa-Dev
☐ Cliquez "Deploy"
☐ Attendez le déploiement (2-3 min)
☐ Allez à "Domains"
☐ Ajoutez africa-dev.com
☐ Changez les serveurs DNS chez le registrar
☐ Attendez la propagation (10 min - 24h)
☐ Vérifiez: https://africa-dev.com ✓
```

### (Optionnel) Netlify:
```
☐ Allez sur https://netlify.com
☐ "Sign up" avec GitHub
☐ "Add new site" → Import from Git
☐ Sélectionnez Africa-Dev
☐ Laissez les settings par défaut
☐ Cliquez "Deploy"
☐ Attendez le déploiement (1-2 min)
☐ Allez à "Domain management"
☐ Ajoutez africa-dev.com
☐ Changez les serveurs DNS
☐ Attendez la propagation
☐ Vérifiez: https://africa-dev.com ✓
```

---

## 🎉 RÉSUMÉ

**Vous avez tout ce qu'il faut pour déployer!**

Les étapes:
1. Créer compte Vercel/Netlify (5 min)
2. Importer votre repo (1 min)
3. Vercel/Netlify déploie (2-3 min)
4. Acheter domaine si pas encore fait (10 min)
5. Changer serveurs DNS (5 min)
6. Attendre propagation DNS (30 min - 24h)
7. Vérifier: https://africa-dev.com ✓

**Total: ~1 heure (+ attente DNS)**

---

**Prêt à déployer? Allez-y! 🚀**

Des questions? Consultez ce guide ou demandez-moi!
