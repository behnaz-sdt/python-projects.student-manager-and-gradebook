from assessment import Assessment

class Project(Assessment):
    def display_info(self):
        print(f"Project: {self.title}- Max score: {self.max_score}")