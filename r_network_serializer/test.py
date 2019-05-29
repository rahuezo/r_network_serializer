from rnetwork import RNetwork
from serialize import to_listvector, rserialize

import tkFileDialog as fd

fins = fd.askopenfiles(title="Choose networks")

networks = [RNetwork(f).serialize_ready for f in fins]

print networks

net_listvector = to_listvector(networks)

serialized = rserialize(net_listvector)

with open("serialized_networks.rda", "wb") as outf:
    outf.write(serialized)



