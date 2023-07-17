from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.audioservice import AudioService
from mycroft.audio import wait_while_speaking


class NieuwsAfspelen(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.audio_service = AudioService(self.bus)

    @intent_file_handler('nieuws_afspelen.intent')
    def handle_afspelen(self, message):
        self.speak_dialog('nieuws_afspelen')
        wait_while_speaking()
        self.audio_service.play('https://cdn.nos.nl/content/radio/ditisdenieuweurlvoorhetradiobulletinvoorgooglevanafjuli2019.mp3')

def create_skill():
    return NieuwsAfspelen()

