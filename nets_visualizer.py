import pyshark
import datetime
import csv
import matplotlib.pyplot as plt
import threading

#SOURCE Vs DESTINATION
def showVisualDataIP():
    x = []
    y = []
    a = []
    b = []
    print('showVisualData initiated...IP vs IP')
    with open('/home/gemini/Documents/cycle4/data.txt','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(str(row[1])) 
            y.append(str(row[3])) 
            a.append(str(row[1])) 
            b.append(str(row[2])) 

    figs, ((ax1,ax2),(ax3,ax4))  = plt.subplots(2,2)
    #ax1 = axes[0]
    #ax2 = axes[1]
    #ax3 = axes[2]
    #ax4 = axes[4]

    ax1.scatter(x,y,c='red',marker='+',alpha=0.5)
    ax1.set_title('IP vs IP Connection')
    ax1.set_xlabel('Source IP')
    ax1.set_ylabel('Destination IP')

    ax2.scatter(a,b,alpha=0.5)
    ax2.set_title('IP vs Port Access')
    ax2.set_xlabel('IP Ports')
    ax2.set_ylabel('IP Addresses')

    ax3.bar(x,y,)
    ax3.set_title('BAR Graph')
    ax4.bar(a,b)
    ax4.set_title('BAR Graph')
    plt.subplots_adjust(wspace=0.20, hspace=0.5)
    plt.get_current_fig_manager().canvas.set_window_title('Ports/IPs Visual Representation/Relationship: Mar Castro - Developer')
    plt.show()

#Show which port Source IP is using
def showVisualDataPorts():
    x = []
    y = []
    print('showVisualData initiated..IP Source/port')
    with open('/home/gemini/Documents/cycle4/data.txt','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(str(row[1]))
            y.append(str(row[2]))
    plt.scatter(x,y,alpha=0.2)
    plt.title('Mapping IP to PORTS: Incident Response Team A')
    plt.xlabel('SOURCE IP')
    plt.ylabel('PORTS')
    plt.legend('MAR CASTRO - PCAP PLOT ip/ports')
    plt.show()


def print_dns_info(pkt):
    print('dns_info_initiated..')
    outfile = open("/home/gemini/Documents/cycle4/data.txt","a+")
    try:
        pro = pkt.transport_layer
        src_a = pkt.ip.src
        src_p = pkt[pkt.transport_layer].srcport
        dst_a = pkt.ip.dst
        dst_p = pkt[pkt.transport_layer].dstport
        print (pro, src_a, src_p, dst_a, dst_p)
        outstring = pro+","+src_a+","+src_p+","+dst_a+","+dst_p+"\n"
        print(outstring)
        outfile.write(outstring)
    except AttributeError as e:
        print("error...")
        pass
    outfile.close()

def saveCapturedFile():
    print('traversing...: Captured PCAP Data initiated..')
    capture = pyshark.LiveCapture(interface="enp0s3", output_file="/home/gemini/Documents/cycle4/marcap")
    capture.sniff(timeout=10)
    c = pyshark.FileCapture("/home/gemini/Documents/cycle4/marcap")
    c.apply_on_packets(print_dns_info)

def captureLiveData():
    print("Init captureData..")
    cap = pyshark.LiveCapture(interface="eth0")
    cap.sniff(packet_count=10)
    print("check data captured..")
    cap.apply_on_packets(print_dns_info)


#captureLiveData()
#saveCapturedFile()
showVisualDataIP()
print("Exiting Main Thread...")
