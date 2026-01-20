# Python code to validate if the user input Ip address is valid IPv4/Ipv6 or not using inbuilt module
import ipaddress
def validate_ip(ip):
    try:
        # Try to create an IPv4 address
        ipaddress.IPv4Address(ip)
        return "Valid IPv4 address"
    except ipaddress.AddressValueError:
        try:
            # Try to create an IPv6 address
            ipaddress.IPv6Address(ip)
            return "Valid IPv6 address"
        except ipaddress.AddressValueError:
            return "Invalid IP address"
# Example usage
ip_input = input("Enter an IP address: ")
result = validate_ip(ip_input)
print(result)
