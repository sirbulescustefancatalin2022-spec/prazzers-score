
[app]
title = Prazzers Score
package.name = prazzersscore
package.domain = club.prazzers
source.dir = .
android.api = 34
android.minapi = 21
android.accept_sdk_license = True

source.include_exts = py,kv,png,jpg,ttf,wav,mp3,ogg,json
version = 0.1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

android.archs = armeabi-v7a, arm64-v8a
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
icon.filename = assets/icon.png
presplash.filename = assets/presplash.png

[buildozer]
log_level = 2
warn_on_root = 0
