from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

def init(): #ngatur display
    glClearColor(0,0,0,0)
    gluOrtho2D(-25, 25, -35, 25)

    
    
    
def ZombieNormal():
    glClear(GL_COLOR_BUFFER_BIT)
    # Kepala
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(0.6, 1)  # A
    glVertex2f(0.8, 1)  # B
    glVertex2f(0.8, 0.8)  # C
    glVertex2f(0.6, 0.8)  # D

    glEnd()
    glFlush()

    # Mata Kiri
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.62, 0.94)  # a1
    glVertex2f(0.66, 0.94)  # b1
    glVertex2f(0.66, 0.92)  # d1
    glVertex2f(0.62, 0.92)  # c1

    glEnd()
    glFlush()

    # Mata Kanan
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.78, 0.94)  # e1
    glVertex2f(0.78, 0.92)  # f1
    glVertex2f(0.74, 0.92)  # g1
    glVertex2f(0.74, 0.94)  # h1

    glEnd()
    glFlush()

    # Hidung
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex2f(0.7, 0.92)  # i1
    glVertex2f(0.7, 0.88)  # j1

    glEnd()
    glFlush()

    # Mulut
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)
    glVertex2f(0.6313111475542, 0.8598252454853)  # k1
    glVertex2f(0.7058465544436, 0.8171720357624)  # n1
    glVertex2f(0.76, 0.86)  # l1
    glVertex2f(0.6377737550879, 0.836990698866)  # m1

    glEnd()
    glFlush()

    # Baju
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.4, 0.8)  # e
    glVertex2f(1, 0.8)  # f
    glVertex2f(1, 0.6672267981896)  # v
    glVertex2f(0.4, 0.6648157628024)  # u

    glEnd()
    glFlush()

    # Katok
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.5988777900477, 0.6663285821281)  # n
    glVertex2f(0.5980205111936, 0.5003031557436)  # o1
    glVertex2f(0.800802651271, 0.4999978524878)  # p1
    glVertex2f(0.8012507387269, 0.6674744134589)  # l

    glEnd()
    glFlush()

    # Lengan Kiri
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(0.4, 0.4)  # g
    glVertex2f(0.5214547775229, 0.4019053655365)  # m
    glVertex2f(0.5214547775229, 0.6651032612454)  # h
    glVertex2f(0.4, 0.6652495951776)  # w

    glEnd()
    glFlush()

    # Lengan Kanan
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(0.874118850666, 0.6674222293276)  # k
    glVertex2f(1, 0.6669200275299)  # v
    glVertex2f(1, 0.4)  # i
    glVertex2f(0.8751645376724, 0.4015439479263)  # j

    glEnd()
    glFlush()

    # Kaki kiri
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(0.5980205111936, 0.5003031557436)  # o1
    glVertex2f(0.6733533594482, 0.5001897366632)  # d
    glVertex2f(0.6716767015819, 0.2061454188146)  # q
    glVertex2f(0.6, 0.2)  # o

    glEnd()
    glFlush()

    # Kaki Kanan
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(0.7360881401951, 0.5000952848895)  # z
    glVertex2f(0.800802651271, 0.4999978524878)  # p1
    glVertex2f(0.8, 0.2)  # p
    glVertex2f(0.7467142378143, 0.2050997318082)  # t

    glEnd()
    glFlush()

    # Resleting
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.6455849916677, 0.5002315439599)  # d
    glVertex2f(0.7699094693381, 0.5000443644193)  # z
    glVertex2f(0.7357143208171, 0.4007674406646)  # s
    glVertex2f(0.6742224411222, 0.401813127671)  # r

    glEnd()
    glFlush()

    glBegin(GL_LINES)
    glColor3ub(255, 229, 129)
    glVertex2f(0.495139575863, 0.6789879980599)  # m
    glVertex2f(0.495139575863, 0.6789879980599)  # q1

    glVertex2f(0.495139575863, 0.6789879980599)  # q1
    glVertex2f(0.4912062423357, 0.7041616020308)  # r1

    glVertex2f(0.4912062423357, 0.7041616020308)  # r1
    glVertex2f(0.4634898672411, 0.723563064597)  # s1

    glVertex2f(0.4634898672411, 0.723563064597)  # s1
    glVertex2f(0.4676473235053, 0.7568227147104)  # t1

    glVertex2f(0.4676473235053, 0.7568227147104)  # t1
    glVertex2f(0.45, 0.8)  # u1

    glVertex2f(0.8012507387269, 0.6674744134589)  # l
    glVertex2f(0.778070724564, 0.6840672300873)  # v1

    glVertex2f(0.778070724564, 0.6840672300873)  # v1
    glVertex2f(0.7649054463941, 0.7291063396159)  # w1

    glVertex2f(0.7649054463941, 0.7291063396159)  # w1
    glVertex2f(0.7898501839791, 0.7651376272388)  # z1

    glVertex2f(0.7898501839791, 0.7651376272388)  # z1
    glVertex2f(0.8, 0.8)  # c

    glEnd()
    glFlush()
    
