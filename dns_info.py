import socket
import dns.resolver

def get_dns_info(domain_name):
    # Get the IP address for the domain
    ip_address = socket.gethostbyname(domain_name)
    print(f"IP address: {ip_address}")

    # Get the DNS resolver for the domain
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [socket.gethostbyname('ns1.' + domain_name)]
    nameservers = resolver.query(domain_name, 'NS')
    print("Nameservers:")
    for nameserver in nameservers:
        print(nameserver.target)

    # Get the MX records for the domain
    mx_records = resolver.query(domain_name, 'MX')
    print("MX records:")
    for mx_record in mx_records:
        print(f"{mx_record.preference} {mx_record.exchange}")

def main():
    domain_name = input("Enter a domain name: ")
    get_dns_info(domain_name)

if __name__ == "__main__":
    main()