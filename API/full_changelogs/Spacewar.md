# 19-06-2026

   * hardware tree
NGlyphs: Import third party call and notification sounds
NGlyphs: support built-in ogg-only ringtones with embedded glyph metadata
NGlyphs: Clean up UI strings and improve localization
NGlyphs: Add contributor credits dialog
Glyphs: Add settings backup and restore support
NGlyphs: Add notification cooldown and VIP app exceptions
NGlyphs: Add advanced glyph behavior settings
NGlyphs: Add battery warning and full charge pulse
NGlyphs: Add Tasker automation receiver
NGlyphs: Improve settings management UI
dolby: fix headphone surround slider stuck at 35
dolby: show active audio output device on home screen
dolby: add device memory management screen
dolby: add full configuration backup and restore
dolby: add hold-to-bypass A/B comparison on main card
dolby: cycle profiles on QS tile long press
dolby: add custom full-configuration user presets and fix build errors
dolby: read dialogue enhancer strength from prefs
dolby: add scheduled time-based profile switching
dolby: add live audio visualizer to equalizer screen
dolby: add preset share codes for community import/export
dolby: allow hybrid app and device profile priority
dolby: add loudness tuning engine with output and volmax boost
dolby: add loudness tuning UI with per-feature enable toggles
dolby: raise default volmax in dax-default for speaker and headphone
dolby: persist audio tuning settings in device memory snapshots
dolby: add optional DSP volume loudness lift from shared prefs
dolby: Update credits section
dolby: Update Turkish translate

# 06-06-2026

   * device tree
Spacewar: overlay: Enable bluetooth sco by default
Spacewar: audio: Restore alarm, ringtone and notification helpers
Spacewar: Nuke Dirac
Spacewar: init: reduce zram size to 2GB
Spacewar: sepolicy: Allow zygote to search apk_data_file dirs
Spacewar: sepolicy: Allow platform_app to read vendor_sysfs_msm_subsys
Spacewar: Tune init script align whit thermal-engine
Spacewar: Fix migration to Lineage libperfmgr Power HAL
Spacewar: thermal: Custom thermal engine config
Spacewar: Move thermal engine config for device tree
Spacewar: overlay: Update power_profile from Spacewar_V3.2-260416-1140
Spacewar: rootdir: Fix /dev/goodix_fp permissions in ueventd
Spacewar: sepolicy: Allow glyph to find thermal_service
Spacewar: sensors: Drain stale poll events on sensor re-enable
Spacewar: sepolicy: Dontaudit glyph default_prop access
Spacewar: udfps: Fix null pointer dereference and thread lifecycle in UdfpsHandler
Spacewar: overlay: Remove redundant config_screenBrightnessDoze integer
spacewar: Include bcr
spacewar: Import GameBar
Spacewar: Set SurfaceFlinger uclamp.min to 20%
Spacewar: Silence BLASTBufferQueue ENOSYS
Spacewar: powerhint: Tune INTERACTION hint for smoother animations
spacewar: fix gamebar denials
spacewar: overlay: Enable Smart 5G
spacewar: overlay: Enable Smart Pixels
spacewar: Tune up powerhint for better rendering
spacewar: Silence some spammy logging
spacewar: overlay: Add overlay to improve signal reception
spacewar: props: Disable camera enhancements
spacewar: overlay-lineage: Enable blurs by default
spacewar: NGlyphs: Import for Phone(1)
spacewar: properties: force Kawase2 blur filter
spacewar: Update GameBar
Spacewar: Update bluetooth properties from NOS 3.2
Spacewar : remove config_screenBrightnessDoze
Spacewar: Move displayconfig to device tree
Spacewar: Trigger HBM at lower ambient light
Spacewar: Allow more brightness range for manual use
Spacewar: Enable thermal mitigation for HBM
Spacewar: Remove time limitation for HBM
Spacewar: Patch vidhance components with libui-v34
spacewar: Reduce logcat spam noise from HAL/services
spacewar: Fix glyph_app sepolicy (mediaserver + trust_service access)
spacewar: Disable NL80211_REG_CHANGED event
spacewar: Drop TARGET_USES_VULKAN
spacewar: sepolicy: Allow perf HAL to read proc_sched entries
spacewar: overlay: Remove default doze_display_state_supported
spacewar: recovery: Load ADSP modules and firmware for battery monitoring
spacewar: overlay: Set audio Panel On Left Side
spacewar: rootdir: Improve overall system tuning
spacewar: Prefer 'cache' backing storage
spacewar: udfps: s/hander/handler
spacewar: sepolicy: Allow system_suspend to read sysfs_wakeup
spacewar: powerhint: reduce launch boost duration from 4000ms to 2000ms
spacewar: Disable FRP
spacewar: overlay: Disable color inversion preference
spacewar: Silence ACDB-LOADER spam
spacewar: Set call volume steps to 6
spacewar: Silence minksocket error logs
spacewar: Override 120 for SurfaceFlinger frame_rate_category_min
spacewar: properties: Tune up a bit for smooth ui
Spacewar: Update from Spacewar_V3.2-260416-1140
Spacewar: overlay: Reduce blur radius
Spacewar: sepolicy: allow hal_power_default:vendor_sysfs_msm_perf
Spacewar: import init.qcom.post_boot.sh from NOS 3.2
Spacewar: vibrator: Allow to remap AOSP effect IDs to RichTap's internal effect IDs
Spacewar: vibrator: Improve richtap vibration consistency
Spacewar: vibrator: change vibration strength
Spacewar: unpin libaacvibrator.so
Spacewar: vibrator: change amplitude on init
Spacewar: wifi: Enable GreenAp
Spacewar: wifi: Bump the RuntimePM delay
Spacewar: wifi: Disable SNR Monitoring
Spacewar: wifi: Disable NAN
Spacewar: wifi: Disable TDLS external control
Spacewar: wifi: Enable MccToSccSwitchMode
Spacewar: wifi: Bump the NeighborScanTimerPeriod
Spacewar: wifi: Choose more the 5GHz band
Spacewar: displayconfig: tune brightness curve
Spacewar: displayconfig: lower the minimum brightness
Spacewar: displayconfig: tune high brightness mode thresholds
Spacewar: displayconfig: limit high brightness mode duration
Spacewar: displayconfig: reduce aggressive HDR boosting
Spacewar: perf: drop the all INTERACTION boosts duration to 250ms
Spacewar: perf: drop the all LAUNCH boosts duration to 1200ms
Spacewar: Use 8Gb dalvik heap size config
Spacewar: Opt out of speaker_layout_channel_mask field
Spacewar: properties: Reduce max acquired frame buffers to 2
Spacewar: properties: nuke ro.config.avoid_gfx_accel
Spacewar: disable sf backpressure
Spacewar: Add MIUI/HyperOS Dolby Atmos Support
Spacewar: Enable UDFPS icons and animations
Spacewar: overlay: enable 5G SA and NSA
Spacewar: Enable screen off udpfs support
Spacewar: overlay: Optimized auto brightness adjustment
Spacewar: overlay: Enable ambient display notifications by default

   * kernel
