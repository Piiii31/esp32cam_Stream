# ESP32-CAM Streaming with Django

This repository contains a Django application that streams video frames from an ESP32-CAM module. The application captures frames from the camera and serves them in real-time, allowing users to view the live video stream through a web interface.

## :dart: About ##

The **ESP32-CAM Streaming with Django** project is designed to demonstrate how to capture and stream video frames from an ESP32-CAM to a web application. This integration provides users with the ability to monitor their surroundings remotely and in real-time.

## :sparkles: Features ##

- **Real-time Video Streaming**: Stream live video frames captured by the ESP32-CAM.
- **Web Interface**: A simple and responsive web interface for viewing the video stream.
- **Django Backend**: Utilizes Django to handle the streaming and web requests.

## :rocket: Technologies ##

The following technologies were used to build this project:

- [Django](https://www.djangoproject.com/)
- [Python](https://www.python.org/)
- [ESP32-CAM](https://www.espressif.com/en/products/hardware/esp32/overview)

## :white_check_mark: Requirements ##

To run this project, you'll need:

- [Python](https://www.python.org/) installed on your machine.
- Basic knowledge of Django and video streaming.

## :checkered_flag: Running the Project ##

1. Clone the repository to your local machine:

    ```bash
    $ git clone https://github.com/Piiii31/esp32cam_Stream.git
    ```

2. Navigate to the project directory:

    ```bash
    $ cd esp32cam_Stream
    ```

3. Install the dependencies:

    ```bash
    $ pip install -r requirements.txt
    ```

4. Configure your ESP32-CAM to connect to your Wi-Fi network and set the correct streaming URL in your Django application.

5. Run the Django server:

    ```bash
    $ python manage.py runserver
    ```

6. Access the application at `http://localhost:8000/` to view the live video stream.



## :handshake: Contributions ##

Contributions are welcome! Feel free to open an issue or submit a pull request.

## :mailbox_with_mail: Contact ##

For any inquiries, feel free to reach out: [Piiii31](mailto:meddeb65@gmail.com)

---

<p align="center">
  Made with :heart: by <a href="https://github.com/Piiii31" target="_blank">Piiii31</a>
</p>
