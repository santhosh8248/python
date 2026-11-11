
class Candidate:

    def __init__(self, name, qualification, experience, skills):
        self.name = name
        self.qualification = qualification
        self.experience = experience
        self.skills = skills

    def display_details(self):
        print("\nCandidate Details")
        print("Name:", self.name)
        print("Qualification:", self.qualification)
        print("Experience:", self.experience)
        print("Skills:", self.skills)

    def matching_score(self):
        score = 0

        if self.qualification == "BE":
            score += 20

        if "Python" in self.skills:
            score += 30

        if "SQL" in self.skills:
            score += 20

        if "HTML" in self.skills:
            score += 10

        if self.experience >= 1:
            score += 20

        return score

    def screen_resume(self):
        score = self.matching_score()

        print("Matching Score:", score, "%")

        if score >= 70:
            print("Result: Resume Selected")
        else:
            print("Result: Resume Rejected")


# Creating object
candidate1 = Candidate(
    "Santhosh",
    "BE",
    2,
    ["Python", "SQL", "HTML"]
)

candidate1.display_details()
candidate1.screen_resume()
