#should be able to run thr games in succesion
from ikeja import IkejaUnderBridge
from religion import ReligiousPlace
from police import PoliceStation
from garage import Garage
from club import Club

class Engine(object):
    
    def Play(self):
        name = IkejaUnderBridge().enter() 
        scene = {
            'police' : PoliceStation,
            'club' : Club,
            'religion' : ReligiousPlace,
            'garage' : Garage
        }
        scene[str(name)].enter(self)
Engine().Play()