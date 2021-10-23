from time import sleep
import scapy.all as scapy

BCAST_MAC = 'ff:ff:ff:ff:ff:ff'

def create_ARP_request_gratuituous(host_ip, fake_ip, mac):
    arp = scapy.ARP(psrc=fake_ip,
                    hwsrc=mac,
                    pdst=host_ip)
    return scapy.Ether(dst=BCAST_MAC) / arp

def main():
    host_ip = input("Your computer's IP:")
    bogus_mac = input("Input a fake MAC (e.g 02:02:02:02:02:02):")
    fake_ip_1 = input("Input an unused IP:")
    fake_ip_2 = input("Input a second unused IP:")

    for x in range(10):
        packet = create_ARP_request_gratuituous(host_ip, fake_ip_1, bogus_mac)
        scapy.sendp(packet)
        sleep(1)
        packet = create_ARP_request_gratuituous(host_ip, fake_ip_2, bogus_mac)
        scapy.sendp(packet)
        sleep(1)

if __name__ == "__main__":
    main()