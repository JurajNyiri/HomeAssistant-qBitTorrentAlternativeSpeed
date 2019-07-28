# qBittorrent alternative speed switch for Home Assistant
Adds ability to switch alternative speed in qBittorrent through Home Assistant.

## Installation:
Copy file custom_components/qbittorrent_alternative_speed/switch.py to custom_components/qbittorrent_alternative_speed/switch.py

## Usage:
Add to configuration.yaml:

```
switch:
  - platform: qbittorrent_alternative_speed
    host: [Mandatory: IP address to qbittorrent]
    username: [Mandatory: Username to sign in]
    password: [Mandatory: Password to sign in]
    port: [Optional: Port on which qbittorrent is running, default: 8080]
    protocol: [Optional: Protocol on which qbittorrent is running, default: http]
    name: [Optional: Name of switch in Home Assistant, default: qbittorrent_alternative_speed]
```

## Track Updates
This custom component can be tracked with the help of [custom-lovelace](https://github.com/ciotlosm/custom-lovelace).

In your configuration.yaml

```
custom_updater:
  component_urls:
    - https://raw.githubusercontent.com/JurajNyiri/HomeAssistant-qBitTorrentAlternativeSpeed/master/custom_updater.json
```