class Student:
    """
    Represents a student with a name, age, and grade.

    Parameters
    ----------
    name : str
        The name of the student.
    age : int
        The age of the student.
    grade : int
        The grade of the student.

    Attributes
    ----------
    name : str
        The name of the student.
    age : int
        The age of the student.
    grade : int
        The grade of the student.
    """

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        """
        Returns the name of the student.

        Returns
        -------
        str
            The name of the student.
        """
        return self.name

    def get_age(self):
        """
        Returns the age of the student.

        Returns
        -------
        int
            The age of the student.
        """
        return self.age

    def get_grade(self):
        """
        Returns the grade of the student.

        Returns
        -------
        int
            The grade of the student.
        """
        return self.grade
        """
        Returns the grade of the student.
        """
        return self.grade

    def set_name(self, name):
        """
        Sets the name of the student.
        """
        self.name = name

    def set_age(self, age):
        """
        Sets the age of the student.
        """
        self.age = age

    def set_grade(self, grade):
        """
        Sets the grade of the student.
        """
        self.grade = grade