drivers: haptics: Silence spammy errors
drivers: Import KernelSU-Next v3.1.0 legacy
drivers: Rename makefiles for KernelSU inline build
drivers: Set proper version for KernelSU-Next
BACKPORT: seccomp: add filter_count field for KernelSU
BACKPORT: fs: path_umount for KernelSu
kernelsu: Add manual hooks v1.6
kernelsu: Allow compatible manager apks
drivers: ksu: change guard for ksu_vfs_read_hook and ksu_input_hook
[PATCH] GKI: use Android ABI padding for SYSVIPC task_struct fields
defconfig: enabled required configs for Droidspaces
defconfig: additional Kernel Configuration for UFW/Fail2ban support in Droidspaces
droidspaces: fixing build errors
qcom-hv-haptics: stop logspam
drivers: Import KernelSU-Next v3.2.0 legacy_susfs
BACKPORT: seccomp: add filter_count field for KernelSU
BACKPORT: fs: path_umount for KernelSu
fs: Add susfs 2.1.0
ksu: add hooks
susfs: implement susfs_try_umount
arch: arm64: update defconfig
ksu: supercall: drop use of deprecated susfs_add_try_umount
fs: add mount missing include
fs: ensure TWA_RESUME is defined for compatibilityfs: update ksu_vfs_read_hook for VFS fstat handling
techpack: q6afe: Silence cal_block unavailability logs

   * hardware
NGlyphs: Add recording indicator LED service
NGlyphs: Add turkish translate
NGlyphs: Update Licenses to reflect GPLv3
NGlyphs: Add audio-glyph sync with stock Nothing tones
NGlyphs: Light glyph pattern on system ringtone / notification preview
NGlyphs: Cap ringtone-preview visualizer at user brightness pref
NGlyphs: Redesign Glyph Light strength dialog to match flashlight strength tile
NGlyphs: Gate recording LED on Glyph MainSwitch state
NGlyphs: Sync stock tone glyphs to audio via wall-clock frame timing
NGlyphs: Guard tile click against null status bar service
NGlyphs: Harden essential-lights state tracking
NGlyphs: Add delay to notification and ringtone effects
dolby: Fixup dax-default-spatializer.xml path
NGlyph: Fixup! Prevent fallback to built-in pattern for imported CSV styles
NGlyphs: Glyph Converter rewrite with real Opus-in-Ogg encoding
NGlyphs: Ringtone sync observer and preview overlap fixes
NGlyphs: Music visualizer modes mirror stock behaviour
NGlyphs: Sync call glyph to ringtone audio onset
NGlyphs: Auto-grant notification listener access on boot
NGlyphs: Gate third-party SDK writes on master_allow
dolby: Update DolbyUI and switch to MotoDolbyAtmos
NGlyphs: Restore ParanoidGlyph-style beat blink and auto-off
NGlyphs: Respect essential unlock toggle and fix stuck threads

   * vendor tree
Spacewar: Update from Spacewar_V3.2-260416-1140

# 13-03-2026
Initial release
