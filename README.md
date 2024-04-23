# Electronic Time Clock

This application serves as an electronic time clock for tracking work hours. It allows users to record their entry and exit times, and saves this data to a CSV file.

## Features

- Register entry and exit times with the press of a button.
- Data is saved in a CSV file with columns for the day, entry time, and exit time.
- Runs minimally in the system tray, allowing for easy access without cluttering the desktop.

## Installation

To run this application, you will need Python installed on your system, along with several dependencies.

### Prerequisites

- Windows, Linux, or macOS with support for Python if running from source.
- No additional installations required for running the executable.

### Running the Executable

1. Download the latest release from [GitHub Releases page](https://github.com/yourgithubusername/EletronicDot/releases) or unpack the provided distribution package.
2. Navigate to the `dist/eletronic_point/` directory.
3. Run the executable:
   - On Windows: Double-click `eletronic_point.exe`.
   - On Linux or macOS: Open a terminal and execute `./eletronic_point`.

## From Source

If you prefer to run the application from the source:

### Prerequisites

- Python 3.x
- tkinter
- Pillow
- pystray

### Installing Dependencies

Install the required Python packages using pip:

```bash
pip install Pillow pystray
```

### Running the Application

To start the application, navigate to the folder containing eletronic_point.py and run:


```bash
python3 eletronic_point.py
```

### Usage

*   **Starting the application**: Run the script as mentioned above. The application window will appear with two buttons: "Entrada" (Entry) and "Saída" (Exit).

*   **Registering Entry**: Click the "Entrada" button to record your entry time. The entry button will disappear, and a timer will start showing the elapsed time since entry.

*   **Registering Exit**: Click the "Saída" button to record your exit time and close the application. The data will be saved to `dataset_ponto.csv` in the same directory as the script.

*   **Viewing Records**: Open `dataset_ponto.csv` with any text editor or spreadsheet software to view your time records.


### System Tray Functionality

When minimized, the application resides in the system tray as an icon. Right-click the tray icon to show the application window or quit the application.

## License

This project is licensed under the MIT License - see the LICENSE file for details.



