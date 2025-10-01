# **Numworks Enchantements**  
Collection de scripts Python  
Développé en Python révision 3.12.8  
Distribué au format script Python  
**Version 2025 – Service Pack 1**  

*Robert Henning – sous licence MIT*  

---

## Descriptif  

Il s’agit d’une collection de scripts Python destinée à faciliter et automatiser les tâches de calcul sur la NumWorks.  

### Spécifications  

- **Langue** : Français  
- **Base** : *tout*  
- **Interface** : Terminal (CLI)  
- **Format** : Script Python  
- **Licence** : MIT  

### Support  

| **Version**       | **Fonction principale** | **État**     | **Fin de support** | **Date de sortie** |
|:-----------------:|:-----------------------:|:------------:|:------------------:|:------------------:|
| Service Pack 1    | Lancement initial       | Maintenue    | 24/09/2025         | *Inconnue*         |

---

## Documentation  

Étant donné qu’il s’agit d’une collection, il n’est nullement requis de télécharger l’ensemble des scripts ; prenez seulement ceux qui vous sont utiles.  

### Sommaire des scripts  

| **Nom** | **Fonction**                              |
|:-------:|:------------------------------------------|
| `rad`  | Convertit des degrés en radians & vis versa | 
| `mpr`  | Détermine la mesure primitive d'un radiants |  

#### Formatage de menu  

Présente la structure d’un menu dans lequel vous devez sélectionner le mode au moyen d’options numérotées.  

### Sommaire des librairies  

Du fait que la NumWorks ne possède pas de variables d’environnement, il faut donc intégrer manuellement les librairies dans le script.  

| **Nom** | **Fonction**                              |
|:-------:|:------------------------------------------|
| `Frac`  | Forme fractionnaire sur un entier avec une logique binaire | 

#### Fonctionnements des rationnels (Frac.py)


Cette bibliothèque permet de convertir **deux entiers relatifs** (un numérateur et un dénominateur) en un **unique entier**. L’entier résultant est qualifié de **pack** ou d’**agglomération**.  

La logique adoptée est purement binaire : on réserve un mot de **64 bits**, découpé en deux sous-parties de 32 bits chacune.  
- La **partie haute** (bits 63→32) encode le **numérateur**.  
- La **partie basse** (bits 31→0) encode le **dénominateur**.  

> *Exemple simplifié sur 8 bits* :  
> `0bNNNN.DDDD`  
> où `N` désigne les bits du numérateur et `D` ceux du dénominateur.  

La césure est fixée par la constante `SHIFT` (ici 32). Le `MASK`, défini par `(1 << SHIFT) - 1`, permet d’extraire la partie basse.  

Pourquoi ce fonctionnement ?  
Parce que les opérations sur fractions exigent souvent une manipulation directe des numérateurs et dénominateurs. Les implémentations orientées objets sont coûteuses, et un simple tuple occupe deux emplacements mémoire. L’encodage binaire réduit ce coût : un seul entier, manipulé par décalages et opérations logiques, donc **rapide** et **léger en cycles CPU**.

##### Fonction `pack(num, den)`  

Transforme deux entiers en un entier unique.  
- Le numérateur est décalé : `num << SHIFT`.  
- Le dénominateur est masqué et fusionné par OR binaire : `(den & MASK)`.  

Formule : `(num << SHIFT) | (den & MASK)`  

##### Fonction `unpack(packed)`  

Inverse de `pack`.  
- Extraction du numérateur : `packed >> SHIFT`.  
- Extraction du dénominateur : `packed & MASK`.  

##### Point crucial  

**Si l’on veut isoler `X`, il faut éliminer `Y`.**  
D’où l’usage systématique du **décalage** ou du **masquage**, suivant la composante visée.

---

## Dépendances  

Cette section présente l’ensemble des exigences techniques, logicielles et matérielles nécessaires pour l’utilisation et le développement du système logiciel fourni.  

### I. Connaissances requises

| **Compétence**              | **Niveau minimal**       | **Niveau recommandé**                   |
|:---------------------------:|:-------------------------:|:----------------------------------------:|
| Langue de travail           | Français                  | Français & Anglais                      |
| Langage de programmation    | Python (notions)          | Documentation NumWorks & Python (avancé) |

### II. Outils logiciels

| **Composant**      | **Option minimale** | **Option recommandée**     |
|:------------------:|:-------------------:|:---------------------------:|
| Éditeur de code    | QBASIC              | Visual Studio Code          |