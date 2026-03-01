import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
try:
    from app import app
    FLASK_AVAILABLE = True
except ModuleNotFoundError:
    FLASK_AVAILABLE = False


@unittest.skipUnless(FLASK_AVAILABLE, "Flask is not installed in this environment")
class TestRepeatedEquals(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def _post(self, expr: str):
        return self.client.post("/", data={"display": expr})

    def test_repeated_equals_add(self):
        r1 = self._post("5+2")
        self.assertIn(b'value="7.0"', r1.data)
        r2 = self._post("7.0")
        self.assertIn(b'value="9.0"', r2.data)
        r3 = self._post("9.0")
        self.assertIn(b'value="11.0"', r3.data)

    def test_repeated_equals_subtract(self):
        r1 = self._post("10-4")
        self.assertIn(b'value="6.0"', r1.data)
        r2 = self._post("6.0")
        self.assertIn(b'value="2.0"', r2.data)

    def test_repeated_equals_multiply(self):
        r1 = self._post("6*3")
        self.assertIn(b'value="18.0"', r1.data)
        r2 = self._post("18.0")
        self.assertIn(b'value="54.0"', r2.data)

    def test_repeated_equals_power(self):
        r1 = self._post("2**3")
        self.assertIn(b'value="8.0"', r1.data)
        r2 = self._post("8.0")
        self.assertIn(b'value="512.0"', r2.data)

    def test_number_without_prior_operation_does_not_crash(self):
        r = self._post("42")
        self.assertIn(b'value="42.0"', r.data)


if __name__ == "__main__":
    unittest.main()
