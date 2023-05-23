# Countdown Time till Date

This repository contains a simple Python script that allows you to calculate the remaining time until a specific deadline. It takes a goal and a deadline as input from the user and provides the time remaining in hours.

## How to Use

1. Clone the repository to your local machine using the following command:

   ```
   git clone https://github.com/your-username/Countdown-Time-till-Date.git
   ```

2. Navigate to the project directory:

   ```
   cd Countdown-Time-till-Date
   ```

3. Make sure you have Python installed on your machine. If not, you can download and install Python from the official website: [python.org](https://www.python.org/).

4. Run the script by executing the following command:

   ```
   python countdown.py
   ```

5. Follow the on-screen instructions and enter your goal and deadline in the format `goal:deadline`. The deadline should be in the format `dd.mm.yyyy`.

6. The script will calculate the remaining time until the deadline and display it in hours.

## Example

```
Enter your goal with a deadline separated by colon
Learn a new language:15.07.2023

Dear user! Time remaining for your goal to Learn a new language is 1296 hours
```

## Customization

You can easily customize the script according to your needs. For example, if you prefer to display the remaining time in days instead of hours, follow these steps:

1. Open the `countdown.py` file in a text editor.

2. Comment out or remove the line `hours_till = int(time_till.total_seconds() / 60 / 60)`.

3. Uncomment or add the line `days_till = time_till.days` below.

4. Replace `int(hours_till)` in the print statement with `days_till`.

5. Save the file.

Now, when you run the script, it will display the remaining time in days instead of hours.

## Contributions

Contributions to this project are welcome. If you find any issues or want to suggest improvements, please open an issue or submit a pull request.

Happy countdown-ing!
