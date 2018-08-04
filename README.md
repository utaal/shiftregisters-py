# Shift register support for GPIO-like hardware interfaces

Pins should have been initialised as "output".

```python
sr = ShiftRegisters(
  set_output = lambda pin, lvl: GPIO.output(pin, GPIO.HIGH if lvl else GPIO.LOW),
  ser = 17,
  srclk = 27,
  rclk = 22,
  srclk_delay = 5)

sr.set_all({3, 5, 6})
```

