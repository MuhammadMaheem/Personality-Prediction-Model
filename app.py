from core.personality import Personality

def main():
    app = Personality()

    print("\n--- Personality Predictor ---")
    print("Answer the following questions:\n")

    time_spent_alone = float(input("Time Spent alone (Hours/Day): "))
    stage_fear = input("Do you have Stage Fear? (Yes/No): ").strip().lower()
    social_event_attendance = int(input("Social Event Attendance (Events/Month): "))
    going_outside = int(input("Do you like to go outside? (1 = Not at all, 10 = Love it): "))
    drained_after_socializing = input("Do you feel drained after socializing? (Yes/No): ").strip().lower()
    friends_circle = int(input("How many friends do you have?: "))
    post_frequency = int(input("Social Media Post Frequency (Posts/Month): "))

    input_data = {
        "TimeSpentAlone": time_spent_alone,
        "StageFear": 1 if stage_fear == "yes" else 0,
        "SocialEventAttendance": social_event_attendance,
        "GoingOutside": going_outside,
        "DrainedAfterSocializing": 1 if drained_after_socializing == "yes" else 0,
        "FriendsCircleSize": friends_circle,
        "PostFrequency": post_frequency
    }

    personality = app.predict(input_data)
    print(f"\nYour Personality is: {personality}")
    if personality == "Introvert":
        print("Nigga Get a Life and touch Some Grass")
    else:
        print("You are more outgoing and gain energy from interacting with others.")


if __name__ == "__main__":
    main()
