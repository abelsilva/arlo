import os

from Arlo import Arlo

USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']

try:
    # Instantiating the Arlo object automatically calls Login(), which returns an oAuth token that gets cached.
    # Subsequent successful calls to login will update the oAuth token.
    arlo = Arlo(USERNAME, PASSWORD)
    # At this point you're logged into Arlo.

    # Get the list of devices.
    devices = arlo.GetDevices()

    # Filter on device type to only get the cameras.
    # This will return an array which includes all of the cameras and their associated metadata.
    cameras = [ device for device in devices if device['deviceType'] == 'camera' ]

    # Take the snapshot.
    arlo.TakeSnapshot(cameras[0]['parentId'], cameras[0]['deviceId'], cameras[0]['xCloudId'], cameras[0]['properties']['olsonTimeZone']);

except Exception as e:
    print (e)
