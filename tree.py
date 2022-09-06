from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def treeTopo():
    net = Mininet( controller=RemoteController )
    
    info( 'Controller wordt toegevoegd\n' )
    net.addController('c1')
    
    info( 'Hosts worden toegevoegd\n' )
    h1 = net.addHost( 'h1', ip='10.0.0.1', mac='00:00:00:00:00:01' )
    h2 = net.addHost( 'h2', ip='10.0.0.2', mac='00:00:00:00:00:02' )
    h3 = net.addHost( 'h3', ip='10.0.0.3', mac='00:00:00:00:00:03' )

    info( 'Switches worden toegevoegd\n' )
    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )
    
    info( 'Verbindingen worden toegevoegd\n' )
    net.addLink( h1, s1 )
    net.addLink( h2, s1 )
    net.addLink( h3, s2 )
   
    root = s1
    layer1 = [s1,s2]
    
    for idx,l1 in enumerate(layer1):
        net.addLink( root,l1 )
        
    info( 'Netwerk wordt gestart\n')
    net.start()
    
    info( 'CLI wordt gestart\n' )
    CLI( net )
    
    info( 'Netwerk wordt gestopt' )
    net.stop()
    
if __name__ == '__main__':
    setLogLevel( 'info' )
    treeTopo()
