import requests

API_KEY = "55977157-8bf3-4ff9-90c1-5042f42f6460"
team_name=input("Enter team name: ")

url = f"https://api.cricapi.com/v1/currentMatches?apikey={API_KEY}&offset=0"

response = requests.get(url)
data = response.json()

if data["status"] != "success":
    print("Error:", data.get("message"))
else:
    matches = data["data"]
    live_found = False
    print(f"\n🏏 LIVE MATCHES FOR {team_name.upper()}:\n")



    for match in matches:
        # Check if match is live
        if "live" in match["status"].lower():
            live_found = True

            print("Match:", match["name"])
            print("Status:", match["status"])

            if match["score"]:
                for innings in match["score"]:
                    print(
                        f"{innings['inning']} - "
                        f"{innings['r']}/{innings['w']} "
                        f"({innings['o']} overs)"
                    )
            else:
                print("No score available")

            print("-" * 40)

    if not live_found:
        print("No live matches right now. ")