[app]

title = My Awesome App

package.name = myawesomeapp

package.domain = org.myawesomeapp

source.dir = .

source.include_exts = py,png,jpg,kv

version = 1.0

requirements = kivy,pyrogram

source.custom_requirements = python3,pyrogram,kivy

android.entrypoint = appmain.py

android.logcat_filters = *:S python:D

android.permissions = INTERNET

android.api = 29

android.minapi = 21

android.sdk = 29

android.ndk = 21.4.7075529

android.private_storage = True

target = android
