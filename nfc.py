import nfc

def device_found(target):
	print(f"Device detected {target}")
	return True

def main():
    with nfc.ContactlessFrontend('usb') as clf:
		if clf:
			print("NFC reader/writer connected.")
			clf.connect(rdwr={'on-connect': device_found})
		else:
	    	print("No NFC device found")

if __name__ == "__main__":
    main()
