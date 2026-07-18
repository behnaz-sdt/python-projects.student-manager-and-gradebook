from assessment import Assessment

class Project(Assessment):
    def display_info(self):
        print(f"Project: {self.title}- Max score: {self.max_score}")

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 60:
            return "Project completed successfully."
        else:
            return "Project needs improvement."