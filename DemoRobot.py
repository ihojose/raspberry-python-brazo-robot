import RPi.GPIO as GPIO
from time import sleep

# SET PINS ==================================================================================
b = 12
a = 11
c = 13
h = 15

# GPIO CONFIGURATION ========================================================================
GPIO.setmode( GPIO.BOARD )
GPIO.setup( b, GPIO.OUT )
GPIO.setup( a, GPIO.OUT )
GPIO.setup( c, GPIO.OUT )
GPIO.setup( h, GPIO.OUT )

base = GPIO.PWM( b, 50 )
ante = GPIO.PWM( a, 50 )
codo = GPIO.PWM( c, 50 )
hand = GPIO.PWM( h, 50 )

base.start( 0 )
ante.start( 0 )
codo.start( 0 )
hand.start( 0 )

# SET GLOBAL ================================================================================
_angle = {
  "b": 50,
  "a": 0,
  "c": 65,
  "h": 0
}

def setAngle( angle ):
  return 2 + ( angle / 18 )

def setPos( e, name, angle, speed ):
  if _angle[ name ] > angle:
    speed = speed * -1
  for i in range( _angle[ name ], angle, int( speed ) ):
    e.ChangeDutyCycle( setAngle( i ) )
    _angle[ name ] = i
    sleep(0.1)
  e.ChangeDutyCycle( setAngle( angle ) )
  _angle[ name ] = angle

def setBase( angle, speed ):
  setPos( base, "b", angle, speed )

def setHand( angle, speed ):
  setPos( hand, "h", angle, speed )

def setCodo( angle, speed ):
  setPos( codo, "c", angle, speed )

def setAnte( angle, speed ):
  setPos( ante, "a", angle, speed )

# START ROBOT DEMO MODE =====================================================================
print("==> INICIANDO ROBOT <-> HOLA A TODOS")
print("==> VERIFICANDO...")

setHand(0, 1)
sleep(0.1)
setBase(50, 1)
sleep(0.1)
setAnte(0, 1)
sleep(0.1)
setCodo(65, 1)
sleep(0.5)

print("==> PROBANDO BRAZO")
setAnte(90, 7)
sleep(1)
print("==> SALUDANDO...")
setHand(55, 20)
sleep(0.2)
setHand(0, 20)
sleep(0.2)
setHand(55, 20)
sleep(1)
setBase(10, 8)
sleep(0.5)
setBase(90, 8)
sleep(0.5)
setHand(0, 20)
sleep(0.5)
setHand(55, 20)
sleep(0.5)
setCodo(10, 10)
setBase(50, 10)
setAnte(40, 10)
setHand(0, 15)
setHand(55, 15)
print("==> TOMEMOS ALGO...")
sleep(0.5)
setAnte(0, 12)
setCodo(65, 10)
sleep(0.5)
print("==> PON UN OBJETO [3]...")
sleep(1)
print("==> PON UN OBJETO [2]...")
sleep(1)
print("==> PON UN OBJETO [1]...")
sleep(0.5)
setHand(0, 15)
sleep(1)
print("==> TRANSPORTANDO OBJETO...")
setCodo(10, 6)
setAnte(20, 10)
setCodo(20, 10)
setAnte(40, 10)
setCodo(40, 10)
setAnte(65, 10)
setCodo(60, 10)
setAnte(90, 10)
setCodo(70, 10)
sleep(0.5)
setBase(0, 10)
sleep(0.5)
setCodo(90, 10)
sleep(0.5)
setBase(90, 10)
sleep(0.5)
setCodo(65, 10)
sleep(0.5)
setCodo(10, 10)
sleep(0.5)
setAnte(0, 10)
setCodo(65, 10)
print("==> DEJARÉ EL OBJETO...")
sleep(1)
setHand(55, 18)
print("==> VOLVIENDO...")
sleep(0.5)
setAnte(90, 8)

# RESET =====================================================================================
sleep(2)
setHand(0, 10)
sleep(0.1)
setBase(50, 10)
sleep(0.1)
setAnte(0, 10)
sleep(0.1)
setCodo(65, 10)

# FINALLY ===================================================================================
sleep(2)
base.stop()
ante.stop()
codo.stop()
hand.stop()
GPIO.cleanup()
print("====> GOODBYE BRO!!!")
