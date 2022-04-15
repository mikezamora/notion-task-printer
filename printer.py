from escpos.printer import Usb
from escpos import config
# USB\VID_04B8&PID_0202\L7HF001361

c = config.Config()
p = c.printer()

""" Seiko Epson Corp. Receipt Printer (EPSON TM-T88IV) """
# p = Usb(0x04B8, 0x0202, 0)
# p.text("Hello World\n")
p.image("resources/he-man-yaaaaassss.gif")
# p.barcode('1324354657687', 'EAN13', 64, 2, '', '')
p.cut()