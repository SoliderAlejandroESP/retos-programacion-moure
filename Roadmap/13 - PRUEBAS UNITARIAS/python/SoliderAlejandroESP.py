import unittest

"""
Ejercicio
"""

def sum(a, b):
  if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    raise ValueError("Los argumentos deben de ser de tipo entero o decimales.")
  return a + b

class TestSum(unittest.TestCase):
  def test_sum(self):
    self.assertEqual(sum(2, 2), 4)
    self.assertEqual(sum(3, 2), 5)
    self.assertEqual(sum(-1, -2), -3)
    self.assertEqual(sum(0, 0), 0)
  
  def test_sum_type(self):
    with self.assertRaises(ValueError):
      sum("5", 7)
    with self.assertRaises(ValueError):
      sum(5, "7")
    with self.assertRaises(ValueError):
      sum("5", "7")
    with self.assertRaises(ValueError):
      sum("a", 7)
    with self.assertRaises(ValueError):
      sum(None, 7)


"""
Extra
"""

class TestDictionary(unittest.TestCase):
  def setUp(self):
    self.dictionary = {
      "name": "Alejandro",
      "age": 19,
      "birth_date": "23/09/2004",
      "programming_languages": ["Python", "JavaScript", "C#", "C++", "Java", "C"]
    }

  def test_fields(self):
    self.assertIn("name", self.dictionary)
    self.assertIn("age", self.dictionary)
    self.assertIn("birth_date", self.dictionary)
    self.assertIn("programming_languages", self.dictionary)
  
  def test_values(self):
    self.assertIsInstance(self.dictionary["name"], str)
    self.assertIsInstance(self.dictionary["age"], int)
    self.assertIsInstance(self.dictionary["birth_date"], str)
    self.assertIsInstance(self.dictionary["programming_languages"], list)

unittest.main()