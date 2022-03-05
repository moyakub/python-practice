from colorama import Fore, Back, Style, init

#To reseet colorama color automatically
init(autoreset=True)


def print_message(error,message):
  if error:
      print(Fore.RED + message)
  else:
      print(message)
        