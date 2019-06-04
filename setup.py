from setuptools import setup

setup(
    name="tljh-shared-directory",
    entry_points={"tljh": ["shared-directory = tljh_shared_directory"]},
    py_modules=["tljh_shared_directory"],
)