from likeprocessing.processing import *
import paho.mqtt.client as mqtt
import random
textAlign("center")
textFont("Comic sans ms", 30)
ihm = IhmScreen()

plateau = [["", "", ""], ["", "", ""], ["", "", ""]]

class MqttGame(mqtt.Client):
    def __init__(self, broker: str, subscribe_name: str, player: str = "joueur", nb_joueurs=2):
        player = "".join([str(randint(0, 9)) for i in range(5)])+ "#" + player
        super().__init__()
        self.subscribe_name = subscribe_name
        self.room_game = ""
        self.nb_joueur = nb_joueurs
        self.all_connected = False
        self.player = player
        self.player_list = []
        self.player_list.append(self.player)
        self.reception = ""
        self.flag_reception = False
        self.connect(broker)
        self.subscribe(subscribe_name)
        self.publish(self.subscribe_name, f"{self.player}:{self.player_list}")
        #self.on_message = self.message


    def on_message(self, client, userdata, message):
        msg = str(message.payload.decode('utf-8'))
        print(msg)
        msg = msg.split(":")
        if msg[0] not in self.player_list:
            self.player_list.append(msg[0])
        if len(msg) == 3 and msg[0] != joueur:
            if msg[2][:9]=="room_game":
                self.room_game = msg[2].split(" ")[1]
                self.subscribe(self.subscribe_name + self.room_game)
                self.all_connected = True
            else:
                self.player_list = eval(f"{msg[1]}")
                self.reception = msg[2]
                self.flag_reception = True
        if self.all_connected is False:
            if len(self.player_list) == self.nb_joueur:
                self.player_list.sort()
                self.room_game = self.player[:self.player.find("#")]
                self.publish(self.subscribe_name, f"{self.player}:{self.player_list}:room_game {self.room_game}")
                self.subscribe(self.subscribe_name+self.room_game)
                self.all_connected = True
        elif self.all_connected is True and len(self.player_list) != self.nb_joueur:
            self.deconnect()
        elif len(self.player_list) != self.nb_joueur:
            self.all_connected = False


    def recept_message(self) -> bool:
        """retourne True si un nouveau message est reçu"""
        if self.flag_reception:
            self.flag_reception = False
            return True
        return False

    def send(self, message: str):
        """envoie un message aux autres joueur
        dont la trame est la suivante:
        nom_joueur:liste_des_joueurs:message"""
        self.publish(self.subscribe_name+self.room_game, f"{self.player}:{self.player_list}:{message}")

    def change_player(self, player:str=""):
        """change le nom du joueur et recalcule son suffixe"""
        if player=="":
            player = self.player[self.player.find("#")+1:]
        self.player="".join([str(randint(0, 9)) for i in range(5)]) + "#" + player

    def deconnect(self):
        """deconnecte le joueur du reseau"""
        self.player_list.remove(self.player)
        self.publish(self.subscribe_name+self.room_game, f"{self.player}:{self.player_list}")
        self.unsubscribe(self.subscribe_name+self.room_game)
        self.room_game =""
        self.all_connected = False

    def in_game_room(self)->bool:
        """retourne True si le joueur est dans la game_room"""
        return not self.room_game ==""

    def room(self)->str:
        return self.subscribe_name+self.room_game

# initialisation de mqtt
joueur = "Matteo"
mqtt_broker = "mqtt.eclipseprojects.io"
jeu = MqttGame(mqtt_broker, "mygamebox", joueur)

def recherche(liste):
    for i in range(3):
        for j in range(3):
            if liste[i][j] == "":
                return True
    return False



def gagne(tour):
    global plateau, gagnant
    for j in range(len(plateau)):
        if plateau[j][0] == tour and plateau[j][1] == tour and plateau[j][2] == tour or plateau[0][j] == tour \
                and plateau[1][j] == tour and plateau[2][j] == tour:
            print(f'{plateau[0]}\n{plateau[1]}\n{plateau[2]}')
            print(f"Le joueur {tour} à gagné")
            gagnant = tour
            return True
    if plateau[0][0] == tour and plateau[1][1] == tour and plateau[2][2] == tour or plateau[2][0] == tour \
            and plateau[1][1] == tour and plateau[0][2] == tour:
        print(f'{plateau[0]}\n{plateau[1]}\n{plateau[2]}')
        print(f"Le joueur {tour} à gagné")
        gagnant = tour
        return True
    return False


