import time
products = []
with open('addProduct.txt') as f:
    products = f.readlines()
# Listed by Name, sku, length, width, height, weight
#ABpackages are divided by A and B parts of a package
ABpackages= [['Davislegend 12U 19in Wall Mount server network equipment Data Cabinet Rack','SWC-PKST-01-12U645-CBK','27','19','5','19'],
['Davislegend 12U 19in Wall Mount server network equipment Data Cabinet Rack','SWC-PKST-01-12U645-CBK','30','25','5','46'],
['45U 2 Post Open frame Rack 7Ft 19inch wide Steel Tap with free top cable tray','SRK-PKST-0602-45U514-CH-CBK','23','9','5','32'],
['45U 2 Post Open frame Rack 7Ft 19inch wide Steel Tap with free top cable tray','SRK-PKST-0602-45U514-CH-CBK','87','4','2','26'],
['DavisLegend 9U 19in Wall Mount server network equipment Data Cabinet Rack','SWC-PKST-01-9U645-CBK','22','6','2','7'],
['DavisLegend 9U 19in Wall Mount server network equipment Data Cabinet Rack','SWC-PKST-01-9U645-CBK','27','21','7','48']
]
sku = [['DavisLegend 6U 19in Wall Mount server network equipment Data Cabinet Rack','SWC-PKST-01-6U645-CBK','27','21','7','48'],
['DavisLegend 12U Wall Mount IT Open Frame Swing Network Rack Hinged Black 19" Tap','SG-12','25','20','6','30'],
['Wall Mount IT Open Frame Swing Out Network Rack Hinged Black 19" Tap 24U','SG-24U','45','20','6','41'],
['DavisLegend 1U Rack Blank Panel (5 pack)','SUA-BPST-01-1U-CBK-5','21','3','3','4'],
['DavisLegend model 800 1U Sliding Shelf 21 3/4" deep with back support rails','SUA-SSST-01-80-CBK','26','19','2','13'],
['DavisLegend 1U Horizontal Cable Management-Plastic','DavisLegend 1U Horizontal Cable Management-Plastic','20','4','3','1'],
['Round Speaker Wire 14AWG OFC * 2 conductor','PCW-RO25-01-L100-CBL','11','11','10','22'],
['DavisLegend Wall Mount IT Open Frame Swing Network Rack Hinged Black 19" Tap 18U','SG-18U','35','21','6','36']
]
for product in products:
    item = product.split(',')
    if(len(item[5])>1):
        if(item[5][len(item[5])-1:] == '\n'):
            item[5] = item[5][:len(item[5])-1]
    sku.append(item)