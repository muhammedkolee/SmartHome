import time
import adafruit_dht
import board
from RPLCD.i2c import CharLCD
from time import sleep

dht_device = adafruit_dht.DHT11(board.D12, use_pulseio=False)

temperature = "None"
humidity = "None"

def startTemperatureSensor(queue, logger):
	count = 0
	while True:
		try:
			temperature = dht_device.temperature
			humidity = dht_device.humidity
			if temperature == None or humidity == None:
				pass
			else:	
				queue.put(f"Sicaklik: {temperature}C\nNem: {humidity}%")
			if count == 600:
				count = 0
				logger.info(f"Sicaklik: {temperature}C\nNem: {humidity}%")
			count += 1
			time.sleep(1)
		except Exception as e:
			logger.error(f"temperatureSensor.py dosyasinda bir hata olustu: {e}")
