from ovos_workshop.skills import OVOSSkill
from ovos_workshop.decorators import intent_handler
from ovos_audio.utils import wait_while_speaking
from ovos_plugin_common_play.ocp.mycroft_cps import MycroftAudioService

class NieuwsAfspelen(OVOSSkill):

    def __init__(self):
        super().__init__(name="Nieuws NOS")
        self.url = "https://cdn.nos.nl/content/radio/ditisdenieuweurlvoorhetradiobulletinvoorgooglevanafjuli2019.mp3"

    def initialize(self):
        self.audio_service = MycroftAudioService(self.bus)

    @intent_handler('nieuws_afspelen.intent')
    
    def play(self, message):
        self.log.info("Hier is het NOS nieuws")
        self.speak_dialog('nieuws_afspelen')
        wait_while_speaking()
        self.audio_service.play(self.url)

    def stop(self):
        self.audio_service.stop()
