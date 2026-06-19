# Installation Guide

## Clean Flash (Coming from Another ROM)

> **Important:** Make sure you are on the required firmware version before proceeding. Flashing from unsupported firmware may cause boot issues or other problems.

### 1) Extract Required Images

Extract the following files from the ROM ZIP:

- `boot.img`
- `dtbo.img`
- `vendor_boot.img`

You can use the Fastboot Firmware Flasher Tool (`#flash_tool`) or any payload extraction utility.

### 2) Reboot to Bootloader

```bash
adb reboot bootloader
```

### 3) Flash Required Images

```bash
fastboot flash --slot=all boot boot.img
```

```bash
fastboot flash --slot=all dtbo dtbo.img
```

```bash
fastboot flash --slot=all vendor_boot vendor_boot.img
```

### 4) Boot into Recovery

```bash
fastboot reboot recovery
```

### 5) Format Data (Clean Flash Only)

Select:

**Factory Reset → Format Data**

> Skip this step if updating from the same ROM and you wish to keep your data.

### 6) Sideload the ROM

Select:

**Apply Update → Apply from ADB**

Then run:

```bash
adb sideload aosp_package.zip
```

> Replace `aosp_package.zip` with the actual ROM filename.

### 7) Reboot System

Select:

**Reboot → System**

<br>

## Dirty Flash (Updating Current Installation)

### 1) Reboot to Recovery

### 2) Select "Apply Update" → "Apply from ADB"

```bash
adb sideload aosp_package.zip
```

### 3) Reboot System

<br>

## Notes

⚠️ First boot can take several minutes.

### Error 7 Fix

If sideloading fails with **Error 7**:

1. Reboot to bootloader.
2. Flash `super_empty.img`:

```bash
fastboot flash super super_empty.img
```

3. Retry the installation process.
