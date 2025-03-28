
class Device:
    def __init__(self, topic, mqtt_broker='localhost', port=1883):
        self.topic = topic
        self.topic_list = self.topic.split('/')
        self.group = self.topic_list[1]
        self.device_type = self.topic_list[2]
        self.name = self.topic_list[3]
        self.port = port
        self.mqtt_broker = mqtt_broker
        self.status = 'off'
        self.speed = 0

    def connect_mqtt(self):

        self.mqtt_client.connect(self.mqtt_broker, self.port)
        print(f'{self.name} connected to mqtt')

    def setup_gpio(self):
        if self.device_tye == 'lights':
            GPIO.setup(17, GPIO.OUT)
            print(f'{self.name} connected to gpio')

        elif self.device_type == 'doors':
            GPIO.setup(27, GPIO.OUT)
            print(f'{self.name} connected to gpio')

        elif self.device_type == 'fans':
            GPIO.setup(22, GPIO.OUT)
            if self.speed > 0:
                GPIO.setup(18, GPIO.OUT)  # For fan speed, if using PWM
                print(f'{self.name} connected to gpio')
            elif self.device_type == 'fire_water':
                GPIO.setup(21, GPIO.OUT)
        
        elif self.device_type == 'fire_water':
            GPIO.setup(21, GPIO.OUT)
            print(f'{self.name} connected to gpio')
            
    def turn_on(self):
        self.status = 'on'
        print(f'{self.name} is turned on')
        if self.device_type == 'lights':
            pass

        elif self.device_type == 'doors':
            pass

        elif self.device_type == 'fans':
            pass

        elif self.device_type == 'fire_water':
            pass

    def set_speed(self, speed):

        if self.status == 'off':
            print(f'{self.name} currently is off')
            return None

        else:
            self.speed = speed

    def turn_off(self):
        self.status = 'off'
        print(f'{self.name} is turned off')

        if self.device_type == 'lights':
            pass

        elif self.device_type == 'doors':
            pass

        elif self.device_type == 'fans':
            pass

        elif self.device_type == 'fire_water':
            pass
            
    def get_status(self):
        return self.status

    def send_command(self, command):
        self.mqtt_client.publish(self.topic, command)
        print(f'command {command} send to topic {self.topic}')
        self.topic = topic

        self.topic_list = self.topic.split('/')


a1 = Device('home/living_room/lamps/lamp45')

a1.name

a1.group

a1.turn_on()

a1.get_status()

a1.turn_off()

a1.get_status()

a2 = Device('home/kitchen/fire_water/FW1')
a2.name
print(a2.group)
a2.turn_on()
a2.get_status()
a2.turn_off()
a2.get_status()

