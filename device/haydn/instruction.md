### Step 1: Flash recovery:
* Download recommanded recovery zip
* On your pc open your platform-tools's cmd if using (windows) or open terminal on (linux/mac)

```
adb -d reboot bootloader
```
or just boot into fastboot mode via volume down + power button.
* Once you are in fastboot mode check if your device is connected correctly or not by: 

```
fastboot devices
```
* Now install recovery by using:

```
fastboot boot recovery.img
```
***WARNING:***  
*Dont use (fastboot "flash" recovery.img) for installing recovery*
* Use downloaded recovery's image in above command (i am assuming its recovery.img)
* Wipe everything (ASCP*.zip must be on your pc)

### Step 2: Installing recovery:
* Reboot into recovery
* Ensure that you have downloaded latest version of required files
* Now go to advanced tab in your recovery and press start_sideload
* Now install ASCP zip via sideload

```
adb sideload ASCP*.zip
```
* When rom sideloading is done reboot recovery and sideload any other preferred zips
* Format data when everything is done (for clean flash) ,if it throw error "Cant merge status" then go to fastboot mode again then use:

```
fastboot -w
```
* This will erase 'Userdata' or you can simple format through ascp's recovery

#### Via OTA:
* Go to Settings -> System -> Updater and download latest build
* Choose install and let it finish
* Reboot
