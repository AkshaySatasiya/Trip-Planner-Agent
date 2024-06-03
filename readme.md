# 🌍 Trip Planner Crew
Welcome to Trip Planner Crew, an intelligent travel planning application built using Crewai agents. This project aims to help users create detailed travel itineraries, select the best cities for travel, and provide in-depth city guides. The application leverages various AI agents with specific roles to enhance the travel planning experience.

## 📋 Table of Contents
- Project Structure
- Features
- Installation
- Usage
- Agents
- Tasks
- Contributing
- License


## 📁 Project Structure
```
TRIP_PLANNER
│
├── tools
│   ├── calculator_tools.py
│   └── search_tools.py
├── .env
├── .gitignore
├── agents.py
├── main.py
├── readme.md
├── requirements.txt
└── tasks.py
```

## ✨ Features
### Expert Travel Agent: 
-  Creates travel itineraries including budget, packing suggestions, and safety tips.

### City Selection Expert: 
- Picks the best travel destinations based on weather, season, prices, and traveler interests.

### Local Tour Guide: 
- Provides comprehensive city guides, including key attractions, local customs, and hidden gems.

## 🔨 Installation
Clone the repository:

```
git clone https://github.com/yourusername/trip_planner_crew.git
cd trip_planner_crew
``` 

Set up a virtual environment:

```
python -m venv venv
source venv/bin/activate  
```
Install the required packages:

```
pip install -r requirements.txt
```

Set up environment variables:

- Rename .env.example to .env and configure your API keys and other settings.

## 🚀 Usage
Run the application:

```
python main.py
```

Follow the prompts to input your travel details, and let the AI agents handle the rest!

## 🤖 Agents

### Expert Travel Agent
- Role: Expert in travel planning and logistics.
- Goal: Create travel itinerary with detailed per-day plans, including budget, packing suggestions, and safety tips.
- Tools: SearchTools.search_internet, CalculatorTools.calculate

### City Selection Expert
- Role: Expert at analyzing travel data to pick ideal destinations.
- Goal: Select the best cities based on weather, season, prices, and traveler interests.
- Tools: SearchTools.search_internet

### Local Tour Guide
- Role: Knowledgeable local guide with extensive information about the city, its attractions, and customs.
- Goal: Provide the best insights about the selected city.
- Tools: SearchTools.search_internet, CalculatorTools.calculate


## 📋 Tasks

### Plan Itinerary
- Description: Develop travel itinerary with detailed per-day plans, including weather forecasts, places to eat, packing suggestions, and a budget breakdown.
- Parameters: City, Trip Date, Traveler Interest
### Identify City
- Description: Analyze and select the best city for the trip based on specific criteria such as weather patterns, seasonal events, and travel costs.
- Parameters: Origin, Cities, Travel Date, Interests
### Gather City Info
- Description: Compile an in-depth guide for someone traveling to the city, including key attractions, local customs, special events, and daily activity recommendations.
- Parameters: City, Travel Date, Interests


## 🤝 Contributing
We welcome contributions! Please read our Contributing Guidelines for more details.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.