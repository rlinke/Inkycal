import sys

def main(config_filepath: str):
  from inkycal import Inkycal
  inky = Inkycal(config_filepath, render=True)
  inky.run_once()


def get_filepath(default_config="settings.json"):
  
  if len(sys.argv) > 1:
    return sys.argv[1]
  else:
    return default_config

if __name__ == '__main__':

  config_filepath = get_filepath("settings.json")
  print(f"running with {config_filepath}")

  main(config_filepath)

