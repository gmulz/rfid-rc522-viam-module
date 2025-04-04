# Module rfid-rc522

Provide a description of the purpose of the module and any relevant information.

## Model viam:rfid-rc522:rfid-rc522

Provide a description of the model and any relevant information.

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
