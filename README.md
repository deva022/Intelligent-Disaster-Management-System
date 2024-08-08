# Intelligent Disaster Management System

## Overview

The Intelligent Disaster Management System is a comprehensive solution designed to predict disasters, allocate resources, determine the shortest routes for emergency responders, and facilitate communication among the various stakeholders involved. The system integrates several components, each responsible for a crucial aspect of disaster management, creating an efficient and responsive workflow.

## Features

- **Real-time Data Collection**: Collects live data from external APIs (e.g., weather data) to assess current conditions.
- **Disaster Prediction**: Utilizes a machine learning model to predict the likelihood of disasters based on the collected data.
- **Resource Allocation**: Automatically allocates resources, such as rescue teams and medical supplies, in response to predicted disasters.
- **Emergency Routing**: Implements Dijkstra's algorithm to find the shortest and safest path for emergency responders.
- **Communication**: Manages communication between dispatchers and emergency teams to ensure coordinated efforts.

## Project Structure

The project is organized into the following modules:

- **`data_collection.py`**: Handles the collection of data, such as weather conditions, using external APIs.
- **`disaster_prediction.py`**: Contains the machine learning model used to predict disasters. The model is trained on historical data to identify patterns that indicate the likelihood of a disaster.
- **`resource_allocation.py`**: Simulates the allocation of resources based on the predictions made by the model.
- **`emergency_routing.py`**: Manages the graph data structure used to represent the map and computes the shortest path between locations using Dijkstra’s algorithm.
- **`communication.py`**: Manages the communication channels between different entities, sending out alerts and instructions during disaster scenarios.
- **`dashboard.py`**: Integrates all the components and coordinates the overall workflow. It collects data, makes predictions, allocates resources, determines routes, and sends communication messages.
- **`main.py`**: The entry point of the application, which initiates the system by running the dashboard.

## Installation

To get started with the project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/intelligent-disaster-management.git
   cd intelligent-disaster-management
    ```

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up your API keys**:
   Create a .env file in the root directory of the project and add your API key(s) for the data collection module. For example:
   ```bash
   API_KEY=your_actual_api_key
   ```
Thankyou !

