from random import randint
from re import match

def choose_name() -> str:
    """
    
    Choisit le Nom du joueur
    """
    #Beug
    player_name = input("Quelle est ton nom ?\n")
    print(f"Bonjour {player_name} et bonne chance !")
    return player_name


def choose_action() -> str:
    """
    
    Choisi L'action du Joueur
    """
    player_action = input("\nPierre, Papier ou Ciseau ?\n")
    if player_action.lower() == "pierre" or "papier" or "ciseau":
        return player_action.capitalize()
    choose_action()


def action_bot() -> str:
    """
    
    Choisi L'action du robot
    """
    rdm_int = randint(1, 3)
    action_bot = ""
    if rdm_int == 1:
        action_bot = "Pierre"
    if rdm_int == 2:
        action_bot = "Papier"
    if rdm_int == 3:
        action_bot = "Ciseau"
    print(f"L'enemy as fais {action_bot}")
    return action_bot



def verif_winner(player_move, bot_moove) -> str:
    """
    
    Verifie qui a gagné le round
    """
    if player_move == bot_moove:
        return "Egalité !!"

    WIN = "You Win !!"
    LOOSE = "You Loose !!"
    match player_move:
        case "Pierre":
            if bot_moove == "Papier":
                return LOOSE
            return WIN

        case "Papier":
            if bot_moove == "Ciseau":
                return LOOSE
            return WIN

        case "Ciseau":
            if bot_moove == "Pierre":
                return LOOSE
            return WIN


if __name__ == '__main__':
    choose_name()
    while True:
        print(verif_winner(choose_action(), action_bot()))
