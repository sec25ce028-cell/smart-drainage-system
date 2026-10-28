
import unittest
from src.drainage_monitor import check_drainage


class TestDrainageMonitor(unittest.TestCase):

    def test_normal_drainage(self):
        self.assertEqual(
            check_drainage(5, False),
            "NORMAL: Drainage flow appears normal"
        )

    def test_blockage_detected(self):
        self.assertEqual(
            check_drainage(25, True),
            "WARNING: Possible blockage detected"
        )

    def test_high_water_level(self):
        self.assertEqual(
            check_drainage(35, False),
            "WARNING: High water level"
        )


if __name__ == "__main__":
    unittest.main()
