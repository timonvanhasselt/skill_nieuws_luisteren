from ovos_workshop.skills import OVOSSkill
from ovos_workshop.decorators import intent_handler
from ovos_audio.utils import wait_while_speaking
from ovos_utils.messagebus import Message
from ovos_utils.skills.audioservice import OCPInterface
from ovos_plugin_common_play.ocp import MediaType, PlaybackType
import time


class NieuwsAfspelen(OVOSSkill):
    def __init__(self):
        super(NieuwsAfspelen, self).__init__()
        self.skill_id = "skill_nieuws_luisteren"
        self.url = "https://cdn.nos.nl/content/radio/ditisdenieuweurlvoorhetradiobulletinvoorgooglevanafjuli2019.mp3"
        self.image = "https://raw.githubusercontent.com/timonvanhasselt/skill-ovos-news/dev/ui/images/nos.jpg"
        self.audio = None
        self.playlist = [
            {
                "media_type": MediaType.RADIO,
                "uri": self.url,
                "playback": PlaybackType.AUDIO,
                "image": self.image,
                "bg_image": self.image,
                "skill_icon": self.image,
                "author": "NOS journaal",
                "title" : " ",
                "length": 0
            }
        ]
    def initialize(self):
        # Initialize the OCP audio service with the bus
        self.audio = OCPInterface(self.bus)

    @intent_handler('nieuws_afspelen.intent')

    def play(self):
        self.log.info("Hier is het NOS nieuws")
        self.speak_dialog('nieuws_afspelen')
        self.gui.show_image(self.image, fill="PreserveAspectCrop", override_idle=120, override_animations=False)
        time.sleep(5)
        self.audio.play(self.playlist)


    def stop(self):
        if self.audio:
            self.audio.stop()
