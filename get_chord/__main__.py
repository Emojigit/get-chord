# (in - 9) % 12
import mido
from . import chord_analyze

if __name__ == "__main__":
    print("Chord Analyzer")
    with mido.open_input() as inport:
        pressed_notes = set()
        last_last_output = ""
        last_output = ""
        try:
            for msg in inport:
                if msg.type == "note_on":
                    pressed_notes.add(msg.note)
                elif msg.type == "note_off":
                    pressed_notes.discard(msg.note)
                else:
                    continue
                output = "N.C."
                if len(pressed_notes) > 1:
                    pressed_notes_mod12 = set(v % 12 for v in pressed_notes)
                    chord = chord_analyze.get_chord(
                        pressed_notes_mod12, min(pressed_notes) % 12)
                    if len(chord) != 0:
                        output = " or ".join(chord)
                if output != last_output:
                    if last_output == "N.C.":
                        print("\033[A\x1b[2K\r", end="")
                        if last_last_output != output:
                            print(output)
                    else:
                        print(output)
                    last_last_output = last_output
                    last_output = output
        except KeyboardInterrupt:
            print()
            import sys
            sys.exit(0)