def ZombieAnjing():
    glClear(GL_COLOR_BUFFER_BIT)

    # Telinga kiri
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(0.4939668896146, 0.9934184139604)  # b
    glVertex2f(0.4939668896146, 0.9934184139604)  # b
    glVertex2f(0.6, 0.8)  # c
    glVertex2f(0.4, 0.8)  # a

    glEnd()
    glFlush()

    # Telinga Kanan
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(0.8, 1)  # g
    glVertex2f(0.8, 1)  # g
    glVertex2f(0.9, 0.8)  # h
    glVertex2f(0.7, 0.8)  # f

    glEnd()
    glFlush()

    # Kepala
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.4, 0.8)  # a
    glVertex2f(0.9, 0.8)  # h
    glVertex2f(0.9, 0.4)  # h2
    glVertex2f(0.4, 0.4)  # w

    glEnd()
    glFlush()

    # Mata
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)
    glVertex2f(0.5, 0.7)  # l1
    glVertex2f(0.6, 0.7)  # o1
    glVertex2f(0.6, 0.6)  # n1
    glVertex2f(0.5, 0.6)  # m1

    glEnd()
    glFlush()

    # Kelopak Mata
    glBegin(GL_POLYGON)
    glColor3ub(255, 255, 255)
    glVertex2f(0.5, 0.68)  # p1
    glVertex2f(0.56, 0.68)  # q1
    glVertex2f(0.56, 0.62)  # r1
    glVertex2f(0.5, 0.62)  # s1

    glEnd()
    glFlush()

    # leher
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)
    glVertex2f(0.8, 0.5)  # k
    glVertex2f(0.9, 0.5)  # l
    glVertex2f(0.9, 0.4)  # h2
    glVertex2f(0.8, 0.4)  # i

    glEnd()
    glFlush()

    # Mulut
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.2, 0.6)  # d
    glVertex2f(0.4, 0.6)  # e
    glVertex2f(0.4, 0.4)  # w
    glVertex2f(0.2, 0.4)  # j

    glEnd()
    glFlush()

    # lidah
    glBegin(GL_LINES)
    glColor3ub(255, 255, 255)
    glVertex2f(0.2, 0.5)  # o
    glVertex2f(0.4, 0.5)  # p

    glEnd()
    glFlush()

    # Badan
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.9, 0.7)  # n
    glVertex2f(1.7, 0.7)  # q
    glVertex2f(1.7, 0.4)  # m
    glVertex2f(0.9, 0.4)  # h2

    glEnd()
    glFlush()

    # KakiDepan kiri
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(0.7, 0.4)  # r
    glVertex2f(0.8, 0.4)  # i
    glVertex2f(0.8, 0.1)  # t
    glVertex2f(0.7, 0.1)  # s

    glEnd()
    glFlush()

    # KakiDepan kanan
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.8445078479215, 0.4)  # i
    glVertex2f(0.9389268057445, 0.4027037703656)  # h2
    glVertex2f(0.9018020421892, 0.2533699127881)  # g2
    glVertex2f(0.8709649969508, 0.2171699031604)  # f2
    glVertex2f(0.8709649969508, 0.1796291524354)  # e2
    glVertex2f(0.8997340307991, 0.1479507332206)  # v
    glVertex2f(0.8427263581513, 0.1550766923015)  # u

    glEnd()
    glFlush()

    # KakiBelakang kiri
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(1.5, 0.4)  # z
    glVertex2f(1.6, 0.4)  # c1
    glVertex2f(1.6, 0.1)  # b1
    glVertex2f(1.5, 0.1)  # a1

    glEnd()
    glFlush()

    # KakiBelakang kanan
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(1.62480036728880, 0.4)  # e1
    glVertex2f(1.7, 0.4)  # m
    glVertex2f(1.7014044274093, 0.1532952025313)  # w
    glVertex2f(1.6230188775185, 0.1532952025313)  # d1

    glEnd()
    glFlush()

    glBegin(GL_LINES)
    glColor3ub(255, 229, 129)
    glVertex2f(1.27184658505, 0.7011774392935)  # d2
    glVertex2f(1.2276021288384, 0.6636366885685)  # c2

    glVertex2f(1.2276021288384, 0.6636366885685)  # c2
    glVertex2f(1.1699502616536, 0.6462070543033)  # b2

    glVertex2f(1.1699502616536, 0.6462070543033)  # b2
    glVertex2f(1.1310687698312, 0.6743626173471)  # a2

    glVertex2f(1.1310687698312, 0.6743626173471)  # a2
    glVertex2f(1.080120608133, 0.6260959378435)  # z1

    glVertex2f(1.080120608133, 0.6260959378435)  # z1
    glVertex2f(1.0506243039919, 0.6891107694176)  # w1

    glVertex2f(1.0506243039919, 0.6891107694176)  # w1
    glVertex2f(1.009061329975, 0.6274366789408)  # v1

    glVertex2f(1.009061329975, 0.6274366789408)  # v1
    glVertex2f(0.9661576148607, 0.6944737338069)  # u1

    glVertex2f(0.9661576148607, 0.6944737338069)  # u1
    glVertex2f(0.9366613107196, 0.6636366885685)  # t1

    glVertex2f(0.9366613107196, 0.6636366885685)  # t1
    glVertex2f(0.9, 0.7)  # n

    # Ekor
    glVertex2f(1.7, 0.5550962851543)  # G
    glVertex2f(1.8, 0.6)  # h1

    glVertex2f(1.8, 0.6)  # h1
    glVertex2f(1.8706470233421, 0.5163759157859)  # i1

    glVertex2f(1.8706470233421, 0.5163759157859)  # i1
    glVertex2f(1.8706470233421, 0.5163759157859)  # j1

    glVertex2f(1.8706470233421, 0.5163759157859)  # j1
    glVertex2f(2.0303685469868, 0.4841089413122)  # k1

    glEnd()
    glFlush()
    
    
