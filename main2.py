from tabulate import tabulate
from datetime import datetime

# Fonction pour calculer les intérêts simples sur une plage de temps
def calculer_interets_simples(capital, taux, debut_annee, debut_mois, fin_annee, fin_mois):
    data = []
    debut_date = datetime(debut_annee, debut_mois, 1)
    fin_date = datetime(fin_annee, fin_mois, 1)
    while debut_date <= fin_date:
        date_str = debut_date.strftime("%d-%m-%Y")
        interets = (capital * taux * (debut_date.year + debut_date.month / 12)) / 100
        montant_total = capital + interets
        data.append([date_str, interets, montant_total])
        debut_date = debut_date.replace(month=debut_date.month + 1) if debut_date.month < 12 else debut_date.replace(year=debut_date.year + 1, month=1)
    return data

# Fonction pour calculer les intérêts composés sur une plage de temps
def calculer_interets_composes(capital, taux, debut_annee, debut_mois, fin_annee, fin_mois):
    data = []
    debut_date = datetime(debut_annee, debut_mois, 1)
    fin_date = datetime(fin_annee, fin_mois, 1)
    while debut_date <= fin_date:
        date_str = debut_date.strftime("%d-%m-%Y")
        total_mois = debut_date.year + debut_date.month / 12
        montant_total = capital * ((1 + (taux / 100)) ** total_mois)
        interets = montant_total - capital
        data.append([date_str, interets, montant_total])
        debut_date = debut_date.replace(month=debut_date.month + 1) if debut_date.month < 12 else debut_date.replace(year=debut_date.year + 1, month=1)
    return data

# Fonction pour calculer les annuités pour un emprunt sur une plage de temps
def calculer_annuite_emprunt(capital_emprunte, taux, debut_annee, debut_mois, fin_annee, fin_mois):
    data = []
    debut_date = datetime(debut_annee, debut_mois, 1)
    fin_date = datetime(fin_annee, fin_mois, 1)
    while debut_date <= fin_date:
        date_str = debut_date.strftime("%d-%m-%Y")
        duree = (fin_date - debut_date).days / 30  # approximativement en mois
        taux_mensuel = taux / 12 / 100
        annuite = capital_emprunte * (taux_mensuel / (1 - (1 + taux_mensuel) ** (-duree)))
        data.append([date_str, annuite])
        debut_date = debut_date.replace(month=debut_date.month + 1) if debut_date.month < 12 else debut_date.replace(year=debut_date.year + 1, month=1)
    return data

# Fonction pour calculer les annuités pour une obligation sur une plage de temps
def calculer_annuite_obligation(capital_obligation, taux, debut_annee, debut_mois, fin_annee, fin_mois):
    data = []
    debut_date = datetime(debut_annee, debut_mois, 1)
    fin_date = datetime(fin_annee, fin_mois, 1)
    while debut_date <= fin_date:
        date_str = debut_date.strftime("%d-%m-%Y")
        annuite = capital_obligation * (taux / 100)
        data.append([date_str, annuite])
        debut_date = debut_date.replace(month=debut_date.month + 1) if debut_date.month < 12 else debut_date.replace(year=debut_date.year + 1, month=1)
    return data

# Fonction pour calculer les détails d'un escompte sur une plage de temps
def calculer_escompte(capital, taux_escompte, debut_annee, debut_mois, fin_annee, fin_mois, taux_agios, tva):
    data = []
    debut_date = datetime(debut_annee, debut_mois, 1)
    fin_date = datetime(fin_annee, fin_mois, 1)
    while debut_date <= fin_date:
        date_str = debut_date.strftime("%d-%m-%Y")
        escompte = capital * (taux_escompte * (debut_date.year + debut_date.month / 12)) / 360
        montant_escompte = capital - escompte

        agios = montant_escompte * (taux_agios / 100)
        montant_agios = montant_escompte + agios

        tva_sur_agios = agios * (tva / 100)
        montant_total = montant_agios + tva_sur_agios

        data.append([date_str, escompte, montant_escompte, agios, montant_agios, tva_sur_agios, montant_total])
        debut_date = debut_date.replace(month=debut_date.month + 1) if debut_date.month < 12 else debut_date.replace(year=debut_date.year + 1, month=1)
    return data

# Fonction pour sauvegarder les données dans un fichier
def sauvegarder_dans_fichier(nom_fichier, headers, data):
    with open(nom_fichier, 'w') as file:
        file.write(tabulate(data, headers=headers, tablefmt="grid"))

