define fart_randomness = 4
define farts = [
    "cum/fart-with-extra-reverb.mp3",
    "cum/vine-boom.mp3"
]

python early hide:
    from functools import partial
    import random

    random.seed()

    class PlayDecorator(object):
        def __init__(self, func):
            self.func = func

        def randomize(self, file):
            fart_randomness = getattr(store, "fart_randomness", 4)
            farts = getattr(store, "farts", [ ])

            if farts and random.randint(0, fart_randomness) == 0:
                return random.choice(farts)

            return file

        def __call__(self, filenames, channel="music", *args, **kwargs):
            if not isinstance(filenames, list):
                filenames = [ filenames ]

            if channel != "music":
                filenames = map(self.randomize, filenames)

            return self.func(list(filenames), channel, *args, **kwargs)

    renpy.music.play = PlayDecorator(renpy.music.play)