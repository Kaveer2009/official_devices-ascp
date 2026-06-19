# Installation Guide

## Clean Flash (coming from another ROM)

 ***Important: You won't be able to downgrade to any firmware lower than OOS 16.0.3.500 after flashing this ROM, you could risk bricking your device! Make sure to have the latest OOS 16.0.3.500 firmware in both slots before proceding if you're coming from stock.***

### 1) Enter bootloader mode by pressing and holding the Power + Volume Down buttons, and plug your device to your PC when it boots. Then open a terminal on your platform tools folder and flash the following files:

```bash
fastboot flash boot boot.img
```
```bash
fastboot flash dtbo dtbo.img
```
```bash
fastboot flash init_boot init_boot.img
```
```bash
fastboot flash vendor_boot vendor_boot.img
```

### 2) Reboot to bootloader mode by typing:
```bash
fastboot reboot bootloader
```

### 3) Flash the ROM's recovery onto your device by typing:
```bash
fastboot flash recovery recovery.img
```

### 4) Now reboot into recovery to verify the installation. Use the volume buttons and the menu to navigate and to select the "Recovery" option, then press the power button to select it.

### 5) While in the recovery, select "Factory Reset", then "Format data" and continue with the formatting process. This will remove encryption and delete all files stored in the internal storage

### 6) Return to the main menu

### 7) Select "Apply update", then "Apply from ADB". Then type on your PC:
```bash
adb sideload ROM.zip
```
#### Note: Replace "ROM" with the name of the zip file you downloaded for your device, or just drag and drop the file on the terminal.

### 8) Reboot to system
<br>
<br>

## Dirty Flash (updating your current installation)

### 1) Reboot to recovery

### 2) Select "Apply update", then "Apply from ADB". Then type on your PC:
```bash
adb sideload ROM.zip
```
#### Note: Replace "ROM" with the name of the zip file you downloaded for your device, or just drag and drop the file on the terminal.

### 3) Reboot to system
