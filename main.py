from LOLGui import LOLGui
from LOLManager import LOLManager


def main():
    LOL_Manager = LOLManager()
    LOL_gui = LOLGui(LOL_Manager)
    LOL_gui.show()


if __name__ == '__main__':
    main()
