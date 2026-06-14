[app]
title = Legal Assistant
package.name = legalassistant
package.domain = org.mohammedalrahim
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 0.1

requirements = python3==3.10.11,kivy==2.3.0,android==2024.10.30,pyjnius==1.6.0,hostpython3==3.10.11

orientation = portrait
fullscreen = 0

android.accept_sdk_license = True
android.api = 34
android.minapi = 21
android.ndk = 27c
android.sdk = 34
android.archs = arm64-v8a
android.enable_androidx = True
android.gradle_dependencies = 'androidx.browser:browser:1.7.0'

[buildozer]
log_level = 2
warn_on_root = 0
