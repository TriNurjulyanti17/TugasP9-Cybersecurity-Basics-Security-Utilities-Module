from security_utils import generate_random_password, is_valid_ip, bytes_to_human

# 1. Tes Generate Password
print("[+] Password Baru:", generate_random_password())

# 2. Tes Validasi IP
print("[+] Validasi IP 192.168.1.1 :", is_valid_ip("192.168.1.1"))
print("[+] Validasi IP 256.0.0.1   :", is_valid_ip("256.0.0.1"))

# 3. Tes Konversi Bytes
print("[+] Ukuran File 1048576 B   :", bytes_to_human(1048576))
