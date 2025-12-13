from RPLCD.i2c import CharLCD
import time
temp = False

lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)

char_o_with_dots    = (0b01010,0b00000,0b01110,0b10001,0b10001,0b10001,0b01110,0b00000)
char_u_with_dots    = (0b01010,0b00000,0b10001,0b10001,0b10001,0b10001,0b01110,0b00000)
char_heart          = (0b00000,0b01010,0b10101,0b10001,0b01010,0b00100,0b00000,0b00000)
char_heart_fill     = (0b00000,0b01010,0b11111,0b11111,0b01110,0b00100,0b00000,0b00000)
char_degree 		= (0b01110,0b10001,0b10001,0b10001,0b01110,0b00000,0b00000,0b00000)

lcd.create_char(0, char_o_with_dots)
lcd.create_char(1, char_u_with_dots)
lcd.create_char(2, char_heart)
lcd.create_char(3, char_heart_fill)
lcd.create_char(4, char_degree)

def writeTemperatureText(message, message2, queue):
    global temp
    queue.put("\n")
    if temp == False:
        time.sleep(3)
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string(message)
        lcd.cursor_pos = (1, 0)
        lcd.write_string(message2)
        temp = True
        

def writeText(message, queue):
    global temp
    if "\n" in message:
        newMessage = message.split("\n")
        writeTemperatureText(newMessage[0], newMessage[1], queue)
        return

    temp = False
    lcd.clear()
    lcd.cursor_pos = (0, 0)

    if len(message) <= 16:
        lcd.write_string(message)
        return

    first = message[:16]

    if len(message) <= 32:
        second = message[16:]
    else:
        second = message[16:32]

    lcd.write_string(first)
    lcd.cursor_pos = (1, 0)
    lcd.write_string(second)
    time.sleep(1)

def startLedScreen(queue):
    while True:
        message = queue.get()
        writeText(message, queue)
        time.sleep(0.5)
        queue.task_done()
