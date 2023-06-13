import argparse
import shodan
from termcolor import colored

class KeyTester:
    def __init__(self, filename=None, api_key=None):
        self.filename = filename
        self.api_key = api_key
        self.valid_keys = []
        self.paid_keys = []
        self.comm_keys = []

    def test_key(self, key):
        api = shodan.Shodan(key)
        print(colored(f"{key} Key being tested...", "yellow"))
        try:
            info = api.info()
        except Exception:
            print(colored(f"Key {key} invalid!", "red"))
            return False,False
        if info['plan'] == 'dev' or info['plan'] == 'edu':
            print(colored(f"Key {key} valid and also paid!!", "green"))
            return True,True
        elif info['plan'] == 'oss':
            print(colored(f"Key {key} valid! But free!", "blue"))
            return True,False

    def process_keys(self):
        if self.api_key:
            key = self.api_key
            is_valid, is_paid = self.test_key(key=key)
            if is_valid:
                self.valid_keys.append(key)
                if is_paid:
                    self.paid_keys.append(key)
                else:
                    self.comm_keys.append(key)
        else:
            with open(self.filename, "r") as f:
                keys = f.readlines()
            for key in keys:
                key = key.strip()
                is_valid, is_paid = self.test_key(key=key)
                if is_valid:
                    self.valid_keys.append(key)
                    if is_paid:
                        self.paid_keys.append(key)
                    else:
                        self.comm_keys.append(key)

    def print_keys(self):
        print(colored(f"\nin total {len(self.valid_keys)} valid key obtained.", "green"))
        print(colored(f"in total {len(self.paid_keys)} paid key obtained.", "green"))
        print(colored(f"in total {len(self.comm_keys)} community key obtained.", "green"))

        if self.api_key:
            return

        print(colored("\nÜcretli Keyler:", "yellow"))
        for key in self.paid_keys:
            print(key)

        print(colored("\nTopluluk Keyleri:", "yellow"))
        for key in self.comm_keys:
            print(key)

def main():
    parser = argparse.ArgumentParser(description="Shodan API Key List Checker")
    parser.add_argument('--filename', type=str, help='txt file with things to test')
    parser.add_argument('--api', type=str, help='a single API key to test')

    args = parser.parse_args()

    if not args.filename and not args.api:
        parser.error('You must specify at least one of the filename or api arguments')

    key_tester = KeyTester(args.filename, args.api)
    key_tester.process_keys()
    key_tester.print_keys()

if __name__ == "__main__":
    main()
