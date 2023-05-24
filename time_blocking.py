#Time blocking is a way of executing your daily schedule to be the most productive possible. It is easy to run into distractions and funnel too much or too
#little time into a project that could be done much more efficiently with focused concentration. Elon Musk is a great example of someone who sees the benefit 
#of using this method. Although this schedule is much broader than it could be, it is a great way to start using time blocking and will work for a wide range 
#of people.

class Time_blocking:
    def __init__(self, exercise, breakfast, studying, lunch, activity, next_topic, dinner):
        self.exercise = exercise
        self.breakfast = breakfast
        self.studying = studying
        self.lunch = lunch 
        self.activity = activity
        self.next_topic = next_topic
        self.dinner = dinner



    def outline(self):
        return(f"You will wake up at 8am, at 8:30am, partake in {self.exercise} for exercise, at 10am, eat {self.breakfast}, then study {self.studying} for 2 hours. Next up is a {self.lunch} for lunch at 12pm followed by {self.activity} at 1pm with more studying of {self.next_topic} to follow. Finally, having {self.dinner} for dinner at 5pm. The rest of the night is yours to do as you please.")

person1 = Time_blocking("running", "eggs", "geography", "sandwich", "drawing", "mathmatics", "pasta")
person2 = Time_blocking("eliptical", "pancakes", "science", "cup of soup", "horse riding", "politics", "casserole")
person3 = Time_blocking("biking", "cereal", "writing", "blt", "painting", "writing", "bagel")
print(person1.outline())
print(person2.outline())
print(person3.outline())
