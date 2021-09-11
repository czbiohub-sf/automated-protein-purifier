import logging
from czpurifier.ui import UICommands


logging.getLogger().setLevel(logging.INFO)
ui = UICommands()
ui.connect('1mL','pure1.local',4)
