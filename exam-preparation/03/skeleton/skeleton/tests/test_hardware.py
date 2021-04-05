import unittest

from project.hardware.hardware import Hardware
from project.software.light_software import LightSoftware


class TestHardware(unittest.TestCase):
    NAME = "SSD"
    TYPE = "Power"
    CAPACITY = 500
    MEMORY = 500

    def setUp(self):
        self.hardware = Hardware(self.NAME, self.TYPE, self.CAPACITY, self.MEMORY)

    def test_hardware_install__when_enough_memory_and_capacity__expect_install_software(self):
        software = LightSoftware("Software_1", 100, 100)
        self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))

    def test_hardware_install__when_not_enough_memory_and_capacity__expect_exception(self):
        software = LightSoftware("Software_1", 500, 500)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_hardware_uninstall__when_software_not_there__expect_to_do_nothing(self):
        software = LightSoftware("Software_1", 100, 100)
        self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))
        software_1 = LightSoftware("Other_software", 100, 100)
        self.hardware.uninstall(software_1  )
        self.assertEqual(1, len(self.hardware.software_components))

    def test_hardware_uninstall__expect_remove_software_from_hardware(self):
        software = LightSoftware("Software_1", 100, 100)
        self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))
        self.hardware.uninstall(software)
        self.assertEqual(0, len(self.hardware.software_components))


if __name__ == '__main__':
    unittest.main()
