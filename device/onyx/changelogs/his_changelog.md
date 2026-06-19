# 02-June-2026
- Update blobs from OS3.0.7.0.WOLMIXM
- Fixup call volume issue on voip call
- Update sf early & late duration to 12.3ms & 13.6ms
- Set 60hz refresh rate for AOD
- Set ro.netflix.bsp_rev for L1
- Use hwui and add some hwui props for improve perf
- Reduce surfaceflinger min uclamp value to 125
- Update CarrierConfig from OS3.0.7.0.WOLMIXM
- Update kernel from OS3.0.7.0.WOLMIXM
- Introduce displayfeature color service for MIUI color modes
- Enable motion prediction for ultra-low latency input
- Optimize scroll friction for high-performance 120Hz usage
- Increase max fling velocity
- Reduce paging touch slop for improved responsiveness
- Reduce touch slop to 6dp for improved gesture responsiveness

# 12-Mar-2026
- Lowered default screen density
- Switch to QTI Vibrator service
- Switch to AOSP NXP authsecret service
- Switch to AOSP NXP keymint service
- Switch to libperfmgr
- Drop more unused blobs and fw
- Re-implemented Dolby Atmos support(thanks to @unmoved21)
- Update blobs & fingerprint from OS3.0.6.0.WOLMIXM
- Update parts

# 28-Dec-2025
- Add props to improve battery backup
- Optimize auto brightness adjustment
- Tune ambient display burn-in protection

# 16-Dec-2025
- Synced with latest qpr1 source
- enabled the 1k nits brightness by default
- Some mics changes in boosts
- Disable Lift to check by default
- Partially import parts from sm8350-common:
* Thermals
* Per-app refresh rate
* Clear speaker
* Doze
- Force enable volte and wifi calling
- Fixed USSD dial issue
- Enabled 120Hz Keyguard
- Optimize SurfaceFlinger properties for graphics performance(This should improve graphics performance, smoothness, and screen responsiveness)
- Add Gcam by default
