# 15-03-2026
- Initial release
- Dolby & MI Cam included
- Pre-rooted with multi manager support

# 07-06-2026
- Non-Root build
- Merged latest upstream source changes up to version 5.4
- Update from OS3.0.5.0.WNRMIXM (@grewal)
- Use hwui and add some hwui props for improve perf
- Set vulkan as default renderer
- Import V837.0.7 GPU drivers (@adrenolaboratory)
- Relax thermal limits and optimize charging behavior (@zerotwo-alt)
- GameBar update (@kenway214)
- Move Xiaomi Parts to one section
- Explicitly disable Enable GL comp backpressure
- Rm package cache on early boot
- Add support for Dolby Spatial Audio (Wired headphones)
- Enable Dolby Vision support
- Reduce uclamp.min value to 125
- props: Set ro.netflix.bsp_rev from stock
- Include JamesDSP
- kernel: Merge Linux Stable branch (5.10.258)
- Merge tag 'KERNEL.PLATFORM.1.0.r3-07500-kernel.0' of https://git.codelinaro.org/clo/la/kernel/msm-5.10
- Merge tag 'CAMERA.LA.2.0.r2-06600-WAIPIO.0' of https://git.codelinaro.org/clo/la/platform/vendor/opensource/camera-kernel
- Merge tag 'DISPLAY.LA.2.0.r3-04000-WAIPIO.0' of https://git.codelinaro.org/clo/la/platform/vendor/opensource/display-drivers
- Merge tag 'VIDEO.LA.2.0.r2-04500-WAIPIO.0' of https://git.codelinaro.org/clo/la/platform/vendor/opensource/video-driver
- Merge tag 'LA.VENDOR.1.0.r2-16600-WAIPIO.QISI15.0' of https://git.codelinaro.org/clo/la/platform/vendor/qcom-opensource/wlan/qcacld-3.0
- Merge tag 'LA.VENDOR.1.0.r2-16600-WAIPIO.QISI15.0' of https://git.codelinaro.org/clo/la/platform/vendor/qcom-opensource/wlan/qca-wifi-host-cmn
Merge tag 'LA.VENDOR.1.0.r2-16600-WAIPIO.QISI15.0' of https://git.codelinaro.org/clo/la/platform/vendor/qcom-opensource/wlan/fw-api
- kernel: Imported Adaptive Deadline I/O Scheduler (ADIOS) v3.2.0
- kernel: Import Reflex CPUFreq Governor v0.3.0r2
- kernel: Enabled IP set support
- power: Improved deep sleep and switched to suspend-to-idle
- f2fs: Optimized GC, fsync, and cache pressure
- zRAM: Fixed race conditions and optimized entry flags
- GPU: Forced idle timeout to 58ms for better balance
- system: Reduced OOM and scheduler logspam
- cpufreq: reflex: call android_vh_map_util_freq to fix SODs
- cpufreq: reflex: avoid startup race in rfx_start
- ANDROID: GKI: Build multi-gen LRU
- ANDROID: Enable CONFIG_LAZY_RCU
- Enable BBRplus
- Various upstream fixes and improvements for block & I/O scheduler

# 15-06-2026
- Sync latest upstream source up to v5.5
- Disable Skia tracing by default
- Update MiuiCamera from OS3.0.5.0.WNRMIXM (@grewal)
- surfaceflinger: Reduce max acquired frame buffers to 2
- Add overlay to improve signal reception
- Drop Spatial Audio