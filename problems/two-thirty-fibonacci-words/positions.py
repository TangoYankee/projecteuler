def find_highest_position(positions):
    """
    positions are presorted to have the highest at the end
    """
    return positions[-1]


def find_positions(to_n):
    """
    collect all of the calculated positions into a list
    """
    positions = []
    for n in range(to_n + 1):
        position = find_position(n)
        positions.append(position)
    print((positions[-1]-positions[-2])/100)
    return positions


def find_position(n):
    """
    generate a position for nth the character
    """
    return (127 + 19 * n) * (7 ** n)
