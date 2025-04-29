# RedBomberBD - SMS Bombing Tool for Bangladesh

RedBomberBD is a powerful Python-based **SMS bombing tool** designed for Bangladesh, enabling users to send multiple OTP requests to phone numbers for testing purposes. Ideal for developers and security researchers, it helps test SMS OTP APIs under controlled, authorized conditions.

> **⚠️ Legal and Ethical Warning**: RedBomberBD is for **authorized testing only**. Sending unsolicited SMS or spamming without explicit consent from the phone number owner and API providers is **illegal** and **unethical**, potentially violating Bangladesh laws and API terms of service. Misuse may lead to legal consequences, account bans, or service disruptions. The developer is not responsible for any misuse.

## Key Features
- Sends multiple OTP requests to Bangladesh-specific APIs for SMS bombing tests.
- Simple command-line interface optimized for Termux on Android.
- Configurable request limits to simulate SMS spam responsibly.
- Open-source and lightweight, requiring minimal dependencies.

## Installation

Install RedBomberBD on Termux with these commands:

```bash
pkg update -y && pkg upgrade -y
pkg install python -y
pkg install git -y
git clone https://github.com/Redwiat/RedBomberBD.git
cd RedBomberBD
pip install requests colorama
python redbombbd.py
```

### Prerequisites
- **Termux**: Install from [F-Droid](https://f-droid.org/en/packages/com.termux/) for the latest version.
- **Internet Connection**: Needed to clone the repository and install dependencies.
- **Storage Permission** (optional): Run `termux-setup-storage` for file access.

## Usage
1. Start the tool:
   ```bash
   python redbombbd.py
   ```
2. Enter a valid Bangladesh phone number (e.g., `+8801712345678` or `01712345678`).
3. Specify the number of OTP requests (e.g., 1–5 to avoid API rate limits).
4. Check the output for success (`SMS Sent ✅`) or error messages.

> **Important**: Always obtain explicit permission from the phone number owner and API providers. Limit requests to prevent API blocks or legal issues.

## Screenshots
![RedBomberBD SMS Bombing Demo](https://user-images.githubusercontent.com/90413704/138064859-98178dde-d6fd-422c-9aa4-a1ee7ccae2da.gif)
*Showcasing the SMS bombing process in Termux.*

![RedBomberBD Interface](https://user-images.githubusercontent.com/90413704/138065091-22a7fdd9-0766-4c0a-bcd7-25a8a0217ce4.png)
*Command-line interface for SMS bombing tests.*

## Why Choose RedBomberBD?
- **Targeted Testing**: Designed for Bangladesh SMS APIs, perfect for local developers.
- **Educational Value**: Learn about OTP systems and API rate limits.
- **Ethical Focus**: Encourages responsible use with clear guidelines.
- **Easy Setup**: Runs seamlessly on Termux with minimal configuration.

## License
RedBomberBD is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

## Contributing
Contributions are welcome to enhance RedBomberBD! To contribute:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit changes:
   ```bash
   git commit -m 'Add YourFeature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a pull request on GitHub.

## Troubleshooting
- **Git Clone Fails**: Check the repository URL and internet (`ping github.com`).
- **Script Errors**: Verify `requests` and `colorama` are installed:
  ```bash
  pip show requests colorama
  ```
- **API Failures**: Errors may indicate rate limits or outdated APIs. Update `redbombbd.py` if needed.
- **Termux Issues**: Switch mirrors if packages fail:
  ```bash
  termux-change-repo
  ```

## Contact
- **Author**: Redwiat
- **GitHub**: [Redwiat](https://github.com/Redwiat)
- **Issues**: Report bugs or suggestions on the [Issues page](https://github.com/Redwiat/RedBomberBD/issues).

## Disclaimer
RedBomberBD is an **SMS bombing tool** for authorized testing only. Using it to send unsolicited SMS or spam is illegal and may violate laws in Bangladesh and API policies. Always obtain permission and use ethically.

---

*Keywords*: SMS bombing tool Bangladesh, OTP spam testing, RedBomberBD, Termux SMS bomber, ethical SMS testing, Bangladesh Python tools.