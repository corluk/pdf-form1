from datetime import date
class BeneficaryTypes: 
    LYRIC = "soz"
    COMPOSER = "beste" 
    ARRANGER = "aranjör" 
    SOURCE_PERSON= "kaynak_kişi"
    COMPILER = "derleyen"
    PERFORMER = "performer"

class Beneficary: 
    Name : str 
    Role : str  
class PerformerOnTrack(Beneficary) : 
    Role : BeneficaryTypes = BeneficaryTypes.PERFORMER
    RoleOnTrack : str 
    Share : float 

class Duration: 
    minutes : int 
    seconds : int 
class Track:
    Title: str 
    FirstLine : str
    Beneficiaries : list[Beneficary]
    MainPerformer : Beneficary
    Genre : str 
    Duration : Duration 
    Order : int 
    Isrc : str 
    def GetBeneficary(self,type :BeneficaryTypes) : 
        founded : list[str]= []
        for person in self.Beneficiaries: 
            if person.Role == BeneficaryTypes.COMPOSER:
                founded.append(person.Name)
        return ",".join(founded)
    
    def AddPerformer(self,name :str, isMain = False, share = 100):
        person= Beneficary() 
        person.Name = name 
        person.Role = BeneficaryTypes.PERFORMER
        if isMain == True: 
            self.MainPerformer = person
        else : 
            self.Beneficiaries.append(person)
         
class Album:
    Label : str 
    ReleaseDate : date 
    Tracks : list[Track]

    def AddTrack(self,track:Track): 
        if track.Order == None :
            track.Order == len(self.Tracks)
        self.Tracks = self.Tracks.append(track)
    
    def GetTracks(self): 
        return self.Tracks.sort(key=lambda x: x.Order, reverse=True )
    
 