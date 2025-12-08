# Module rfid-rc522

This module provides an interface to the RFID-RC522 component for RFID tag reading/writing. It is based off the Python library `mfrc522` which assumes a specific pin configuration on a Raspberry Pi to connect to the component

## Model viam:rfid-rc522:rfid-rc522

RFID reader component using SPI

### Configuration

The module works only with a Raspberry Pi with the following specific configuration of pins:

| Pin  | Module |
| ---- | ------ |
| 24   | SDA    |
| 23   | SCK    |
| 19   | MOSI   |
| 21   | MISO   |
| 22   | RST    |
| GND  | GND    |
| 3.3V | 3.3V   |

### DoCommand

Two DoCommands are available to read and write an RFID tag. The commands are blocking until a tag is presented.

Writing to the tag can accept messages up to

```json
{
  "cmd": "read"
}
```

```json
{
  "cmd": "write",
  "text": "text-to-write"
}
```
