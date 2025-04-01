
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

a3 = Device('home/living_room/lamps/lamp40')

a3.name

a3.group

a3.turn_on()

a3.get_status()

a3.turn_off()

a3.get_status()


class AdminPanel:

    def __init__(self):
        self.groups = {}

    def create_group(self, group_name):

        if group_name not in self.groups:
            self.groups[group_name] = []
            print(f'groups {group_name} created')

        else:
            print('yout group name is duplicated name')

    def add_device_to_group(self, group_name, device):
        if group_name in self.groups:
            self.groups[group_name].append(device)
            print(f'device {device} was added to groups {group_name}')

        else:
            print(f'Group {group_name} does not exist')


    def create_device(self, group_name, device_type, name):

        if group_name in self.groups:
            topic = f'home/{group_name}/{device_type}/{name}'
            new_device = Device(topic)
            self.add_device_to_group(group_name, new_device)
            print(f'device {device_type} was created')

        else:
            print(f'Group {group_name} does not exist')


    def create_multiple_devices(self, group_name, device_type, number_of_devices):
        if group_name in self.groups:
            for i in range(1, number_of_devices + 1):
                device_name = f"{device_type}{i}"

                topic = f'home/{group_name}/{device_type}/{device_name.lower()}'

                new_device = Device(topic)

                self.add_device_to_group(group_name, new_device)

            print(f'{number_of_devices} of {device_type} were created in group {group_name}')

        else:
            print(f'Group {group_name} does not exist')



    def get_devices_in_groups(self, group_name):
        if group_name in self.groups:
            return self.groups[group_name]

        else:
            print(f'Group {group_name} does not exist')
            return []

    def turn_on_all_in_group(self, group_name):
        devices = self.get_devices_in_groups(group_name)
        divices_no=0
        for device in devices:
            device.turn_on()
            divices_no += 1
        print(f'{divices_no} devices in group {group_name} are turned on')


    def turn_off_all_in_group(self, group_name):
        devices = self.get_devices_in_groups(group_name)
        divices_no = 0
        for device in devices:
            device.turn_off()
            divices_no += 1
        print(f'{divices_no} devices in group {group_name} are turned off')

    '''''''''''
    def trun_on_all(self):



    def turn_off_all(self):
    
        pass

    def get_status_in_group(self, group_name):

      
        pass

    def get_status_in_device_type(self, device_type):

     
        pass

    def create_sensor(self):
        # bar asase clASS SENSOR argument bzarid
        pass

    def get_status_sensor_in_group(self, group_name):

        pass
'''''''''''

a1 = AdminPanel()

a1.create_group('living_room')
a1.create_multiple_devices('living_room', 'lamps', 40)

a1.turn_on_all_in_group('living_room')

a1.turn_off_all_in_group('living_room')

# check koni bbini roshan

mygroups = a1.groups['living_room']

mygroups[1].name  # lamps2'

mygroups[1].turn_on()

# besazi