def ZombieMini() : 
    glClear(GL_COLOR_BUFFER_BIT)

    # Kepala
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.6, 0.8)  # a
    glVertex2f(1, 0.8)  # b
    glVertex2f(1, 0.6)  # c
    glVertex2f(0.6, 0.6)  # d

    glEnd()
    glFlush()

    # Mata kanan
    glBegin(GL_POLYGON)
    glColor3ub(255, 255, 255)
    glVertex2f(0.85, 0.75)  # a1
    glVertex2f(0.95, 0.75)  # b1
    glVertex2f(0.95, 0.7)  # c1
    glVertex2f(0.85, 0.7)  # d1

    glEnd()
    glFlush()

    # Mata kiri
    glBegin(GL_POLYGON)
    glColor3ub(255, 255, 255)
    glVertex2f(0.65, 0.75)  # u
    glVertex2f(0.75, 0.75)  # v
    glVertex2f(0.75, 0.7)  # w
    glVertex2f(0.65, 0.7)  # z

    glEnd()
    glFlush()

    # mulut
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)
    glVertex2f(0.7193414154579, 0.6656604398402)  # f1
    glVertex2f(0.7777642709223, 0.6879985904589)  # g1
    glVertex2f(0.8327504878299, 0.6776886747887)  # h1
    glVertex2f(0.8739901505106, 0.6656604398402)  # i1
    glVertex2f(0.9186664517481, 0.645899768139)  # j1
    glVertex2f(0.7, 0.65)  # e1

    glEnd()
    glFlush()

    # Badan
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.5, 0.6)  # e
    glVertex2f(1.1, 0.6)  # j
    glVertex2f(1.1, 0.5)  # g2
    glVertex2f(0.5, 0.5)  # f2

    glEnd()
    glFlush()

    # Pinggang
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.5, 0.6)  # i
    glVertex2f(1.1, 0.6)  # n
    glVertex2f(0.9400736525626, 0.3197776955167)  # g2
    glVertex2f(0.6649992228385, 0.3224602773655)  # f2

    glEnd()
    glFlush()

    # Paha Kiri
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.6649992228385, 0.3224602773655)  # f2
    glVertex2f(0.7720604232502, 0.329122388605)  # s
    glVertex2f(0.7722962674069, 0.2554822968337)  # p1
    glVertex2f(0.6643167849984, 0.2523966591136)  # o1

    glEnd()
    glFlush()

    # Paha kanan
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.8407786486901, 0.329122388605)  # r
    glVertex2f(0.9400736525626, 0.3197776955167)  # g2
    glVertex2f(0.939523955786, 0.2497668252158)  # r1
    glVertex2f(0.840955044044, 0.2565201844544)  # q1

    glEnd()
    glFlush()

    # Kaki kiri
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(0.6643167849984, 0.2523966591136)  # o1
    glVertex2f(0.7722962674069, 0.2554822968337)  # p1
    glVertex2f(0.7727872822425, 0.1021675907895)  # t
    glVertex2f(0.6628535148524, 0.1021675907895)  # o

    glEnd()
    glFlush()

    # Kaki kanan
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(0.840955044044, 0.2565201844544)  # q1
    glVertex2f(0.939523955786, 0.2497668252158)  # r1
    glVertex2f(0.9383346025477, 0.0982875754699)  # p
    glVertex2f(0.8439208964361, 0.1034609292294)  # q

    glEnd()
    glFlush()

    # lengan kiri
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(0.5, 0.5)  # f2
    glVertex2f(0.6, 0.5)  # h
    glVertex2f(0.6, 0.3)  # g
    glVertex2f(0.5864713049377, 0.3160143458701)  # z1
    glVertex2f(0.5664912440691, 0.3151456475714)  # w1
    glVertex2f(0.5517233729923, 0.3264387254537)  # v1
    glVertex2f(0.5508546746936, 0.363792752295)  # u1
    glVertex2f(0.5204502342414, 0.3420752948291)  # t1
    glVertex2f(0.5195815359428, 0.3142769492728)  # s1
    glVertex2f(0.5, 0.3)  # f
    glEnd()
    glFlush()

    # lengan kanan
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(1, 0.5)  # m
    glVertex2f(1.1, 0.5)  # h2
    glVertex2f(1.1, 0.3)  # k
    glVertex2f(1.0712049555762, 0.2838725088206)  # e2
    glVertex2f(1.0616492742912, 0.2977716815987)  # d2
    glVertex2f(1.040800515124, 0.3403378982318)  # c2
    glVertex2f(1.0208204542554, 0.3073273628837)  # b2
    glVertex2f(1.0208204542554, 0.3290448203496)  # a2
    glVertex2f(1, 0.3)  # l

    glEnd()
    glFlush()

    # Tali kiri
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)
    glVertex2f(0.6609185599935, 0.6)  # k1
    glVertex2f(0.6918483070041, 0.6)  # n1
    glVertex2f(0.666733530172, 0.5005158302738)  # i
    glVertex2f(0.6, 0.5)  # h

    glEnd()
    glFlush()

    # Tali Kanan
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)
    glVertex2f(0.8878664972304, 0.6)  # l1
    glVertex2f(0.9272580481399, 0.6)  # m1
    glVertex2f(1, 0.5)  # m
    glVertex2f(0.9414937244653, 0.500641899259)  # n

    glEnd()
    glFlush()

    # Tali bawah kiri
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)
    glVertex2f(0.666733530172, 0.5005158302738)  # i
    glVertex2f(0.666733530172, 0.5005158302738)  # i
    glVertex2f(0.6643167849984, 0.2523966591136)  # o1
    glVertex2f(0.7722962674069, 0.2554822968337)  # p1

    glEnd()
    glFlush()

    # Tali bawah kiri
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)
    glVertex2f(0.9414937244653, 0.500641899259)  # n
    glVertex2f(0.9414937244653, 0.500641899259)  # n
    glVertex2f(0.939523955786, 0.2497668252158)  # r1
    glVertex2f(0.840955044044, 0.2565201844544)  # q1

    glEnd()
    glFlush()
    
    
