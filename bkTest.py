import bk1687bdrv

bk = bk1687bdrv.bk1687b()

print (bk.ports)

bk.setPort(0)
#bk.setV(20.0)

bk.enable()
print (bk.getSettings())
print (bk.getValues())

bk.disable()
