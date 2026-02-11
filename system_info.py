# Récupérer les données de l'ordinateur de l'utilisateur pour les afficher puis les ajouter dans le pdf
# DOC utilisée : https://docs.python.org/3/library/platform.html, https://docs.python.org/fr/3/library/subprocess.html
import platform
import subprocess


# Ici on créé la classe qui récupèrera les informations de l'ordinateur
class SystemInfo:

    def __init__(self):
        # La liste des informations
        self.data = {}
        self.collect_all()

    def collect_all(self):
        # On récupère les informations
        self.data["cpu"] = self.get_cpu_info()
        self.data["gpu"] = self.get_gpu_info()
        self.data["ram"] = self.get_ram_info()
        self.data["stockage"] = self.get_stockage_info()
        self.data["os"] = self.get_os_info()
        self.data["name"] = self.get_name_info()

    # Récupérer le CPU de l'utilisateur
    def get_cpu_info(self):

        if platform.system() == "Windows":
            # Commande pour récupérer le nom du CPU
            command_windows = "wmic cpu get name"
            # Le logiciel éxécute la commande et renvoie, Name\n <Nom du CPU>
            cpu_windows = subprocess.check_output(command_windows, shell=True).decode()
            # On retire donc le "Name" pour garder seulement le CPU
            return cpu_windows.split("\n")[1].split("with")[0].split("@")[0].replace("(R)", "").replace("(TM)", "").strip()

        elif platform.system() == "Darwin":
            # La commande sur Mac renvoie directement le nom du CPU
            command_mac = "sysctl -n machdep.cpu.brand_string"
            return subprocess.check_output(command_mac, shell=True).decode().strip().split("with")[0]

        elif platform.system() == "Linux":
            # Linux sous forme, model name : <Nom du CPU>
            command_linux = 'cat /proc/cpuinfo | grep "model name" | head -n 1'
            cpu_linux = subprocess.check_output(command_linux, shell=True).decode()
            return cpu_linux.split(":")[1].split("with")[0].split("@")[0].replace("(R)", "").replace("(TM)", "").strip()  # On retire le "model name :"

        return "CPU non détecté"

    # Récupérer le GPU de l'utilisateur
    def get_gpu_info(self):

        if platform.system() == "Windows":
            # Commande pour récupérer le nom du GPU
            command_windows = "wmic path win32_VideoController get name"
            # Le logiciel éxécute la commande et renvoie, Name\n <Nom du GPU>
            gpu_windows = subprocess.check_output(command_windows, shell=True).decode()
            return gpu_windows.split("\n")[1].strip()

        elif platform.system() == "Darwin":
            command_mac = 'system_profiler SPDisplaysDataType | grep "Chipset Model"'
            gpu_mac = subprocess.check_output(command_mac, shell=True).decode()
            return gpu_mac.split(":")[1].strip()

        elif platform.system() == "Linux":
            # Linux sous forme, model name : <Nom du GPU>
            command_linux = "lspci | grep -i vga"
            gpu_linux = subprocess.check_output(command_linux, shell=True).decode()
            # On retire le "VGA compatible controller:"
            return gpu_linux.split(":")[1].strip()

        return "GPU non détecté"

    # Récupérer la ram de l'utilisateur
    def get_ram_info(self):
        # Récupérer la ram dans l'ordi de l'utilisateur
        if platform.system() == "Windows":
            windows_command = "wmic computersystem get TotalPhysicalMemory"
            ram_windows = subprocess.check_output(windows_command, shell=True).decode()
            octets = int(ram_windows.split("\n")[1].strip())
            gb = octets / 1073741824  # octets -> giga octets
            return f"{gb:.0f} GB"

        elif platform.system() == "Darwin":
            mac_command = "sysctl -n hw.memsize"
            ram_mac = int(
                subprocess.check_output(mac_command, shell=True).decode().strip()
            )
            gb = ram_mac / 1073741824  # octets -> giga octets
            return f"{gb:.0f} GB"

        elif platform.system() == "Linux":
            linux_command = "free -h | grep Mem"
            linux_ram = subprocess.check_output(linux_command, shell=True).decode()
            return linux_ram.split(":")[1].strip()

        return "RAM non détecté"

    # Récupérer les informations sur le disque de l'utilisateur
    def get_stockage_info(self):
        # Récupérer la taille du disque/ssd du octets
        if platform.system() == "Windows":
            command_windows = 'wmic logicaldisk where DeviceID="C:" get Size'
            windows = subprocess.check_output(command_windows, shell=True).decode()
            octets = int(windows.split("\n")[1].strip())
            GB = octets / 1073741824  # octets -> giga octets

            # HDD ou SDD (si SDD -> Media\n SSD, si HDD -> Media\n Fixed hard disk media)
            windows_disk_command = "wmic diskdrive get MediaType"
            disk_windows = subprocess.check_output(
                windows_disk_command, shell=True
            ).decode()
            type = disk_windows.split("\n")[1].strip()

            disk = "Type inconnu"
            if type == "SSD":
                disk = "SSD"
            else:
                disk = "HDD"
            return f"{disk} - {GB:.0f} GB (total)"  # afficher les GB(Ex: 931 GB)

        # Récupérer pour les macOS
        elif platform.system() == "Darwin":
            command_mac = 'diskutil info / | grep "Disk Size"'
            mac = subprocess.check_output(command_mac, shell=True).decode()
            storage = mac.replace(" ", "").split(":")[1].split("(")[0]

            # HDD ou SDD (si SDD -> Solid State: Yes, si HDD -> Solid State: No)
            mac_disk_command = 'diskutil info / | grep "Solid State"'
            disk_mac = subprocess.check_output(mac_disk_command, shell=True).decode()
            type = disk_mac.split(":")[1].strip()

            if type == "Yes":
                disk = "SSD"
            elif type == "No":
                disk = "HDD"
            else:
                disk = "Type inconnu"

            return f"{disk} - {storage} (total)"

        # Récupérer pour Linux
        elif platform.system() == "Linux":
            command_linux = "df -h --output=size / | tail -1"
            linux = subprocess.check_output(command_linux, shell=True).decode()

            # HDD ou SDD (si SDD -> Rota\n 0, si HDD -> Rota\n 1)
            linux_disk_command = 'diskutil info / | grep "Solid State"'
            disk_linux = subprocess.check_output(
                linux_disk_command, shell=True
            ).decode()
            type = disk_linux.split("\n")[1].strip()

            if type == "0":
                disk = "SSD"
            elif type == "1":
                disk = "HDD"
            else:
                disk = "Type inconnu"

            return f"{disk} - {linux} (total)"
        return "disque/SSD non détecté"

    # Récupérer l'OS de l'utilisateur
    def get_os_info(self):
        # Récupérer Windows, sa version (11 Pro, 10 Famille, etc...)
        if platform.system() == "Windows":
            command_windows = "wmic os get Caption"
            windows = subprocess.check_output(command_windows, shell=True).decode()
            return windows.split("\n")[1].replace("Windows", "Win").replace("Microsoft", "").strip()

        # Version de MacOS
        elif platform.system() == "Darwin":
            os_name = (
                subprocess.check_output("sw_vers -productName", shell=True)
                .decode()
                .strip()  # Nom l'OS
            )
            os_version = (
                subprocess.check_output("sw_vers -productVersion", shell=True)
                .decode()
                .strip()  # Version de l'OS
            )
            return f"{os_name} {os_version}"

        # Version de Linux
        elif platform.system() == "Linux":
            command_linux = "cat /etc/os-release | grep PRETTY_NAME"
            linux = subprocess.check_output(command_linux, shell=True).decode()
            return linux.split("=")[1].strip().strip('"')
        return "OS non détecté"

    def get_name_info(self):
        # Récupérer le nom de l'Ordi de la personne
        if platform.system() == "Windows":
            command_windows = "echo %COMPUTERNAME%"
            windows = subprocess.check_output(command_windows, shell=True).decode()
            return windows.strip()

        elif platform.system() == "Darwin":
            command_mac = "scutil --get ComputerName"
            mac = subprocess.check_output(command_mac, shell=True).decode()
            return mac.strip()
        elif platform.system() == "Linux":
            command_linux = "hostname"
            linux = subprocess.check_output(command_linux, shell=True)
            return linux.strip()
        return "Nom non détecté"
