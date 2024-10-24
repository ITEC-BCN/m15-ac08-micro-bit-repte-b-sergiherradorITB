def on_button_pressed_a():
    # Obtener la inclinación y ajustar el tempo
    inclinacion = input.rotation(Rotation.PITCH)
    tempo = 120 + (inclinacion // 2)
    music.set_tempo(tempo)
    music.play(music.string_playable("G F G A - F E D ", tempo), music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    music.play(music.string_playable("G F G A - F E D ", 400), music.PlaybackMode.UNTIL_DONE)
    music.set_tempo(61)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    music.play(music.string_playable("A B A B A B A B ", 120), music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
