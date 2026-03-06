#Problem 1: Contact Manager

class ContactBook:
    def __init__(self):
        self.contacts = {}
    def add_contact(self, name, phone, email):
        self.contacts[name] = {"phone": phone, "email": email}
    def search(self, query):
        query = query.lower()
        results = []
        for name, info in self.contacts.items():
            if query in name.lower() or query in info["phone"].lower() or query in info["email"].lower():
                results.append(name)
        return results
    def merge(self, other_book):
        self.contacts.update(other_book.contacts)
    def export_csv(self):
        lines = []
        for name in sorted(self.contacts):
            info = self.contacts[name]
            lines.append(f"{name},{info['phone']},{info['email']}")
        return "\n".join(lines)
# Test cases
book1 = ContactBook()
book1.add_contact("Alice Smith", "555-1234", "alice@mail.com")
book1.add_contact("Bob Jones", "555-5678", "bob@work.com")
book1.add_contact("Carol White", "555-9999", "carol@mail.com")
# Search
print(book1.search("alice"))
# ['Alice Smith']
print(book1.search("555"))
# ['Alice Smith', 'Bob Jones', 'Carol White']
print(book1.search("mail.com"))
# ['Alice Smith', 'Carol White']
# Merge
book2 = ContactBook()
book2.add_contact("Alice Smith", "555-0000", "alice@new.com") # Updated info
book2.add_contact("Dave Brown", "555-4444", "dave@mail.com") # New contact
book1.merge(book2)
# Export
print(book1.export_csv())
# Alice Smith,555-0000,alice@new.com
# Bob Jones,555-5678,bob@work.com
# Carol White,555-9999,carol@mail.com
# Dave Brown,555-4444,dave@mail.com


print("="*50)
print("="*50)

#Problem 3: Weather Data Analysis


import numpy as np
def weather_analysis(temps_2d):
    city_averages = np.mean(temps_2d, axis=1)
    daily_averages = np.mean(temps_2d, axis=0)
    hottest_day = np.argmax(daily_averages)
    coldest_city = np.argmin(city_averages)
    above_80 = temps_2d > 80
    normalized = (temps_2d - np.min(temps_2d, axis=1, keepdims=True)) / (np.max(temps_2d, axis=1, keepdims=True) - np.min(temps_2d, axis=1, keepdims=True))
    return {
        "city_averages": city_averages,
        "daily_averages": daily_averages,
        "hottest_day": hottest_day,
        "coldest_city": coldest_city,
        "above_80": above_80,
        "normalized": normalized
    }
pass
# Test cases
temps = np.array([
[72, 75, 78, 82, 85, 80, 74], # City 0 (moderate)
[88, 91, 93, 95, 90, 87, 85], # City 1 (hot)
[55, 58, 60, 62, 59, 56, 53], # City 2 (cool)
])
report = weather_analysis(temps)
print("City averages:", report["city_averages"])
# [78. 89.86 57.57] (approximately)
print("Daily averages:", report["daily_averages"])
# [71.67 74.67 77. 79.67 78. 74.33 70.67] (approximately)
print("Hottest day index:", report["hottest_day"])
# 3
print("Coldest city index:", report["coldest_city"])
# 2
print("Above 80 (City 0):", report["above_80"][0])
# [False False False True True False False]
print("Normalized (City 2):", np.round(report["normalized"][2], 2))
# [0.22 0.56 0.78 1. 0.67 0.33 0. ]