def ZombieMutant():
    glClear(GL_COLOR_BUFFER_BIT)

    # Kepala
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.6, 1)  # e
    glVertex2f(0.6, 1.2)  # a
    glVertex2f(0.7449770023713, 1.4047635959641)  # b
    glVertex2f(1.0551768212506, 1.4080288572154)  # c
    glVertex2f(1.2, 1.2)  # d
    glVertex2f(1.2, 1)  # f

    glEnd()
    glFlush()

    # Mata kanan
    glBegin(GL_POLYGON)
    glColor3ub(255, 255, 255)
    glVertex2f(0.7, 1.3)  # k
    glVertex2f(0.7842898193841, 1.2989034222913)  # l
    glVertex2f(0.7836521567991, 1.2606436671956)  # n
    glVertex2f(0.6999927598263, 1.2607656556879)  # m

    glEnd()
    glFlush()

    # Mata kiri
    glBegin(GL_POLYGON)
    glColor3ub(255, 255, 255)
    glVertex2f(1.0141981750183, 1.2989282567234)  # p
    glVertex2f(1.1, 1.3)  # o
    glVertex2f(1.0981558972963, 1.2645819157914)  # r
    glVertex2f(1.0141981750183, 1.2633098290903)  # q

    glEnd()
    glFlush()

    # mulut
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)
    glVertex2f(0.8001378780738, 1.2318615216231)  # h
    glVertex2f(0.9995382046608, 1.2311946308987)  # i
    glVertex2f(1, 1)  # j
    glVertex2f(0.8, 1)  # g

    glEnd()
    glFlush()

    # Badan
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.4, 1)  # s
    glVertex2f(1.4, 1)  # t
    glVertex2f(1.4, 0.8)  # h2
    glVertex2f(0.4, 0.8)  # g2

    glEnd()
    glFlush()

    # lengan kiri
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(0.4, 0.8)  # g2
    glVertex2f(0.6, 0.8)  # w
    glVertex2f(0.6, 0.75)  # z1
    glVertex2f(0.4, 0.75)  # w1

    glEnd()
    glFlush()

    # Lengan kanan
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(1.2, 0.8)  # e1
    glVertex2f(1.4, 0.8)  # h2
    glVertex2f(1.4, 0.75)  # b2
    glVertex2f(1.2, 0.75)  # a2

    glEnd()
    glFlush()

    # # Paha kiri
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.7, 0.8)  # z
    glVertex2f(0.7, 0.8)  # z
    glVertex2f(0.8407257445556, 0.7000449438084)  # j1
    glVertex2f(0.7, 0.7)  # i2

    glEnd()
    glFlush()

    # Paha kanan
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(1.1, 0.8)  # f1
    glVertex2f(1.1, 0.8)  # f1
    glVertex2f(1.1, 0.7)  # j2
    glVertex2f(0.9483914234208, 0.7000449438084)  # i1

    glEnd()
    glFlush()

    # Kaki kiri
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(0.7, 0.7)  # i2
    glVertex2f(0.8407257445556, 0.7000449438084)  # j1
    glVertex2f(0.8393799235698, 0.199399537085)  # b1
    glVertex2f(0.7, 0.2)  # a1

    glEnd()
    glFlush()

    # Kaki Kanan
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(0.9483914234208, 0.7000449438084)  # i1
    glVertex2f(1.1, 0.7)  # j2
    glVertex2f(1.1, 0.2)  # g1
    glVertex2f(0.9483914234208, 0.2047828210283)  # h1
    glEnd()
    glFlush()

    # Lubang Tengah
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(0.8407257445556, 0.7000449438084)  # j1
    glVertex2f(0.7, 0.8)  # z
    glVertex2f(0.8, 1)  # g
    glVertex2f(1, 1)  # j
    glVertex2f(1.1, 0.8)  # f1
    glVertex2f(0.9483914234208, 0.7000449438084)  # i1

    glEnd()
    glFlush()

    # Lubang tengah dalem
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)
    glVertex2f(0.8, 0.9)  # c2
    glVertex2f(0.921883987339, 0.9599825618992)  # f2
    glVertex2f(1.0151459465328, 0.8338046171076)  # e2
    glVertex2f(0.8703156099024, 0.752611852633)  # d2

    glEnd()
    glFlush()

    # Luka 1
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.8, 0.9)  # c2
    glVertex2f(0.831090388891, 0.8914688904101)  # k2
    glVertex2f(0.8380067426774, 0.8756600817554)  # l2
    glVertex2f(0.8636960567412, 0.8667676268872)  # m2
    glVertex2f(0.8725885116094, 0.8499707676916)  # n2
    glVertex2f(0.8597438545776, 0.8302097568733)  # o2
    glVertex2f(0.8404781733621, 0.8151539325491)  # p2

    glEnd()
    glFlush()

    # Luka 2
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.9576895150705, 0.911539789086)  # q2

    glVertex2f(0.9338476451462, 0.904313547442)  # r2
    glVertex2f(0.9289073924416, 0.8825764355419)  # s2
    glVertex2f(0.9129368477433, 0.8688596062771)  # t2
    glVertex2f(0.9078921811646, 0.8382312734777)  # u2
    glVertex2f(0.9190268870325, 0.8183531503824)  # v2
    glVertex2f(0.913098583787, 0.8025443417277)  # w2

    glVertex2f(0.9074339191542, 0.773420601759)  # z2
    glEnd()
    glFlush()

    # Tangan Kiri
    glBegin(GL_POLYGON)
    glColor3ub(0, 255, 0)
    glVertex2f(0.4, 0.75)  # w1
    glVertex2f(0.6, 0.75)  # z1
    glVertex2f(0.6, 0.6)  # v
    glVertex2f(0.4, 0.6)  # u

    glEnd()
    glFlush()

    # Tangan kanan
    glBegin(GL_POLYGON)
    glColor3ub(0, 255, 0)
    glVertex2f(1.2, 0.75)  # a2
    glVertex2f(1.4, 0.75)  # b2
    glVertex2f(1.4, 0.6)  # c1
    glVertex2f(1.2, 0.6)  # d1

    glEnd()
    glFlush()
    
    

