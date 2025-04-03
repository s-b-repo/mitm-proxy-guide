Alright — let's lock this in 🔒🚀

Below is a **full end-to-end guide** to:

1. ✅ Set up `mitmproxy` with a trusted certificate.
2. ⚡ Improve the script for speed and stability.
3. 📲 Make it all work with apps (even mobile).

---

## 🧱 STEP 1: Install `mitmproxy`

Install `mitmproxy` via pip (recommended):

```bash
pip install mitmproxy
```

Or download from [https://mitmproxy.org](https://mitmproxy.org/).

---

## 🔐 STEP 2: Set Up the Certificate (For HTTPS Decryption)

### 🖥️ On Your PC/Mac (System-wide Trust):

1. Run mitmproxy:
   ```bash
   mitmproxy
   ```

2. In your browser, visit:
   ```
   http://mitm.it
   ```

3. Click your platform (Windows/macOS/Linux) and download the CA certificate.

4. **Install & trust the CA certificate**:
   - **Windows**: Open the `.pem` file > Install Certificate > Local Machine > Trusted Root Certification Authorities.
   - **macOS**: Open Keychain > drag in the `.pem` > Right-click > "Trust" for all usages.
   - **Linux**: Copy cert to `/usr/local/share/ca-certificates/` and run:
     ```bash
     sudo update-ca-certificates
     ```

---

### 📱 On Android (Emulator or Physical):

**For Android 7+**, system apps do **not trust user-installed certs** by default unless:

#### Option A: Install Cert as System CA (rooted phone or emulator)

1. Push the cert to `/system/etc/security/cacerts/`:
   ```bash
   adb root
   adb remount
   adb push ~/.mitmproxy/mitmproxy-ca-cert.pem /system/etc/security/cacerts/12345678.0
   ```

2. Reboot:
   ```bash
   adb reboot
   ```

3. Ensure the cert is owned by `root:root` and has `644` permissions.

#### Option B: Patch the App to Trust User Certs (certificate pinning)

- Use **Frida**, **Objection**, or **Xposed** to bypass or hook SSL pinning.
- Tools like [TrustMeAlready](https://github.com/ViRb3/TrustMeAlready) can patch some apps automatically.

---

### 🍏 On iOS

- Use a **proxy profile** from `http://mitm.it` or manually install the certificate.
- Trust the cert under Settings → General → About → Certificate Trust Settings.
- Apps using pinning need to be reverse-engineered or hooked (Frida works here too).

---

## ⚡ Improved Fast & Lightweight Script: `add_api_key_fast.py`

This version avoids unnecessary parsing, keeps logs minimal, and is tuned for speed.

```python

```

---

## ✅ Launch & Test

```
mitmproxy -s add_api_key_fast.py --listen-port 8080
```

Then:

- Route your app or system traffic through `127.0.0.1:8080`
- Watch requests flow through with API keys silently added 😎

---

## 🧪 Optional: Force Specific Ports/Apps

Want it to only modify requests to a specific path, or only GETs/POSTs? Just ask — I can fine-tune this for your exact use case.

Wanna test it live now with your app or emulator? Or need help with cert pinning bypass?
