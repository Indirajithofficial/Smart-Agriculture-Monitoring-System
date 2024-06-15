# Smart-Agriculture-Monitoring-System

## Overview
This project aims to optimize water usage and improve crop health using IoT sensors and Azure services.

## Setup Instructions
1. Clone the repository.
2. Install necessary dependencies: `pip install -r requirements.txt`
3. Configure Azure IoT Hub, Stream Analytics, Custom Vision, and Cosmos DB with your credentials.
4. Run the sensor data collection script: `python src/sensor_data_collection.py`
5. Run the data processing script: `python src/data_processing.py`
6. Run the image analysis script: `python src/image_analysis.py`
7. Start the dashboard: `python src/app.py`

## Usage
- Monitor real-time sensor data.
- Analyze crop images for disease detection.
- View insights and recommendations on the dashboard.

## Azure Services Used
- Azure IoT Hub
- Azure Stream Analytics
- Azure Functions
- Azure AI Custom Vision
- Power BI Embedded (for dashboards)
