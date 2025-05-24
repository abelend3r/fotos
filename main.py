import os
from agent import TimeAgent

def main():
    api_key = os.environ.get("GOOGLE_API_KEY")

    if api_key is None:
        print("Error: GOOGLE_API_KEY environment variable not set.")
        return  # Exit the function, effectively exiting the script if main() is the entry point

    agent = TimeAgent(api_key=api_key)

    while True:
        city = input("Enter city name (or type 'exit' to quit): ")
        if city.lower() in ['exit', 'quit']:
            print("Exiting...")
            break
        
        time_response = agent.get_local_time(city)
        print(time_response)

if __name__ == "__main__":
    main()
