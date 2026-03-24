from recommendation.recommender import recommend_items, generate_itinerary
from llm.explanation_generator import generate_explanation

def print_header():
    print("🕌 Istanbul Guided Recommendation System")
    print("=" * 50)

def show_menu():
    print("\n📍 Main Menu:")
    print("1. Get Personalized Recommendations")
    print("2. Generate Itinerary")
    print("3. Exit")
    return input("Choose an option (1-3): ").strip()

def handle_recommendations(interests):
    print("\n🎯 Getting Recommendations...")
    if not interests:
        print("❌ No interests found. Please enter interests first.")
        return

    recommendations = recommend_items(interests, limit=5)

    if not recommendations:
        print("❌ No recommendations found. Try different interests.")
        return

    print(f"\n✨ Top {len(recommendations)} Recommendations:")
    print("-" * 60)

    for i, rec in enumerate(recommendations, 1):
        explanation = generate_explanation(rec, interests)
        print(f"{i}. 🏛️  {rec['name']}")
        print(f"   Category: {rec['category']}")
        print(f"   Score: ⭐ {rec['hybrid_score']:.3f}")
        print(f"   💡 Why: {explanation}")
        print()



def handle_generate_itinerary(interests):
    print("\n📅 Generate Itinerary")
    if not interests:
        print("❌ No interests found. Please enter interests first.")
        return

    try:
        days = int(input("Enter number of days (1-7): ").strip())
        if not 1 <= days <= 7:
            print("❌ Days must be between 1-7.")
            return
    except ValueError:
        print("❌ Invalid number of days.")
        return

    itinerary = generate_itinerary(interests, days)

    print(f"\n📅 {days}-Day Itinerary")
    print("=" * 50)

    for day, activities in itinerary.items():
        print(f"\n{day}:")
        if activities:
            for activity in activities:
                print(f"  {activity['time']} - {activity['activity']}")
                print(f"    └─ {activity['description']}")
        else:
            print("  No activities planned for this day.")



def main():
    print_header()

    while True:
        interests_input = input("\n🎯 Enter your interests (comma-separated, e.g., history, culture): ").strip()
        interests = [i.strip() for i in interests_input.split(',') if i.strip()]
        
        if interests:
            break
        print("❌ Please enter at least one interest.")

    print(f"✅ Great! Your interests: {', '.join(interests)}")

    while True:
        choice = show_menu()

        if choice == '1':
            handle_recommendations(interests)
        elif choice == '2':
            handle_generate_itinerary(interests)
        elif choice == '3':
            print("\n👋 Goodbye! Safe travels in Istanbul! 🕌")
            break
        else:
            print("❌ Invalid option. Please choose 1-3.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()