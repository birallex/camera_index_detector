import cv2


def get_video_devices(min_device_number = 0, max_device_number = 20):
    list_of_founded_devices = []
    for device_number in range(min_device_number, max_device_number):
        cap = cv2.VideoCapture(device_number)
        if cap is None or not cap.isOpened():
            pass
        else:
            list_of_founded_devices.append(device_number)
        del cap
    return list_of_founded_devices


if __name__ == '__main__':
    print("Found devices: ", get_video_devices())