root_notes = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")


class modSet(set):
    def __init__(self, iterable=None):
        if iterable is None:
            super().__init__()
        else:
            super().__init__(i % 12 for i in iterable)

    def __add__(self, b):
        return modSet((i + b) % 12 for i in self)


chords = {
    # augmented
    "aug": modSet((0, 4, 8)),
    # major
    "": modSet((0, 4, 7)),
    # minor
    "m": modSet((0, 3, 7)),
    # diminshed
    "dim": modSet((0, 3, 6)),
    # five
    "5": modSet((0, 7)),
    # sus2
    "sus2": modSet((0, 2, 7)),
    # sus4
    "sus4": modSet((0, 5, 7)),
    # dominant seven
    "7": modSet((0, 4, 7, 10)),
    # major seven
    "maj7": modSet((0, 4, 7, 11)),
    # minor seven
    "min7": modSet((0, 3, 7, 10)),
    # major seven sus 2
    "maj7sus2": modSet((0, 2, 7, 11)),
    # major seven sus 4
    "maj7sus4": modSet((0, 5, 7, 11)),
    # dominant seven sus 2
    "7sus2": modSet((0, 2, 7, 10)),
    # dominant seven sus 4
    "7sus4": modSet((0, 5, 7, 10)),
    # minor major seven
    "min(maj7)": modSet((0, 3, 7, 11)),
    # diminshed seven
    "dim7": modSet((0, 3, 6, 9)),
    # half diminshed seven
    "m7b5": modSet((0, 3, 6, 10)),
    # add9
    "add9": modSet((0, 4, 7, 14)),
    # 9 or C7 add 9
    "9": modSet((0, 4, 7, 10, 14)),
    # major 9
    "maj9": modSet((0, 4, 7, 11, 14)),
    # minor 9
    "min9": modSet((0, 3, 7, 10, 14)),
    # add 11
    "add11": modSet((0, 4, 7, 17)),
    # 11
    "11": modSet((0, 4, 7, 10, 14, 17)),
    # 13
    "13": modSet((0, 4, 7, 10, 14, 17, 21)),
    # 6 or add6
    "6": modSet((0, 4, 7, 9)),
    # minor 6 (add 6 of the MAJOR scale)
    "m6": modSet((0, 3, 7, 9)),
    # minor flat 6
    "m(b6)": modSet((0, 3, 7, 8)),
    # 69 (add 6 add 9)
    "69": modSet((0, 4, 7, 9, 14)),
}


def get_chord(notes, lowest=None):
    chord_names = []
    for k, v in chords.items():
        for i in range(0, 12):
            if notes == (v + i):
                chord_name = root_notes[i] + k
                if lowest is not None and lowest != i:
                    chord_name += "/" + root_notes[lowest]
                chord_names.append(chord_name)
    return chord_names
