from tabulate import tabulate

# Fonction pour calculer les intérêts simples sur une plage d'années
def calculer_interets_simples(capital, taux, debut_annee, fin_annee):
    data = []
    for annee in range(debut_annee, fin_annee + 1):
        for mois in range(1, 13):
            interets = (capital * taux * (annee + mois / 12)) / 100
            montant_total = capital + interets
            data.append([f"{annee}-{mois:02d}", interets, montant_total])
    return data

# Fonction pour calculer les intérêts composés sur une plage d'années
def calculer_interets_composes(capital, taux, debut_annee, fin_annee):
    data = []
    for annee in range(debut_annee, fin_annee + 1):
        for mois in range(1, 13):
            total_mois = annee + mois / 12
            montant_total = capital * ((1 + (taux / 100)) ** total_mois)
            interets = montant_total - capital
            data.append([f"{annee}-{mois:02d}", interets, montant_total])
    return data

# Fonction pour calculer les annuités pour un emprunt sur une plage d'années
def calculer_annuite_emprunt(capital_emprunte, taux, debut_annee, fin_annee):
    data = []
    for annee in range(debut_annee, fin_annee + 1):
        for mois in range(1, 13):
            duree = (fin_annee - debut_annee) * 12
            taux_mensuel = taux / 12 / 100
            annuite = capital_emprunte * (taux_mensuel / (1 - (1 + taux_mensuel) ** (-duree)))
            data.append([f"{annee}-{mois:02d}", annuite])
    return data

# Fonction pour calculer les annuités pour une obligation sur une plage d'années
def calculer_annuite_obligation(capital_obligation, taux, debut_annee, fin_annee):
    data = []
    for annee in range(debut_annee, fin_annee + 1):
        for mois in range(1, 13):
            annuite = capital_obligation * (taux / 100)
            data.append([f"{annee}-{mois:02d}", annuite])
    return data

# Fonction pour calculer les détails d'un escompte sur une plage d'années
def calculer_escompte(capital, taux_escompte, debut_annee, fin_annee, taux_agios, tva):
    data = []
    for annee in range(debut_annee, fin_annee + 1):
        for mois in range(1, 13):
            escompte = capital * (taux_escompte * (annee + mois / 12)) / 360
            montant_escompte = capital - escompte

            agios = montant_escompte * (taux_agios / 100)
            montant_agios = montant_escompte + agios

            tva_sur_agios = agios * (tva / 100)
            montant_total = montant_agios + tva_sur_agios

            data.append([f"{annee}-{mois:02d}", escompte, montant_escompte, agios, montant_agios, tva_sur_agios, montant_total])
    return data

# Fonction pour sauvegarder les données dans un fichier
def sauvegarder_dans_fichier(nom_fichier, headers, data):
    with open(nom_fichier, 'w') as file:
        file.write(tabulate(data, headers=headers, tablefmt="grid"))

# Fonction pour afficher un tableau
def afficher_tableau(headers, data):
    print(tabulate(data, headers=headers, tablefmt="grid"))

def main():
    print("Bienvenue dans le calculateur financier.")

    choix = input("Que souhaitez-vous calculer ?\n"
                  "1. Intérêts simples pour un compte d'épargne\n"
                  "2. Intérêts composés pour un escompte\n"
                  "3. Annuités pour un emprunt\n"
                  "4. Annuités pour une obligation\n"
                  "5. Escompte (bordereau d'escompte)\n"
                  "Choisissez l'option (1/2/3/4/5) : ")

    if choix == '1':
        capital = float(input("Entrez le capital initial sur le compte d'épargne : "))
        taux = float(input("Entrez le taux d'intérêt en pourcentage : "))
        debut_annee = int(input("Entrez l'année de début : "))
        fin_annee = int(input("Entrez l'année de fin : "))

        data = calculer_interets_simples(capital, taux, debut_annee, fin_annee)
        headers = ["Date", "Intérêts", "Montant Total"]
        afficher_tableau(headers, data)
        sauvegarder_dans_fichier("interets_simples.txt", headers, data)

    elif choix == '2':
        capital = float(input("Entrez le montant du bordereau d'escompte : "))
        taux_escompte = float(input("Entrez le taux d'escompte en pourcentage : "))
        debut_annee = int(input("Entrez l'année de début : "))
        fin_annee = int(input("Entrez l'année de fin : "))
        taux_agios = float(input("Entrez le taux d'agios en pourcentage : "))
        tva = float(input("Entrez le taux de TVA en pourcentage : "))

        data = calculer_escompte(capital, taux_escompte, debut_annee, fin_annee, taux_agios, tva)
        headers = ["Date", "Escompte", "Montant après Escompte", "Agios", "Montant Total avec Agios", "TVA sur les Agios", "Montant Total avec TVA"]
        afficher_tableau(headers, data)
        sauvegarder_dans_fichier("bordereau_escompte.txt", headers, data)

    elif choix == '3':
        capital_emprunte = float(input("Entrez le montant emprunté : "))
        taux = float(input("Entrez le taux d'intérêt annuel en pourcentage : "))
        debut_annee = int(input("Entrez l'année de début : "))
        fin_annee = int(input("Entrez l'année de fin : "))

        data = calculer_annuite_emprunt(capital_emprunte, taux, debut_annee, fin_annee)
        headers = ["Date", "Annuité"]
        afficher_tableau(headers, data)
        sauvegarder_dans_fichier("annuite_emprunt.txt", headers, data)

    elif choix == '4':
        capital_obligation = float(input("Entrez le montant de l'obligation : "))
        taux = float(input("Entrez le taux d'intérêt annuel en pourcentage : "))
        debut_annee = int(input("Entrez l'année de début : "))
        fin_annee = int(input("Entrez l'année de fin : "))

        data = calculer_annuite_obligation(capital_obligation, taux, debut_annee, fin_annee)
        headers = ["Date", "Annuité"]
        afficher_tableau(headers, data)
        sauvegarder_dans_fichier("annuite_obligation.txt", headers, data)

    elif choix == '5':
        capital = float(input("Entrez le montant de la facture : "))
        taux_escompte = float(input("Entrez le taux d'escompte en pourcentage : "))
        debut_annee = int(input("Entrez l'année de début : "))
        fin_annee = int(input("Entrez l'année de fin : "))
        taux_agios = float(input("Entrez le taux d'agios en pourcentage : "))
        tva = float(input("Entrez le taux de TVA en pourcentage : "))

        data = calculer_escompte(capital, taux_escompte, debut_annee, fin_annee, taux_agios, tva)
        headers = ["Date", "Escompte", "Montant après Escompte", "Agios", "Montant Total avec Agios", "TVA sur les Agios", "Montant Total avec TVA"]
        afficher_tableau(headers, data)
        sauvegarder_dans_fichier("bordereau_escompte.txt", headers, data)

    else:
        print("Choix invalide. Veuillez choisir parmi les options disponibles (1/2/3/4/5).")

if __name__ == "__main__":
    main()
