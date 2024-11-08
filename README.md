# Anomaly Detector

This mini project simulates a real-time anomaly detection system by generating a stream of floating-point numbers ranging from -1 to 1. The number of data points generated is defined by user input. Using the Interquartile Range (IQR) method, the project identifies and visualizes outliers, while also saving detected anomalies along with their computed mean in a `.tsv` file.

## Features

- **Data Generation**: Creates a user-defined stream of random floating-point numbers in the range [-1, 1] using normal distribution.
- **Anomaly Detection**: Utilizes IQR (Interquartile Range) methodology, marking any values outside the 1.5 * IQR threshold as outliers.
- **Real-Time Plotting**: Displays a dynamic plot, highlighting outliers as they are detected.
- **Outlier Logging**: Exports all detected outliers and their means to a `.tsv` file for record-keeping.

## Setup Instructions

This code has been tested on Python 3.12.3. Follow these steps to set up and execute the project in a Unix environment:

1. Clone the repository and navigate to the root directory.
2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   ```
3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the project:
   ```bash
   python3 main.py [ITERATIONS]
   ```
   Replace `[ITERATIONS]` with the desired number of data points to generate in a session.

   **Example**:
   ```bash
   python3 main.py 4000
   ```

## Algorithm

This project employs a robust statistical method to detect anomalies:

1. Generates data points with a normal distribution using `np.random.normal`.
2. Calculates the IQR to determine thresholds for detecting outliers:
   - Outliers are defined as points that lie outside `1.5 * (Upper Quartile - Lower Quartile)`.
3. Logs and plots each outlier in real time, providing a visual representation of detected anomalies.

## Dependencies

- Python 3.12.3
- `numpy`
- `matplotlib`
- Any additional packages listed in `requirements.txt`
