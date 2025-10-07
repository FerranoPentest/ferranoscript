#!/usr/bin/env python3
"""
nmap_scan.py
Usage: python3 nmap_scan.py target.com
Génère un scan Nmap de base (top 100 ports) en sortie XML + résumé.
"""
import sys, subprocess

def main():
    if len(sys.argv)!=2:
        print("Usage: python3 nmap_scan.py target.com")
        sys.exit(1)
    target=sys.argv[1]
    xml_out=f"{target}_scan.xml"
    subprocess.run(["nmap","-sV","--top-ports","100","-oX",xml_out, target])
    print(f"[+] Scan enregistré dans {xml_out}")

if __name__=="__main__":
    main()
