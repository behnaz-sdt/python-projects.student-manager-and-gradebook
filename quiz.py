from assessment import Assessment

class Quiz(Assessment):
    def display_info(self):
        print(f"Quiz{self.title}- Max score: {self.max_score}")