def ZombieMonsterMutant() :
    glClear(GL_COLOR_BUFFER_BIT)

    # Kepala
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(1, 2)  # a
    glVertex2f(1.2, 2)  # b
    glVertex2f(1.2, 1.8)  # c
    glVertex2f(1, 1.8)  # d

    glEnd()
    glFlush()

    # Mata kanan
    glBegin(GL_POLYGON)
    glColor3ub(255, 255, 255)
    glVertex2f(1.02, 1.96)  # i4
    glVertex2f(1.06, 1.96)  # l4
    glVertex2f(1.06, 1.94)  # k4
    glVertex2f(1.02, 1.94)  # j4

    glEnd()
    glFlush()

    # Mata kiri
    glBegin(GL_POLYGON)
    glColor3ub(255, 255, 255)
    glVertex2f(1.14, 1.96)  # p4
    glVertex2f(1.18, 1.96)  # m4
    glVertex2f(1.18, 1.94)  # n4
    glVertex2f(1.14, 1.94)  # o4

    glEnd()
    glFlush()

    # mulut
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)
    glVertex2f(1.1017207139006, 1.9179395735005)  # q4
    glVertex2f(1.1017207139006, 1.9179395735005)  # q4
    glVertex2f(1.1421590421689, 1.8527435413079)  # s4
    glVertex2f(1.0247650202728, 1.8525640671143)  # r4

    glEnd()
    glFlush()

    # Bahu
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.2, 1.8)  # t4
    glVertex2f(2, 1.8)  # f
    glVertex2f(2, 1.4868569374103)  # v4
    glVertex2f(0.2, 1.4850305894915)  # u4

    glEnd()
    glFlush()

    # lengan kiri
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(0.2, 1.4850305894915)  # u4
    glVertex2f(0.4767773257226, 1.4862197401209)  # i
    glVertex2f(0.4716431463297, 0.9963145796604)  # p1
    glVertex2f(0.2, 1)  # q3

    glEnd()
    glFlush()

    # Tangan kiri
    glBegin(GL_POLYGON)
    glColor3ub(0, 229, 0)
    glVertex2f(0.2, 1)  # q3
    glVertex2f(0.4716431463297, 0.9963145796604)  # p1
    glVertex2f(0.463313923208, 0.2015372495938)  # h
    glVertex2f(0.2, 0.2)  # g

    glEnd()
    glFlush()

    # Tangan kiri (2)
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(0.6, 1.2)  # a5
    glVertex2f(0.8, 1.2)  # m
    glVertex2f(0.8, 0.4)  # l
    glVertex2f(0.6, 0.4)  # k

    glEnd()
    glFlush()

    # Lengan kanan
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(1.7090082252569, 1.4868307031535)  # p
    glVertex2f(2, 1.4868569374103)  # v4
    glVertex2f(2, 1)  # v1
    glVertex2f(1.707593196409, 0.994673579253)  # u1

    glEnd()
    glFlush()

    # Tangan Kanan
    glBegin(GL_POLYGON)
    glColor3ub(0, 229, 0)
    glVertex2f(1.707593196409, 0.994673579253)  # u1
    glVertex2f(2, 1)  # v1
    glVertex2f(2, 0.2)  # n
    glVertex2f(1.7053128051837, 0.2015372495938)  # o

    glEnd()
    glFlush()

    # Tangan Kanan (2)
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(1.4, 1.2)  # t
    glVertex2f(1.6, 1.2)  # b5
    glVertex2f(1.6, 0.4)  # r
    glVertex2f(1.4, 0.4)  # s

    glEnd()
    glFlush()

    # Ketiak kiri
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.5464132155503, 1.5761041023151)  # w4
    glVertex2f(0.6576879616988, 1.4939279447288)  # m2
    glVertex2f(0.6, 1.4)  # j
    glVertex2f(0.4767773257226, 1.4862197401209)  # i

    glEnd()
    glFlush()

    # Ketiak kanan
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(1.5307020697971, 1.5167305520299)  # q2
    glVertex2f(1.6616415099909, 1.5673913812647)  # z4
    glVertex2f(1.7090082252569, 1.4868307031535)  # p
    glVertex2f(1.6, 1.4)  # q

    glEnd()
    glFlush()

    # Dada
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.6576879616988, 1.4939279447288)  # m2
    glVertex2f(1.5307020697971, 1.5167305520299)  # q2
    glVertex2f(1.6, 1.2)  # b5
    glVertex2f(0.6, 1.2)  # a5

    glEnd()
    glFlush()

    # Perut
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.9, 1.2)  # u
    glVertex2f(1.3192333819799, 1.2032603864024)  # v
    glVertex2f(1.3188957323721, 1.0008752569612)  # c3
    glVertex2f(0.8998074171556, 1.0000001854409)  # b3

    glEnd()
    glFlush()

    # Pinggang
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.8998074171556, 1.0000001854409)  # b3
    glVertex2f(1.3188957323721, 1.0008752569612)  # c3
    glVertex2f(1.3190103582616, 0.7972116914255)  # d5
    glVertex2f(0.8996148343112, 0.8000003708819)  # c5
    glEnd()
    glFlush()

    # Kaki Kiri
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(0.8996148343112, 0.8000003708819)  # c5
    glVertex2f(1.0441975899366, 0.8002726145284)  # a1
    glVertex2f(1.0391442567974, 0.6404302763503)  # z
    glVertex2f(0.8994584837387, 0.6376282469109)  # w
    glEnd()
    glFlush()

    # Kaki Kanan
    glBegin(GL_POLYGON)
    glColor3ub(255, 229, 129)
    glVertex2f(1.2, 0.8)  # b1
    glVertex2f(1.3190103582616, 0.7972116914255)  # d5
    glVertex2f(1.3189255508013, 0.6428067749976)  # d1
    glVertex2f(1.2, 0.6455412219822)  # c1

    glEnd()
    glFlush()

    # Lubang tengah dalem
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)
    glVertex2f(0.8561775761267, 1.4163159037614)  # w3
    glVertex2f(0.9495519121785, 1.4516849704477)  # z3
    glVertex2f(1.0599034002398, 1.5280821544901)  # a4
    glVertex2f(1.1744991763034, 1.5535478825043)  # b4
    glVertex2f(1.3131459177137, 1.621456490542)  # c4
    glVertex2f(1.4277416937773, 1.6554107945608)  # d4
    glVertex2f(1.3456854590651, 1.5719397971811)  # e4
    glVertex2f(1.2466520723435, 1.5351559678274)  # f4
    glVertex2f(1.1179086696053, 1.5012016638085)  # g4
    glVertex2f(1.0273638588884, 1.4219749544312)  # h4

    glEnd()
    glFlush()

    # Luka kiri
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)
    glVertex2f(0.2, 1.8)  # t4
    glVertex2f(0.4, 1.8)  # t1
    glVertex2f(0.4, 1.7)  # q1
    glVertex2f(0.3, 1.7)  # o1
    glVertex2f(0.3, 1.6)  # m1
    glVertex2f(0.2, 1.6)  # e

    glEnd()
    glFlush()
    
    
    
    
    
