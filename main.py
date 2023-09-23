"""
Main cli or app entry point
"""

import platform
import sys

def main():
    print(platform.system())
    print(sys.version)
    return 0


if __name__ == "__main__":
    main()
