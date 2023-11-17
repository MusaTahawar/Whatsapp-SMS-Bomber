# WhatsApp Message Bomber

WhatsApp Message Sender is a simple Python application that allows users to send WhatsApp messages programmatically using the `pywhatkit` library. This application provides a graphical user interface (GUI) built with the `tkinter` library, enabling users to enter phone numbers, messages, and schedule messages to be sent at specific times.

## Features

- **Send Single Message:** Send a single WhatsApp message to a specified phone number at a specified time.
- **SMS Bomber:** Send multiple messages (spam) to a phone number at specific intervals.

## Requirements

- Python 3.x
- `pywhatkit` library (Install using `pip install pywhatkit`)

## How to Use

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your_username/Whatsapp-SMS-Bomber.git
    cd WhatsApp-Message-Bomber
    ```

2. **Install Dependencies**

    Ensure you have Python installed. Install the required `pywhatkit` library using pip:

    ```bash
    pip install pywhatkit
    ```

3. **Run the Application**

    Execute the Python script `whatsapp_message_bomber.py`:

    ```bash
    python whatsapp_message_bomber.py
    ```

4. **Using the Application**

    - Enter the phone number, message, and the time (in 24-hour format) to schedule the message.
    - Click the **Send Single Message** button to send a single message at the specified time.
    - Use the **SMS Bomber** feature to send multiple messages by specifying the number of times to spam.

5. **Notes**

    - Ensure the device used for running the application is connected to the internet and has WhatsApp installed.
    - The `pywhatkit` library might have limitations or restrictions imposed by WhatsApp. Use responsibly and avoid spamming.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements, bug fixes, or additional features.

## License

This project is licensed under the [MIT License](LICENSE).