def aspal():
    glPointSize(1)
    glBegin(GL_QUADS)
    glColor3ub(198,138,89)
    
    glVertex2f(-20, 20)
    glVertex2f(20, 20)
    glVertex2f(20, -30)
    glVertex2f(-20, -30)
    
    glEnd()
    glFlush()

def garisputih():
    glPointSize(1)
#1
    glBegin(GL_QUADS)
    glColor3ub(255,255,255)
    
    glVertex2f(-1, -30)
    glVertex2f(1, -30)
    glVertex2f(1, -24)
    glVertex2f(-1, -24)
    
    glEnd()
    glFlush()
#2
    glBegin(GL_QUADS)
    glColor3ub(255,255,255)
    
    glVertex2f(-1, -20)
    glVertex2f(1, -20)
    glVertex2f(1, -14)
    glVertex2f(-1, -14)
    
    glEnd()
    glFlush()
#3
    glBegin(GL_QUADS)
    glColor3ub(255,255,255)
    
    glVertex2f(-1, -10)
    glVertex2f(1, -10)
    glVertex2f(1, -4)
    glVertex2f(-1, -4)
    
    glEnd()
    glFlush()
#4
    glBegin(GL_QUADS)
    glColor3ub(255,255,255)
    
    glVertex2f(-1, 0)
    glVertex2f(1, 0)
    glVertex2f(1, 6)
    glVertex2f(-1, 6)
    
    glEnd()    
    
    glFlush()
