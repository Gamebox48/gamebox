import paho.mqtt.client as mqtt
from random import randint
from time import time


class MqttGame(mqtt.Client):
    def __init__(self, broker: str, subscribe_name: str, player: str = "joueur", nb_joueurs_maxi=2,
                 nb_joueurs_mini=None):
        player = "".join([str(randint(0, 9)) for i in range(5)]) + "#" + player
        super().__init__()
        self.subscribe_name = subscribe_name
        self.room_game = ""
        self.nb_joueur_maxi = nb_joueurs_maxi
        self.nb_joueur_mini = nb_joueurs_mini
        if nb_joueurs_mini is None:
            self.nb_joueur_mini = nb_joueurs_maxi
        self.all_connected = False
        self.player = player
        self.player_list = []
        self.player_list.append(self.player)
        self._reception = ""
        self.envoyeur = ""
        self._go = False
        self.flag_reception = False
        self.connect(broker)
        self.subscribe(subscribe_name)
        self.publish(self.subscribe_name, f"{self.player}:connecter")
        self.start_time = time()
        self.start_game = False
        self.master = True
        self.hand = 0

    @property
    def nb_joueurs(self):
        return len(self.player_list)

    @property
    def reception(self):
        return self._reception

    @reception.setter
    def reception(self, value):
        self._reception = value
        self.flag_reception = True

    def on_message(self, client, userdata, message):
        msg = str(message.payload.decode('utf-8'))
        msg = msg.split(":")
        print(msg)
        if msg[0] != self.player:
            if len(msg) >= 2:
                if msg[1] == "room_game":
                    if self.room_game == "":
                        for j in eval(msg[-1]):
                            self.add_player(j, self.nb_joueur_maxi)
                        self.player_list.sort()
                        self.nb_joueur_maxi = len(self.player_list)
                        self.room_game = msg[2]
                        self.subscribe(self.subscribe_name + self.room_game)
                        self.unsubscribe(self.subscribe_name)
                        self.hand = 0
                        self.all_connected = True
                elif msg[1] == "connecter":
                    if self.add_player(msg[0], self.nb_joueur_maxi):
                        if self.all_connected is False:
                            self.start_room_game()
                        self.publish(self.subscribe_name, f"{self.player}:connecter")
                        if time() - self.start_time < 1:
                            self.master = False

                elif msg[1] == "deconnecter":
                    self.del_player(msg[0])
                    if len(self.player_list) < self.nb_joueur_mini:
                        self.deconnect()
                    if eval(msg[2]) and self.player == self.player_list[0]:
                        self.master = True
                elif msg[1] == "datas":
                    self.reception = msg[2]
                    self.envoyeur = msg[0]
                elif msg[1] == "hand":
                    self.hand = int(msg[2])
                elif msg[0] == "all":
                    if msg[1] == "go":
                        self._go = True


    def start_room_game(self):
        if len(self.player_list) == self.nb_joueur_maxi or (self.start_game and self.room_game == ""):
            self.player_list.sort()
            if self.master or self.start_game:
                self.nb_joueur_maxi = len(self.player_list)
                self.nb_joueur_mini = min(self.nb_joueur_mini, self.nb_joueur_maxi)
                self.room_game = self.player[:self.player.find("#")]
                self.publish(self.subscribe_name, f"{self.player}:room_game:{self.room_game}:{self.player_list}")
                self.subscribe(self.subscribe_name + self.room_game)
                self.unsubscribe(self.subscribe_name)
                self.all_connected = True
                self.hand = 0
                self.start_game = False

    def add_player(self, player, maxi):
        """ajoute un joueur de la liste des joueurs et retourne True s'il a pu être
        ajouté et false dans le cas contraire"""
        if len(self.player_list) < maxi and player not in self.player_list:
            self.player_list.append(player)
            return True
        return False

    def del_player(self, player):
        """supprime un joueur de la liste des joueurs"""
        if player in self.player_list:
            self.player_list.remove(player)

    def recept_message(self) -> bool:
        """retourne True si un nouveau message est reçu"""
        if self.flag_reception:
            self.flag_reception = False
            return True
        return False

    def send(self, message: str):
        """envoie un message aux autres joueur
        dont la trame est la suivante:
        nom_joueur:message"""
        self.publish(self.subscribe_name + self.room_game, f"{self.player}:datas:{message}")

    def send_all(self, message: str):
        """envoie un message à tous les joueur y compris l'envoyeur
        dont la trame est la suivante:
        nom_joueur:message"""
        self.publish(self.subscribe_name + self.room_game, f"{self.player}:datas:{message}")

    def change_player(self, player: str = ""):
        """change le nom du joueur et recalcule son suffixe"""
        if player == "":
            player = self.player[self.player.find("#") + 1:]
        self.player = "".join([str(randint(0, 9)) for i in range(5)]) + "#" + player

    def deconnect(self):
        """deconnecte le joueur du reseau"""
        self.publish(self.subscribe_name + self.room_game, f"{self.player}:deconnecter:{self.master}")
        if self.hand_is_me():
            self.del_player(self.player)
            if self.nb_joueurs>0:
                self.to_hand_over(0)
        else:
            self.del_player(self.player)
        self.player_list = [self.player]
        self.unsubscribe(self.subscribe_name + self.room_game)
        self.room_game = ""
        self.subscribe(self.subscribe_name)
        self.all_connected = False

    def in_game_room(self) -> bool:
        """retourne True si le joueur est dans la game_room"""
        return not self.room_game == ""

    def room(self) -> str:
        """retourne nom de la room_game"""
        return self.subscribe_name + self.room_game

    def to_hand_over(self, step=1):
        """passe la main au joueur suivant"""
        self.hand = (self.hand + step) % self.nb_joueurs
        if self.hand == self.nb_joueurs:
            self.hand = 0
        self.publish(self.subscribe_name + self.room_game,
                     f"{self.player}:hand:{self.hand}")

    def hand_is_me(self):
        """retourne True si le joueur à la main"""
        try:
            return self.player_list[self.hand] == self.player
        except:
            return False

    def courant_player(self):
        """retourne le nom du joueur courant"""
        try :
            return self.player_list[self.hand]
        except:
            return ""

    def is_go(self):
        """retourn True si go est reçu"""
        g = self._go
        self._go = False
        return g

    def go(self):
        """lance un top départ à l'ensemble des joueurs"""
        self.publish(self.subscribe_name + self.room_game, f"all:go:{self.player}")

    def __str__(self):
        return f"""        subscribe_name: {self.subscribe_name}
        room_game: {self.room_game}
        player: {self.player}
        player_list: {self.player_list}
        nb joueurs maxi: {self.nb_joueur_maxi} nb joueurs mini: {self.nb_joueur_mini} 
        reception: {self.reception}
        master: {self.master}
        hand: {self.hand}"""
