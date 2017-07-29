from pushbullet import Pushbullet

pb = Pushbullet('1234567890')

# push = pb.push_note("This is the title", "This is the body")

# Get all devices that the current user has access to.
# print(pb.devices)
# [Device('Motorola Moto G'), Device('N7'), Device('Chrome')]

# Select a device from the array using indexing
# motog = pb.devices[0]

# Or retrieve a device by its name. Note that an InvalidKeyError is raised if the name does not exist
iphone = pb.get_device('iPhone')

push = iphone.push_note('Still testing...',
                        'Voltage: 3V\nTime: 5 hours\nDisplay: ON')

# push = pb.push_note("Hello world!", "We're using the api.", device=motog)

