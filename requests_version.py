from packaging.specifiers import SpecifierSet
from packaging.version import Version

if __name__ == "__main__":
    # Requests 2.26.0
    spec1 = SpecifierSet("~=1.0")
    print(spec1)
