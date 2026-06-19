#16-06-2026
- Reworked on thermal profiles.
- Powerhint: major cleanup for better perf and battery backup.
- Improved task_profiles for better efficiency.
- Added back the dolby vision support. (thanks to pablo for fixing issue)
- Introduced double tap on fingerprint sensor gesture.
- upstreamed kernel to v5.10.258.
- Overall improvement in perf and stability.
- sm8450-common: Updated blobs from diting OS3.0.4.0.VLFMIXM.

#05-June-2026
- sm8450-common: Update blobs from diting OS3.0.1.0.VLFMIXM.
- marble: Update blobs and firmware from OS3.0.3.0.VMRMIXM.
- Fixed BHIM upi qr scanner goes blank while scanning.
- sm8450-common: sepolicy: allow power HAL access to cpu_dma_latency.
- Import task_profiles.json from AOSPA (CLO).
- Optimise Powerhint for better perf and stability.
- Updated Cpuset cores.
- sm8450-common: reduce uclamp.min value to 125.

# 20-Jan-2026
- Switched to qti perf hal
- Switched to prebuilt audio hal for better sound quality
- Improved overall smoothness
- Fixed dolby issues (switch to old dolby ui)
- Misc improvements

# 13-Jan-2026
- Updated blobs/firmware from latest hyperOS 2.0.216.0.
- Updated kernel to version 5.10.246.
- Updated some stuffs to fix jank in display.
- Fixed the auto brightness completely.
- Fixed memory leak in sensor causing issue with auto brightness.
- Improvement in powerhint.

# 28-Dec-2025
- Fixed the issue with no ringtone sound during call in bluetooth.
- Minor improvements in powerhint.
- Added built-in latest GameBar implementation.

# 14-Dec-2025
- Latest QPR1 source changes.
- Refine powerhint for balanced perf.
- Fixed the call loud speaker bug.
- Updated the dolby tuning for better experience.
- updated blobs and firmware from latest hyperOS 2.0.211 global.
