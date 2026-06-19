# 01-Feb-2026

- Latest source changes
- Kernel: Updated to 6.1.159-GlaciumKernel-2.7
- Updated Graphics blobs to v819
- Fixed GPU freq stuck at lower speed
- Added missing secure element permission
- Updated powerhint to work msm performance
- Fixed no sound occasionally with TWS
- Updated powertools
- Tuned devfreq for balanced profile
- Fixed Custom recovery decryption issue

# 25-Jan-2026

- Hotfix Build ,Hyperos 3 blobs and firmware based (OS3.0.3.0.WNPEUXM).
- Fixed camera issues and occasional crashes
- Fixed some apps not able to access location & GPS services
- Fixed VoIP and VoNR calling for some carriers
- Fixed no-incallsound in some cases
- Dolby profile reset issue fixed
- Fixed display occasopnal crashes


# 22-Jan-2026

- Latest Hyperos 3 blobs and firmware based (OS3.0.3.0.WNPEUXM).
- Kernel: Updated to Glacium-2.6


# 18-Jan-2026

- Latest QPR2 source changes


# 28-Dec-2025

- Latest QPR1 source changes
- Dec security patch
- Kernel: Switched to Glacium-2.5 (NonRooted)
- Updated blobs from OS2.0.207.0.VNPMIXM
- Better tuned devfreq boost for better performance, active and idle drain
- Implemented touch based input boost in gameboost mode for better scrooling/finger movement (wip)
- Impletemted focaltech game mode touch delay fix (still under testing) (use htsr switch to apply)
- updated some graphics blobs for better stability
- Implemented camera privacy toggle
- Minor improvement in autobrightness responsivity
- Misc Other Changes


# 14-Dec-2025

- Latest QPR1 source changes
- Dec security patch
- Kernel: Switched to Glacium-2.3 (NonRooted)
- Updated blobs from OS2.0.206.0.VNPMIXM
- Updated some Camera blobs from aurora for better processing
- Implement haptics xiaomi effects
- Implement idle manager for better idle(Enable toggle battery/Idle manager)
- Dropped parts:Refresh rate impl (use rom per app refresh rate-better)
- Dropped parts:Saturation impl (use rom impl settings/display/colors)
- Rework boost freq implementation with seperate implementation
- Rework fastcharge implementation (custom implementation in slow and superfast mode)
- Tuned dev-frq boost implementation
- powertools: Updated CPU Sets defaults
- Powertools: Implement custom configuration and backup functionality
- Implement Displayfeature color service
- Updated Dolby Implementation
- Implement miui proved color modes
- Bring back bypass charging feature (fake)
- Use night_charging node for lineage charge control (only works above 80%)
- Added PSI-based LMKD configuration
- Updated HintManager for better CPU scheduling
- Force enable volte , vonr for unsupported carrier
- Implment QCOM custom doze
- Tuned powerhint for balanced profile
- Tuned boost freq implementation for better CPU scheduling
- lmkd optimize scheduling
- Fix SCREEN_BRIGHTNESS inconsistency issue before and after reboot
- updated BCR to 1.87
- Misc Other Changes


# 23-Nov-2025

- Initial ASCP build
- Based on latest qpr1 spurce
- kernel: Nitron-2.6 (non rooted)
