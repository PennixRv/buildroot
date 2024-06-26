from tests.package.test_python import TestPythonPackageBase


class TestPythonYamllint(TestPythonPackageBase):
    __test__ = True
    config = TestPythonPackageBase.config + \
        """
        BR2_PACKAGE_PYTHON3=y
        BR2_PACKAGE_PYTHON_YAMLLINT=y
        """
    sample_scripts = ["tests/package/sample_python_yamllint.py"]
