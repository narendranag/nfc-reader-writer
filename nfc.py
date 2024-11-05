import pynfc

def main():
    try:
        # Initialize NFC device
        device = pynfc.NFC('usb')
        print("NFC reader/writer connected.")
        
        # Attempt to read data from the device as a test
        tag = device.poll()  # This will wait for an NFC tag to come into range
        if tag:
            print(f"Device detected: {tag}")
        else:
            print("No NFC tag detected.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()