#5
    glBegin(GL_QUADS)
    glColor3ub(255,255,255)
    
    glVertex2f(-1, 10)
    glVertex2f(1, 10)
    glVertex2f(1, 16)
    glVertex2f(-1, 16)
    
    glEnd()
    glFlush()

def gradasi_aspal_kiri():
    glPointSize(1)
    glBegin(GL_POLYGON)
    glColor3ub(134,84,57)
    
    glVertex2f(-16.5935, 20)
    glVertex2f(-14.8730823391585, 15.0591529126151)
    glVertex2f(-15.3018503127147, 11.9182155518996)
    glVertex2f(-15.3018503127147, 11.9182155518996)
    glVertex2f(-15.1830574122144, 6.3349492283857)
    glVertex2f(-14.2327142082121, 3.246333815378)
    glVertex2f(-14,0)
    glVertex2f(-15.0668263861428, -2.214128760864)
    glVertex2f(-15.6735959951736, -6.1711465551626)
    glVertex2f(-15, -10)
    glVertex2f(-14.7265302084601, -11.6956969776578)
    glVertex2f(-13.6860484437535, -13.9102825964051)
    glVertex2f(-12.2861912903378, -17.7406857455354)
    glVertex2f(-12.2531831062776, -21.1390447811974)
    glVertex2f(-12.8941119719634, -23.3021797028866)
    glVertex2f(-14.4163180279669, -25.8658951656294)
    glVertex2f(-14.1968467929593, -28.9358610058285)
    glVertex2f(-15,-30)
    glVertex2f(-20, -30)
    glVertex2f(-20, 20)

    glEnd()
    glFlush()
    
