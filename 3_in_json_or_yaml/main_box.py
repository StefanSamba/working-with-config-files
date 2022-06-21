import yaml
from box import Box

cfg = Box.from_yaml(filename="3_in_json_or_yaml/conf.yaml",
                    Loader=yaml.FullLoader)


def main():
    print("Box config \n")
    print(f"Config: {cfg} \n")
    print(f"Bucket: {cfg.storage.bucket} \n")
    return "Done"


if __name__ == "__main__":
    print(main())

# python3 3_in_json_or_yaml/main_box.py
