import cv2


def try_camera(source):
    cap = cv2.VideoCapture(source)
    if cap is None or not cap.isOpened():
        print('Warning: unable to open video source: ', source)
    else:
        print('Device found: ', source)
        return True
    return False


if __name__ == '__main__':
    valid_device = []
    for index in range(0, 50):
        if try_camera(index):
            valid_device.append(index)
    
    print("Found devices: ", valid_device)