def gradasi_aspal_kanan():
    glPointSize(1)
    glBegin(GL_POLYGON)
    glColor3ub(134,84,57)
    
    glVertex2f(11.7477, 20)
    glVertex2f(13.9866346469667, 16.5506078580791)
    glVertex2f(14.514762715606, 13.1051008641174)
    glVertex2f(13.4615666864947, 6.690179595894)
    glVertex2f(14.1317823413837, 3.2433562278933)
    glVertex2f(16.4296645867175, -2.6928395725522)
    glVertex2f(16.7168998673842, -7.9588197181088)
    glVertex2f(16.4296645867175, -9.7779764956647)
    glVertex2f(13.844547060717, -15.8099173896658)
    glVertex2f(13.844547060717, -15.8099173896658)
    glVertex2f(13.0785863122724, -20.2141916932222)
    glVertex2f(13.7488019671614, -26.1503874936677)
    glVertex2f(15,-30)
    glVertex2f(20, -30)
    glVertex2f(20,20)
    glVertex2f(11.7477, 20)


    glEnd()
    glFlush()


def gabung():
    aspal()
    garisputih()
    gradasi_aspal_kiri()
    gradasi_aspal_kanan()

def garisbase():
    glPointSize(5)
    glBegin(GL_LINE)
    glColor3ub(255,0,0)
    
    glVertex2f(-20, 20)
    glVertex2f(20, 20)
    
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(400,600)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Zombie Defense")
    glutDisplayFunc(gabung)
    init()
    glutMainLoop()

main()
