import random

class Pendu:
    def __init__(self):
        informatique = ["python", "ordinateur", "programmation", "algorithmique", "intelligence"]
        nature = ["paysage","environnement","arbre","fleur","montagne"]
        self.themes = [informatique,nature,]
        self.mots = random.choice(self.themes)
        self.mot = random.choice(self.mots)
        self.vies = 11
        self.lettres_utilisees = []

    def jouer(self):
        print("Bienvenue au jeu du pendu!")
        while self.vies > 0:
            affichage = ""
            for lettre in self.mot:
                if lettre in self.lettres_utilisees:
                    affichage += lettre
                else:
                    affichage += "_"

            if affichage == self.mot:
                print(f"Félicitations, vous avez trouvé le mot '{self.mot}'!")
                break

            print(f"Mot à deviner: {affichage}")
            print(f"Il vous reste {self.vies} tentatives.")

            lettre_jouee = input("Entrez une lettre: ").lower()

            if lettre_jouee in self.lettres_utilisees:
                print("Vous avez déjà joué cette lettre, veuillez en choisir une autre.")
            elif lettre_jouee in self.mot:
                print("Bravo! Cette lettre est bien dans le mot.")
                self.lettres_utilisees.append(lettre_jouee)
            else:
                print("Cette lettre n'est pas dans le mot.")
                self.vies -= 1
                self.lettres_utilisees.append(lettre_jouee)

        if self.vies == 0:
            print(f"Dommage, vous avez perdu. Le mot était '{self.mot}'.")

if __name__ == '__main__':
    jeu = Pendu()
    jeu.jouer()

