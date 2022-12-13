import argparse
from Main.main_console import ApplicationConsole
from Main.main_gui import ApplicationGUI


def main():
    parser = argparse.ArgumentParser(
        description='Choisissez l\'interface que vous désirez')
    parser.add_argument('interface', metavar='interface', type=str, help='Entrez "gui" pour l\'interface graphique et '
                                                                         '"console" pour l\'interface console')
    args = parser.parse_args()
    interface_choice = args.interface
    if interface_choice == "gui":
        ApplicationGUI()
    elif interface_choice == "console":
        ApplicationConsole()
    else:
        print(
            "Vous n'avez pas rentré un nombre correspondant à une interface existante.\n"
            "Faites 'py main.py -h' pour avoir plus d'informations.")


if __name__ == "__main__":
    main()
