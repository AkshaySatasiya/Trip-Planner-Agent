import os
from crewai import Crew
from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks
from dotenv import load_dotenv

load_dotenv()

class TripCrew:
    def __init__(self, origin, cities, date_range, interests):
        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TravelAgents()
        tasks = TravelTasks()

        # Define your custom agents and tasks here
        expert_travel_agent = agents.expert_travel_agent()
        city_selection_expert = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()

        # Custom tasks include agent name and variables as input
        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.cities,
            self.date_range,
            self.interests
        )

        identify_city = tasks.identify_city(
            city_selection_expert,
            self.origin,
            self.cities,
            self.interests,
            self.date_range
        )

        gather_city_info = tasks.gather_city_info(
            local_tour_guide,
            self.cities,
            self.date_range,
            self.interests
        )


        # Define your custom crew here
        crew = Crew(
            agents=[ 
                city_selection_expert,
                local_tour_guide,
                expert_travel_agent
                ],
            tasks=[
                identify_city,
                gather_city_info,
                plan_itinerary
                ],
            verbose=True,
        )

        result = crew.kickoff()
        return result


if __name__ == "__main__":
    print("## Welcome to Trip Planner Crew")
    print('-------------------------------')

    
    origin = input("Origin: ")
    cities  = input("Destination: ")
    date_range = input("Date Range: ")
    interests = input("Enter your Interest: ")
    trip_crew = TripCrew(str(origin), str(cities ), str(date_range), str(interests))
    result = trip_crew.run()


    print("\n\n########################")
    print("## Here is you Trip Plan")
    print("########################\n")
    print(result)