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
android.build_tools = 33.0.0   # <-- هذا السطر الجديد
android.archs = arm64-v8a, armeabi-v7a
