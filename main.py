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

def calculer_escompte(capital, taux, duree):
    escompte = capital * (taux * duree) / 360
    montant_escompte = capital - escompte
    return escompte, montant_escompte

def main():
    print("Bienvenue dans l'outil financier interactif.")

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

        print(f"Les intérêts simples pour une durée de {duree} années sont de : {interets} euros.")
        print(f"Le montant total sur le compte après {duree} années sera de : {montant_total} euros.")

    elif choix == '2':
        capital = float(input("Entrez le montant du bordereau d'escompte : "))
        taux = float(input("Entrez le taux d'escompte en pourcentage : "))
        duree = float(input("Entrez la durée en jours : "))

        interets, montant_total = calculer_interets_composes(capital, taux, duree)

        print(f"Les intérêts composés pour une durée de {duree} jours sont de : {interets} euros.")
        print(f"Le montant à rembourser après escompte sera de : {montant_total} euros.")

    elif choix == '3':
        capital_emprunte = float(input("Entrez le montant emprunté : "))
        taux = float(input("Entrez le taux d'intérêt annuel en pourcentage : "))
        duree = int(input("Entrez la durée de l'emprunt en années : "))

        annuite_emprunt = calculer_annuite_emprunt(capital_emprunte, taux, duree)

        print(f"Les annuités pour un emprunt de {capital_emprunte} euros sur {duree} années seront de : {annuite_emprunt} euros par an.")

    elif choix == '4':
        capital_obligation = float(input("Entrez le montant de l'obligation : "))
        taux = float(input("Entrez le taux d'intérêt annuel en pourcentage : "))
        duree = int(input("Entrez la durée de l'obligation en années : "))

        annuite_obligation = calculer_annuite_obligation(capital_obligation, taux, duree)

        print(f"Les intérêts annuels pour une obligation de {capital_obligation} euros sur {duree} années seront de : {annuite_obligation} euros par an.")

    elif choix == '5':
        capital = float(input("Entrez le montant de la facture : "))
        taux = float(input("Entrez le taux d'escompte en pourcentage : "))
        duree = float(input("Entrez la durée en jours : "))

        escompte, montant_escompte = calculer_escompte(capital, taux, duree)

        print(f"L'escompte pour une durée de {duree} jours est de : {escompte} euros.")
        print(f"Le montant à payer après escompte sera de : {montant_escompte} euros.")

    else:
        print("Choix invalide. Veuillez choisir parmi les options disponibles (1/2/3/4/5).")

if __name__ == "__main__":
    main()

