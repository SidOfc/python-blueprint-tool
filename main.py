#pip install kivy screeninfo pygame

import zlib
import base64
import json
from screeninfo import get_monitors

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.config import Config

first_monitor = get_monitors()[0]

Config.set('graphics', 'width', first_monitor.width)
Config.set('graphics', 'height', first_monitor.height)
Config.write()

# blueprintStr = input('Paste blueprint:\n')
blueprintStr = '0eNqdWNtu4yAQ/ReebckYfIl/paoq4pAsksEWxlWzUf99Saw225a4M/Nk+cI5h8Mww/jC9sOiJ29cYN2FmX50M+ueLmw2J6eG67NwnjTrmAnasow5Za93ap613Q/GnXKr+j/G6Zyz94wZd9BvrOPvzxnTLphg9Ip3uzm/uMXutY8fbCNlbBrnOHh0VwURMK8zdo4XETm87s1N0tF4rbyN407qbxwYBfwgKrFEgkgkkEQFkUcieajzqZA81AWqP3mOag65cbP2Ib74uTLVysAjwyEC9+s7mcBsPjE34OoPuARACxYlwaJ2EFHlhiheQFUVYFGcA1TxLVElVJSAixIAUZtOSaioBi6qAojaiil+j/TglZun0Yd8r4eQCINVVvFVVZ0CbZDbJy2thW8YiFW7r6KWWBT8yY/x+mjCdXLC2UfxGZcwLSGZ3++bAkBTbdMY94iFIxNC0ubyvlesPpjF5nqIIrzp82kc9MNilAYTaJMFdfYS47EkL2UFz5CAKCxrtEElWXqDcYhT16HFFYB03OzAGR9gsiiwJlMnLzjC4oK6kAJZzpIWC3j9glgssRaTw1hUCI+p2UTUyCy4kVFFg/WGWgFEi7CGnALFDndwSZoiC/BJBRB+8lvp++3sUkOPLrJEONoQl00KWqOJb8skrdHEE1WkRhPPU5MaTTxPQ2o0f+F5ztYfFt1//zcyNqgYXVcia8f8qPow+nN8/Kr9fMNvRMFbzmVRxY31DzMIs1E='

zippedBp = base64.b64decode(blueprintStr[1:])
inflated = zlib.decompress(zippedBp)
blueprint = json.loads(inflated)
blueprint = blueprint['blueprint']['entities']
# print(blueprint)

class Application(App):
    def build(self):
        xSize = 21
        ySize = 21
        defaultSize = 48
        xCenter = (xSize - 1) / 2
        yCenter = (ySize - 1) / 2

        layout = GridLayout(
                cols = xSize,
                rows = ySize,
                row_force_default = True,
                row_default_height = defaultSize,
                col_force_default = True,
                col_default_width = defaultSize
        )

        for y in range(ySize):
            for x in range(xSize):
                currentCoordinations = [int(x - xCenter), int(y - yCenter)]
                backgroundColor = (1, 1, 1, 1)

                if currentCoordinations[0] == 0 or currentCoordinations[1] == 0:
                    backgroundColor = (1, 1, 1, 0.8)

                for entity in blueprint:
                    if entity['position']['x'] == currentCoordinations[0] and entity['position']['y'] == currentCoordinations[1]:
                        backgroundColor = (1, 0, 0, 1)


                layout.add_widget(Button(
                    text = ', '.join(list(map(str, currentCoordinations))),
                    background_color = backgroundColor)
                )
        return layout

if __name__ == '__main__':
    Application().run();
