SCORING_RULES = {
    "cgpa_ace": 20,           # CGPA >= 3.75
    "cgpa_good": 15,          # CGPA >= 3.00
    "income_low": 20,         # isi rumah < RM2000
    "income_mid": 10,
    "cocu": 5                # Active in co-curricular activities
}

value = {
    "cgpa_ace": 3.75,
    "cgpa_good": 3.00,
    "income_low": 2000,
    "income_mid": 4000
}

qualify = 30

def calculate_score(cgpa, income, cocu):
    score = 0

    if cgpa >= value["cgpa_ace"]:
        score += SCORING_RULES["cgpa_ace"]
    elif cgpa >= value["cgpa_good"]:
        score += SCORING_RULES["cgpa_good"]

    if income < value["income_low"]:
        score += SCORING_RULES["income_low"]
    elif income < value["income_mid"]:
        score += SCORING_RULES["income_mid"]
    if cocu:
        score += SCORING_RULES["cocu"]

    return score

def is_qualified(cgpa, income, cocu):
    return calculate_score(cgpa, income, cocu) >= qualify

class Student:
    def __init__(self, name, cgpa, income, cocu):
        self.name = name
        self.cgpa = cgpa
        self.income = income
        self.cocu = cocu

    def calculate_score(self):
        return calculate_score(self.cgpa, self.income, self.cocu)

    def describe(self):
        return (
            "CGPA: " + str(self.cgpa) +
            "\nIsi Rumah: RM" + str(self.income) +
            "\nKokurikulum: " + str(self.cocu)
        )

class Application(Student):
    def __init__(self, name, cgpa, income, cocu):
        super().__init__(name, cgpa, income, cocu)
        self.score = self.calculate_score()

    def application_status(self):
        if self.score >= qualify:
            return f"Application Status: Approved (Score: {self.score})"
        else:
            return f"Application Status: Denied (Score: {self.score})"