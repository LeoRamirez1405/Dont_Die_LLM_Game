def fc_valid_action(possible:bool, survives:bool) -> bool:
    """
    Dada la situación y la respuesta del jugador, se evalua si la acción es posible y si sobrevive.
    """
    if possible == 1 and survives == 1:
        return True
    else:
        return False