def init_jeu():
    global plateau, fini, gagnant
    plateau = [["", "", ""], ["", "", ""], ["", "", ""]]
    ihm.objet_by_name('bouton_recommencer').visible = False
    ihm.objet_by_name('bouton_menu').visible = False
    fini = 0
    gagnant = 0

def morpion(name):
    global plateau, tour
    if fini == 0:
        print(name)
        plateau[name[1]][name[0]] = tour
        gagne(tour)
        tour = tour % 2 + 1
        jeu.send(f"{plateau},{tour}")


taillecase = 100
ihm.addObjet(Bouton(ihm, (0, taillecase*4.5, 150, 50), 'Recommencer', command=init_jeu), 'bouton_recommencer')
ihm.objet_by_name('bouton_recommencer').visible = False
ihm.addObjet(Bouton(ihm, (150, taillecase*4.5, 150, 50), 'Retour au menu', command=init_jeu), 'bouton_menu', )
ihm.objet_by_name('bouton_menu').visible = False
tour = 0
gagnant = 0
fini = 0

def exit():
    jeu.deconnect()
    jeu.loop_stop()

def setup():
    createCanvas(taillecase * 3, taillecase * 5,True)
    background("grey")
    jeu.loop_start()
    title(jeu.player+" "+jeu.room())

def compute():
    global tour,plateau
    title(jeu.player + " " + jeu.room())
    if jeu.all_connected and tour==0:
        tour=1
    if jeu.in_game_room():
        if jeu.recept_message():
            plateau, tour = eval(jeu.reception)
            t = tour
            t -= 1
            if t == 0:
                t = 2
            gagne(t)
    else:
        tour = 0
    ihm.scan_events()


def draw():
    global tour, gagnant, fini
    for i in range(3):
        for j in range(3):
            couleur = None
            if gagnant ==0:
                if tour == 1:
                    couleur = "red"
                    text(f'Au joueur \n{jeu.player_list[0]}\nde jouer.', 0, 300, 300, 2*taillecase,align_v="center")
                elif tour == 2:
                    couleur = "blue"
                    text(f'Au joueur \n{jeu.player_list[1]}\nde jouer.', 0, 300, 300, 2*taillecase,align_v="center")
            if plateau[j][i] == "" and tour>0 and jeu.player == jeu.player_list[tour-1]:
                rect(taillecase * i, taillecase * j, taillecase, taillecase, fill_mouse_on=couleur, command=morpion,
                     name=(i, j))
            elif plateau[j][i] == 1:
                rect(taillecase * i, taillecase * j, taillecase, taillecase, fill="white")
                circle(10 + taillecase * i, 10 + taillecase * j, taillecase - 20, no_fill=True, stroke="red",
                       stroke_weight=5)
            elif plateau[j][i] == 2:
                rect(taillecase * i, taillecase * j, taillecase, taillecase, fill="white")
                strokeWeight(5)
                line(taillecase * i + 10, taillecase * j + 10, taillecase * (i + 1) - 10, taillecase * (j + 1) - 10,
                     stroke="blue")
                line(taillecase * (i + 1) - 10, taillecase * j + 10, taillecase * i + 10, taillecase * (j + 1) - 10,
                     stroke="blue")
                strokeWeight(1)
            else:
                rect(taillecase * i, taillecase * j, taillecase, taillecase, fill="white")
            if gagnant == 1:
                text(f'Le joueur\n{jeu.player_list[0]}\na gagné!', 0, 300, 300, taillecase*1.5,align_v="center")
                fini = 2
            elif gagnant == 2:
                text(f'Le joueur\n{jeu.player_list[1]}\na gagné!', 0, 300, 300, taillecase*1.5,align_v="center")
                fini = 2
            if recherche(plateau) == False and fini!=2:
                text('Match nul', 0, 300, 300, taillecase*1.5,align_v="center")
                fini = 1
            if tour ==0:
                text('En attente\nde connexion', 0, 300, 300, 2*taillecase,align_v="center")
    if fini != 0:
        ihm.objet_by_name('bouton_recommencer').visible = True
        ihm.objet_by_name('bouton_menu').visible = True
    ihm.draw()


run(globals())
