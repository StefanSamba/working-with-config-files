import hydra


@hydra.main(config_path="", config_name="conf.yaml")
def main(cfg):
    print("Hydra config \n")
    print(f"Config: {cfg} \n")
    print(f"Bucket: {cfg.storage.bucket} \n")
    return "Done"


if __name__ == "__main__":
    print(main())

# python3 3_in_json_or_yaml/main_hydra.py
