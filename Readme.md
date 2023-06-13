# ShodanKeyChecker
ShodanKeyChecker is a Python script dedicated to validating the authenticity and subscription type of Shodan API keys. Each API key is tested and categorized according to the subscription type: paid (developer or educational plan) and free (open-source software plan).

## Installation
```
git clone https://github.com/HalilDeniz/ShodanKeyChecker.git
```
## Requirements

Before you can use ShodanKeyChecker, you need to make sure that you have the necessary requirements installed. You can install these requirements by running the following command:

```
pip install -r requirements.txt
```

## Usage
To test the validity of a single API key:

```
python3 ShodanKeyChecker.py --api YOUR_API_KEY
```

To test the validity of multiple API keys from a file:
```
python3 ShodanKeyChecker.py --filename keys-to-test.txt
```
In the above keys-to-test.txt example, each line should contain a single API key.

## Known Limitations
This script endeavors to capture most errors. However, some cases, particularly those related to the API, may not be as explicitly handled.

## Contributing
Contributions are welcome! To contribute to SpeedyTest, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Open a pull request in the main repository.


## Contact

If you have any questions, comments, or suggestions about ShodanKeyChecker, please feel free to contact me:
- Denizhalil....: [DenizHalil](https://denizhalil.com)
- LinkedIn......: [LinkedIn](https://www.linkedin.com/in/halil-ibrahim-deniz/)
- TryHackMe.: [TryHackMe](https://tryhackme.com/p/halilovic)
- Instagram...: [Instagram](https://www.instagram.com/deniz.halil333/)
- YouTube.....: [YouTube](https://www.youtube.com/c/HalilDeniz)
- Email: halildeniz313@gmail.com

## About the Original Author
ShodanKeyChecker is a fork of the original tool called shodan_key_checker, which was created by [Caessi](https://github.com/Caessi). Caessi developed the initial version of the tool four years ago. However, the original tool was written in Python 2.7 and is no longer compatible with the latest versions. Therefore, this forked version, ShodanKeyChecker, has been updated and modified to work with Python3.
I would like to express my gratitude to Caessi  for the inspiration and foundation provided by the original tool. Without his work, this updated version would not have been possible.
If you would like to learn more about the original tool, you can visit the [shodan_key_checker repository](https://github.com/Caessi/shodan_key_checker).


## License
This project is licensed under the MIT License. For more information, please refer to the  [License](LICENSE) file.