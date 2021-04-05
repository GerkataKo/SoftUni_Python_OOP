import unittest

from project.student import Student


class StudentTest(unittest.TestCase):
    def setUp(self):
        self.student = Student('Pesho', {'Python Advanced': [], 'Python OOP': []})

    def test_student__when_courses_none(self):
        self.student = Student('Pesho', None)
        self.assertEqual('Pesho', self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_student__when_courses(self):
        self.assertEqual('Pesho', self.student.name)
        self.assertEqual({'Python Advanced': [], 'Python OOP': []}, self.student.courses)

    def test_student_enroll__when_course_exists_update_notes(self):
        actual_result = self.student.enroll('Python OOP', ['Encapsulation'], '')
        expected_result = "Course already added. Notes have been updated."
        self.assertEqual(['Encapsulation'], self.student.courses['Python OOP'])
        self.assertEqual(expected_result, actual_result)

    def test_student_enroll__when_course_not_exists_with_notes_empty(self):
        actual_result = self.student.enroll('Python Fundamentals', ['RegEx'], '')
        expected_result = "Course and course notes have been added."
        self.assertEqual(['RegEx'], self.student.courses['Python Fundamentals'])
        self.assertEqual(expected_result, actual_result)

    def test_student_enroll__when_course_not_exists_with_notes_y(self):
        actual_result = self.student.enroll('Python Fundamentals', ['RegEx'], 'Y')
        expected_result = "Course and course notes have been added."
        self.assertEqual(['RegEx'], self.student.courses['Python Fundamentals'])
        self.assertEqual(expected_result, actual_result)

    def test_student_enroll__when_course_not_exists_without_notes(self):
        actual_result = self.student.enroll('Python Basics', None, 'N')
        expected_result = "Course has been added."
        self.assertEqual([], self.student.courses['Python Basics'])
        self.assertEqual(expected_result, actual_result)

    def test_student_add_notes_success(self):
        actual_result = self.student.add_notes('Python OOP', 'Defining classes')
        expected_result = "Notes have been updated"
        self.assertEqual(expected_result, actual_result)

    def test_student_add_notes_course_not_in_courses_expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.student.add_notes('Python Basics', 'Encapsulation')
        expected_result = "Cannot add notes. Course not found."
        self.assertEqual(expected_result, str(context.exception))

    def test_student_leave_course_success(self):
        actual_result = self.student.leave_course('Python OOP')
        expected_result = "Course has been removed"
        self.assertTrue('Python OOP' not in self.student.courses)
        self.assertEqual(expected_result, actual_result)

    def test_student_leave_course_expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.student.leave_course('Python Basics')
        expected_result = "Cannot remove course. Course not found."
        self.assertEqual(expected_result, str(context.exception))


if __name__ == '__main__':
    unittest.main()