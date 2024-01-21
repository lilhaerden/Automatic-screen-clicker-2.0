## AutoClicker

This auto-clicker tool checks if a specific desktop image is present on the screen and clicks on it if found.

### Usage

1. **Python Version**: It is recommended to use Python 3.

2. **Installation of Required Modules**: The program will automatically install the necessary modules for it to function. Therefore, there is no need to manually install the modules.

3. **Running the Program**: Start the program by running the `autoclicker.py` file. The program will wait for a specific image on the desktop and click on it when found.

    ```bash
    python autoclicker.py
    ```

4. **Usage Steps**:

    - First, you will be prompted to enter the name of an image on the desktop (e.g., "image.png" or "image.jpg").
    - When the program finds the image, it will display a "Image found!" message and click on the image.
    - If the program cannot find the image, it will display "Image not found. Continuing..." and check again after a certain period.

### Notes

- It is important to correctly enter the file name and extension of the image for the program to recognize it.
- Adequate confidence levels are specified for the program to identify the image's position on the screen. If the program cannot find the image, adjusting the confidence level may be necessary.
