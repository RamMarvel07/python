employee1_skills = {"Python", "SQL", "Machine Learning", "Docker"}
employee2_skills = {"Java", "SQL", "Docker", "Kubernetes", "Spring Boot"}
print("Employee 1 skills:", employee1_skills)
print("Employee 2 skills:", employee2_skills)
common_skills    = employee1_skills.intersection(employee2_skills)
unique_to_emp1   = employee1_skills.difference(employee2_skills)
unique_to_emp2   = employee2_skills.difference(employee1_skills)
all_skills       = employee1_skills.union(employee2_skills)
print("\nCommon skills              :", common_skills)
print("Skills unique to Employee 1:", unique_to_emp1)
print("Skills unique to Employee 2:", unique_to_emp2)
print("All available skills        :", all_skills)
