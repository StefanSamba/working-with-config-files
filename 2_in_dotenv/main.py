import os

from dotenv import load_dotenv

load_dotenv()


def main():
    bucket = os.getenv("bucket")
    print("Config")
    print(f"Bucket: {bucket} \n")
    return "Done"


if __name__ == "__main__":
    print(main())
# python3 2_in_dotenv/main.py