# Fonction pour afficher un tableau
def afficher_tableau(headers, data):
    print(tabulate(data, headers=headers, tablefmt="grid"))

def collecter_date():
    date_str = input("Entrez la date au format JJ-MM-AAAA : ")
    try:
        date = datetime.strptime(date_str, "%d-%m-%Y")
        return date.year, date.month
    except ValueError:
        print("Format de date incorrect. Veuillez saisir la date au format JJ-MM-AAAA.")
        return collecter_date()

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
        # Option 1: Intérêts simples pour un compte d'épargne
        capital = float(input("Entrez le capital initial sur le compte d'épargne : "))
        taux = float(input("Entrez le taux d'intérêt en pourcentage : "))

        print("Saisie de la plage de temps pour le calcul :")
        debut_annee, debut_mois = collecter_date()
        fin_annee, fin_mois = collecter_date()

        data = calculer_interets_simples(capital, taux, debut_annee, debut_mois, fin_annee, fin_mois)
        headers = ["Date", "Intérêts", "Montant Total"]
        afficher_tableau(headers, data)
        sauvegarder_dans_fichier("interets_simples.txt", headers, data)

    elif choix == '2':
        # Option 2: Intérêts composés pour un escompte
        capital = float(input("Entrez le montant du bordereau d'escompte : "))
        taux_escompte = float(input("Entrez le taux d'escompte en pourcentage : "))

        print("Saisie de la plage de temps pour le calcul :")
        debut_annee, debut_mois = collecter_date()
        fin_annee, fin_mois = collecter_date()

        taux_agios = float(input("Entrez le taux d'agios en pourcentage : "))
        tva = float(input("Entrez le taux de TVA en pourcentage : "))

        data = calculer_escompte(capital, taux_escompte, debut_annee, debut_mois, fin_annee, fin_mois, taux_agios, tva)
        headers = ["Date", "Escompte", "Montant après Escompte", "Agios", "Montant Total avec Agios", "TVA sur les Agios", "Montant Total avec TVA"]
        afficher_tableau(headers, data)
        sauvegarder_dans_fichier("bordereau_escompte.txt", headers, data)

    elif choix == '3':
        # Option 3: Annuités pour un emprunt
        capital_emprunte = float(input("Entrez le montant emprunté : "))
        taux = float(input("Entrez le taux d'intérêt annuel en pourcentage : "))

        print("Saisie de la plage de temps pour le calcul :")
        debut_annee, debut_mois = collecter_date()
        fin_annee, fin_mois = collecter_date()

        data = calculer_annuite_emprunt(capital_emprunte, taux, debut_annee, debut_mois, fin_annee, fin_mois)
        headers = ["Date", "Annuité"]
        afficher_tableau(headers, data)
        sauvegarder_dans_fichier("annuite_emprunt.txt", headers, data)

    elif choix == '4':
        # Option 4: Annuités pour une obligation
        capital_obligation = float(input("Entrez le montant de l'obligation : "))
        taux = float(input("Entrez le taux d'intérêt annuel en pourcentage : "))

        print("Saisie de la plage de temps pour le calcul :")
        debut_annee, debut_mois = collecter_date()
        fin_annee, fin_mois = collecter_date()

        data = calculer_annuite_obligation(capital_obligation, taux, debut_annee, debut_mois, fin_annee, fin_mois)
        headers = ["Date", "Annuité"]
        afficher_tableau(headers, data)
        sauvegarder_dans_fichier("annuite_obligation.txt", headers, data)

    elif choix == '5':
        # Option 5: Escompte (bordereau d'escompte)
        capital = float(input("Entrez le montant de la facture : "))
        taux_escompte = float(input("Entrez le taux d'escompte en pourcentage : "))

        print("Saisie de la plage de temps pour le calcul :")
        debut_annee, debut_mois = collecter_date()
        fin_annee, fin_mois = collecter_date()

        taux_agios = float(input("Entrez le taux d'agios en pourcentage : "))
        tva = float(input("Entrez le taux de TVA en pourcentage : "))

        data = calculer_escompte(capital, taux_escompte, debut_annee, debut_mois, fin_annee, fin_mois, taux_agios, tva)
        headers = ["Date", "Escompte", "Montant après Escompte", "Agios", "Montant Total avec Agios", "TVA sur les Agios", "Montant Total avec TVA"]
        afficher_tableau(headers, data)
        sauvegarder_dans_fichier("bordereau_escompte.txt", headers, data)

    else:
        print("Choix invalide. Veuillez choisir parmi les options disponibles (1/2/3/4/5).")

if __name__ == "__main__":
    main()
