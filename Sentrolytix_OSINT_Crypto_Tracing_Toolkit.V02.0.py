# sentrolytix_v2_gui.py
import sys
import requests

from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit,
    QVBoxLayout, QHBoxLayout, QGroupBox, QFileDialog, QTextBrowser
)
from PyQt6.QtCore import Qt

class SentrolytixV2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🛡️ Sentrolytix V2 – Advanced OSINT & Crypto Toolkit")
        self.setGeometry(200, 100, 800, 650)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # ---- Header ----
        header = QLabel("📂 Enter All Available Information About the Suspect")
        header.setStyleSheet("font-size: 18px; font-weight: bold;")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(header)

        # ---- Wallets ----
        wallet_group = QGroupBox("💰 Wallet Addresses")
        wallet_layout = QVBoxLayout()
        self.tron_input = QLineEdit(); self.tron_input.setPlaceholderText("Tron Address (TX...)")
        self.btc_input = QLineEdit(); self.btc_input.setPlaceholderText("Bitcoin Address")
        self.eth_input = QLineEdit(); self.eth_input.setPlaceholderText("Ethereum / USDT Address")
        wallet_layout.addWidget(self.tron_input)
        wallet_layout.addWidget(self.btc_input)
        wallet_layout.addWidget(self.eth_input)
        wallet_group.setLayout(wallet_layout)
        main_layout.addWidget(wallet_group)

        # ---- Telegram Info ----
        telegram_group = QGroupBox("💬 Telegram Information")
        telegram_layout = QVBoxLayout()
        self.telegram_id = QLineEdit(); self.telegram_id.setPlaceholderText("Telegram ID or @username")
        self.telegram_channel = QLineEdit(); self.telegram_channel.setPlaceholderText("Telegram Channel Link")
        telegram_layout.addWidget(self.telegram_id)
        telegram_layout.addWidget(self.telegram_channel)
        telegram_group.setLayout(telegram_layout)
        main_layout.addWidget(telegram_group)

        # ---- Contact Info ----
        contact_group = QGroupBox("📞 Contact Details")
        contact_layout = QVBoxLayout()
        self.phone_input = QLineEdit(); self.phone_input.setPlaceholderText("Phone Number (any country)")
        self.email_input = QLineEdit(); self.email_input.setPlaceholderText("Email Address (if any)")
        contact_layout.addWidget(self.phone_input)
        contact_layout.addWidget(self.email_input)
        contact_group.setLayout(contact_layout)
        main_layout.addWidget(contact_group)

        # ---- Social/Web ----
        web_group = QGroupBox("🌐 Website & Social Profiles")
        web_layout = QVBoxLayout()
        self.website_input = QLineEdit(); self.website_input.setPlaceholderText("Website URL")
        self.instagram_input = QLineEdit(); self.instagram_input.setPlaceholderText("Instagram Profile URL")
        self.facebook_input = QLineEdit(); self.facebook_input.setPlaceholderText("Facebook Profile URL")
        web_layout.addWidget(self.website_input)
        web_layout.addWidget(self.instagram_input)
        web_layout.addWidget(self.facebook_input)
        web_group.setLayout(web_layout)
        main_layout.addWidget(web_group)

        # ---- Media / Screenshot ----
        media_group = QGroupBox("🖼️ Uploaded Image / Screenshot")
        media_layout = QVBoxLayout()
        self.upload_button = QPushButton("📎 Upload Image / Screenshot")
        self.upload_button.clicked.connect(self.upload_image)
        self.image_path_label = QLabel("No file selected")
        media_layout.addWidget(self.upload_button)
        media_layout.addWidget(self.image_path_label)
        media_group.setLayout(media_layout)
        main_layout.addWidget(media_group)

        # ---- Start Button & Monitor ----
        self.start_button = QPushButton("🚀 Start Full Analysis")
        self.start_button.setStyleSheet("padding: 10px; font-weight: bold; font-size: 15px;")
        self.start_button.clicked.connect(self.start_analysis)
        main_layout.addWidget(self.start_button)

        self.status_monitor = QTextBrowser()
        self.status_monitor.setStyleSheet("background-color: #1e1e1e; color: #00ff00; font-family: Consolas;")
        main_layout.addWidget(self.status_monitor)

        self.setLayout(main_layout)

    def upload_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select Image or Screenshot")
        if path:
            self.image_path_label.setText(path)
            self.status_monitor.append(f"🖼️ Uploaded: {path}")

    def start_analysis(self):
        self.status_monitor.append("🟢 Starting full analysis with available data...\n")
        # اتصال به ماژول‌ها در مراحل بعدی اضافه می‌شود
        self.status_monitor.append("🔎 [TODO] Processing wallet, telegram, phone, site, image...\n")

    def start_analysis(self):
        self.status_monitor.append("🟢 Starting full analysis with available data...\n")

            # ---- Tron Wallet ----
        tron = self.tron_input.text().strip()
        if tron.startswith("T"):
            self.status_monitor.append(f"🔵 Analyzing Tron Address: {tron}")
            self.analyze_tron(tron)

            # ---- Bitcoin Wallet ----
        btc = self.btc_input.text().strip()
        if btc:
            self.status_monitor.append(f"🟠 Analyzing Bitcoin Address: {btc}")
            self.analyze_btc(btc)

            # ---- Ethereum Wallet ----
        eth = self.eth_input.text().strip()
        if eth.startswith("0x"):
            self.status_monitor.append(f"🟣 Analyzing Ethereum Address: {eth}")
            self.analyze_eth(eth)

            self.status_monitor.append("\n✅ Wallet analysis complete.\n" + "-"*50 + "\n")


def analyze_tron(self, address):
    try:
        url = f"https://apilist.tronscan.org/api/account?address={address}"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            balance = float(data.get("balance", 0)) / 1_000_000
            txs = data.get("totalTransaction", "N/A")
            self.status_monitor.append(f"📍 Tron Balance: {balance:.6f} TRX")
            self.status_monitor.append(f"📍 Transactions: {txs}")
        else:
            self.status_monitor.append(f"❌ TronScan Error: {r.status_code}")
    except Exception as e:
        self.status_monitor.append(f"❗ TronScan Exception: {e}")

def analyze_btc(self, address):
    try:
        url = f"https://api.blockcypher.com/v1/btc/main/addrs/{address}/balance"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            balance = data.get("balance", 0) / 1e8
            txs = data.get("n_tx", 0)
            self.status_monitor.append(f"📍 BTC Balance: {balance:.8f} BTC")
            self.status_monitor.append(f"📍 Transactions: {txs}")
        else:
            self.status_monitor.append(f"❌ BTC API Error: {r.status_code}")
    except Exception as e:
        self.status_monitor.append(f"❗ BTC Exception: {e}")

def analyze_eth(self, address):
    try:
        url = f"https://api.blockcypher.com/v1/eth/main/addrs/{address}/balance"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            balance = data.get("balance", 0) / 1e18
            txs = data.get("n_tx", 0)
            self.status_monitor.append(f"📍 ETH Balance: {balance:.8f} ETH")
            self.status_monitor.append(f"📍 Transactions: {txs}")
        else:
            self.status_monitor.append(f"❌ ETH API Error: {r.status_code}")
    except Exception as e:
        self.status_monitor.append(f"❗ ETH Exception: {e}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = SentrolytixV2()
    gui.show()
    sys.exit(app.exec())
