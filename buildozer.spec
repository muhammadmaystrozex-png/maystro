[app]
title = Legal Assistant
package.name = legalassistant
package.domain = org.mohammedalrahim
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy
orientation = portrait
fullscreen = 0

android.api = 31
android.minapi = 24
android.ndk = 25b
android.sdk = 31
android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
