"""Kleine MIDI-Toolbox"""

if __name__ == '__main__':
    # Vorschlag 1        # Akkord
    my_pitches = [60, 62, [64, 59, 53], 65, 67, 67]
    my_durations = [1/4, 1/4, 1/4, 1/4, 1/2, 1/2]

    # Vorschlag 2
    my_sequence = [{'p': 60, 'd': 1/4},
                   {'p': 62, 'd': 1/4},
                   {'p': [64, 59, 53], 'd': 1/4}, # Akkord
                   {'p': 65, 'd': 1/4},
                   {'p': 67, 'd': 1/4},
                   {'p': 67, 'd': 1/4}]


def create_midinote(pitch: int, duration: float) -> dict:
    """Erstellt ein Dictionary, das eine MIDI-Noten-Tonhöhe und -Dauer enthält.

    Parameters:
    pitch (int): Die MIDI-Tonhöhe der Noten. Dies kann ein einzelner Ton oder ein Akkord sein.
                 Für einen Akkord wird eine Liste von Tönen verwendet.
    duration (float): Die Dauer der Noten in Beats. Ein Viertelton hat eine Dauer von 0.25, etc.

    Returns:
    dict: Ein Dictionary mit den Schlüsseln 'p' (Pitch) und 'd' (Duration), die die
          MIDI-Noten-Tonhöhe und -Dauer enthalten.
    """
    return {'p': pitch, 'd': duration}


if __name__ == '__main__':
    print('------------------------\nMidinote als Dictionary')
    print(create_midinote(60, 1/4))


def create_midinote_sequence(pitches: list[int], durations: list[float]) -> list[dict[int, float]]:
    """Gibt eine Liste an MIDI-Noten als Dictionaries (wie in `create_midnote`) zurück.

    Parameters:
    pitches (list): Eine Liste von MIDI-Tonhöhen, die jeweils einzelne Töne oder Akkorde sein
                    können.
                    Für einen Akkord wird eine Liste von Tönen verwendet.
    durations (list): Eine Liste von Dauern für die jeweiligen Töne in Beats.
                      Ein Viertelton hat eine Dauer von 0.25, etc.

    Returns:
    list: Eine Liste von Dictionaries, wobei jedes Dictionary die Schlüssel 'p' (Pitch) und
          'd' (Duration) enthält, die die MIDI-Noten-Tonhöhe und -Dauer repräsentieren.
    """
    midinote_sequence = []

    for pitch, duration in zip(pitches, durations):

        midinote = create_midinote(pitch=pitch, duration=duration)
        midinote_sequence.append(midinote)

    return midinote_sequence


if __name__ == '__main__':
    print('------------------------\nMidinoten-Sequenz')
    print(create_midinote_sequence(my_pitches, my_durations))


def pitches_and_durations_from_sequence(sequence: list[dict[int, float]]) \
        -> tuple[list[int], list[float]]:
    """Extrahiert Tonhöhen und Tondauern aus einer MIDI-Sequenz und gibt sie als separate Listen
    zurück.

    Parameters:
    sequence (list): Eine Liste von MIDI-Noten, wobei jede Note ein Dictionary mit den Schlüsseln
                     'p' (Pitch) und 'd' (Duration) ist.

    Returns:
    tuple: Ein Tupel mit zwei Listen. Die erste Liste enthält die Tonhöhen aller Noten,
           während die zweite Liste die Dauern aller Noten enthält.
    """
    pitches, durations = [], []

    for midinote in sequence:
        pitches.append(midinote['p'])
        durations.append(midinote['d'])

    return pitches, durations


if __name__ == '__main__':
    print('------------------------\nListen aus Sequenz')
    new_pitches, new_durations = pitches_and_durations_from_sequence(my_sequence)
    print(f'{new_pitches}\n{new_durations}')
