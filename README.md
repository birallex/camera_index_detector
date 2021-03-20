# camera_index_detector
This script allows to detect cameras index due to opencv2


## Описание

Данный скрипт позволяет получить номера девайсов для cv2, благодаря чему можно с лёгкостью получить изображение.

Скрипт `demonstration.py` cлужит для вывода номеров устройств в терминал и является прородителем для `stream_devices_detector.py`.

В результате запуска `demonstration.py` вы можете получить детальный вывод в консоль об отсутсвии устройств по определённым номерам, либо об их присутствии.

Скрипт `stream_devices_detector.py` является самобытной реализацией, дающей на выходе python list с номерами обнаруженных устройств, а также позволящией задавать максимальный диапазон для поиска устройств.

## Пример работы скрипта `demonstration.py`:

<p align="center">    
<img src="https://github.com/birallex/camera_index_detector/blob/main/example.png"/>
</p>

## Требования

Установленный `OpenCV 2.x` ^_^
