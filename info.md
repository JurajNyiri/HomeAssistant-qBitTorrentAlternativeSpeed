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