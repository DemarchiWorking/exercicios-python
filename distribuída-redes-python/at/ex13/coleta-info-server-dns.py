import dns.resolver
import dns.query
import dns.zone
import dns.reversenameKimport

dns.rdatatype
import dns.exception
import subprocess
import json
import sys
from typing import List, Set


def get_dns_records(domain: str, record_types: List[str], nameserver: str = None) -> dict:
    results = {}
    resolver = dns.resolver.Resolver()

    if nameserver:
        resolver.nameservers = [nameserver]

    for rtype in record_types:
        try:
            answers = resolver.resolve(domain, rtype)
            results[rtype] = [str(rdata) for rdata in answers]
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.exception.DNSException):
            results[rtype] = []
    return results


def attempt_zone_transfer(domain: str, nameserver: str) -> Set[str]:
    records = set()
    try:
        zone = dns.zone.from_xfr(dns.query.xfr(nameserver, domain))
        for name, rdata in zone.iterate_rdatas():
            records.add(f"{name} {rdata}")
    except (dns.exception.FormError, dns.query.TransferError):
        print(f"Transferência de zona falhou para {domain} em {nameserver}")
    return records


def run_dnsrecon(domain: str, options: List[str] = ["-t", "std"]) -> dict:
    cmd = ["dnsrecon", "-d", domain] + options
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {"output": result.stdout, "error": result.stderr}
    except subprocess.CalledProcessError as e:
        return {"output": e.stdout, "error": e.stderr}


def main(domain: str, nameserver: str = None):
    record_types = ["A", "AAAA", "MX", "NS", "SOA", "TXT", "CNAME"]

    print(f"\nconsultando registros dns para {domain}.")
    dns_records = get_dns_records(domain, record_types, nameserver)
    print(json.dumps(dns_records, indent=2))

    if nameserver:
        print(f"\ntentando transferencia de zona de {domain} em {nameserver}")
        zone_records = attempt_zone_transfer(domain, nameserver)
        if zone_records:
            print("registros encontrados na transferencia de zona:")
            for record in zone_records:
                print(record)
        else:
            print("nenhum registro obtido na transferencia de zona.")

    print(f"\nexecutando dnsrecon para {domain} (padrão)")
    dnsrecon_result = run_dnsrecon(domain)
    print(dnsrecon_result["output"])


    print(f"\nexecutando dnsrecon com brute force  {domain}")
    dnsrecon_brute = run_dnsrecon(domain, ["-t", "brute", "-D", "/usr/share/dnsrecon/namelist.txt"])
    print(dnsrecon_brute["output"])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("uso: python3 coleta-info.py <dominio> [nomeserver]")
        sys.exit(1)

    domain = sys.argv[1]
    nameserver = sys.argv[2] if len(sys.argv) > 2 else None
    main(domain, nameserver)