from ..models import Professor
from ..course_api.schedule import Schedule as Schedule_API
import ratemyprofessor
from ..course_api.exceptions import DepartmentNotFoundException
from django.db import IntegrityError
import time
#['ALI', 'AMST', 'ANTH', 'ARCG', 'ARAB', 'AHIS', 'ASTR', 'BISC', 'CHEM', 'CLAS', 'COLT', 'CORE', 'CSLC', 'EALC', 'EASC', 'ECON', 'ENGL', 'ENST', 'GSEC', 'FREN', 'FS', 'PHYS', 'POIR', 'PORT', 'POSC', 'PSYC', 'QBIO', 'REL', 'RNR', 'RUSS', 'SLL', 'SOCI', 'SPAN', 'SSCI', 'SSEM', 'USC', 'VISS', 'WRIT', 'ACCT', 'ARCH', 'ACAD', 'IDSN', 'PRIN', 'ACCT', 'BAEP', 'BUAD', 'BUCO', 'DSO', 'FBE', 'GSBA', 'MKT', 'MOR', 'CJ', 'EM', 'HRM', 'HT', 'PJMT', 'CMPP', 'CNTV', 'CTAN', 'CTCS', 'CTIN', 'CTPR', 'CTWR', 'IML', 'CTXA', 'ASCJ', 'CMGT', 'COMM', 'DMM', 'DSM', 'JOUR', 'PR', 'PUBD', 'DANC', 'ADNT', 'DENT', 'COH', 'CBY', 'DHIS', 'DPBL', 'GDEN', 'OFP', 'OFPM', 'OPR', 'THTE', 'THTR', 'EDCO', 'EDHP', 'EDUC', 'EDUE', 'AME', 'ASTE', 'BME', 'CHE', 'CE', 'CSCI', 'DSCI', 'EE', 'EIS', 'ENE', 'ENGR', 'ISE', 'ITP', 'MASC', 'PTE', 'SAE', 'ART', 'CRIT', 'DES', 'WCT', 'GCT', 'SCIN', 'SCIS', 'ARLT', 'SI', 'ARTS', 'HINQ', 'SANA', 'LIFE', 'PSC', 'QREA', 'GPG', 'GPH', 'GESM', 'DCL', 'GERO', 'GRSC', 'LAW', 'ACMD', 'ADSC', 'IAS', 'ANST', 'BIOC', 'CBG', 'DSR', 'HP', 'INTD', 'MBPH', 'MDED', 'MED', 'MEDB', 'MEDS', 'MICB', 'MPHY', 'NIIN', 'OHNS', 'PAIN', 'PATH', 'PBHS', 'PHBI', 'PM', 'PCPA', 'SCRM', 'TRGN', 'ARTL', 'MTEC', 'MSCR', 'MTAL', 'MUCM', 'MUCO', 'MUCD', 'MUEN', 'MUHL', 'MUIN', 'MUJZ', 'MPEM', 'MPGU', 'MPKS', 'MPPM', 'MPST', 'MPVA', 'MPWP', 'MUSC', 'SCOR', 'OT', 'BPMK', 'BPSI', 'CXPT', 'HCDA', 'MPTX', 'PHRD', 'PMEP', 'PSCI', 'RXRS', 'BKN', 'PT', 'AEST', 'HMGT', 'MS', 'NAUT', 'NSC', 'PPD', 'PPDE', 'PLUS', 'RED', 'SWKC', 'SWKO']
class ProfessorPopulator:
    def __init__(self):
        self.rmp_school = ratemyprofessor.get_school_by_name("USC")
        self.tags = ['ALI', 'AMST', 'ANTH', 'ARCG', 'ARAB', 'AHIS', 'ASTR', 'BISC', 'CHEM', 'CLAS', 'COLT', 'CORE', 'CSLC', 'EALC', 'EASC', 'ECON', 'ENGL', 'ENST', 'GSEC', 'FREN', 'FSEM', 'PHYS', 'POIR', 'PORT', 'POSC', 'PSYC', 'QBIO', 'REL', 'RNR', 'RUSS', 'SLL', 'SOCI', 'SPAN', 'SSCI', 'SSEM', 'USC', 'VISS', 'WRIT', 'ACCT', 'ARCH', 'ACAD', 'IDSN', 'PRIN', 'ACCT', 'BAEP', 'BUAD', 'BUCO', 'DSO', 'FBE', 'GSBA', 'MKT', 'MOR', 'CJ', 'EM', 'HRM', 'HT', 'PJMT', 'CMPP', 'CNTV', 'CTAN', 'CTCS', 'CTIN', 'CTPR', 'CTWR', 'IML', 'CTXA', 'ASCJ', 'CMGT', 'COMM', 'DMM', 'DSM', 'JOUR', 'PR', 'PUBD', 'DANC', 'ADNT', 'DENT', 'COH', 'CBY', 'DHIS', 'DPBL', 'GDEN', 'OFP', 'OFPM', 'OPR', 'THTE', 'THTR', 'EDCO', 'EDHP', 'EDUC', 'EDUE', 'AME', 'ASTE', 'BME', 'CHE', 'CE', 'CSCI', 'DSCI', 'EE', 'EIS', 'ENE', 'ENGR', 'ISE', 'ITP', 'MASC', 'PTE', 'SAE', 'ART', 'CRIT', 'DES', 'WCT', 'GCT', 'SCIN', 'SCIS', 'ARLT', 'SI', 'ARTS', 'HINQ', 'SANA', 'LIFE', 'PSC', 'QREA', 'GPG', 'GPH', 'GESM', 'DCL', 'GERO', 'GRSC', 'LAW', 'ACMD', 'ADSC', 'IAS', 'ANST', 'BIOC', 'CBG', 'DSR', 'HP', 'INTD', 'MBPH', 'MDED', 'MED', 'MEDB', 'MEDS', 'MICB', 'MPHY', 'NIIN', 'OHNS', 'PAIN', 'PATH', 'PBHS', 'PHBI', 'PM', 'PCPA', 'SCRM', 'TRGN', 'ARTL', 'MTEC', 'MSCR', 'MTAL', 'MUCM', 'MUCO', 'MUCD', 'MUEN', 'MUHL', 'MUIN', 'MUJZ', 'MPEM', 'MPGU', 'MPKS', 'MPPM', 'MPST', 'MPVA', 'MPWP', 'MUSC', 'SCOR', 'OT', 'BPMK', 'BPSI', 'CXPT', 'HCDA', 'MPTX', 'PHRD', 'PMEP', 'PSCI', 'RXRS', 'BKN', 'PT', 'AEST', 'HMGT', 'MS', 'NAUT', 'NSC', 'PPD', 'PPDE', 'PLUS', 'RED', 'SWKC', 'SWKO']
        self.semesters = ["20231", "20232", "20233", "20221", "20222", "20223", "20211", "20212", "20213", "20201", "20202", "20203"]
    def populate_professors(self):
        schedule_api = Schedule_API()
        professors = set()
        for semester in self.semesters:
            for tag in self.tags:
                print(tag + "\n")
                time.sleep(0.001)
                try:
                    department = schedule_api.get_department(department_id=tag, semester_id=semester)
                    for course in department.courses:
                        professors_in_dept = course.get_professors()
                        for professor in professors_in_dept:
                            professors.add(professor)
                except DepartmentNotFoundException:
                    print(f"didn't find {semester} {tag}")
        for professor in professors:
            rmp_data = self.get_prof_rmp_data(professor)
            if rmp_data == None:
                self.create_professor(professor, rating=None, num_ratings=None, difficulty=None)
            else:
                self.create_professor(professor, rmp_data[0], rmp_data[1], rmp_data[2])
            

        

    def get_prof_rmp_data(self, name):
        print(name)
        rmp_prof = ratemyprofessor.get_professor_by_school_and_name(self.rmp_school, name)
        if rmp_prof is None:
            return None
        print(f"{rmp_prof.name} {rmp_prof.department} {rmp_prof.rating} {rmp_prof.num_ratings} {rmp_prof.difficulty} ")
        return (rmp_prof.rating, rmp_prof.num_ratings, rmp_prof.difficulty)


    def create_professor(self, name:str, rating:float, num_ratings:int, difficulty:float):
        profs = Professor.objects.filter(name=name)
        if len(profs) == 0:
            Professor.objects.create(name=name, 
                                    rating=rating, 
                                    num_ratings=num_ratings,
                                    difficulty=difficulty)
        else:
            profs.update(rating=rating, 
                         num_ratings=num_ratings,
                         difficulty=difficulty)
            
            

