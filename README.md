# smart-drainage-system
Sensor-based drainage monitoring and blockage detection for sustainable urban development.
# Smart Drainage System for Sustainable Development

## 1. Project Overview
The Smart Drainage System aims to detect potential drainage blockages and high water levels using sensor-based monitoring. It supports timely action to reduce water stagnation, urban flooding, and plastic waste pollution.

## 2. Problem Statement
Plastic waste and solid materials can block drainage channels, reduce water flow, and cause water stagnation and urban flooding. Early detection helps improve drainage maintenance.

## 3. Proposed Solution
The system monitors water levels and possible blockages using sensors. A microcontroller processes the readings and can trigger an alert when abnormal conditions are detected. A waste collection mechanism can help remove plastic waste.

## 4. Repository Structure
- `src/drainage_monitor.py` — Python drainage-monitoring simulation
- `data/sample_data.csv` — illustrative sample sensor readings
- `docs/architecture.md` — system architecture
- `tests/test_drainage_monitor.py` — automated test cases
- `LICENSE` — MIT License

## 5. Requirements
- Python 3
- No external Python packages are required for the basic simulation and tests.

## 6. Setup and Usage
1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the simulation:

   `python src/drainage_monitor.py`

5. Run the tests:

   `python -m unittest discover -s tests`

## 7. Sample Data
The CSV file contains illustrative water-level readings and blockage flags. These values are examples and are not actual sensor measurements.

## 8. Current Prototype Status
This repository contains a software simulation of drainage monitoring. Physical sensor integration, hardware alerts, and automatic waste removal require further implementation and testing.

## 9. Sustainable Development Goals
- SDG 6: Clean Water and Sanitation
- SDG 11: Sustainable Cities and Communities
- SDG 12: Responsible Consumption and Production
- SDG 13: Climate Action

## 10. License
This project is shared under the MIT License. See the `LICENSE` file for details.
