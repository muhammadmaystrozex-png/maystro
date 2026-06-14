[app]
title = Legal Assistant
package.name = legalassistant
package.domain = org.mohammedalrahim
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 0.1

requirements = python3,kivy,android,pyjnius
orientation = portrait
fullscreen = 0

# Android SDK & NDK Settings (متوافقة مع Buildozer)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.archs = arm64-v8a, armeabi-v7a

# Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Gradle & Build Settings
android.gradle_dependencies = com.android.support:support-compat:28.0.0
android.add_aars = 
android.add_jars = 

# Signing (Debug Mode)
android.release_artifact = apk

# Logs
[buildozer]
log_level = 2
warn_on_root = 0
