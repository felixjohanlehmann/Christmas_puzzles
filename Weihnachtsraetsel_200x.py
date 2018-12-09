from pylab import *

class cube(object):
    def __init__(self, number, kind):
        self.number = array(number)
        self.kind = array(kind)
    def sumCubeNumber(self):
        return sum(self.number)
    def sumCubeKind(self):
        return sum(self.kind)
    def createLargeCube(self, self2, self3, self4, self5, self6, self7, self8):
        return cube(
            [
                array([[self2.number[1],self.number[1]],[self6.number[1],self5.number[1]]]),
                array([[self.number[2],self3.number[2]],[self5.number[2],self7.number[2]]]),
                array([[self.number[3],self2.number[3]],[self3.number[3],self4.number[3]]]),
                array([[self4.number[4],self2.number[4]],[self8.number[4],self6.number[4]]]),
                array([[self3.number[5],self4.number[5]],[self7.number[5],self8.number[5]]]),
                array([[self7.number[3],self8.number[3]],[self5.number[3],self6.number[3]]])
                ],
            [
                array([[self2.kind[1],self.kind[1]],[self6.kind[1],self5.kind[1]]]),
                array([[self.kind[2],self3.kind[2]],[self5.kind[2],self7.kind[2]]]),
                array([[self.kind[3],self2.kind[3]],[self3.kind[3],self4.kind[3]]]),
                array([[self4.kind[4],self2.kind[4]],[self8.kind[4],self6.kind[4]]]),
                array([[self3.kind[5],self4.kind[5]],[self7.kind[5],self8.kind[5]]]),
                array([[self7.kind[3],self8.kind[3]],[self5.kind[3],self6.kind[3]]])
                ])
    def testFunction(self, self2):
        return cube(add(self.number, self2.number), self.kind)

#Definitionen:
    #Zahlenkodierung der Symbole fuer die Objekteigenschaft "kind":
        #leer = 0
        #Kreis = 1
        #Sechseck = 2
        #Dreieck = 3
    #Anzahl der Symbole entspricht der Objekteigenschaft "number"
    #Abrollkonvention fuer die Wuerfel:
        #1. Man betrachte das Wuerfelfeld mit den meisten Sechsecken
        #   (falls keine Sechsecke vorhanden sind: mit den meisten Kreisen)
        #2. Man drehe den Wuerfel unter Beibehaltung des Blickes auf
        #   das im 1. Schritt gewaehlte Wuerfelfeld bis das Wuerfelfeld mit den meisten Dreiecken
        #   (falls keine Dreiecke vorhanden sind: mit den meisten Kreisen) nach oben zeigt
        #   (falls zwei Wuerfelfelder gleich viele Dreiecke zeigen:
        #   zeigt eines der beiden Wuerfelfelder nach oben und das Andere nach links)
        #3. Der Wuerfel wird wie folgt abgerollt:
        #       1                   oben
        #   2   3   4       links   vorne   rechts
        #       5                   unten
        #       6                   hinten
    #Abrollkonvention fuer den grossen Wuerfel:
        #1. Die Vorderseiten der ersten vier Wuerfel bilden von links nach rechts
        #   und von oben nach unten die Seite "vorne":
        #       1   2
        #       3   4
        #   Darunter liegen die Wuerfel 5 bis 8:
        #       5   6
        #       7   8
        #2. Der Wuerfel wird wie folgt abgerollt:
        #       1                   oben
        #   2   3   4       links   vorne   rechts
        #       5                   unten
        #       6                   hinten
        #
        #               d   c
        #               b   a
        #       c   a   a   b   b   d
        #       d   b   c   d   a   c
        #               a   b
        #               c   d
        #               a   b
        #               c   d
#Die Wuerfel cube_1 bis cube_8 sind sortiert nach:
        #1. aufsteigender Anzahl an Symbolen und
        #2. aufsteigender Summe der Wertigkeit der Symbole pro Wuerfel
        #(siehe Prozedur "Summierung()" am Ende des Codes)

cube_1 = cube([1,0,1,1,0,0],[3,0,2,1,0,0])
cube_2 = cube([1,1,3,0,0,1],[1,1,3,0,0,1])
cube_3 = cube([1,0,2,1,1,2],[3,0,2,1,1,3])
cube_4 = cube([3,2,2,2,0,1],[3,2,2,1,0,1])
cube_5 = cube([3,1,3,0,2,1],[3,3,2,0,3,1])
cube_6 = cube([3,2,3,0,1,3],[1,2,2,0,1,3])
cube_7 = cube([3,3,2,3,2,1],[3,3,2,1,1,1])
cube_8 = cube([3,3,3,1,3,2],[3,1,2,3,1,2])



def Weihnachtsraetsel():
    print 'test'
    testCube = cube([1,2,3],[4,5,6])
    
    
    test = testCube.number
    print test
    print test[1]
    
    largeCube = cube_1.testFunction(cube_2)
    print largeCube.number, largeCube.kind

    largeCube = cube_1.createLargeCube(cube_2, cube_3, cube_4, cube_5, cube_6, cube_7, cube_8)
    print largeCube.number, largeCube.kind

Weihnachtsraetsel()


#####
Cubes = [cube_1, cube_2, cube_3, cube_4, cube_5, cube_6, cube_7, cube_8]

def Summierung():
    counter = 0
    for c in Cubes:
        counter = counter + 1
        print '           Wuerfel', counter, ':'
        print '      Anzahl:', c.sumCubeNumber()
        print 'Wertigkeit:', c.sumCubeKind()

#Summierung()
