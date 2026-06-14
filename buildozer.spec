[app]
title = Legal Assistant
package.name = legalassistant
package.domain = org.mohammedalrahim
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 0.1

requirements = python3==3.10.11,kivy==2.3.0,android,pyjnius,hostpython3==3.10.11
orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET,ACCESS_NETWORK_STATE

[buildozer]
log_level = 2
warn_on_root = 0
