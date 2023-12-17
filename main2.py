from tabulate import tabulate

def calculer_interets_simples(capital, taux, duree):
    interets = (capital * taux * duree) / 100
    montant_total = capital + interets
    return interets, montant_total

def calculer_interets_composes(capital, taux, duree):
    montant_total = capital * ((1 + (taux / 100)) ** duree)
    interets = montant_total - capital
    return interets, montant_total

def calculer_annuite_emprunt(capital_emprunte, taux, duree):
    taux = taux / 100
    annuite = capital_emprunte * (taux / (1 - (1 + taux) ** (-duree)))
    return annuite

def calculer_annuite_obligation(capital_obligation, taux, duree):
    annuite = capital_obligation * (taux / 100)
    return annuite

def calculer_escompte(capital, taux_escompte, duree, taux_agios, tva):
    escompte = capital * (taux_escompte * duree) / 360
    montant_escompte = capital - escompte

    agios = montant_escompte * (taux_agios / 100)
    montant_agios = montant_escompte + agios

    tva_sur_agios = agios * (tva / 100)
    montant_total = montant_agios + tva_sur_agios

    return escompte, montant_escompte, agios, montant_agios, tva_sur_agios, montant_total

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
        duree = float(input("Entrez la durée en années : "))

        interets, montant_total = calculer_interets_simples(capital, taux, duree)

        data = [["Capital", capital],
                ["Intérêts", interets],
                ["Montant Total", montant_total]]
        headers = ["Détails", "Montant"]

        afficher_tableau(headers, data)

    elif choix == '2':
        capital = float(input("Entrez le montant du bordereau d'escompte : "))
        taux_escompte = float(input("Entrez le taux d'escompte en pourcentage : "))
        duree = float(input("Entrez la durée en jours : "))
        taux_agios = float(input("Entrez le taux d'agios en pourcentage : "))
        tva = float(input("Entrez le taux de TVA en pourcentage : "))

        escompte, montant_escompte, agios, montant_agios, tva_sur_agios, montant_total = calculer_escompte(
            capital, taux_escompte, duree, taux_agios, tva)

        data = [["Escompte", escompte],
                ["Montant après Escompte", montant_escompte],
                ["Agios", agios],
                ["Montant Total avec Agios", montant_agios],
                ["TVA sur les Agios", tva_sur_agios],
                ["Montant Total avec TVA", montant_total]]
        headers = ["Détails", "Montant"]

        afficher_tableau(headers, data)

    elif choix == '3':
        capital_emprunte = float(input("Entrez le montant emprunté : "))
        taux = float(input("Entrez le taux d'intérêt annuel en pourcentage : "))
        duree = int(input("Entrez la durée de l'emprunt en années : "))

        annuite_emprunt = calculer_annuite_emprunt(capital_emprunte, taux, duree)

        data = [["Montant Emprunté", capital_emprunte],
                ["Annuité pour l'emprunt", annuite_emprunt]]
        headers = ["Détails", "Montant"]

        afficher_tableau(headers, data)

    elif choix == '4':
        capital_obligation = float(input("Entrez le montant de l'obligation : "))
        taux = float(input("Entrez le taux d'intérêt annuel en pourcentage : "))
        duree = int(input("Entrez la durée de l'obligation en années : "))

        annuite_obligation = calculer_annuite_obligation(capital_obligation, taux, duree)

        data = [["Montant de l'Obligation", capital_obligation],
                ["Annuité pour l'obligation", annuite_obligation]]
        headers = ["Détails", "Montant"]

        afficher_tableau(headers, data)

    elif choix == '5':
        capital = float(input("Entrez le montant de la facture : "))
        taux_escompte = float(input("Entrez le taux d'escompte en pourcentage : "))
        duree = float(input("Entrez la durée en jours : "))
        taux_agios = float(input("Entrez le taux d'agios en pourcentage : "))
        tva = float(input("Entrez le taux de TVA en pourcentage : "))

        escompte, montant_escompte, agios, montant_agios, tva_sur_agios, montant_total = calculer_escompte(
            capital, taux_escompte, duree, taux_agios, tva)

        data = [["Escompte", escompte],
                ["Montant après Escompte", montant_escompte],
                ["Agios", agios],
                ["Montant Total avec Agios", montant_agios],
                ["TVA sur les Agios", tva_sur_agios],
                ["Montant Total avec TVA", montant_total]]
        headers = ["Détails", "Montant"]

        afficher_tableau(headers, data)

    else:
        print("Choix invalide. Veuillez choisir parmi les options disponibles (1/2/3/4/5).")

if __name__ == "__main__":
    main()
