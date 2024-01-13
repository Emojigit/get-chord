root_notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B",]


def all_mod_12(*t):
    l = [i % 12 for i in t]
    l.sort()
    return tuple(l)


chords = {
    # augmented
    "aug": tuple(all_mod_12(i + 0, i + 4, i + 8) for i in range(0, 12)),
    # major
    "": tuple(all_mod_12(i + 0, i + 4, i + 7) for i in range(0, 12)),
    # minor
    "m": tuple(all_mod_12(i + 0, i + 3, i + 7) for i in range(0, 12)),
    # diminshed
    "dim": tuple(all_mod_12(i + 0, i + 3, i + 6) for i in range(0, 12)),
    # five
    "5": tuple(all_mod_12(i + 0, i + 7) for i in range(0, 12)),
    # sus2
    "sus2": tuple(all_mod_12(i + 0, i + 2, i + 7) for i in range(0, 12)),
    # sus4
    "sus4": tuple(all_mod_12(i + 0, i + 5, i + 7) for i in range(0, 12)),
    # dominant seven
    "7": tuple(all_mod_12(i + 0, i + 4, i + 7, i + 10) for i in range(0, 12)),
    # major seven
    "maj7": tuple(all_mod_12(i + 0, i + 4, i + 7, i + 11) for i in range(0, 12)),
    # minor seven
    "min7": tuple(all_mod_12(i + 0, i + 3, i + 7, i + 10) for i in range(0, 12)),
    # minor major seven
    "min(maj7)": tuple(all_mod_12(i + 0, i + 3, i + 7, i + 11) for i in range(0, 12)),
    # diminshed seven
    "dim7": tuple(all_mod_12(i + 0, i + 3, i + 6, i + 9) for i in range(0, 12)),
    # half diminshed seven
    "m7b5": tuple(all_mod_12(i + 0, i + 3, i + 6, i + 10) for i in range(0, 12)),
    # add9
    "add9": tuple(all_mod_12(i + 0, i + 4, i + 7, i + 14) for i in range(0, 12)),
    # 9 or C7 add 9
    "9": tuple(all_mod_12(i + 0, i + 4, i + 7, i + 10, i + 14) for i in range(0, 12)),
    # major 9
    "maj9": tuple(all_mod_12(i + 0, i + 4, i + 7, i + 11, i + 14) for i in range(0, 12)),
    # add 11
    "add11": tuple(all_mod_12(i + 0, i + 4, i + 7, i + 17) for i in range(0, 12)),
    # 11
    "11": tuple(all_mod_12(i + 0, i + 4, i + 7, i + 10, i + 14, i + 17) for i in range(0, 12)),
    # 13
    "13": tuple(all_mod_12(i + 0, i + 4, i + 7, i + 10, i + 14, i + 17, i + 21) for i in range(0, 12)),
    # 6 or add6
    "6": tuple(all_mod_12(i + 0, i + 4, i + 7, i + 9) for i in range(0, 12)),
    # minor 6 (add 6 of the MAJOR scale)
    "m6": tuple(all_mod_12(i + 0, i + 3, i + 7, i + 9) for i in range(0, 12)),
    # minor flat 6
    "m(b6)": tuple(all_mod_12(i + 0, i + 3, i + 7, i + 8) for i in range(0, 12)),
    # 69 (add 6 add 9)
    "69": tuple(all_mod_12(i + 0, i + 4, i + 7, i + 9, i + 14) for i in range(0, 12)),
}


def get_chord(notes, lowest=None):
    notes = all_mod_12(*notes)
    chord_names = []
    for k, v in chords.items():
        for i, c in enumerate(v):
            if c == notes:
                chord_name = root_notes[i] + k
                if lowest != None:
                    if lowest != i:
                        chord_name += "/" + root_notes[lowest]
                chord_names.append(chord_name)
    return chord_names
