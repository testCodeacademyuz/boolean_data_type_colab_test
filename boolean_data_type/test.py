import requests
import math

class CheckSolution:
    def __init__(self, task_name):
        self.task_name = task_name
        self.url = "https://calms.pythonanywhere.com/reporter/attempt/"
    
    def checking(self, tg_username, isSolved, homework_name):
        data = {
            "tg_username": tg_username,
            "assignment_name": homework_name,
            "task_name": self.task_name,
            "is_correct": isSolved
        }
        # print(data)
        response = requests.post(self.url, data=data)
        if isSolved:
            # done emoji
            print("✅ Accepted")
        else:
            # fail emoji
            print("❌ Failed")
        if response.status_code == 404:
            print("❗️ Siz kursga ro'yxatga olinmagansiz!")
        elif response.status_code == 201:
            print("❕ Sizning javobingiz muvafaqqiyatli yuborildi!")
        else:
            print("Sizda noma'lum xatolik yuz berdi!")
    

# input 4, 4 output True, input 4, 5 output False, input -3, 3 output False, input 0, 0 output True
class TaskOne(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        answer = solution(4, 4)
        expected = True

        result = {
            "input": ["4", "4"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        answer = solution(4, 5)
        expected = False

        result = {
            "input": ["4", "5"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_3(self, solution):
        answer = solution(-3, 3)
        expected = False

        result = {
            "input": ["-3", "3"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_4(self, solution):

        answer = solution(0, 0)
        expected = True

        result = {
            "input": ["0", "0"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution)
        ]

        isSolved = [test_case["isSolved"] for test_case in test_cases]
        isSolved = all(isSolved)
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)
        
        for i, test_case in enumerate(test_cases, 1):
            # is solve emoji
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case["isSolved"]:
                print(f"Input: {', '.join(test_case['input'])}")
                print(f"Output: {test_case['answer']}")
                print(f"Expected: {test_case['expected']}\n")

# TaskTwo
# check the following statement "The variable 'a' is equal 7"
# input 7, output True, input 8, output False
class TaskTwo(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        answer = solution(7)
        expected = True

        result = {
            "input": ["7"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        answer = solution(8)
        expected = False

        result = {
            "input": ["8"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution)
        ]

        isSolved = [test_case["isSolved"] for test_case in test_cases]
        isSolved = all(isSolved)
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)

        for i, test_case in enumerate(test_cases, 1):
            # is solve emoji
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case["isSolved"]:
                print(f"Input: {', '.join(test_case['input'])}")
                print(f"Output: {test_case['answer']}")
                print(f"Expected: {test_case['expected']}\n")

# TaskThree
# check the following statement "The variable "b" is positive"
# input 4, output True, input -3, output False, input 0, output False
class TaskThree(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        answer = solution(4)
        expected = True

        result = {
            "input": ["4"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        answer = solution(-3)
        expected = False

        result = {
            "input": ["-3"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_3(self, solution):
        answer = solution(0)
        expected = False

        result = {
            "input": ["0"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution)
        ]

        isSolved = [test_case["isSolved"] for test_case in test_cases]
        isSolved = all(isSolved)
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)

        for i, test_case in enumerate(test_cases, 1):
            # is solve emoji
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case["isSolved"]:
                print(f"Input: {', '.join(test_case['input'])}")
                print(f"Output: {test_case['answer']}")
                print(f"Expected: {test_case['expected']}\n")
    
# check the following statement "The variable "a" is negative"
# input 4, output False, input -3, output True, input 0, output False
class TaskFour(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        answer = solution(4)
        expected = False

        result = {
            "input": ["4"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        answer = solution(-3)
        expected = True

        result = {
            "input": ["-3"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_3(self, solution):
        answer = solution(0)
        expected = False

        result = {
            "input": ["0"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution)
        ]

        isSolved = [test_case["isSolved"] for test_case in test_cases]
        isSolved = all(isSolved)
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)

        for i, test_case in enumerate(test_cases, 1):
            # is solve emoji
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case["isSolved"]:
                print(f"Input: {', '.join(test_case['input'])}")
                print(f"Output: {test_case['answer']}")
                print(f"Expected: {test_case['expected']}\n")

# check the following statement "The variable "a" is an odd number"
# input 4, output False, input -3, output True, input 7, output True, input 101, output True
class TaskFive(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        answer = solution(4)
        expected = False

        result = {
            "input": ["4"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        answer = solution(-3)
        expected = True

        result = {
            "input": ["-3"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_3(self, solution):
        answer = solution(7)
        expected = True

        result = {
            "input": ["7"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_4(self, solution):
        answer = solution(101)
        expected = True

        result = {
            "input": ["101"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution)
        ]

        isSolved = [test_case["isSolved"] for test_case in test_cases]
        isSolved = all(isSolved)
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)

        for i, test_case in enumerate(test_cases, 1):
            # is solve emoji
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case["isSolved"]:
                print(f"Input: {', '.join(test_case['input'])}")
                print(f"Output: {test_case['answer']}")
                print(f"Expected: {test_case['expected']}\n")

# check the following statement "The variable "a" is an even number"
# input 4, output True, input -3, output False, input 7, output False, input 101, output False
class TaskSix(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    def test_case_1(self, solution):
        answer = solution(4)
        expected = True

        result = {
            "input": ["4"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        answer = solution(-3)
        expected = False

        result = {
            "input": ["-3"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    def test_case_3(self, solution):
        answer = solution(7)
        expected = False

        result = {
            "input": ["7"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_4(self, solution):
        answer = solution(101)
        expected = False

        result = {
            "input": ["101"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution)
        ]

        isSolved = [test_case["isSolved"] for test_case in test_cases]
        isSolved = all(isSolved)
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)

        for i, test_case in enumerate(test_cases, 1):
            # is solve emoji
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case["isSolved"]:
                print(f"Input: {', '.join(test_case['input'])}")
                print(f"Output: {test_case['answer']}")
                print(f"Expected: {test_case['expected']}\n")

# check the following statement "They are not equal"
# input 4, 5, output True, input -3, -3, output False, input -7, 7, output True
class TaskSeven(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)
    def test_case_1(self, solution):
        answer = solution(4, 5)
        expected = True

        result = {
            "input": ["4", "5"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        answer = solution(-3, -3)
        expected = False

        result = {
            "input": ["-3", "-3"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    def test_case_3(self, solution):
        answer = solution(-7, 7)
        expected = True

        result = {
            "input": ["-7", "7"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution)
        ]

        isSolved = [test_case["isSolved"] for test_case in test_cases]
        isSolved = all(isSolved)
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)

        for i, test_case in enumerate(test_cases, 1):
            # is solve emoji
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case["isSolved"]:
                print(f"Input: {', '.join(test_case['input'])}")
                print(f"Output: {test_case['answer']}")
                print(f"Expected: {test_case['expected']}\n")

# check the whole number. It is 0 or positive.
# input 4, output True, input 3.1 output False, input 0, output True, input -7, output False
class TaskEight(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        answer = solution(4)
        expected = True

        result = {
            "input": ["4"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    def test_case_2(self, solution):
        answer = solution(3.1)
        expected = False

        result = {
            "input": ["3.1"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    def test_case_3(self, solution):
        answer = solution(0)
        expected = True

        result = {
            "input": ["0"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_4(self, solution):
        answer = solution(-7)
        expected = False

        result = {
            "input": ["-7"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution)
        ]

        isSolved = [test_case["isSolved"] for test_case in test_cases]
        isSolved = all(isSolved)
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)

        for i, test_case in enumerate(test_cases, 1):
            # is solve emoji
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case["isSolved"]:
                print(f"Input: {', '.join(test_case['input'])}")
                print(f"Output: {test_case['answer']}")
                print(f"Expected: {test_case['expected']}\n")

# Check if an input is number which are used in counting.
# input 4, output True, input 3.1 output False, input 0, output False, input -7, output False, input 1, output True
class TaskNine(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        answer = solution(4)
        expected = True

        result = {
            "input": ["4"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    def test_case_2(self, solution):
        answer = solution(3.1)
        expected = False

        result = {
            "input": ["3.1"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    def test_case_3(self, solution):
        answer = solution(0)
        expected = False

        result = {
            "input": ["0"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_4(self, solution):
        answer = solution(-7)
        expected = False

        result = {
            "input": ["-7"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_5(self, solution):
        answer = solution(1)
        expected = True

        result = {
            "input": ["1"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution),
            self.test_case_5(solution)
        ]

        isSolved = [test_case["isSolved"] for test_case in test_cases]
        isSolved = all(isSolved)
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)
        for i, test_case in enumerate(test_cases, 1):
            # is solve emoji
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case["isSolved"]:
                print(f"Input: {', '.join(test_case['input'])}")
                print(f"Output: {test_case['answer']}")
                print(f"Expected: {test_case['expected']}\n")

# Check that the number "a" is a perfect square.
# input 4, output True, input 3.1 output False, input 0, output True, input 25, output True, input 81 output True
class TaskTen(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        answer = solution(4)
        expected = True

        result = {
            "input": ["4"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        answer = solution(3.1)
        expected = False

        result = {
            "input": ["3.1"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_3(self, solution):
        answer = solution(0)
        expected = True

        result = {
            "input": ["0"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_4(self, solution):
        answer = solution(25)
        expected = True

        result = {
            "input": ["25"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_5(self, solution):
        answer = solution(81)
        expected = True

        result = {
            "input": ["81"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution),
            self.test_case_5(solution)
        ]

        isSolved = [test_case["isSolved"] for test_case in test_cases]
        isSolved = all(isSolved)
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)

        for i, test_case in enumerate(test_cases, 1):
            # is solve emoji
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case["isSolved"]:
                print(f"Input: {', '.join(test_case['input'])}")
                print(f"Output: {test_case['answer']}")
                print(f"Expected: {test_case['expected']}\n")

q1 = TaskOne("bool01", "boolean_data_type")
q2 = TaskTwo("bool02", "boolean_data_type")
q3 = TaskThree("bool03", "boolean_data_type")
q4 = TaskFour("bool04", "boolean_data_type")
q5 = TaskFive("bool05", "boolean_data_type")
q6 = TaskSix("bool06", "boolean_data_type")
q7 = TaskSeven("bool07", "boolean_data_type")
q8 = TaskEight("bool08", "boolean_data_type")
q9 = TaskNine("bool09", "boolean_data_type")
q10 = TaskTen("bool10", "boolean_data_type")

# def main10(a):
#     # Check that the number "a" is a perfect square.
#     return int(math.sqrt(a)) ** 2 == a

# q10.check(main10, "JavohirJalilov")